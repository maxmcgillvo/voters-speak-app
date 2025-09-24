#!/usr/bin/env python3
"""
Verify and Fix Data File Paths

This script verifies that the data file paths in the configuration are correct
and updates them if necessary.
"""

import os
import sys
import json
import logging
from pathlib import Path

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config import config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("api_implementation/logs/verify_paths.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("verify_paths")

def find_file(filename, search_dirs=None):
    """
    Find a file in the specified directories or common locations
    
    Args:
        filename (str): Name of the file to find
        search_dirs (list, optional): List of directories to search
        
    Returns:
        str: Path to the file if found, None otherwise
    """
    if search_dirs is None:
        # Default search directories
        search_dirs = [
            ".",
            "..",
            "/workspace",
            os.path.expanduser("~"),
            os.path.join(os.path.expanduser("~"), "voters_speak")
        ]
    
    logger.info(f"Searching for {filename} in {len(search_dirs)} directories")
    
    for directory in search_dirs:
        # Check if the directory exists
        if not os.path.isdir(directory):
            continue
        
        # Check if the file exists in this directory
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            logger.info(f"Found {filename} at {file_path}")
            return file_path
        
        # Also check subdirectories (one level deep)
        for subdir in os.listdir(directory):
            subdir_path = os.path.join(directory, subdir)
            if os.path.isdir(subdir_path):
                file_path = os.path.join(subdir_path, filename)
                if os.path.isfile(file_path):
                    logger.info(f"Found {filename} at {file_path}")
                    return file_path
    
    logger.warning(f"Could not find {filename} in any of the search directories")
    return None

def verify_data_file_path():
    """
    Verify that the data file path in the configuration is correct
    
    Returns:
        bool: True if the path is correct or was fixed, False otherwise
    """
    # Get the current data file path from the configuration
    current_path = config.get('paths.data_file')
    logger.info(f"Current data file path in configuration: {current_path}")
    
    # Check if the file exists at the current path
    if os.path.isfile(current_path):
        logger.info(f"Data file exists at the current path: {current_path}")
        return True
    
    # Try to find the file
    filename = os.path.basename(current_path)
    file_path = find_file(filename)
    
    if file_path:
        # Update the configuration
        config.set('paths.data_file', file_path)
        logger.info(f"Updated data file path in configuration to: {file_path}")
        return True
    else:
        logger.error(f"Could not find data file: {filename}")
        return False

def verify_directories():
    """
    Verify that the required directories exist and create them if necessary
    
    Returns:
        bool: True if all directories exist or were created, False otherwise
    """
    required_dirs = [
        "api_implementation/logs",
        "api_implementation/data",
        "api_implementation/backups",
        "api_implementation/reports"
    ]
    
    for directory in required_dirs:
        if not os.path.isdir(directory):
            try:
                os.makedirs(directory, exist_ok=True)
                logger.info(f"Created directory: {directory}")
            except Exception as e:
                logger.error(f"Error creating directory {directory}: {e}")
                return False
    
    return True

def main():
    """
    Main function to verify and fix paths
    """
    logger.info("Starting path verification")
    
    # Verify directories
    if not verify_directories():
        logger.error("Failed to verify directories")
        return False
    
    # Verify data file path
    if not verify_data_file_path():
        logger.error("Failed to verify data file path")
        return False
    
    logger.info("Path verification completed successfully")
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)