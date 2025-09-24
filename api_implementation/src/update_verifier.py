#!/usr/bin/env python3
"""
Update Verifier Module

This module provides verification functionality for the congressional data
update process, ensuring that updates are valid and complete.
"""

import os
import sys
import json
import logging
from typing import Dict, List, Any, Optional, Tuple, Set

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_validator import DataValidator

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("api_implementation/logs/update_verifier.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("update_verifier")

class UpdateVerifier:
    """
    Verifies congressional data updates to ensure they are valid and complete
    """
    
    def __init__(self):
        """Initialize the update verifier"""
        self.verification_errors = []
        self.verification_warnings = []
        self.data_validator = DataValidator()
    
    def verify_update(self, 
                     new_data: Dict[str, List[Dict[str, Any]]],
                     old_data: Optional[Dict[str, List[Dict[str, Any]]]] = None) -> bool:
        """
        Verify that an update is valid and complete
        
        Args:
            new_data (dict): Dictionary with 'house' and 'senate' keys containing lists of legislators
            old_data (dict, optional): Dictionary with 'house' and 'senate' keys containing lists of legislators
            
        Returns:
            bool: True if update is valid, False otherwise
        """
        # Reset verification lists
        self.verification_errors = []
        self.verification_warnings = []
        
        # Validate the new data using the data validator
        if not self.data_validator.validate_data(new_data):
            # Get validation results and add them to verification results
            validation_results = self.data_validator.get_validation_results()
            self.verification_errors.extend(validation_results['errors'])
            self.verification_warnings.extend(validation_results['warnings'])
            return False
        
        # Verify changes if old data is provided
        if old_data:
            if not self._verify_changes(new_data, old_data):
                return False
        
        # Log verification results
        if self.verification_warnings:
            logger.warning(f"Verification warnings: {len(self.verification_warnings)}")
            for warning in self.verification_warnings[:10]:  # Log first 10 warnings
                logger.warning(f"  {warning}")
            if len(self.verification_warnings) > 10:
                logger.warning(f"  ... and {len(self.verification_warnings) - 10} more warnings")
        
        logger.info("Update verification passed")
        return True
    
    def _find_duplicates(self, items: List[Any]) -> Set[Any]:
        """
        Find duplicate items in a list
        
        Args:
            items (list): List of items
            
        Returns:
            set: Set of duplicate items
        """
        seen = set()
        duplicates = set()
        
        for item in items:
            if item in seen:
                duplicates.add(item)
            else:
                seen.add(item)
        
        return duplicates
    
    def _verify_changes(self, new_data: Dict[str, List[Dict[str, Any]]], 
                       old_data: Dict[str, List[Dict[str, Any]]]) -> bool:
        """
        Verify that changes between old and new data are reasonable
        
        Args:
            new_data (dict): Dictionary with 'house' and 'senate' keys containing lists of legislators
            old_data (dict): Dictionary with 'house' and 'senate' keys containing lists of legislators
            
        Returns:
            bool: True if changes are reasonable, False otherwise
        """
        # Check for large changes in House count
        old_house_count = len(old_data['house'])
        new_house_count = len(new_data['house'])
        house_change = abs(new_house_count - old_house_count)
        
        if house_change > 50:
            self.verification_errors.append(f"Large change in House count: {old_house_count} -> {new_house_count} (change: {house_change})")
            return False
        elif house_change > 20:
            self.verification_warnings.append(f"Significant change in House count: {old_house_count} -> {new_house_count} (change: {house_change})")
        
        # Check for large changes in Senate count
        old_senate_count = len(old_data['senate'])
        new_senate_count = len(new_data['senate'])
        senate_change = abs(new_senate_count - old_senate_count)
        
        if senate_change > 20:
            self.verification_errors.append(f"Large change in Senate count: {old_senate_count} -> {new_senate_count} (change: {senate_change})")
            return False
        elif senate_change > 10:
            self.verification_warnings.append(f"Significant change in Senate count: {old_senate_count} -> {new_senate_count} (change: {senate_change})")
        
        # Get bioguide IDs from old and new data
        old_house_ids = {member.get('bioguide_id') for member in old_data['house'] if member.get('bioguide_id')}
        new_house_ids = {member.get('bioguide_id') for member in new_data['house'] if member.get('bioguide_id')}
        old_senate_ids = {member.get('bioguide_id') for member in old_data['senate'] if member.get('bioguide_id')}
        new_senate_ids = {member.get('bioguide_id') for member in new_data['senate'] if member.get('bioguide_id')}
        
        # Check for members that moved between chambers
        house_to_senate = old_house_ids & new_senate_ids
        senate_to_house = old_senate_ids & new_house_ids
        
        if house_to_senate:
            self.verification_warnings.append(f"Members moved from House to Senate: {house_to_senate}")
        
        if senate_to_house:
            self.verification_warnings.append(f"Members moved from Senate to House: {senate_to_house}")
        
        # Check for large number of new members
        new_house_members = new_house_ids - old_house_ids
        new_senate_members = new_senate_ids - old_senate_ids
        
        if len(new_house_members) > 50:
            self.verification_warnings.append(f"Large number of new House members: {len(new_house_members)}")
        
        if len(new_senate_members) > 20:
            self.verification_warnings.append(f"Large number of new Senate members: {len(new_senate_members)}")
        
        # Check for large number of removed members
        removed_house_members = old_house_ids - new_house_ids
        removed_senate_members = old_senate_ids - new_senate_ids
        
        if len(removed_house_members) > 50:
            self.verification_warnings.append(f"Large number of removed House members: {len(removed_house_members)}")
        
        if len(removed_senate_members) > 20:
            self.verification_warnings.append(f"Large number of removed Senate members: {len(removed_senate_members)}")
        
        return True
    
    def get_verification_results(self) -> Dict[str, List[str]]:
        """
        Get verification results
        
        Returns:
            dict: Dictionary with 'errors' and 'warnings' keys containing lists of messages
        """
        return {
            'errors': self.verification_errors,
            'warnings': self.verification_warnings
        }

# Main function for testing
def main():
    """Main function for testing the update verifier"""
    import json
    import argparse
    
    parser = argparse.ArgumentParser(description='Test the update verifier')
    parser.add_argument('--new-data', help='Path to new data file')
    parser.add_argument('--old-data', help='Path to old data file')
    
    args = parser.parse_args()
    
    # Create sample data if not provided
    if args.new_data:
        try:
            with open(args.new_data, 'r') as f:
                new_data = json.load(f)
        except Exception as e:
            logger.error(f"Error loading new data from {args.new_data}: {e}")
            return False
    else:
        new_data = {
            'house': [
                {'name': 'John Doe', 'title': 'Representative', 'state': 'California', 'party': 'Democrat', 'bioguide_id': 'D000001', 'district': 1},
                {'name': 'Jane Smith', 'title': 'Representative', 'state': 'Texas', 'party': 'Republican', 'bioguide_id': 'S000001', 'district': 2}
            ],
            'senate': [
                {'name': 'Bob Johnson', 'title': 'Senator', 'state': 'New York', 'party': 'Democrat', 'bioguide_id': 'J000001', 'state_rank': 'senior'},
                {'name': 'Alice Brown', 'title': 'Senator', 'state': 'Florida', 'party': 'Republican', 'bioguide_id': 'B000001', 'state_rank': 'junior'}
            ]
        }
    
    if args.old_data:
        try:
            with open(args.old_data, 'r') as f:
                old_data = json.load(f)
        except Exception as e:
            logger.error(f"Error loading old data from {args.old_data}: {e}")
            return False
    else:
        old_data = {
            'house': [
                {'name': 'John Doe', 'title': 'Representative', 'state': 'California', 'party': 'Democrat', 'bioguide_id': 'D000001', 'district': 1},
                {'name': 'Charlie Wilson', 'title': 'Representative', 'state': 'Ohio', 'party': 'Republican', 'bioguide_id': 'W000001', 'district': 3}
            ],
            'senate': [
                {'name': 'Bob Johnson', 'title': 'Senator', 'state': 'New York', 'party': 'Democrat', 'bioguide_id': 'J000001', 'state_rank': 'senior'},
                {'name': 'David Miller', 'title': 'Senator', 'state': 'Nevada', 'party': 'Democrat', 'bioguide_id': 'M000001', 'state_rank': 'junior'}
            ]
        }
    
    # Create update verifier
    verifier = UpdateVerifier()
    
    # Verify update
    is_valid = verifier.verify_update(new_data, old_data)
    
    # Print results
    print(f"Update is valid: {is_valid}")
    
    # Print verification results
    verification = verifier.get_verification_results()
    print(f"Verification errors: {len(verification['errors'])}")
    for error in verification['errors']:
        print(f"  {error}")
    
    print(f"Verification warnings: {len(verification['warnings'])}")
    for warning in verification['warnings']:
        print(f"  {warning}")
    
    return is_valid

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)