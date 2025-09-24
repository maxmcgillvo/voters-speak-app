#!/usr/bin/env python3
"""
Report Generator Module

This module provides enhanced reporting functionality for the congressional data
update process, including detailed change reports and notifications.
"""

import os
import sys
import json
import logging
import datetime
from typing import Dict, List, Any, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("api_implementation/logs/report_generator.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("report_generator")

class ReportGenerator:
    """
    Generates detailed reports about congressional data updates
    """
    
    def __init__(self, report_dir: str = "api_implementation/reports"):
        """
        Initialize the report generator
        
        Args:
            report_dir (str): Directory to store reports
        """
        self.report_dir = report_dir
        
        # Create report directory if it doesn't exist
        os.makedirs(self.report_dir, exist_ok=True)
    
    def generate_update_report(self, 
                              new_members: Dict[str, List[Dict[str, Any]]],
                              updated_members: Dict[str, List[Dict[str, Any]]],
                              removed_members: Dict[str, List[Dict[str, Any]]],
                              validation_results: Optional[Dict[str, List[str]]] = None) -> str:
        """
        Generate a detailed report of the update
        
        Args:
            new_members (dict): Dictionary with 'house' and 'senate' keys containing lists of new members
            updated_members (dict): Dictionary with 'house' and 'senate' keys containing lists of updated members
            removed_members (dict): Dictionary with 'house' and 'senate' keys containing lists of removed members
            validation_results (dict, optional): Dictionary with 'errors' and 'warnings' keys containing lists of messages
            
        Returns:
            str: Path to the generated report
        """
        # Create timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Create report file name
        report_file_name = f"update_report_{timestamp}.md"
        report_path = os.path.join(self.report_dir, report_file_name)
        
        # Generate report content
        report_content = self._generate_report_content(
            timestamp, new_members, updated_members, removed_members, validation_results
        )
        
        # Write report to file
        with open(report_path, 'w') as f:
            f.write(report_content)
        
        logger.info(f"Generated update report at {report_path}")
        
        return report_path
    
    def _generate_report_content(self, 
                               timestamp: str,
                               new_members: Dict[str, List[Dict[str, Any]]],
                               updated_members: Dict[str, List[Dict[str, Any]]],
                               removed_members: Dict[str, List[Dict[str, Any]]],
                               validation_results: Optional[Dict[str, List[str]]] = None) -> str:
        """
        Generate the content of the update report
        
        Args:
            timestamp (str): Timestamp string
            new_members (dict): Dictionary with 'house' and 'senate' keys containing lists of new members
            updated_members (dict): Dictionary with 'house' and 'senate' keys containing lists of updated members
            removed_members (dict): Dictionary with 'house' and 'senate' keys containing lists of removed members
            validation_results (dict, optional): Dictionary with 'errors' and 'warnings' keys containing lists of messages
            
        Returns:
            str: Report content
        """
        # Format timestamp as readable date
        date_str = datetime.datetime.strptime(timestamp, "%Y%m%d_%H%M%S").strftime("%Y-%m-%d %H:%M:%S")
        
        # Start with report header
        content = [
            "# Congressional Data Update Report",
            "",
            f"Generated on: {date_str}",
            ""
        ]
        
        # Add House section
        content.append("## House of Representatives")
        content.append("")
        
        # Add new House members
        if new_members['house']:
            content.append("### New Representatives")
            content.append("")
            for member in sorted(new_members['house'], key=lambda x: (x['state'], str(x.get('district', '')))):
                district = member.get('district', 'At Large')
                content.append(f"- {member['name']} ({member['party']}) - {member['state']}, {district}")
            content.append("")
        
        # Add updated House members
        if updated_members['house']:
            content.append("### Updated Representatives")
            content.append("")
            for member in sorted(updated_members['house'], key=lambda x: (x['state'], str(x.get('district', '')))):
                district = member.get('district', 'At Large')
                content.append(f"- {member['name']} ({member['party']}) - {member['state']}, {district}")
            content.append("")
        
        # Add removed House members
        if removed_members['house']:
            content.append("### Removed Representatives")
            content.append("")
            for member in sorted(removed_members['house'], key=lambda x: (x['state'], str(x.get('district', '')))):
                district = member.get('district', 'At Large')
                content.append(f"- {member['name']} ({member['party']}) - {member['state']}, {district}")
            content.append("")
        
        # Add Senate section
        content.append("## Senate")
        content.append("")
        
        # Add new Senators
        if new_members['senate']:
            content.append("### New Senators")
            content.append("")
            for member in sorted(new_members['senate'], key=lambda x: (x['state'], x.get('state_rank', ''))):
                rank = member.get('state_rank', '').capitalize() if member.get('state_rank') else ''
                if rank:
                    content.append(f"- {member['name']} ({member['party']}) - {rank} Senator, {member['state']}")
                else:
                    content.append(f"- {member['name']} ({member['party']}) - {member['state']}")
            content.append("")
        
        # Add updated Senators
        if updated_members['senate']:
            content.append("### Updated Senators")
            content.append("")
            for member in sorted(updated_members['senate'], key=lambda x: (x['state'], x.get('state_rank', ''))):
                rank = member.get('state_rank', '').capitalize() if member.get('state_rank') else ''
                if rank:
                    content.append(f"- {member['name']} ({member['party']}) - {rank} Senator, {member['state']}")
                else:
                    content.append(f"- {member['name']} ({member['party']}) - {member['state']}")
            content.append("")
        
        # Add removed Senators
        if removed_members['senate']:
            content.append("### Removed Senators")
            content.append("")
            for member in sorted(removed_members['senate'], key=lambda x: (x['state'], x.get('state_rank', ''))):
                rank = member.get('state_rank', '').capitalize() if member.get('state_rank') else ''
                if rank:
                    content.append(f"- {member['name']} ({member['party']}) - {rank} Senator, {member['state']}")
                else:
                    content.append(f"- {member['name']} ({member['party']}) - {member['state']}")
            content.append("")
        
        # Add summary
        content.append("## Summary")
        content.append("")
        content.append("### House of Representatives")
        content.append(f"- New: {len(new_members['house'])}")
        content.append(f"- Updated: {len(updated_members['house'])}")
        content.append(f"- Removed: {len(removed_members['house'])}")
        content.append("")
        content.append("### Senate")
        content.append(f"- New: {len(new_members['senate'])}")
        content.append(f"- Updated: {len(updated_members['senate'])}")
        content.append(f"- Removed: {len(removed_members['senate'])}")
        content.append("")
        
        # Add validation results if provided
        if validation_results:
            content.append("## Validation Results")
            content.append("")
            
            # Add errors
            if validation_results.get('errors'):
                content.append("### Errors")
                content.append("")
                for error in validation_results['errors']:
                    content.append(f"- {error}")
                content.append("")
            
            # Add warnings
            if validation_results.get('warnings'):
                content.append("### Warnings")
                content.append("")
                for warning in validation_results['warnings']:
                    content.append(f"- {warning}")
                content.append("")
        
        return "\n".join(content)
    
    def generate_html_report(self, markdown_report_path: str) -> str:
        """
        Generate an HTML version of a Markdown report
        
        Args:
            markdown_report_path (str): Path to the Markdown report
            
        Returns:
            str: Path to the generated HTML report
        """
        try:
            # Check if markdown report exists
            if not os.path.exists(markdown_report_path):
                logger.error(f"Markdown report not found: {markdown_report_path}")
                return ""
            
            # Read markdown content
            with open(markdown_report_path, 'r') as f:
                markdown_content = f.read()
            
            # Generate HTML file name
            html_file_name = os.path.basename(markdown_report_path).replace('.md', '.html')
            html_path = os.path.join(self.report_dir, html_file_name)
            
            # Convert markdown to HTML
            try:
                import markdown
                html_content = markdown.markdown(markdown_content)
            except ImportError:
                # If markdown module is not available, use a simple conversion
                html_content = f"<pre>{markdown_content}</pre>"
            
            # Add HTML wrapper
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Congressional Data Update Report</title>
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
                    h1 {{ color: #2c3e50; }}
                    h2 {{ color: #3498db; border-bottom: 1px solid #eee; padding-bottom: 5px; }}
                    h3 {{ color: #2980b9; }}
                    pre {{ background-color: #f8f8f8; padding: 10px; border-radius: 5px; overflow-x: auto; }}
                    table {{ border-collapse: collapse; width: 100%; }}
                    th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                    th {{ background-color: #f2f2f2; }}
                    tr:nth-child(even) {{ background-color: #f9f9f9; }}
                </style>
            </head>
            <body>
                {html_content}
            </body>
            </html>
            """
            
            # Write HTML to file
            with open(html_path, 'w') as f:
                f.write(html_content)
            
            logger.info(f"Generated HTML report at {html_path}")
            
            return html_path
        except Exception as e:
            logger.error(f"Failed to generate HTML report: {e}")
            return ""
    
    def send_email_notification(self, 
                               report_path: str, 
                               recipients: List[str],
                               subject: Optional[str] = None) -> bool:
        """
        Send an email notification with the report
        
        Args:
            report_path (str): Path to the report
            recipients (list): List of email recipients
            subject (str, optional): Email subject
            
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        try:
            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            from email.mime.application import MIMEApplication
            
            # Check if report exists
            if not os.path.exists(report_path):
                logger.error(f"Report not found: {report_path}")
                return False
            
            # Read report content
            with open(report_path, 'r') as f:
                report_content = f.read()
            
            # Get SMTP settings from environment variables
            smtp_server = os.environ.get('SMTP_SERVER', 'localhost')
            smtp_port = int(os.environ.get('SMTP_PORT', 25))
            smtp_username = os.environ.get('SMTP_USERNAME', '')
            smtp_password = os.environ.get('SMTP_PASSWORD', '')
            sender = os.environ.get('SMTP_SENDER', 'noreply@example.com')
            
            # Create message
            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = ', '.join(recipients)
            msg['Subject'] = subject or "Congressional Data Update Report"
            
            # Attach report content as text
            msg.attach(MIMEText(report_content, 'plain'))
            
            # Attach report file
            with open(report_path, 'rb') as f:
                attachment = MIMEApplication(f.read(), Name=os.path.basename(report_path))
                attachment['Content-Disposition'] = f'attachment; filename="{os.path.basename(report_path)}"'
                msg.attach(attachment)
            
            # Connect to SMTP server and send email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                if smtp_username and smtp_password:
                    server.starttls()
                    server.login(smtp_username, smtp_password)
                server.send_message(msg)
            
            logger.info(f"Sent email notification to {', '.join(recipients)}")
            
            return True
        except Exception as e:
            logger.error(f"Failed to send email notification: {e}")
            return False

# Main function for testing
def main():
    """Main function for testing the report generator"""
    # Create sample data
    new_members = {
        'house': [
            {'name': 'John Doe', 'party': 'Democrat', 'state': 'California', 'district': 1},
            {'name': 'Jane Smith', 'party': 'Republican', 'state': 'Texas', 'district': 2}
        ],
        'senate': [
            {'name': 'Bob Johnson', 'party': 'Democrat', 'state': 'New York', 'state_rank': 'senior'}
        ]
    }
    
    updated_members = {
        'house': [
            {'name': 'Alice Brown', 'party': 'Democrat', 'state': 'Florida', 'district': 3}
        ],
        'senate': []
    }
    
    removed_members = {
        'house': [],
        'senate': [
            {'name': 'Charlie Wilson', 'party': 'Republican', 'state': 'Ohio', 'state_rank': 'junior'}
        ]
    }
    
    validation_results = {
        'errors': ['Error 1', 'Error 2'],
        'warnings': ['Warning 1']
    }
    
    # Create report generator
    report_generator = ReportGenerator()
    
    # Generate report
    report_path = report_generator.generate_update_report(
        new_members, updated_members, removed_members, validation_results
    )
    
    print(f"Generated report at {report_path}")
    
    # Generate HTML report
    html_path = report_generator.generate_html_report(report_path)
    
    if html_path:
        print(f"Generated HTML report at {html_path}")

if __name__ == "__main__":
    main()