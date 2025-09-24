"""
Test script to verify the API key for Congress.gov API
"""

import os
import sys
import logging

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config import config
from src.congress_api_client import CongressAPIClient, CongressAPIError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("api_implementation/logs/api_key_test.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("api_key_test")

def main():
    """
    Main function to test the API key
    """
    # Get API key from command line argument or environment variable
    api_key = sys.argv[1] if len(sys.argv) > 1 else os.environ.get('CONGRESS_API_KEY')
    
    if not api_key:
        logger.error("API key not provided. Please provide as command line argument or set CONGRESS_API_KEY environment variable.")
        sys.exit(1)
    
    # Update configuration with API key
    config.set_api_key(api_key)
    logger.info(f"Updated configuration with API key: {api_key[:5]}...")
    
    try:
        # Create API client
        client = CongressAPIClient(api_key)
        logger.info("Created API client successfully")
        
        # Test API key with a simple request
        logger.info("Testing API key with a request to get current Congress...")
        current_congress = client.get_current_congress()
        logger.info(f"API key is valid! Current Congress: {current_congress}")
        
        # Test getting members
        logger.info(f"Testing getting members for {current_congress}th Congress, House...")
        house_members = client.get_members(current_congress, 'house')
        logger.info(f"Successfully retrieved {len(house_members)} House members")
        
        logger.info(f"Testing getting members for {current_congress}th Congress, Senate...")
        senate_members = client.get_members(current_congress, 'senate')
        logger.info(f"Successfully retrieved {len(senate_members)} Senate members")
        
        # Print sample data
        if house_members:
            logger.info(f"Sample House member: {house_members[0]}")
        if senate_members:
            logger.info(f"Sample Senate member: {senate_members[0]}")
        
        logger.info("API key verification completed successfully!")
        return True
    
    except CongressAPIError as e:
        logger.error(f"API Error: {e}")
        return False
    except Exception as e:
        logger.error(f"Error: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)