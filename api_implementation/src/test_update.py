#!/usr/bin/env python3
"""
Test script for the congressional data update implementation

This script tests the update_congress_data module by running a test update
and verifying the results.
"""

import os
import sys
import json
import logging
import argparse
from typing import Dict, List, Any

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config import config
from src.update_congress_data import update_congress_data, load_json_data, transform_legislators_data

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("api_implementation/logs/test_update.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("test_update")

def test_data_transformation() -> bool:
    """
    Test the data transformation function
    
    Returns:
        bool: True if test passed, False otherwise
    """
    logger.info("Testing data transformation")
    
    # Look for test data in multiple locations
    test_data_paths = [
        "api_implementation/legislators-current.json",
        "../legislators-current.json",
        "legislators-current.json"
    ]
    
    test_data_path = None
    for path in test_data_paths:
        if os.path.exists(path):
            test_data_path = path
            break
    
    if not test_data_path:
        logger.error(f"Test data file not found. Tried: {', '.join(test_data_paths)}")
        return False
    
    logger.info(f"Using test data from {test_data_path}")
    test_data = load_json_data(test_data_path)
    if not test_data:
        return False
    
    # Transform data
    transformed_data = transform_legislators_data(test_data)
    
    # Verify transformation
    if not transformed_data:
        logger.error("Transformation returned empty result")
        return False
    
    if 'house' not in transformed_data or 'senate' not in transformed_data:
        logger.error("Transformation result missing 'house' or 'senate' keys")
        return False
    
    house_count = len(transformed_data['house'])
    senate_count = len(transformed_data['senate'])
    
    logger.info(f"Transformation produced {house_count} House members and {senate_count} Senate members")
    
    # Verify at least some data was transformed
    if house_count == 0 and senate_count == 0:
        logger.error("Transformation produced no members")
        return False
    
    # Verify data structure for a sample member
    if house_count > 0:
        sample_member = transformed_data['house'][0]
        required_fields = ['name', 'title', 'state', 'party']
        for field in required_fields:
            if field not in sample_member:
                logger.error(f"Sample House member missing required field: {field}")
                return False
    
    if senate_count > 0:
        sample_member = transformed_data['senate'][0]
        required_fields = ['name', 'title', 'state', 'party']
        for field in required_fields:
            if field not in sample_member:
                logger.error(f"Sample Senate member missing required field: {field}")
                return False
    
    logger.info("Data transformation test passed")
    return True

def test_full_update(test_mode: bool = True) -> bool:
    """
    Test the full update process
    
    Args:
        test_mode (bool): Whether to run in test mode (no actual file updates)
        
    Returns:
        bool: True if test passed, False otherwise
    """
    logger.info("Testing full update process")
    
    if test_mode:
        # Set test configuration
        original_data_file = config.get('paths.data_file')
        test_data_file = "api_implementation/test_output/test_congress_dataset.js"
        config.set('paths.data_file', test_data_file)
        
        # Create test directory
        os.makedirs(os.path.dirname(test_data_file), exist_ok=True)
    
    try:
        # Run update
        success = update_congress_data()
        
        if not success:
            logger.error("Update process failed")
            return False
        
        logger.info("Full update test passed")
        return True
    finally:
        if test_mode:
            # Restore original configuration
            config.set('paths.data_file', original_data_file)

def main() -> None:
    """
    Main function to run tests
    """
    parser = argparse.ArgumentParser(description='Test congressional data update implementation')
    parser.add_argument('--transform-only', action='store_true', help='Test only data transformation')
    parser.add_argument('--full-update', action='store_true', help='Test full update process')
    parser.add_argument('--live', action='store_true', help='Run tests on live data files (not test mode)')
    
    args = parser.parse_args()
    
    # Create directories if they don't exist
    os.makedirs("api_implementation/logs", exist_ok=True)
    os.makedirs("api_implementation/test_output", exist_ok=True)
    
    all_tests_passed = True
    
    if args.transform_only or not (args.transform_only or args.full_update):
        transform_test_passed = test_data_transformation()
        all_tests_passed = all_tests_passed and transform_test_passed
    
    if args.full_update or not (args.transform_only or args.full_update):
        full_update_test_passed = test_full_update(not args.live)
        all_tests_passed = all_tests_passed and full_update_test_passed
    
    if all_tests_passed:
        logger.info("All tests passed!")
        sys.exit(0)
    else:
        logger.error("Some tests failed")
        sys.exit(1)

if __name__ == "__main__":
    main()