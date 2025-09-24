#!/usr/bin/env python3
"""
Backup Manager Module

This module provides enhanced backup functionality for the congressional data
update process, including rotation policies and cleanup of old backups.
"""

import os
import sys
import shutil
import logging
import datetime
from typing import List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("api_implementation/logs/backup_manager.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("backup_manager")

class BackupManager:
    """
    Manages backups of data files with rotation policies
    """
    
    def __init__(self, backup_dir: str = "api_implementation/backups", 
                max_backups: int = 10, 
                retention_days: int = 30):
        """
        Initialize the backup manager
        
        Args:
            backup_dir (str): Directory to store backups
            max_backups (int): Maximum number of backups to keep
            retention_days (int): Number of days to keep backups
        """
        self.backup_dir = backup_dir
        self.max_backups = max_backups
        self.retention_days = retention_days
        
        # Create backup directory if it doesn't exist
        os.makedirs(self.backup_dir, exist_ok=True)
    
    def create_backup(self, file_path: str) -> Optional[str]:
        """
        Create a backup of a file
        
        Args:
            file_path (str): Path to the file to backup
            
        Returns:
            str: Path to the backup file, or None if backup failed
        """
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            return None
        
        try:
            # Create timestamp
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Get file name and extension
            file_name = os.path.basename(file_path)
            file_base, file_ext = os.path.splitext(file_name)
            
            # Create backup file name
            backup_file_name = f"{file_base}_{timestamp}{file_ext}"
            backup_path = os.path.join(self.backup_dir, backup_file_name)
            
            # Copy file to backup
            shutil.copy2(file_path, backup_path)
            logger.info(f"Created backup of {file_path} at {backup_path}")
            
            # Rotate backups
            self._rotate_backups(file_base)
            
            return backup_path
        except Exception as e:
            logger.error(f"Failed to create backup of {file_path}: {e}")
            return None
    
    def _rotate_backups(self, file_base: str) -> None:
        """
        Rotate backups based on retention policy
        
        Args:
            file_base (str): Base name of the file (without extension)
        """
        try:
            # Get all backups for this file
            backups = self._get_backups(file_base)
            
            # Apply retention policies
            self._apply_max_backups_policy(backups)
            self._apply_retention_days_policy(backups)
        except Exception as e:
            logger.error(f"Failed to rotate backups for {file_base}: {e}")
    
    def _get_backups(self, file_base: str) -> List[Tuple[str, datetime.datetime]]:
        """
        Get all backups for a file with their timestamps
        
        Args:
            file_base (str): Base name of the file (without extension)
            
        Returns:
            list: List of tuples (backup_path, timestamp)
        """
        backups = []
        
        # List all files in backup directory
        for file_name in os.listdir(self.backup_dir):
            # Check if file is a backup of the specified file
            if file_name.startswith(file_base + "_") and "_" in file_name:
                try:
                    # Extract timestamp
                    timestamp_str = file_name.split("_", 1)[1].split(".")[0]
                    timestamp = datetime.datetime.strptime(timestamp_str, "%Y%m%d_%H%M%S")
                    
                    # Add to list
                    backup_path = os.path.join(self.backup_dir, file_name)
                    backups.append((backup_path, timestamp))
                except (ValueError, IndexError):
                    # Skip files with invalid timestamp format
                    continue
        
        # Sort by timestamp (newest first)
        backups.sort(key=lambda x: x[1], reverse=True)
        
        return backups
    
    def _apply_max_backups_policy(self, backups: List[Tuple[str, datetime.datetime]]) -> None:
        """
        Apply maximum backups policy
        
        Args:
            backups (list): List of tuples (backup_path, timestamp)
        """
        # If we have more backups than the maximum, delete the oldest ones
        if len(backups) > self.max_backups:
            for backup_path, _ in backups[self.max_backups:]:
                try:
                    os.remove(backup_path)
                    logger.info(f"Deleted old backup: {backup_path}")
                except Exception as e:
                    logger.error(f"Failed to delete backup {backup_path}: {e}")
    
    def _apply_retention_days_policy(self, backups: List[Tuple[str, datetime.datetime]]) -> None:
        """
        Apply retention days policy
        
        Args:
            backups (list): List of tuples (backup_path, timestamp)
        """
        # Calculate cutoff date
        cutoff_date = datetime.datetime.now() - datetime.timedelta(days=self.retention_days)
        
        # Delete backups older than cutoff date
        for backup_path, timestamp in backups:
            if timestamp < cutoff_date:
                try:
                    os.remove(backup_path)
                    logger.info(f"Deleted expired backup: {backup_path}")
                except Exception as e:
                    logger.error(f"Failed to delete backup {backup_path}: {e}")
    
    def restore_backup(self, file_path: str, backup_path: Optional[str] = None) -> bool:
        """
        Restore a file from backup
        
        Args:
            file_path (str): Path to restore the file to
            backup_path (str, optional): Path to the backup file to restore.
                                        If None, the most recent backup is used.
            
        Returns:
            bool: True if restore was successful, False otherwise
        """
        try:
            # Get file name and base
            file_name = os.path.basename(file_path)
            file_base, _ = os.path.splitext(file_name)
            
            # If no backup path specified, use the most recent backup
            if not backup_path:
                backups = self._get_backups(file_base)
                if not backups:
                    logger.error(f"No backups found for {file_path}")
                    return False
                backup_path = backups[0][0]
            
            # Check if backup exists
            if not os.path.exists(backup_path):
                logger.error(f"Backup file not found: {backup_path}")
                return False
            
            # Create backup of current file if it exists
            if os.path.exists(file_path):
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                pre_restore_backup = f"{file_path}.pre_restore_{timestamp}"
                shutil.copy2(file_path, pre_restore_backup)
                logger.info(f"Created pre-restore backup at {pre_restore_backup}")
            
            # Copy backup to original location
            shutil.copy2(backup_path, file_path)
            logger.info(f"Restored {file_path} from backup {backup_path}")
            
            return True
        except Exception as e:
            logger.error(f"Failed to restore {file_path} from backup: {e}")
            return False
    
    def list_backups(self, file_path: str) -> List[Tuple[str, datetime.datetime]]:
        """
        List all backups for a file
        
        Args:
            file_path (str): Path to the file
            
        Returns:
            list: List of tuples (backup_path, timestamp)
        """
        # Get file name and base
        file_name = os.path.basename(file_path)
        file_base, _ = os.path.splitext(file_name)
        
        # Get backups
        return self._get_backups(file_base)

# Main function for testing
def main():
    """Main function for testing the backup manager"""
    import tempfile
    
    # Create a test file
    with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as temp:
        temp.write(b"Test content")
        test_file = temp.name
    
    print(f"Created test file: {test_file}")
    
    # Create backup manager
    backup_manager = BackupManager(max_backups=3, retention_days=7)
    
    # Create backups
    for i in range(5):
        backup_path = backup_manager.create_backup(test_file)
        print(f"Created backup {i+1}: {backup_path}")
        
        # Wait a bit to ensure different timestamps
        import time
        time.sleep(1)
    
    # List backups
    backups = backup_manager.list_backups(test_file)
    print(f"Found {len(backups)} backups:")
    for path, timestamp in backups:
        print(f"  {path} - {timestamp}")
    
    # Clean up
    os.unlink(test_file)
    print(f"Deleted test file: {test_file}")

if __name__ == "__main__":
    main()