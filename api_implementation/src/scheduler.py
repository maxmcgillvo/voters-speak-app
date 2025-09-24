#!/usr/bin/env python3
"""
Scheduler for Congressional Data Updates

This script schedules regular updates of congressional data using the
update_congress_data module. It can be run as a daemon process or
as a one-time update.
"""

import os
import sys
import time
import logging
import argparse
import datetime
import schedule
from typing import Optional

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config import config
from src.update_congress_data import update_congress_data

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("api_implementation/logs/scheduler.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("scheduler")

def parse_time(time_str: str) -> tuple:
    """
    Parse a time string in HH:MM format
    
    Args:
        time_str (str): Time string in HH:MM format
        
    Returns:
        tuple: (hour, minute)
    """
    try:
        hour, minute = time_str.split(':')
        return int(hour), int(minute)
    except Exception as e:
        logger.error(f"Error parsing time string '{time_str}': {e}")
        return 2, 0  # Default to 2:00 AM

def schedule_update(schedule_type: str = 'daily', time_str: Optional[str] = None) -> None:
    """
    Schedule updates based on configuration
    
    Args:
        schedule_type (str): Type of schedule ('daily', 'weekly', 'monthly')
        time_str (str, optional): Time to run the update in HH:MM format
    """
    if time_str is None:
        time_str = config.get('update.time', '02:00')
    
    hour, minute = parse_time(time_str)
    time_str_formatted = f"{hour:02d}:{minute:02d}"
    
    if schedule_type == 'daily':
        schedule.every().day.at(time_str_formatted).do(update_congress_data)
        logger.info(f"Scheduled daily update at {time_str_formatted}")
    elif schedule_type == 'weekly':
        schedule.every().monday.at(time_str_formatted).do(update_congress_data)
        logger.info(f"Scheduled weekly update on Monday at {time_str_formatted}")
    elif schedule_type == 'monthly':
        # Schedule on the 1st of every month
        def monthly_job():
            today = datetime.date.today()
            if today.day == 1:
                update_congress_data()
        
        schedule.every().day.at(time_str_formatted).do(monthly_job)
        logger.info(f"Scheduled monthly update on the 1st at {time_str_formatted}")
    else:
        logger.error(f"Unknown schedule type: {schedule_type}")
        return

def run_scheduler(daemon: bool = True) -> None:
    """
    Run the scheduler
    
    Args:
        daemon (bool): Whether to run as a daemon process
    """
    schedule_type = config.get('update.schedule', 'daily')
    time_str = config.get('update.time', '02:00')
    
    logger.info(f"Starting scheduler with {schedule_type} updates at {time_str}")
    schedule_update(schedule_type, time_str)
    
    if daemon:
        logger.info("Running as daemon process")
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    else:
        # Run once and exit
        logger.info("Running scheduled jobs once")
        schedule.run_all()
        logger.info("Completed scheduled jobs")

def main() -> None:
    """
    Main function to parse arguments and run the scheduler
    """
    parser = argparse.ArgumentParser(description='Schedule congressional data updates')
    parser.add_argument('--now', action='store_true', help='Run update immediately')
    parser.add_argument('--daemon', action='store_true', help='Run as daemon process')
    parser.add_argument('--schedule', choices=['daily', 'weekly', 'monthly'], 
                        help='Schedule type (daily, weekly, monthly)')
    parser.add_argument('--time', help='Time to run update (HH:MM format)')
    
    args = parser.parse_args()
    
    # Create directories if they don't exist
    os.makedirs("api_implementation/logs", exist_ok=True)
    
    if args.schedule:
        config.set('update.schedule', args.schedule)
    
    if args.time:
        config.set('update.time', args.time)
    
    if args.now:
        logger.info("Running update now")
        update_congress_data()
    elif args.daemon:
        run_scheduler(daemon=True)
    else:
        run_scheduler(daemon=False)

if __name__ == "__main__":
    main()