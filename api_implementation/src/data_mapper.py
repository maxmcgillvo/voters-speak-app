#!/usr/bin/env python3
"""
Data Mapper Module

This module provides enhanced mapping and transformation functions
for converting United States Project data to Voters Speak format.
"""

import os
import sys
import json
import logging
from typing import Dict, List, Any, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("api_implementation/logs/data_mapper.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("data_mapper")

class DataMapper:
    """
    Maps and transforms congressional data between different formats
    """
    
    def __init__(self):
        """Initialize the data mapper"""
        self.state_names = self._load_state_names()
        self.validation_errors = []
        self.validation_warnings = []
    
    def _load_state_names(self) -> Dict[str, str]:
        """
        Load state abbreviations to full names mapping
        
        Returns:
            dict: Mapping of state abbreviations to full names
        """
        return {
            'AL': 'Alabama',
            'AK': 'Alaska',
            'AZ': 'Arizona',
            'AR': 'Arkansas',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'HI': 'Hawaii',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'IA': 'Iowa',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'ME': 'Maine',
            'MD': 'Maryland',
            'MA': 'Massachusetts',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MS': 'Mississippi',
            'MO': 'Missouri',
            'MT': 'Montana',
            'NE': 'Nebraska',
            'NV': 'Nevada',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NY': 'New York',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VT': 'Vermont',
            'VA': 'Virginia',
            'WA': 'Washington',
            'WV': 'West Virginia',
            'WI': 'Wisconsin',
            'WY': 'Wyoming',
            'DC': 'District of Columbia',
            'AS': 'American Samoa',
            'GU': 'Guam',
            'MP': 'Northern Mariana Islands',
            'PR': 'Puerto Rico',
            'VI': 'Virgin Islands'
        }
    
    def transform_legislators(self, legislators_data: List[Dict[str, Any]],
                             social_media_data: Optional[List[Dict[str, Any]]] = None) -> Dict[str, List[Dict[str, Any]]]:
        """
        Transform legislators data from United States Project format to Voters Speak format
        
        Args:
            legislators_data (list): List of legislators data
            social_media_data (list, optional): List of social media data
            
        Returns:
            dict: Dictionary with 'house' and 'senate' keys containing lists of legislators
        """
        logger.info(f"Transforming {len(legislators_data)} legislators")
        
        # Reset validation lists
        self.validation_errors = []
        self.validation_warnings = []
        
        # Create social media lookup dictionary if provided
        social_media_lookup = {}
        if social_media_data:
            for item in social_media_data:
                if 'id' in item and 'bioguide' in item['id']:
                    bioguide_id = item['id']['bioguide']
                    social_media_lookup[bioguide_id] = item.get('social', {})
        
        # Initialize result
        result = {
            'house': [],
            'senate': []
        }
        
        # Process each legislator
        for legislator in legislators_data:
            try:
                # Skip if no terms
                if 'terms' not in legislator or not legislator['terms']:
                    self.validation_warnings.append(f"Legislator has no terms: {legislator.get('id', {}).get('bioguide', 'unknown')}")
                    continue
                
                # Get the latest term
                latest_term = legislator['terms'][-1]
                
                # Skip if not current
                if not self._is_current_term(latest_term):
                    continue
                
                # Transform the legislator data
                transformed = self._transform_legislator(legislator, latest_term, social_media_lookup)
                
                # Add to appropriate list
                if latest_term['type'] == 'sen':
                    result['senate'].append(transformed)
                elif latest_term['type'] == 'rep':
                    result['house'].append(transformed)
                else:
                    self.validation_warnings.append(f"Unknown term type: {latest_term['type']} for {legislator.get('id', {}).get('bioguide', 'unknown')}")
            except Exception as e:
                bioguide_id = legislator.get('id', {}).get('bioguide', 'unknown')
                logger.error(f"Error transforming legislator {bioguide_id}: {e}")
                self.validation_errors.append(f"Error transforming legislator {bioguide_id}: {e}")
        
        # Sort by state and then by district/rank
        result['house'] = sorted(result['house'], key=lambda x: (x['state'], x.get('district', 0)))
        result['senate'] = sorted(result['senate'], key=lambda x: (x['state'], x.get('state_rank', '')))
        
        logger.info(f"Transformed {len(result['house'])} House members and {len(result['senate'])} Senate members")
        
        # Log validation results
        if self.validation_errors:
            logger.error(f"Validation errors: {len(self.validation_errors)}")
            for error in self.validation_errors[:10]:  # Log first 10 errors
                logger.error(f"  {error}")
            if len(self.validation_errors) > 10:
                logger.error(f"  ... and {len(self.validation_errors) - 10} more errors")
        
        if self.validation_warnings:
            logger.warning(f"Validation warnings: {len(self.validation_warnings)}")
            for warning in self.validation_warnings[:10]:  # Log first 10 warnings
                logger.warning(f"  {warning}")
            if len(self.validation_warnings) > 10:
                logger.warning(f"  ... and {len(self.validation_warnings) - 10} more warnings")
        
        return result
    
    def _is_current_term(self, term: Dict[str, Any]) -> bool:
        """
        Check if a term is current
        
        Args:
            term (dict): Term data
            
        Returns:
            bool: True if the term is current, False otherwise
        """
        import datetime
        
        # Get current date
        today = datetime.date.today()
        
        # Check if term has start and end dates
        if 'start' not in term or 'end' not in term:
            return False
        
        try:
            # Parse dates
            start_date = datetime.datetime.strptime(term['start'], '%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(term['end'], '%Y-%m-%d').date()
            
            # Check if current date is within term
            return start_date <= today <= end_date
        except ValueError:
            # If date parsing fails, return False
            return False
    
    def _transform_legislator(self, legislator: Dict[str, Any], term: Dict[str, Any],
                             social_media_lookup: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        """
        Transform a single legislator
        
        Args:
            legislator (dict): Legislator data
            term (dict): Current term data
            social_media_lookup (dict): Social media lookup dictionary
            
        Returns:
            dict: Transformed legislator data
        """
        # Get basic information
        bioguide_id = legislator.get('id', {}).get('bioguide')
        
        # Validate required fields
        if not bioguide_id:
            raise ValueError("Missing bioguide ID")
        
        if 'name' not in legislator:
            raise ValueError(f"Missing name for {bioguide_id}")
        
        if 'state' not in term:
            raise ValueError(f"Missing state for {bioguide_id}")
        
        # Get name components
        name_parts = []
        if legislator['name'].get('first'):
            name_parts.append(legislator['name']['first'])
        if legislator['name'].get('middle'):
            name_parts.append(legislator['name']['middle'])
        if legislator['name'].get('last'):
            name_parts.append(legislator['name']['last'])
        if legislator['name'].get('suffix'):
            name_parts.append(legislator['name']['suffix'])
        
        # Use official full name if available, otherwise construct from parts
        full_name = legislator['name'].get('official_full', ' '.join(name_parts))
        
        # Get state information
        state_abbrev = term['state']
        state_name = self.state_names.get(state_abbrev, state_abbrev)
        
        # Get party
        party = term.get('party', 'Unknown')
        
        # Get title based on term type
        if term['type'] == 'sen':
            title = "Senator"
        elif term['type'] == 'rep':
            title = "Representative"
        else:
            title = term.get('title', "Member")
        
        # Get district for representatives
        district = None
        if term['type'] == 'rep' and 'district' in term:
            try:
                district = int(term['district'])
            except (ValueError, TypeError):
                if term['district'] == 'At Large':
                    district = 0
                else:
                    district = term['district']
        
        # Get state rank for senators
        state_rank = None
        if term['type'] == 'sen' and 'state_rank' in term:
            state_rank = term['state_rank']
        
        # Get contact information
        contact_info = {
            'phone': term.get('phone', ''),
            'address': term.get('address', ''),
            'office': term.get('office', ''),
            'url': term.get('url', ''),
            'contact_form': term.get('contact_form', '')
        }
        
        # Get social media information
        social_media = {}
        if bioguide_id in social_media_lookup:
            sm_data = social_media_lookup[bioguide_id]
            social_media = {
                'twitter': sm_data.get('twitter', ''),
                'facebook': sm_data.get('facebook', ''),
                'youtube': sm_data.get('youtube', ''),
                'instagram': sm_data.get('instagram', '')
            }
        
        # Create result dictionary
        result = {
            'name': full_name,
            'title': title,
            'state': state_name,
            'party': party,
            'bioguide_id': bioguide_id
        }
        
        # Add district for representatives
        if district is not None:
            result['district'] = district
        
        # Add state rank for senators
        if state_rank is not None:
            result['state_rank'] = state_rank
        
        # Add contact information
        for key, value in contact_info.items():
            if value:
                result[key] = value
        
        # Add social media information
        for key, value in social_media.items():
            if value:
                result[key] = value
        
        # Add additional IDs
        if 'id' in legislator:
            ids = legislator['id']
            for id_type in ['thomas', 'govtrack', 'opensecrets', 'votesmart', 'wikipedia']:
                if id_type in ids and ids[id_type]:
                    result[f"{id_type}_id"] = ids[id_type]
        
        return result
    
    def get_validation_results(self) -> Dict[str, List[str]]:
        """
        Get validation results
        
        Returns:
            dict: Dictionary with 'errors' and 'warnings' keys containing lists of messages
        """
        return {
            'errors': self.validation_errors,
            'warnings': self.validation_warnings
        }

# Main function for testing
def main():
    """Main function for testing the data mapper"""
    import json
    
    # Load test data
    test_data_path = "legislators-current.json"
    if not os.path.exists(test_data_path):
        logger.error(f"Test data file not found: {test_data_path}")
        return
    
    with open(test_data_path, 'r') as f:
        test_data = json.load(f)
    
    # Create data mapper
    mapper = DataMapper()
    
    # Transform data
    transformed = mapper.transform_legislators(test_data)
    
    # Print results
    print(f"Transformed {len(transformed['house'])} House members and {len(transformed['senate'])} Senate members")
    
    # Print validation results
    validation = mapper.get_validation_results()
    print(f"Validation errors: {len(validation['errors'])}")
    print(f"Validation warnings: {len(validation['warnings'])}")

if __name__ == "__main__":
    main()