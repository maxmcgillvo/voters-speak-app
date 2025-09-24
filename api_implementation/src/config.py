"""
Configuration module for the Congress API integration

This module handles configuration settings for the API integration,
including API keys, rate limits, and other settings.
"""

import os
import json
import logging
from typing import Dict, Any, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("config")

class Config:
    """Configuration manager for the API integration"""
    
    # Default configuration values
    DEFAULT_CONFIG = {
        "api": {
            "base_url": "https://api.data.gov/congress/v3",
            "rate_limit": 5000,  # requests per hour
            "rate_limit_window": 3600,  # seconds (1 hour)
            "max_retries": 3
        },
        "update": {
            "schedule": "daily",  # daily, weekly, monthly
            "time": "02:00",  # 24-hour format (2 AM)
            "backup": True,
            "backup_dir": "backups"
        },
        "logging": {
            "level": "INFO",
            "file": "api_implementation/logs/api_integration.log",
            "max_size": 10485760,  # 10 MB
            "backup_count": 5
        },
        "paths": {
            "data_file": "../complete_congress_dataset.js",
            "backup_dir": "api_implementation/backups",
            "log_dir": "api_implementation/logs"
        }
    }
    
    def __init__(self, config_file: Optional[str] = None):
        """
        Initialize configuration
        
        Args:
            config_file (str, optional): Path to configuration file
        """
        # Create instance variables
        self.config_file = config_file or "api_implementation/config.json"
        self.config = self.DEFAULT_CONFIG.copy()
        
        # Load configuration from file if it exists
        self.load_config()
        
        # Ensure directories exist
        self._ensure_directories()
        
        logger.info("Configuration initialized")
    
    def load_config(self) -> None:
        """
        Load configuration from file
        
        If the file doesn't exist, the default configuration is used.
        """
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    file_config = json.load(f)
                
                # Update configuration with values from file
                self._update_nested_dict(self.config, file_config)
                logger.info(f"Loaded configuration from {self.config_file}")
            else:
                logger.warning(f"Configuration file {self.config_file} not found. Using default configuration.")
                # Save default configuration to file
                self.save_config()
        except Exception as e:
            logger.error(f"Error loading configuration: {e}")
    
    def save_config(self) -> None:
        """Save configuration to file"""
        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            
            # Save configuration to file
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            
            logger.info(f"Saved configuration to {self.config_file}")
        except Exception as e:
            logger.error(f"Error saving configuration: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value
        
        Args:
            key (str): Configuration key (dot notation for nested keys)
            default (any, optional): Default value if key not found
            
        Returns:
            any: Configuration value
        """
        # Split key by dots
        keys = key.split('.')
        
        # Navigate through nested dictionaries
        value = self.config
        try:
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default
    
    def set(self, key: str, value: Any) -> None:
        """
        Set configuration value
        
        Args:
            key (str): Configuration key (dot notation for nested keys)
            value (any): Configuration value
        """
        # Split key by dots
        keys = key.split('.')
        
        # Navigate through nested dictionaries
        config = self.config
        for k in keys[:-1]:
            if k not in config or not isinstance(config[k], dict):
                config[k] = {}
            config = config[k]
        
        # Set value
        config[keys[-1]] = value
        
        # Save configuration to file
        self.save_config()
    
    def get_api_key(self) -> Optional[str]:
        """
        Get API key from environment variable or configuration
        
        Returns:
            str: API key, or None if not found
        """
        # Try to get API key from environment variable
        api_key = os.environ.get('CONGRESS_API_KEY')
        
        # If not found, try to get from configuration
        if not api_key:
            api_key = self.get('api.key')
        
        return api_key
    
    def set_api_key(self, api_key: str) -> None:
        """
        Set API key in configuration
        
        Args:
            api_key (str): API key
        """
        self.set('api.key', api_key)
        logger.info("API key set in configuration")
    
    def _update_nested_dict(self, d: Dict[str, Any], u: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update nested dictionary
        
        Args:
            d (dict): Dictionary to update
            u (dict): Dictionary with updates
            
        Returns:
            dict: Updated dictionary
        """
        for k, v in u.items():
            if isinstance(v, dict) and k in d and isinstance(d[k], dict):
                self._update_nested_dict(d[k], v)
            else:
                d[k] = v
        return d
    
    def _ensure_directories(self) -> None:
        """Ensure required directories exist"""
        # Create log directory
        log_dir = self.get('paths.log_dir', 'api_implementation/logs')
        os.makedirs(log_dir, exist_ok=True)
        
        # Create backup directory
        backup_dir = self.get('paths.backup_dir', 'api_implementation/backups')
        os.makedirs(backup_dir, exist_ok=True)


# Singleton instance
config = Config()

# Example usage
if __name__ == "__main__":
    # Get configuration values
    api_base_url = config.get('api.base_url')
    rate_limit = config.get('api.rate_limit')
    log_level = config.get('logging.level')
    
    print(f"API Base URL: {api_base_url}")
    print(f"API Rate Limit: {rate_limit}")
    print(f"Log Level: {log_level}")
    
    # Set configuration values
    config.set('api.rate_limit', 4000)
    print(f"Updated API Rate Limit: {config.get('api.rate_limit')}")
    
    # Get API key
    api_key = config.get_api_key()
    if api_key:
        print(f"API Key: {api_key[:5]}...")
    else:
        print("API Key not found")