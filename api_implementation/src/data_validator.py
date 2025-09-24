#!/usr/bin/env python3
"""
Data Validator Module

This module provides enhanced validation for congressional data.
"""

import os
import sys
import json
import logging
from typing import Dict, List, Any, Optional, Union, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("api_implementation/logs/data_validator.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("data_validator")

class DataValidator:
    """
    Validates congressional data for completeness and correctness
    """
    
    def __init__(self):
        """Initialize the data validator"""
        self.validation_errors = []
        self.validation_warnings = []
        
        # Define required fields for each member type
        self.required_fields = {
            'house': ['name', 'title', 'state', 'party', 'bioguide_id'],
            'senate': ['name', 'title', 'state', 'party', 'bioguide_id']
        }
        
        # Define optional fields for each member type
        self.optional_fields = {
            'house': ['district', 'phone', 'address', 'office', 'url', 'contact_form', 
                     'twitter', 'facebook', 'youtube', 'instagram'],
            'senate': ['state_rank', 'phone', 'address', 'office', 'url', 'contact_form',
                      'twitter', 'facebook', 'youtube', 'instagram']
        }
        
        # Define expected data types for each field
        self.field_types = {
            'name': str,
            'title': str,
            'state': str,
            'party': str,
            'bioguide_id': str,
            'district': (int, str),  # Can be int or str
            'state_rank': str,
            'phone': str,
            'address': str,
            'office': str,
            'url': str,
            'contact_form': str,
            'twitter': str,
            'facebook': str,
            'youtube': str,
            'instagram': str
        }
        
        # Define expected values for certain fields
        self.expected_values = {
            'title': ['Representative', 'Senator', 'Delegate', 'Resident Commissioner'],
            'party': ['Republican', 'Democrat', 'Independent', 'Democratic', 'Republican Party', 'Democratic Party', 'Independent Party'],
            'state_rank': ['junior', 'senior']
        }
    
    def validate_data(self, data: Dict[str, List[Dict[str, Any]]]) -> bool:
        """
        Validate congressional data
        
        Args:
            data (dict): Dictionary with 'house' and 'senate' keys containing lists of legislators
            
        Returns:
            bool: True if validation passed, False otherwise
        """
        logger.info("Validating congressional data")
        
        # Reset validation lists
        self.validation_errors = []
        self.validation_warnings = []
        
        # Check that data has required keys
        if 'house' not in data:
            self.validation_errors.append("Data missing 'house' key")
            return False
        
        if 'senate' not in data:
            self.validation_errors.append("Data missing 'senate' key")
            return False
        
        # Check that house and senate are lists
        if not isinstance(data['house'], list):
            self.validation_errors.append("'house' is not a list")
            return False
        
        if not isinstance(data['senate'], list):
            self.validation_errors.append("'senate' is not a list")
            return False
        
        # Check expected counts
        if len(data['house']) < 400:
            self.validation_warnings.append(f"House count is low: {len(data['house'])} (expected ~435)")
        
        if len(data['house']) > 450:
            self.validation_warnings.append(f"House count is high: {len(data['house'])} (expected ~435)")
        
        if len(data['senate']) < 90:
            self.validation_warnings.append(f"Senate count is low: {len(data['senate'])} (expected 100)")
        
        if len(data['senate']) > 110:
            self.validation_warnings.append(f"Senate count is high: {len(data['senate'])} (expected 100)")
        
        # Validate each house member
        for i, member in enumerate(data['house']):
            self._validate_member(member, 'house', i)
        
        # Validate each senate member
        for i, member in enumerate(data['senate']):
            self._validate_member(member, 'senate', i)
        
        # Check for duplicate bioguide IDs
        self._check_duplicates(data)
        
        # Log validation results
        if self.validation_errors:
            logger.error(f"Validation errors: {len(self.validation_errors)}")
            for error in self.validation_errors[:10]:  # Log first 10 errors
                logger.error(f"  {error}")
            if len(self.validation_errors) > 10:
                logger.error(f"  ... and {len(self.validation_errors) - 10} more errors")
            return False
        
        if self.validation_warnings:
            logger.warning(f"Validation warnings: {len(self.validation_warnings)}")
            for warning in self.validation_warnings[:10]:  # Log first 10 warnings
                logger.warning(f"  {warning}")
            if len(self.validation_warnings) > 10:
                logger.warning(f"  ... and {len(self.validation_warnings) - 10} more warnings")
        
        logger.info("Data validation passed")
        return True
    
    def _validate_member(self, member: Dict[str, Any], chamber: str, index: int) -> None:
        """
        Validate a single member
        
        Args:
            member (dict): Member data
            chamber (str): 'house' or 'senate'
            index (int): Index of the member in the list
        """
        # Check that member is a dictionary
        if not isinstance(member, dict):
            self.validation_errors.append(f"{chamber.capitalize()} member at index {index} is not a dictionary")
            return
        
        # Check required fields
        for field in self.required_fields[chamber]:
            if field not in member:
                self.validation_errors.append(f"{chamber.capitalize()} member at index {index} missing required field: {field}")
            elif member[field] is None or member[field] == '':
                self.validation_errors.append(f"{chamber.capitalize()} member at index {index} has empty required field: {field}")
        
        # Check field types
        for field, value in member.items():
            if field in self.field_types:
                expected_type = self.field_types[field]
                if isinstance(expected_type, tuple):
                    # Multiple allowed types
                    if not any(isinstance(value, t) for t in expected_type):
                        self.validation_warnings.append(
                            f"{chamber.capitalize()} member at index {index} has field '{field}' with wrong type: "
                            f"got {type(value).__name__}, expected one of {[t.__name__ for t in expected_type]}"
                        )
                elif not isinstance(value, expected_type):
                    self.validation_warnings.append(
                        f"{chamber.capitalize()} member at index {index} has field '{field}' with wrong type: "
                        f"got {type(value).__name__}, expected {expected_type.__name__}"
                    )
        
        # Check expected values
        for field, expected_values in self.expected_values.items():
            if field in member and member[field] not in expected_values:
                # Special case for party - just warn if it's not in the expected list
                if field == 'party':
                    self.validation_warnings.append(
                        f"{chamber.capitalize()} member at index {index} has unexpected party: {member[field]}"
                    )
                else:
                    self.validation_errors.append(
                        f"{chamber.capitalize()} member at index {index} has field '{field}' with unexpected value: "
                        f"{member[field]}, expected one of {expected_values}"
                    )
        
        # Special validation for house members
        if chamber == 'house' and 'district' in member:
            # Convert district to int if it's a string representing a number
            if isinstance(member['district'], str) and member['district'].isdigit():
                member['district'] = int(member['district'])
            
            # Check if district is "At Large" or 0 for at-large districts
            if member['district'] not in [0, "At Large", "at-large", "At-Large", "at large"] and not isinstance(member['district'], int):
                self.validation_warnings.append(
                    f"House member at index {index} has district with unexpected format: {member['district']}"
                )
    
    def _check_duplicates(self, data: Dict[str, List[Dict[str, Any]]]) -> None:
        """
        Check for duplicate bioguide IDs
        
        Args:
            data (dict): Dictionary with 'house' and 'senate' keys containing lists of legislators
        """
        # Check for duplicate bioguide IDs within house
        house_ids = {}
        for i, member in enumerate(data['house']):
            if 'bioguide_id' in member:
                bioguide_id = member['bioguide_id']
                if bioguide_id in house_ids:
                    self.validation_errors.append(
                        f"Duplicate bioguide ID in house: {bioguide_id} at indices {house_ids[bioguide_id]} and {i}"
                    )
                else:
                    house_ids[bioguide_id] = i
        
        # Check for duplicate bioguide IDs within senate
        senate_ids = {}
        for i, member in enumerate(data['senate']):
            if 'bioguide_id' in member:
                bioguide_id = member['bioguide_id']
                if bioguide_id in senate_ids:
                    self.validation_errors.append(
                        f"Duplicate bioguide ID in senate: {bioguide_id} at indices {senate_ids[bioguide_id]} and {i}"
                    )
                else:
                    senate_ids[bioguide_id] = i
        
        # Check for duplicate bioguide IDs between house and senate
        for bioguide_id, house_index in house_ids.items():
            if bioguide_id in senate_ids:
                self.validation_errors.append(
                    f"Bioguide ID {bioguide_id} appears in both house (index {house_index}) and senate (index {senate_ids[bioguide_id]})"
                )
    
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
    """Main function for testing the data validator"""
    import json
    import argparse
    
    parser = argparse.ArgumentParser(description='Validate congressional data')
    parser.add_argument('file', help='Path to the data file to validate')
    
    args = parser.parse_args()
    
    # Load data
    try:
        with open(args.file, 'r') as f:
            data = json.load(f)
    except Exception as e:
        logger.error(f"Error loading data from {args.file}: {e}")
        return False
    
    # Create validator
    validator = DataValidator()
    
    # Validate data
    valid = validator.validate_data(data)
    
    # Print results
    if valid:
        print("Data validation passed")
    else:
        print("Data validation failed")
    
    results = validator.get_validation_results()
    
    if results['errors']:
        print(f"Errors ({len(results['errors'])}):")
        for error in results['errors']:
            print(f"  {error}")
    
    if results['warnings']:
        print(f"Warnings ({len(results['warnings'])}):")
        for warning in results['warnings']:
            print(f"  {warning}")
    
    return valid

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)