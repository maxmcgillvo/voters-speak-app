#!/usr/bin/env python3
"""
Notification Manager Module

This module provides functionality for sending notifications about
congressional data updates, including email notifications for successful
and failed updates.
"""

import os
import sys
import json
import logging
import smtplib
import argparse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict, Any, Optional, Union

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config import config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("api_implementation/logs/notification_manager.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("notification_manager")

class NotificationManager:
    """
    Manages notifications for congressional data updates
    """
    
    def __init__(self):
        """Initialize the notification manager"""
        self.smtp_server = config.get('notification.smtp_server', 'localhost')
        self.smtp_port = config.get('notification.smtp_port', 25)
        self.smtp_username = config.get('notification.smtp_username', '')
        self.smtp_password = config.get('notification.smtp_password', '')
        self.smtp_use_tls = config.get('notification.smtp_use_tls', False)
        self.from_address = config.get('notification.from_address', 'voters-speak@example.com')
        self.default_recipients = config.get('notification.email_recipients', [])
    
    def send_email(self, 
                  subject: str, 
                  body: str, 
                  recipients: Optional[List[str]] = None, 
                  html_body: Optional[str] = None) -> bool:
        """
        Send an email notification
        
        Args:
            subject (str): Email subject
            body (str): Email body (plain text)
            recipients (list, optional): List of email recipients
            html_body (str, optional): HTML version of the email body
            
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        if not recipients:
            recipients = self.default_recipients
        
        if not recipients:
            logger.warning("No recipients specified for email notification")
            return False
        
        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.from_address
            msg['To'] = ', '.join(recipients)
            
            # Attach plain text body
            msg.attach(MIMEText(body, 'plain'))
            
            # Attach HTML body if provided
            if html_body:
                msg.attach(MIMEText(html_body, 'html'))
            
            # Connect to SMTP server
            if self.smtp_use_tls:
                smtp = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
            else:
                smtp = smtplib.SMTP(self.smtp_server, self.smtp_port)
            
            # Login if credentials are provided
            if self.smtp_username and self.smtp_password:
                smtp.login(self.smtp_username, self.smtp_password)
            
            # Send email
            smtp.sendmail(self.from_address, recipients, msg.as_string())
            smtp.quit()
            
            logger.info(f"Sent email notification to {len(recipients)} recipients")
            return True
        except Exception as e:
            logger.error(f"Error sending email notification: {e}")
            return False
    
    def send_update_success_notification(self, 
                                        report_path: str, 
                                        recipients: Optional[List[str]] = None) -> bool:
        """
        Send a notification for a successful update
        
        Args:
            report_path (str): Path to the update report
            recipients (list, optional): List of email recipients
            
        Returns:
            bool: True if notification was sent successfully, False otherwise
        """
        try:
            # Read the report
            with open(report_path, 'r') as f:
                report_content = f.read()
            
            # Create email subject and body
            subject = "Voters Speak Congressional Data Update Successful"
            body = f"""
Congressional Data Update Successful

The congressional data update process completed successfully.

Update Report:
{report_content}

This is an automated message from the Voters Speak Congressional Data Update Service.
"""
            
            # Create HTML body
            html_body = f"""
<html>
<head>
    <style>
        body {{ font-family: Arial, sans-serif; }}
        h1 {{ color: #2c3e50; }}
        h2 {{ color: #3498db; }}
        .success {{ color: green; }}
        .warning {{ color: orange; }}
        .error {{ color: red; }}
        pre {{ background-color: #f8f9fa; padding: 10px; border-radius: 5px; }}
    </style>
</head>
<body>
    <h1>Congressional Data Update Successful</h1>
    <p>The congressional data update process completed successfully.</p>
    
    <h2>Update Report</h2>
    <pre>{report_content}</pre>
    
    <p><em>This is an automated message from the Voters Speak Congressional Data Update Service.</em></p>
</body>
</html>
"""
            
            # Send email
            return self.send_email(subject, body, recipients, html_body)
        except Exception as e:
            logger.error(f"Error sending update success notification: {e}")
            return False
    
    def send_update_failure_notification(self, 
                                        error_message: str, 
                                        log_content: Optional[str] = None, 
                                        recipients: Optional[List[str]] = None) -> bool:
        """
        Send a notification for a failed update
        
        Args:
            error_message (str): Error message
            log_content (str, optional): Content of the log file
            recipients (list, optional): List of email recipients
            
        Returns:
            bool: True if notification was sent successfully, False otherwise
        """
        # Create email subject and body
        subject = "Voters Speak Congressional Data Update Failed"
        body = f"""
Congressional Data Update Failed

The congressional data update process failed with the following error:

{error_message}

"""
        
        if log_content:
            body += f"""
Log Content:
{log_content}

"""
        
        body += """
Please check the logs for more information.

This is an automated message from the Voters Speak Congressional Data Update Service.
"""
        
        # Create HTML body
        html_body = f"""
<html>
<head>
    <style>
        body {{ font-family: Arial, sans-serif; }}
        h1 {{ color: #2c3e50; }}
        h2 {{ color: #e74c3c; }}
        .error {{ color: red; }}
        pre {{ background-color: #f8f9fa; padding: 10px; border-radius: 5px; }}
    </style>
</head>
<body>
    <h1>Congressional Data Update Failed</h1>
    <p>The congressional data update process failed with the following error:</p>
    
    <pre class="error">{error_message}</pre>
"""
        
        if log_content:
            html_body += f"""
    <h2>Log Content</h2>
    <pre>{log_content}</pre>
"""
        
        html_body += """
    <p>Please check the logs for more information.</p>
    
    <p><em>This is an automated message from the Voters Speak Congressional Data Update Service.</em></p>
</body>
</html>
"""
        
        # Send email
        return self.send_email(subject, body, recipients, html_body)
    
    def configure_email_settings(self, 
                               smtp_server: str, 
                               smtp_port: int, 
                               from_address: str, 
                               recipients: List[str], 
                               smtp_username: Optional[str] = None, 
                               smtp_password: Optional[str] = None, 
                               smtp_use_tls: bool = False) -> bool:
        """
        Configure email settings
        
        Args:
            smtp_server (str): SMTP server hostname
            smtp_port (int): SMTP server port
            from_address (str): From email address
            recipients (list): List of email recipients
            smtp_username (str, optional): SMTP username
            smtp_password (str, optional): SMTP password
            smtp_use_tls (bool): Whether to use TLS
            
        Returns:
            bool: True if configuration was saved successfully, False otherwise
        """
        try:
            # Update configuration
            config.set('notification.smtp_server', smtp_server)
            config.set('notification.smtp_port', smtp_port)
            config.set('notification.from_address', from_address)
            config.set('notification.email_recipients', recipients)
            
            if smtp_username:
                config.set('notification.smtp_username', smtp_username)
            
            if smtp_password:
                config.set('notification.smtp_password', smtp_password)
            
            config.set('notification.smtp_use_tls', smtp_use_tls)
            
            # Update instance variables
            self.smtp_server = smtp_server
            self.smtp_port = smtp_port
            self.smtp_username = smtp_username
            self.smtp_password = smtp_password
            self.smtp_use_tls = smtp_use_tls
            self.from_address = from_address
            self.default_recipients = recipients
            
            logger.info("Email settings configured successfully")
            return True
        except Exception as e:
            logger.error(f"Error configuring email settings: {e}")
            return False

# Main function for testing
def main():
    """Main function for testing the notification manager"""
    parser = argparse.ArgumentParser(description='Test the notification manager')
    parser.add_argument('--configure', action='store_true', help='Configure email settings')
    parser.add_argument('--test', action='store_true', help='Send a test email')
    parser.add_argument('--smtp-server', help='SMTP server hostname')
    parser.add_argument('--smtp-port', type=int, help='SMTP server port')
    parser.add_argument('--smtp-username', help='SMTP username')
    parser.add_argument('--smtp-password', help='SMTP password')
    parser.add_argument('--smtp-use-tls', action='store_true', help='Use TLS for SMTP')
    parser.add_argument('--from-address', help='From email address')
    parser.add_argument('--recipients', help='Comma-separated list of email recipients')
    
    args = parser.parse_args()
    
    # Create notification manager
    notification_manager = NotificationManager()
    
    if args.configure:
        # Configure email settings
        if not args.smtp_server or not args.smtp_port or not args.from_address or not args.recipients:
            print("Error: --smtp-server, --smtp-port, --from-address, and --recipients are required for configuration")
            return False
        
        recipients = [r.strip() for r in args.recipients.split(',')]
        
        success = notification_manager.configure_email_settings(
            args.smtp_server,
            args.smtp_port,
            args.from_address,
            recipients,
            args.smtp_username,
            args.smtp_password,
            args.smtp_use_tls
        )
        
        if success:
            print("Email settings configured successfully")
        else:
            print("Error configuring email settings")
        
        return success
    
    if args.test:
        # Send a test email
        recipients = None
        if args.recipients:
            recipients = [r.strip() for r in args.recipients.split(',')]
        
        success = notification_manager.send_email(
            "Voters Speak Congressional Data Update - Test Email",
            "This is a test email from the Voters Speak Congressional Data Update Service.",
            recipients,
            "<html><body><h1>Test Email</h1><p>This is a test email from the Voters Speak Congressional Data Update Service.</p></body></html>"
        )
        
        if success:
            print("Test email sent successfully")
        else:
            print("Error sending test email")
        
        return success
    
    # If no arguments provided, print help
    parser.print_help()
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)