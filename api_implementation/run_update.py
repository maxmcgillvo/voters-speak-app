#!/usr/bin/env python3
"""
Run Update Script

This script provides a simple command-line interface to run the congressional data update.
"""

import os
import sys
import argparse
import logging
import traceback
from datetime import datetime

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.update_congress_data import update_congress_data
from src.scheduler import run_scheduler
from src.verify_paths import verify_directories, verify_data_file_path
from src.notification_manager import NotificationManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("api_implementation/logs/run_update.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("run_update")

def setup_environment():
    """
    Set up the environment for running updates
    
    Returns:
        bool: True if setup was successful, False otherwise
    """
    # Verify directories
    if not verify_directories():
        logger.error("Failed to verify directories")
        return False
    
    # Verify data file path
    if not verify_data_file_path():
        logger.error("Failed to verify data file path")
        return False
    
    return True

def main():
    """
    Main function to parse arguments and run the update
    """
    parser = argparse.ArgumentParser(description='Run congressional data update')
    parser.add_argument('--schedule', choices=['daily', 'weekly', 'monthly'], 
                      help='Schedule type (daily, weekly, monthly)')
    parser.add_argument('--time', help='Time to run update (HH:MM format)')
    parser.add_argument('--daemon', action='store_true', help='Run as daemon process')
    parser.add_argument('--now', action='store_true', help='Run update immediately')
    parser.add_argument('--notify', action='store_true', help='Send email notifications')
    parser.add_argument('--recipients', help='Comma-separated list of email recipients for notifications')
    
    args = parser.parse_args()
    
    # Set up environment
    if not setup_environment():
        logger.error("Environment setup failed")
        sys.exit(1)
    
    # Create notification manager
    notification_manager = NotificationManager()
    
    # Update recipients if provided
    if args.recipients:
        recipients = [r.strip() for r in args.recipients.split(',')]
        notification_manager.default_recipients = recipients
    
    if args.now:
        logger.info("Running update now")
        try:
            success = update_congress_data()
            if success:
                logger.info("Update completed successfully")
                
                # Send success notification if requested
                if args.notify:
                    # Find the latest report
                    reports_dir = "api_implementation/reports"
                    if os.path.exists(reports_dir):
                        report_files = [os.path.join(reports_dir, f) for f in os.listdir(reports_dir) 
                                      if f.startswith("update_report_") and f.endswith(".md")]
                        if report_files:
                            latest_report = max(report_files, key=os.path.getmtime)
                            notification_manager.send_update_success_notification(latest_report)
                
                sys.exit(0)
            else:
                logger.error("Update failed")
                
                # Send failure notification if requested
                if args.notify:
                    # Get the last 50 lines of the log file
                    log_file = "api_implementation/logs/update_congress_data.log"
                    log_content = ""
                    if os.path.exists(log_file):
                        with open(log_file, 'r') as f:
                            log_lines = f.readlines()
                            log_content = ''.join(log_lines[-50:])
                    
                    notification_manager.send_update_failure_notification(
                        "The congressional data update process failed. Check logs for details.",
                        log_content
                    )
                
                sys.exit(1)
        except Exception as e:
            logger.error(f"Error running update: {e}")
            logger.error(traceback.format_exc())
            
            # Send failure notification if requested
            if args.notify:
                notification_manager.send_update_failure_notification(
                    f"Error running update: {e}",
                    traceback.format_exc()
                )
            
            sys.exit(1)
    elif args.daemon or args.schedule:
        logger.info("Starting scheduler")
        try:
            run_scheduler(daemon=True, schedule_type=args.schedule, time_str=args.time)
        except Exception as e:
            logger.error(f"Error running scheduler: {e}")
            logger.error(traceback.format_exc())
            
            # Send failure notification if requested
            if args.notify:
                notification_manager.send_update_failure_notification(
                    f"Error running scheduler: {e}",
                    traceback.format_exc()
                )
            
            sys.exit(1)
    else:
        # Default: run update once
        logger.info("Running update once (default)")
        try:
            success = update_congress_data()
            if success:
                logger.info("Update completed successfully")
                
                # Send success notification if requested
                if args.notify:
                    # Find the latest report
                    reports_dir = "api_implementation/reports"
                    if os.path.exists(reports_dir):
                        report_files = [os.path.join(reports_dir, f) for f in os.listdir(reports_dir) 
                                      if f.startswith("update_report_") and f.endswith(".md")]
                        if report_files:
                            latest_report = max(report_files, key=os.path.getmtime)
                            notification_manager.send_update_success_notification(latest_report)
                
                sys.exit(0)
            else:
                logger.error("Update failed")
                
                # Send failure notification if requested
                if args.notify:
                    # Get the last 50 lines of the log file
                    log_file = "api_implementation/logs/update_congress_data.log"
                    log_content = ""
                    if os.path.exists(log_file):
                        with open(log_file, 'r') as f:
                            log_lines = f.readlines()
                            log_content = ''.join(log_lines[-50:])
                    
                    notification_manager.send_update_failure_notification(
                        "The congressional data update process failed. Check logs for details.",
                        log_content
                    )
                
                sys.exit(1)
        except Exception as e:
            logger.error(f"Error running update: {e}")
            logger.error(traceback.format_exc())
            
            # Send failure notification if requested
            if args.notify:
                notification_manager.send_update_failure_notification(
                    f"Error running update: {e}",
                    traceback.format_exc()
                )
            
            sys.exit(1)

if __name__ == "__main__":
    main()