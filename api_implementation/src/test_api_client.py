"""
Test script for the Congress API client

This script tests the functionality of the Congress API client
by making various API calls and verifying the results.
"""

import os
import sys
import json
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import modules
from src.congress_api_client import CongressAPIClient, CongressAPIError
from src.config import Config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("api_implementation/logs/test_api_client.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("test_api_client")

def test_api_client():
    """Test the Congress API client"""
    # Create config
    config = Config()
    
    # Get API key
    api_key = config.get_api_key()
    if not api_key:
        logger.error("API key not found. Please set CONGRESS_API_KEY environment variable or configure it in config.json")
        return False
    
    # Create API client
    client = CongressAPIClient(api_key)
    
    # Create results directory
    results_dir = "api_implementation/test_results"
    os.makedirs(results_dir, exist_ok=True)
    
    # Test get_current_congress
    try:
        logger.info("Testing get_current_congress...")
        current_congress = client.get_current_congress()
        logger.info(f"Current Congress: {current_congress}")
        
        # Save result to file
        with open(f"{results_dir}/current_congress.json", "w") as f:
            json.dump({"current_congress": current_congress}, f, indent=2)
        
        logger.info("get_current_congress test passed")
    except CongressAPIError as e:
        logger.error(f"get_current_congress test failed: {e}")
        return False
    
    # Test get_members
    try:
        logger.info("Testing get_members...")
        house_members = client.get_members(current_congress, "house")
        senate_members = client.get_members(current_congress, "senate")
        
        logger.info(f"Retrieved {len(house_members)} House members and {len(senate_members)} Senate members")
        
        # Save results to files
        with open(f"{results_dir}/house_members.json", "w") as f:
            json.dump(house_members, f, indent=2)
        
        with open(f"{results_dir}/senate_members.json", "w") as f:
            json.dump(senate_members, f, indent=2)
        
        logger.info("get_members test passed")
    except CongressAPIError as e:
        logger.error(f"get_members test failed: {e}")
        return False
    
    # Test get_current_members
    try:
        logger.info("Testing get_current_members...")
        current_members = client.get_current_members()
        
        logger.info(f"Retrieved {len(current_members['house'])} current House members and {len(current_members['senate'])} current Senate members")
        
        # Save result to file
        with open(f"{results_dir}/current_members.json", "w") as f:
            json.dump(current_members, f, indent=2)
        
        logger.info("get_current_members test passed")
    except CongressAPIError as e:
        logger.error(f"get_current_members test failed: {e}")
        return False
    
    # Test search_members
    try:
        logger.info("Testing search_members...")
        search_results = client.search_members("Schumer", in_office=True)
        
        logger.info(f"Found {len(search_results)} members matching 'Schumer'")
        
        # Save result to file
        with open(f"{results_dir}/search_results.json", "w") as f:
            json.dump(search_results, f, indent=2)
        
        logger.info("search_members test passed")
    except CongressAPIError as e:
        logger.error(f"search_members test failed: {e}")
        return False
    
    # Test get_member_by_name
    try:
        logger.info("Testing get_member_by_name...")
        member = client.get_member_by_name("Schumer", in_office=True)
        
        if member:
            logger.info(f"Found member: {member['name']}")
            
            # Save result to file
            with open(f"{results_dir}/member_by_name.json", "w") as f:
                json.dump(member, f, indent=2)
            
            logger.info("get_member_by_name test passed")
        else:
            logger.warning("No member found with name 'Schumer'")
    except CongressAPIError as e:
        logger.error(f"get_member_by_name test failed: {e}")
        return False
    
    # Test get_newly_elected_members
    try:
        logger.info("Testing get_newly_elected_members...")
        newly_elected = client.get_newly_elected_members(days=180)
        
        logger.info(f"Found {len(newly_elected['house'])} newly elected House members and {len(newly_elected['senate'])} newly elected Senate members in the last 180 days")
        
        # Save result to file
        with open(f"{results_dir}/newly_elected_members.json", "w") as f:
            json.dump(newly_elected, f, indent=2)
        
        logger.info("get_newly_elected_members test passed")
    except CongressAPIError as e:
        logger.error(f"get_newly_elected_members test failed: {e}")
        return False
    
    # All tests passed
    logger.info("All tests passed!")
    return True

def save_mock_data():
    """Save mock data for testing without API key"""
    # Create results directory
    results_dir = "api_implementation/test_results"
    os.makedirs(results_dir, exist_ok=True)
    
    # Mock current Congress
    with open(f"{results_dir}/current_congress.json", "w") as f:
        json.dump({"current_congress": 117}, f, indent=2)
    
    # Mock House members
    house_members = [
        {
            "id": "A000374",
            "name": "Alma Adams",
            "first_name": "Alma",
            "last_name": "Adams",
            "state": "NC",
            "district": "12",
            "party": "D",
            "in_office": True,
            "url": "https://adams.house.gov",
            "phone": "202-225-1510",
            "office": "2436 Rayburn House Office Building",
            "twitter_account": "RepAdams",
            "facebook_account": "CongresswomanAdams"
        },
        {
            "id": "A000370",
            "name": "Robert Aderholt",
            "first_name": "Robert",
            "last_name": "Aderholt",
            "state": "AL",
            "district": "4",
            "party": "R",
            "in_office": True,
            "url": "https://aderholt.house.gov",
            "phone": "202-225-4876",
            "office": "2302 Rayburn House Office Building",
            "twitter_account": "Robert_Aderholt",
            "facebook_account": "RobertAderholt"
        }
    ]
    with open(f"{results_dir}/house_members.json", "w") as f:
        json.dump(house_members, f, indent=2)
    
    # Mock Senate members
    senate_members = [
        {
            "id": "B001230",
            "name": "Tammy Baldwin",
            "first_name": "Tammy",
            "last_name": "Baldwin",
            "state": "WI",
            "party": "D",
            "in_office": True,
            "url": "https://www.baldwin.senate.gov",
            "phone": "202-224-5653",
            "office": "709 Hart Senate Office Building",
            "twitter_account": "SenatorBaldwin",
            "facebook_account": "senatortammybaldwin"
        },
        {
            "id": "B001261",
            "name": "John Barrasso",
            "first_name": "John",
            "last_name": "Barrasso",
            "state": "WY",
            "party": "R",
            "in_office": True,
            "url": "https://www.barrasso.senate.gov",
            "phone": "202-224-6441",
            "office": "307 Dirksen Senate Office Building",
            "twitter_account": "SenJohnBarrasso",
            "facebook_account": "johnbarrasso"
        }
    ]
    with open(f"{results_dir}/senate_members.json", "w") as f:
        json.dump(senate_members, f, indent=2)
    
    # Mock current members
    current_members = {
        "house": house_members,
        "senate": senate_members
    }
    with open(f"{results_dir}/current_members.json", "w") as f:
        json.dump(current_members, f, indent=2)
    
    # Mock search results
    search_results = [
        {
            "id": "S000148",
            "name": "Chuck Schumer",
            "first_name": "Chuck",
            "last_name": "Schumer",
            "state": "NY",
            "party": "D",
            "in_office": True,
            "url": "https://www.schumer.senate.gov",
            "phone": "202-224-6542",
            "office": "322 Hart Senate Office Building",
            "twitter_account": "SenSchumer",
            "facebook_account": "chuckschumer"
        }
    ]
    with open(f"{results_dir}/search_results.json", "w") as f:
        json.dump(search_results, f, indent=2)
    
    # Mock member by name
    with open(f"{results_dir}/member_by_name.json", "w") as f:
        json.dump(search_results[0], f, indent=2)
    
    # Mock newly elected members
    newly_elected = {
        "house": [
            {
                "id": "N000026",
                "name": "New Representative",
                "first_name": "New",
                "last_name": "Representative",
                "state": "CA",
                "district": "10",
                "party": "D",
                "in_office": True,
                "url": "https://newrep.house.gov",
                "phone": "202-225-1234",
                "office": "1234 Longworth House Office Building",
                "twitter_account": "NewRep",
                "facebook_account": "NewRepresentative",
                "start_date": datetime.now().strftime("%Y-%m-%d")
            }
        ],
        "senate": [
            {
                "id": "N000027",
                "name": "New Senator",
                "first_name": "New",
                "last_name": "Senator",
                "state": "TX",
                "party": "R",
                "in_office": True,
                "url": "https://newsenator.senate.gov",
                "phone": "202-224-5678",
                "office": "5678 Hart Senate Office Building",
                "twitter_account": "NewSenator",
                "facebook_account": "NewSenator",
                "start_date": datetime.now().strftime("%Y-%m-%d")
            }
        ]
    }
    with open(f"{results_dir}/newly_elected_members.json", "w") as f:
        json.dump(newly_elected, f, indent=2)
    
    logger.info("Saved mock data for testing")

if __name__ == "__main__":
    # Create logs directory
    os.makedirs("api_implementation/logs", exist_ok=True)
    
    # Check if API key is available
    api_key = os.environ.get("CONGRESS_API_KEY")
    
    if api_key:
        # Run tests with real API
        logger.info("Running tests with real API")
        success = test_api_client()
        
        if success:
            logger.info("All tests passed!")
            sys.exit(0)
        else:
            logger.error("Tests failed!")
            sys.exit(1)
    else:
        # Save mock data for testing without API key
        logger.warning("API key not found. Saving mock data for testing.")
        save_mock_data()
        logger.info("Mock data saved. Set CONGRESS_API_KEY environment variable to run tests with real API.")
        sys.exit(0)