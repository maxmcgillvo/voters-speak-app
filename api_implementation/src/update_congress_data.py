#!/usr/bin/env python3
"""
Update Congress Data Script

This script updates the congressional data in the Voters Speak application
using data from the United States Project (unitedstates/congress-legislators).

It downloads the latest data from the GitHub repository, processes it,
and updates the application's data files.
"""

import os
import sys
import json
import logging
import datetime
import requests
from typing import Dict, List, Any, Optional, Union, Tuple

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config import config
from src.utils import load_js_data, save_js_data
from src.data_mapper import DataMapper
from src.backup_manager import BackupManager
from src.report_generator import ReportGenerator
from src.update_verifier import UpdateVerifier

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("api_implementation/logs/update_congress_data.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("update_congress_data")

# URLs for the United States Project data
CURRENT_LEGISLATORS_URL = "https://unitedstates.github.io/congress-legislators/legislators-current.json"
HISTORICAL_LEGISLATORS_URL = "https://unitedstates.github.io/congress-legislators/legislators-historical.json"
SOCIAL_MEDIA_URL = "https://unitedstates.github.io/congress-legislators/legislators-social-media.json"
COMMITTEES_CURRENT_URL = "https://unitedstates.github.io/congress-legislators/committees-current.json"
COMMITTEE_MEMBERSHIP_URL = "https://unitedstates.github.io/congress-legislators/committee-membership-current.json"

def download_data(url: str, local_path: str) -> bool:
    """
    Download data from a URL and save it to a local file
    
    Args:
        url (str): URL to download from
        local_path (str): Path to save the downloaded file
        
    Returns:
        bool: True if download was successful, False otherwise
    """
    try:
        logger.info(f"Downloading data from {url}")
        response = requests.get(url)
        response.raise_for_status()
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        
        # Save data to file
        with open(local_path, 'w') as f:
            f.write(response.text)
            
        logger.info(f"Downloaded data saved to {local_path}")
        return True
    except Exception as e:
        logger.error(f"Error downloading data from {url}: {e}")
        return False

def load_json_data(file_path: str) -> Optional[List[Dict[str, Any]]]:
    """
    Load JSON data from a file
    
    Args:
        file_path (str): Path to the JSON file
        
    Returns:
        list: List of dictionaries containing the JSON data, or None if error
    """
    try:
        logger.info(f"Loading JSON data from {file_path}")
        with open(file_path, 'r') as f:
            data = json.load(f)
        logger.info(f"Loaded {len(data)} records from {file_path}")
        return data
    except Exception as e:
        logger.error(f"Error loading JSON data from {file_path}: {e}")
        return None

def transform_legislators_data(current_data: List[Dict[str, Any]], 
                              social_media_data: Optional[List[Dict[str, Any]]] = None) -> Tuple[Dict[str, List[Dict[str, Any]]], Dict[str, List[str]]]:
    """
    Transform legislators data from the United States Project format to the Voters Speak format
    
    Args:
        current_data (list): List of current legislators
        social_media_data (list, optional): List of social media data
        
    Returns:
        tuple: (transformed_data, validation_results)
            transformed_data: Dictionary with 'house' and 'senate' keys containing lists of legislators
            validation_results: Dictionary with 'errors' and 'warnings' keys containing lists of messages
    """
    logger.info("Transforming legislators data")
    
    # Create data mapper
    mapper = DataMapper()
    
    # Transform data
    transformed_data = mapper.transform_legislators(current_data, social_media_data)
    
    # Get validation results
    validation_results = mapper.get_validation_results()
    
    # Log results
    house_count = len(transformed_data['house'])
    senate_count = len(transformed_data['senate'])
    logger.info(f"Transformed {house_count} House members and {senate_count} Senate members")
    
    return transformed_data, validation_results

def compare_data(new_data: Dict[str, List[Dict[str, Any]]], 
                old_data: Optional[Dict[str, List[Dict[str, Any]]]] = None) -> Tuple[Dict[str, List[Dict[str, Any]]], Dict[str, List[Dict[str, Any]]], Dict[str, List[Dict[str, Any]]]]:
    """
    Compare new data with old data to identify changes
    
    Args:
        new_data (dict): Dictionary with 'house' and 'senate' keys containing lists of legislators
        old_data (dict, optional): Dictionary with 'house' and 'senate' keys containing lists of legislators
        
    Returns:
        tuple: (new_members, updated_members, removed_members)
            new_members: Dictionary with 'house' and 'senate' keys containing lists of new members
            updated_members: Dictionary with 'house' and 'senate' keys containing lists of updated members
            removed_members: Dictionary with 'house' and 'senate' keys containing lists of removed members
    """
    # Initialize result
    new_members = {'house': [], 'senate': []}
    updated_members = {'house': [], 'senate': []}
    removed_members = {'house': [], 'senate': []}
    
    # If no old data, all members are new
    if not old_data:
        new_members = new_data
        return new_members, updated_members, removed_members
    
    # Compare House members
    old_house_by_id = {member.get('bioguide_id'): member for member in old_data['house'] if member.get('bioguide_id')}
    new_house_by_id = {member.get('bioguide_id'): member for member in new_data['house'] if member.get('bioguide_id')}
    
    # Find new and updated House members
    for bioguide_id, member in new_house_by_id.items():
        if bioguide_id not in old_house_by_id:
            new_members['house'].append(member)
        elif member != old_house_by_id[bioguide_id]:
            updated_members['house'].append(member)
    
    # Find removed House members
    for bioguide_id, member in old_house_by_id.items():
        if bioguide_id not in new_house_by_id:
            removed_members['house'].append(member)
    
    # Compare Senate members
    old_senate_by_id = {member.get('bioguide_id'): member for member in old_data['senate'] if member.get('bioguide_id')}
    new_senate_by_id = {member.get('bioguide_id'): member for member in new_data['senate'] if member.get('bioguide_id')}
    
    # Find new and updated Senate members
    for bioguide_id, member in new_senate_by_id.items():
        if bioguide_id not in old_senate_by_id:
            new_members['senate'].append(member)
        elif member != old_senate_by_id[bioguide_id]:
            updated_members['senate'].append(member)
    
    # Find removed Senate members
    for bioguide_id, member in old_senate_by_id.items():
        if bioguide_id not in new_senate_by_id:
            removed_members['senate'].append(member)
    
    return new_members, updated_members, removed_members

def update_congress_data() -> bool:
    """
    Update congressional data in the Voters Speak application
    
    Returns:
        bool: True if update was successful, False otherwise
    """
    try:
        # Create data directory if it doesn't exist
        os.makedirs("api_implementation/data", exist_ok=True)
        
        # Create logs directory if it doesn't exist
        os.makedirs("api_implementation/logs", exist_ok=True)
        
        # Create reports directory if it doesn't exist
        os.makedirs("api_implementation/reports", exist_ok=True)
        
        # Create backup manager
        backup_manager = BackupManager()
        
        # Create report generator
        report_generator = ReportGenerator()
        
        # Create update verifier
        update_verifier = UpdateVerifier()
        
        # Download current legislators data
        current_legislators_path = "api_implementation/data/legislators-current.json"
        if not download_data(CURRENT_LEGISLATORS_URL, current_legislators_path):
            return False
        
        # Download historical legislators data
        historical_legislators_path = "api_implementation/data/legislators-historical.json"
        if not download_data(HISTORICAL_LEGISLATORS_URL, historical_legislators_path):
            return False
        
        # Download social media data
        social_media_path = "api_implementation/data/legislators-social-media.json"
        if not download_data(SOCIAL_MEDIA_URL, social_media_path):
            return False
        
        # Load current legislators data
        current_data = load_json_data(current_legislators_path)
        if not current_data:
            return False
        
        # Load social media data
        social_media_data = load_json_data(social_media_path)
        
        # Transform data
        transformed_data, validation_results = transform_legislators_data(current_data, social_media_data)
        
        # Get path to application data file
        data_file = config.get('paths.data_file', '../complete_congress_dataset.js')
        
        # Load existing data
        try:
            existing_data = load_js_data(data_file)
        except Exception as e:
            logger.warning(f"Could not load existing data from {data_file}: {e}")
            logger.warning("Will create new data file")
            existing_data = None
        
        # Verify transformed data
        if not update_verifier.verify_update(transformed_data, existing_data):
            verification_results = update_verifier.get_verification_results()
            logger.error("Update verification failed")
            for error in verification_results['errors']:
                logger.error(f"  {error}")
            
            # Add verification results to validation results
            if 'errors' not in validation_results:
                validation_results['errors'] = []
            if 'warnings' not in validation_results:
                validation_results['warnings'] = []
            
            validation_results['errors'].extend(verification_results['errors'])
            validation_results['warnings'].extend(verification_results['warnings'])
            
            # Generate report even though verification failed
            report_path = report_generator.generate_update_report(
                {'house': [], 'senate': []},
                {'house': [], 'senate': []},
                {'house': [], 'senate': []},
                validation_results
            )
            logger.info(f"Generated verification failure report at {report_path}")
            
            return False
        
        # Compare data to identify changes
        new_members, updated_members, removed_members = compare_data(transformed_data, existing_data)
        
        # Log changes
        logger.info(f"House: {len(new_members['house'])} new, {len(updated_members['house'])} updated, {len(removed_members['house'])} removed")
        logger.info(f"Senate: {len(new_members['senate'])} new, {len(updated_members['senate'])} updated, {len(removed_members['senate'])} removed")
        
        # Generate update report
        report_path = report_generator.generate_update_report(
            new_members, updated_members, removed_members, validation_results
        )
        logger.info(f"Generated update report at {report_path}")
        
        # Create HTML report
        html_report_path = report_generator.generate_html_report(report_path)
        if html_report_path:
            logger.info(f"Generated HTML report at {html_report_path}")
        
        # Create backup of existing data file if it exists
        if existing_data and os.path.exists(data_file):
            backup_path = backup_manager.create_backup(data_file)
            if backup_path:
                logger.info(f"Created backup of {data_file} at {backup_path}")
        
        # Save updated data
        save_js_data(data_file, transformed_data)
        logger.info(f"Saved updated data to {data_file}")
        
        # Log update summary
        logger.info(f"Update complete. House: {len(new_members['house'])} new, {len(updated_members['house'])} updated, {len(removed_members['house'])} removed")
        logger.info(f"Senate: {len(new_members['senate'])} new, {len(updated_members['senate'])} updated, {len(removed_members['senate'])} removed")
        
        # Send email notification if configured
        email_recipients = config.get('notification.email_recipients', [])
        if email_recipients:
            report_generator.send_email_notification(
                report_path,
                email_recipients,
                "Congressional Data Update Report"
            )
        
        return True
    except Exception as e:
        logger.error(f"Error updating congressional data: {e}")
        return False

# Main function
def main():
    """Main function"""
    success = update_congress_data()
    if success:
        logger.info("Congressional data update completed successfully")
    else:
        logger.error("Congressional data update failed")
        sys.exit(1)

if __name__ == "__main__":
    main()