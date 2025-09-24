"""
Congress.gov API Client

This module provides a robust client for interacting with the Congress.gov API.
It handles authentication, rate limiting, error handling, and logging.
"""

import os
import time
import json
import logging
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("api_implementation/logs/congress_api.log"),
        logging.StreamHandler()
    ]
)

# Create logger
logger = logging.getLogger("congress_api")

class CongressAPIError(Exception):
    """Base exception for Congress API errors"""
    pass

class RateLimitExceededError(CongressAPIError):
    """Exception raised when API rate limit is exceeded"""
    pass

class AuthenticationError(CongressAPIError):
    """Exception raised when API authentication fails"""
    pass

class APIRequestError(CongressAPIError):
    """Exception raised when API request fails"""
    pass

class CongressAPIClient:
    """
    Client for interacting with the Congress.gov API
    
    This client handles authentication, rate limiting, error handling, and logging.
    It provides methods for accessing various endpoints of the Congress.gov API.
    """
    
    # API base URL
    BASE_URL = "https://api.data.gov/congress/v3"
    
    # Default rate limits
    DEFAULT_RATE_LIMIT = 5000  # requests per hour
    DEFAULT_RATE_LIMIT_WINDOW = 3600  # seconds (1 hour)
    
    def __init__(self, api_key: Optional[str] = None, 
                 rate_limit: int = DEFAULT_RATE_LIMIT,
                 rate_limit_window: int = DEFAULT_RATE_LIMIT_WINDOW):
        """
        Initialize the Congress.gov API client
        
        Args:
            api_key (str, optional): API key for Congress.gov API. If not provided,
                                    will look for CONGRESS_API_KEY environment variable.
            rate_limit (int): Maximum number of requests allowed in the rate limit window
            rate_limit_window (int): Rate limit window in seconds
        
        Raises:
            AuthenticationError: If API key is not provided or invalid
        """
        # Get API key from parameter or environment variable
        self.api_key = api_key or os.environ.get('CONGRESS_API_KEY')
        if not self.api_key:
            raise AuthenticationError(
                "API key is required. Set CONGRESS_API_KEY environment variable or pass api_key parameter."
            )
        
        # Set up rate limiting
        self.rate_limit = rate_limit
        self.rate_limit_window = rate_limit_window
        self.request_timestamps = []
        
        # Set up session
        self.session = requests.Session()
        self.session.headers.update({
            'X-API-Key': self.api_key,
            'Accept': 'application/json'
        })
        
        logger.info(f"Initialized Congress API client with rate limit of {rate_limit} requests per {rate_limit_window} seconds")
    
    def _enforce_rate_limit(self):
        """
        Enforce rate limiting by tracking request timestamps and sleeping if necessary
        
        This method tracks the timestamps of API requests and sleeps if the rate limit
        would be exceeded by making another request.
        
        Raises:
            RateLimitExceededError: If rate limit is exceeded and cannot be resolved by sleeping
        """
        # Remove timestamps older than the rate limit window
        current_time = time.time()
        self.request_timestamps = [ts for ts in self.request_timestamps 
                                  if current_time - ts < self.rate_limit_window]
        
        # Check if making a new request would exceed the rate limit
        if len(self.request_timestamps) >= self.rate_limit:
            # Calculate how long to sleep
            oldest_timestamp = min(self.request_timestamps)
            sleep_time = oldest_timestamp + self.rate_limit_window - current_time
            
            if sleep_time > 300:  # If we need to sleep more than 5 minutes
                raise RateLimitExceededError(
                    f"Rate limit exceeded. Would need to sleep for {sleep_time:.2f} seconds."
                )
            
            logger.warning(f"Rate limit approaching. Sleeping for {sleep_time:.2f} seconds")
            time.sleep(sleep_time + 0.1)  # Add a small buffer
            
            # Recursive call to check again after sleeping
            return self._enforce_rate_limit()
        
        # Add current timestamp to the list
        self.request_timestamps.append(current_time)
    
    def _make_request(self, endpoint: str, params: Optional[Dict[str, Any]] = None, 
                     method: str = 'GET', max_retries: int = 3) -> Dict[str, Any]:
        """
        Make a request to the Congress.gov API with rate limiting and error handling
        
        Args:
            endpoint (str): API endpoint to call (without base URL)
            params (dict, optional): Query parameters
            method (str): HTTP method (GET, POST, etc.)
            max_retries (int): Maximum number of retries for transient errors
        
        Returns:
            dict: JSON response from the API
        
        Raises:
            AuthenticationError: If API key is invalid
            RateLimitExceededError: If rate limit is exceeded
            APIRequestError: If API request fails
        """
        # Enforce rate limiting
        self._enforce_rate_limit()
        
        # Build URL
        url = f"{self.BASE_URL}/{endpoint}"
        params = params or {}
        
        # Add format parameter if not already present
        if 'format' not in params:
            params['format'] = 'json'
        
        # Log request
        logger.debug(f"Making {method} request to {url} with params {params}")
        
        # Make request with retries
        retries = 0
        while retries <= max_retries:
            try:
                if method.upper() == 'GET':
                    response = self.session.get(url, params=params)
                elif method.upper() == 'POST':
                    response = self.session.post(url, json=params)
                else:
                    raise ValueError(f"Unsupported HTTP method: {method}")
                
                # Print response details for debugging
                print(f"Response status: {response.status_code}")
                print(f"Response headers: {response.headers}")
                print(f"Response body: {response.text[:500]}...")  # Print first 500 chars
                
                # Check for HTTP errors
                response.raise_for_status()
                
                # Parse JSON response
                try:
                    data = response.json()
                    return data
                except json.JSONDecodeError:
                    raise APIRequestError(f"Invalid JSON response: {response.text}")
            
            except requests.exceptions.HTTPError as e:
                # Handle specific HTTP errors
                if e.response.status_code == 401:
                    raise AuthenticationError("Invalid API key")
                elif e.response.status_code == 429:
                    # Rate limit exceeded
                    retry_after = int(e.response.headers.get('Retry-After', 60))
                    if retries < max_retries:
                        logger.warning(f"Rate limit exceeded. Retrying after {retry_after} seconds")
                        time.sleep(retry_after)
                        retries += 1
                        continue
                    else:
                        raise RateLimitExceededError(f"Rate limit exceeded. Retry after {retry_after} seconds")
                elif e.response.status_code >= 500:
                    # Server error, retry
                    if retries < max_retries:
                        sleep_time = 2 ** retries  # Exponential backoff
                        logger.warning(f"Server error ({e.response.status_code}). Retrying after {sleep_time} seconds")
                        time.sleep(sleep_time)
                        retries += 1
                        continue
                    else:
                        raise APIRequestError(f"Server error after {max_retries} retries: {e}")
                else:
                    # Other HTTP error
                    raise APIRequestError(f"HTTP error: {e}")
            
            except requests.exceptions.RequestException as e:
                # Handle network errors
                if retries < max_retries:
                    sleep_time = 2 ** retries  # Exponential backoff
                    logger.warning(f"Network error: {e}. Retrying after {sleep_time} seconds")
                    time.sleep(sleep_time)
                    retries += 1
                    continue
                else:
                    raise APIRequestError(f"Network error after {max_retries} retries: {e}")
        
        # This should not be reached, but just in case
        raise APIRequestError("Maximum retries exceeded")
    
    def get_members(self, congress: int, chamber: str) -> List[Dict[str, Any]]:
        """
        Get members of Congress for a specific congress and chamber
        
        Args:
            congress (int): Congress number (e.g., 117)
            chamber (str): Chamber ('house' or 'senate')
        
        Returns:
            list: List of members
        
        Raises:
            ValueError: If chamber is invalid
            APIRequestError: If API request fails
        """
        # Validate chamber
        if chamber.lower() not in ['house', 'senate']:
            raise ValueError("Chamber must be 'house' or 'senate'")
        
        # Make request
        endpoint = f"member"
        params = {
            'congress': congress,
            'chamber': chamber.lower(),
            'format': 'json'
        }
        
        try:
            logger.info(f"Getting members for {congress}th Congress, {chamber}")
            response = self._make_request(endpoint, params)
            
            # Extract members from response
            members = response.get('members', [])
            logger.info(f"Retrieved {len(members)} members for {congress}th Congress, {chamber}")
            
            return members
        
        except CongressAPIError as e:
            logger.error(f"Failed to get members: {e}")
            raise
    
    def get_member_details(self, member_id: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific member
        
        Args:
            member_id (str): Member ID
        
        Returns:
            dict: Member details
        
        Raises:
            APIRequestError: If API request fails
        """
        # Make request
        endpoint = f"member/{member_id}"
        
        try:
            logger.info(f"Getting details for member {member_id}")
            response = self._make_request(endpoint)
            
            # Extract member details from response
            member = response.get('member', {})
            logger.info(f"Retrieved details for member {member_id}")
            
            return member
        
        except CongressAPIError as e:
            logger.error(f"Failed to get member details for {member_id}: {e}")
            raise
    
    def get_current_congress(self) -> int:
        """
        Get the current Congress number
        
        Returns:
            int: Current Congress number
        
        Raises:
            APIRequestError: If API request fails
        """
        # Make request to get current Congress
        endpoint = "congress"
        
        try:
            logger.info("Getting current Congress number")
            response = self._make_request(endpoint)
            
            # Extract current Congress from response
            congresses = response.get('congresses', [])
            if not congresses:
                raise APIRequestError("No Congress data returned")
            
            # Get the most recent Congress
            current_congress = max(congresses, key=lambda c: c.get('endYear', 0))
            congress_number = current_congress.get('number')
            
            if not congress_number:
                raise APIRequestError("Could not determine current Congress number")
            
            logger.info(f"Current Congress is {congress_number}")
            return int(congress_number)
        
        except CongressAPIError as e:
            logger.error(f"Failed to get current Congress: {e}")
            raise
    
    def get_current_members(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Get all current members of Congress (House and Senate)
        
        Returns:
            dict: Dictionary with 'house' and 'senate' keys containing lists of members
        
        Raises:
            APIRequestError: If API request fails
        """
        try:
            # Get current Congress number
            current_congress = self.get_current_congress()
            
            # Get House members
            house_members = self.get_members(current_congress, 'house')
            
            # Get Senate members
            senate_members = self.get_members(current_congress, 'senate')
            
            # Filter to only current members
            current_house = [m for m in house_members if m.get('in_office', False)]
            current_senate = [m for m in senate_members if m.get('in_office', False)]
            
            logger.info(f"Retrieved {len(current_house)} current House members and {len(current_senate)} current Senate members")
            
            return {
                'house': current_house,
                'senate': current_senate
            }
        
        except CongressAPIError as e:
            logger.error(f"Failed to get current members: {e}")
            raise
    
    def search_members(self, query: str, congress: Optional[int] = None, 
                      chamber: Optional[str] = None, state: Optional[str] = None,
                      party: Optional[str] = None, in_office: Optional[bool] = None) -> List[Dict[str, Any]]:
        """
        Search for members of Congress
        
        Args:
            query (str): Search query
            congress (int, optional): Congress number
            chamber (str, optional): Chamber ('house' or 'senate')
            state (str, optional): State abbreviation
            party (str, optional): Party ('D', 'R', 'I', etc.)
            in_office (bool, optional): Whether member is currently in office
        
        Returns:
            list: List of members matching the search criteria
        
        Raises:
            ValueError: If chamber is invalid
            APIRequestError: If API request fails
        """
        # Validate chamber if provided
        if chamber and chamber.lower() not in ['house', 'senate']:
            raise ValueError("Chamber must be 'house' or 'senate'")
        
        # Make request
        endpoint = "member/search"
        params = {'query': query}
        
        # Add optional parameters
        if congress:
            params['congress'] = congress
        if chamber:
            params['chamber'] = chamber.lower()
        if state:
            params['state'] = state.upper()
        if party:
            params['party'] = party.upper()
        if in_office is not None:
            params['in_office'] = 'true' if in_office else 'false'
        
        try:
            logger.info(f"Searching for members with query: {query}")
            response = self._make_request(endpoint, params)
            
            # Extract members from response
            members = response.get('members', [])
            logger.info(f"Found {len(members)} members matching query: {query}")
            
            return members
        
        except CongressAPIError as e:
            logger.error(f"Failed to search members: {e}")
            raise
    
    def get_member_by_name(self, name: str, congress: Optional[int] = None, 
                          chamber: Optional[str] = None, in_office: bool = True) -> Optional[Dict[str, Any]]:
        """
        Get a member of Congress by name
        
        Args:
            name (str): Member name
            congress (int, optional): Congress number
            chamber (str, optional): Chamber ('house' or 'senate')
            in_office (bool): Whether member is currently in office
        
        Returns:
            dict: Member details, or None if not found
        
        Raises:
            ValueError: If chamber is invalid
            APIRequestError: If API request fails
        """
        try:
            # Search for member by name
            members = self.search_members(
                query=name,
                congress=congress,
                chamber=chamber,
                in_office=in_office
            )
            
            # Return first match, or None if no matches
            if members:
                return members[0]
            else:
                logger.warning(f"No member found with name: {name}")
                return None
        
        except CongressAPIError as e:
            logger.error(f"Failed to get member by name: {e}")
            raise
    
    def get_newly_elected_members(self, days: int = 90) -> Dict[str, List[Dict[str, Any]]]:
        """
        Get newly elected members of Congress
        
        Args:
            days (int): Number of days to look back
        
        Returns:
            dict: Dictionary with 'house' and 'senate' keys containing lists of newly elected members
        
        Raises:
            APIRequestError: If API request fails
        """
        try:
            # Get current members
            current_members = self.get_current_members()
            
            # Calculate cutoff date
            cutoff_date = datetime.now() - timedelta(days=days)
            cutoff_str = cutoff_date.strftime('%Y-%m-%d')
            
            # Filter to newly elected members
            newly_elected_house = [
                m for m in current_members['house']
                if m.get('start_date') and m.get('start_date') >= cutoff_str
            ]
            
            newly_elected_senate = [
                m for m in current_members['senate']
                if m.get('start_date') and m.get('start_date') >= cutoff_str
            ]
            
            logger.info(f"Found {len(newly_elected_house)} newly elected House members and {len(newly_elected_senate)} newly elected Senate members in the last {days} days")
            
            return {
                'house': newly_elected_house,
                'senate': newly_elected_senate
            }
        
        except CongressAPIError as e:
            logger.error(f"Failed to get newly elected members: {e}")
            raise


# Example usage
if __name__ == "__main__":
    try:
        # Create API client
        api_key = os.environ.get('CONGRESS_API_KEY')
        if not api_key:
            print("Please set the CONGRESS_API_KEY environment variable")
            exit(1)
        
        client = CongressAPIClient(api_key)
        
        # Get current Congress
        current_congress = client.get_current_congress()
        print(f"Current Congress: {current_congress}")
        
        # Get current members
        current_members = client.get_current_members()
        print(f"Current House members: {len(current_members['house'])}")
        print(f"Current Senate members: {len(current_members['senate'])}")
        
        # Search for a member
        search_results = client.search_members("Schumer", in_office=True)
        print(f"Search results for 'Schumer': {len(search_results)}")
        if search_results:
            print(f"First result: {search_results[0]['name']}")
        
        # Get newly elected members
        newly_elected = client.get_newly_elected_members(days=180)
        print(f"Newly elected House members (last 180 days): {len(newly_elected['house'])}")
        print(f"Newly elected Senate members (last 180 days): {len(newly_elected['senate'])}")
        
    except CongressAPIError as e:
        print(f"API Error: {e}")
    except Exception as e:
        print(f"Error: {e}")