#!/usr/bin/env python3
"""
Voters Speak API Integration - Web Interface

This script provides a web interface for monitoring and managing the
congressional data update process.
"""

import os
import sys
import json
import logging
import subprocess
import datetime
from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config import config
from src.notification_manager import NotificationManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("api_implementation/logs/web_interface.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("web_interface")

app = Flask(__name__)

# Helper functions
def get_last_update_time():
    """
    Get the time of the last update
    
    Returns:
        str: Formatted date and time of the last update, or "Never" if no update has been run
    """
    reports_dir = "../reports"
    if not os.path.exists(reports_dir):
        return "Never"
    
    report_files = [os.path.join(reports_dir, f) for f in os.listdir(reports_dir) 
                  if f.startswith("update_report_") and f.endswith(".md")]
    
    if not report_files:
        return "Never"
    
    latest_report = max(report_files, key=os.path.getmtime)
    mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(latest_report))
    
    return mod_time.strftime("%Y-%m-%d %H:%M:%S")

def get_next_update_time():
    """
    Get the time of the next scheduled update
    
    Returns:
        str: Formatted date and time of the next update, or "Not scheduled" if no update is scheduled
    """
    schedule_type = config.get('update.schedule', 'daily')
    schedule_time = config.get('update.time', '02:00')
    
    now = datetime.datetime.now()
    hour, minute = map(int, schedule_time.split(':'))
    
    if schedule_type == 'daily':
        next_update = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if next_update <= now:
            next_update += datetime.timedelta(days=1)
    elif schedule_type == 'weekly':
        # Schedule for next Monday
        days_ahead = 0 - now.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        next_update = now.replace(hour=hour, minute=minute, second=0, microsecond=0) + datetime.timedelta(days=days_ahead)
    elif schedule_type == 'monthly':
        # Schedule for 1st of next month
        if now.day == 1 and now.replace(hour=hour, minute=minute, second=0, microsecond=0) > now:
            next_update = now.replace(day=1, hour=hour, minute=minute, second=0, microsecond=0)
        else:
            # Move to next month
            if now.month == 12:
                next_update = now.replace(year=now.year+1, month=1, day=1, hour=hour, minute=minute, second=0, microsecond=0)
            else:
                next_update = now.replace(month=now.month+1, day=1, hour=hour, minute=minute, second=0, microsecond=0)
    else:
        return "Not scheduled"
    
    return next_update.strftime("%Y-%m-%d %H:%M:%S")

def get_member_counts():
    """
    Get the current counts of House and Senate members
    
    Returns:
        tuple: (house_count, senate_count)
    """
    data_file = config.get('paths.data_file')
    
    if not os.path.exists(data_file):
        return (0, 0)
    
    try:
        # Read the first few lines to extract the variable name
        with open(data_file, 'r') as f:
            first_line = f.readline().strip()
            
        # Extract variable name from first line
        var_name = "completeCongressData"
        if "const " in first_line:
            var_name = first_line.split("const ")[1].split(" =")[0]
        
        # Use Node.js to parse the JavaScript file
        cmd = f"node -e &quot;const fs = require('fs'); const data = fs.readFileSync('{data_file}', 'utf8'); eval(data); console.log(JSON.stringify({{ house: {var_name}.house.length, senate: {var_name}.senate.length }}));&quot;"
        result = subprocess.check_output(cmd, shell=True, text=True)
        counts = json.loads(result)
        
        return (counts['house'], counts['senate'])
    except Exception as e:
        logger.error(f"Error getting member counts: {e}")
        return (0, 0)

def get_recent_updates(limit=5):
    """
    Get information about recent updates
    
    Args:
        limit (int): Maximum number of updates to return
        
    Returns:
        list: List of dictionaries with update information
    """
    reports_dir = "../reports"
    if not os.path.exists(reports_dir):
        return []
    
    report_files = [os.path.join(reports_dir, f) for f in os.listdir(reports_dir) 
                  if f.startswith("update_report_") and f.endswith(".md")]
    
    if not report_files:
        return []
    
    # Sort by modification time (newest first)
    report_files.sort(key=os.path.getmtime, reverse=True)
    
    updates = []
    for i, report_file in enumerate(report_files[:limit]):
        try:
            # Extract date from filename
            filename = os.path.basename(report_file)
            date_str = filename.replace("update_report_", "").replace(".md", "")
            date = datetime.datetime.strptime(date_str, "%Y%m%d_%H%M%S")
            
            # Parse report to extract status and changes
            with open(report_file, 'r') as f:
                content = f.read()
            
            # Extract status
            status = "Completed"
            status_class = "status-success"
            if "Error" in content or "Failed" in content:
                status = "Failed"
                status_class = "status-danger"
            elif "Warning" in content:
                status = "Completed with warnings"
                status_class = "status-warning"
            
            # Extract changes
            house_new = senate_new = house_updated = senate_updated = house_removed = senate_removed = 0
            
            # Look for summary section
            if "## Summary" in content:
                summary_section = content.split("## Summary")[1].split("##")[0]
                
                # Extract House changes
                if "### House of Representatives" in summary_section:
                    house_section = summary_section.split("### House of Representatives")[1].split("###")[0]
                    for line in house_section.split("\n"):
                        if "New:" in line:
                            try:
                                house_new = int(line.split("New:")[1].split()[0])
                            except:
                                pass
                        elif "Updated:" in line:
                            try:
                                house_updated = int(line.split("Updated:")[1].split()[0])
                            except:
                                pass
                        elif "Removed:" in line:
                            try:
                                house_removed = int(line.split("Removed:")[1].split()[0])
                            except:
                                pass
                
                # Extract Senate changes
                if "### Senate" in summary_section:
                    senate_section = summary_section.split("### Senate")[1].split("###")[0]
                    for line in senate_section.split("\n"):
                        if "New:" in line:
                            try:
                                senate_new = int(line.split("New:")[1].split()[0])
                            except:
                                pass
                        elif "Updated:" in line:
                            try:
                                senate_updated = int(line.split("Updated:")[1].split()[0])
                            except:
                                pass
                        elif "Removed:" in line:
                            try:
                                senate_removed = int(line.split("Removed:")[1].split()[0])
                            except:
                                pass
            
            total_changes = house_new + senate_new + house_updated + senate_updated + house_removed + senate_removed
            changes_text = f"{total_changes} changes"
            
            updates.append({
                'id': date_str,
                'date': date.strftime("%Y-%m-%d %H:%M:%S"),
                'status': status,
                'status_class': status_class,
                'changes': changes_text,
                'house_changes': f"{house_new} new, {house_updated} updated, {house_removed} removed",
                'senate_changes': f"{senate_new} new, {senate_updated} updated, {senate_removed} removed",
                'duration': "N/A"  # Duration information not available in reports
            })
        except Exception as e:
            logger.error(f"Error parsing report {report_file}: {e}")
    
    return updates

def get_chart_data():
    """
    Get data for the update statistics chart
    
    Returns:
        tuple: (labels, house_data, senate_data)
    """
    reports_dir = "../reports"
    if not os.path.exists(reports_dir):
        return ([], [], [])
    
    report_files = [os.path.join(reports_dir, f) for f in os.listdir(reports_dir) 
                  if f.startswith("update_report_") and f.endswith(".md")]
    
    if not report_files:
        return ([], [], [])
    
    # Sort by modification time (oldest first)
    report_files.sort(key=os.path.getmtime)
    
    labels = []
    house_data = []
    senate_data = []
    
    for report_file in report_files:
        try:
            # Extract date from filename
            filename = os.path.basename(report_file)
            date_str = filename.replace("update_report_", "").replace(".md", "")
            date = datetime.datetime.strptime(date_str, "%Y%m%d_%H%M%S")
            
            # Parse report to extract changes
            with open(report_file, 'r') as f:
                content = f.read()
            
            # Extract changes
            house_changes = senate_changes = 0
            
            # Look for summary section
            if "## Summary" in content:
                summary_section = content.split("## Summary")[1].split("##")[0]
                
                # Extract House changes
                if "### House of Representatives" in summary_section:
                    house_section = summary_section.split("### House of Representatives")[1].split("###")[0]
                    for line in house_section.split("\n"):
                        if "New:" in line:
                            try:
                                house_changes += int(line.split("New:")[1].split()[0])
                            except:
                                pass
                        elif "Updated:" in line:
                            try:
                                house_changes += int(line.split("Updated:")[1].split()[0])
                            except:
                                pass
                        elif "Removed:" in line:
                            try:
                                house_changes += int(line.split("Removed:")[1].split()[0])
                            except:
                                pass
                
                # Extract Senate changes
                if "### Senate" in summary_section:
                    senate_section = summary_section.split("### Senate")[1].split("###")[0]
                    for line in senate_section.split("\n"):
                        if "New:" in line:
                            try:
                                senate_changes += int(line.split("New:")[1].split()[0])
                            except:
                                pass
                        elif "Updated:" in line:
                            try:
                                senate_changes += int(line.split("Updated:")[1].split()[0])
                            except:
                                pass
                        elif "Removed:" in line:
                            try:
                                senate_changes += int(line.split("Removed:")[1].split()[0])
                            except:
                                pass
            
            labels.append(date.strftime("%Y-%m-%d"))
            house_data.append(house_changes)
            senate_data.append(senate_changes)
        except Exception as e:
            logger.error(f"Error parsing report {report_file} for chart data: {e}")
    
    return (labels, house_data, senate_data)

def get_log_content(log_type):
    """
    Get the content of a log file
    
    Args:
        log_type (str): Type of log to get
        
    Returns:
        str: Content of the log file
    """
    log_file = f"../logs/{log_type}.log"
    
    if not os.path.exists(log_file):
        return f"Log file not found: {log_file}"
    
    try:
        with open(log_file, 'r') as f:
            # Get the last 100 lines
            lines = f.readlines()[-100:]
            return ''.join(lines)
    except Exception as e:
        logger.error(f"Error reading log file {log_file}: {e}")
        return f"Error reading log file: {e}"

# Routes
@app.route('/')
def index():
    """Render the dashboard page"""
    # Get system status
    last_update = get_last_update_time()
    next_update = get_next_update_time()
    update_schedule = config.get('update.schedule', 'daily').capitalize()
    update_schedule += f" at {config.get('update.time', '02:00')}"
    
    house_count, senate_count = get_member_counts()
    
    # Determine system status
    status_text = "System Operational"
    status_class = "status-success"
    
    # Get recent updates
    recent_updates = get_recent_updates()
    
    # Get all updates for the updates tab
    all_updates = get_recent_updates(limit=100)
    
    # Get chart data
    chart_labels, chart_house_data, chart_senate_data = get_chart_data()
    
    # Get log content
    log_content = get_log_content("update_congress_data")
    
    # Get email settings
    smtp_server = config.get('notification.smtp_server', 'localhost')
    smtp_port = config.get('notification.smtp_port', 25)
    smtp_username = config.get('notification.smtp_username', '')
    from_address = config.get('notification.from_address', 'voters-speak@example.com')
    recipients = ', '.join(config.get('notification.email_recipients', []))
    use_tls = config.get('notification.smtp_use_tls', False)
    
    # Get schedule settings
    update_schedule_type = config.get('update.schedule', 'daily')
    update_schedule_time = config.get('update.time', '02:00')
    
    return render_template('index.html',
                          status_text=status_text,
                          status_class=status_class,
                          last_update=last_update,
                          next_update=next_update,
                          update_schedule=update_schedule,
                          house_count=house_count,
                          senate_count=senate_count,
                          recent_updates=recent_updates,
                          all_updates=all_updates,
                          chart_labels=json.dumps(chart_labels),
                          chart_house_data=chart_house_data,
                          chart_senate_data=chart_senate_data,
                          log_content=log_content,
                          smtp_server=smtp_server,
                          smtp_port=smtp_port,
                          smtp_username=smtp_username,
                          from_address=from_address,
                          recipients=recipients,
                          use_tls=use_tls,
                          update_schedule_type=update_schedule_type,
                          update_schedule_time=update_schedule_time)

@app.route('/run-update', methods=['POST'])
def run_update():
    """Run an update"""
    try:
        # Run the update script
        subprocess.Popen(["python", "../run_update.py", "--now"], 
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
        
        return jsonify({'success': True})
    except Exception as e:
        logger.error(f"Error running update: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/logs/<log_type>')
def get_logs(log_type):
    """Get log content"""
    return get_log_content(log_type)

@app.route('/view-report/<report_id>')
def view_report(report_id):
    """View a report"""
    report_file = f"../reports/update_report_{report_id}.md"
    
    if not os.path.exists(report_file):
        return "Report not found", 404
    
    try:
        with open(report_file, 'r') as f:
            content = f.read()
        
        # Convert Markdown to HTML
        # For a real implementation, use a Markdown library
        html_content = f"<pre>{content}</pre>"
        
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Update Report {report_id}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                pre {{ background-color: #f8f9fa; padding: 15px; border-radius: 5px; }}
                .back-link {{ margin-bottom: 20px; }}
            </style>
        </head>
        <body>
            <div class="back-link">
                <a href="/">&larr; Back to Dashboard</a>
            </div>
            <h1>Update Report {report_id}</h1>
            {html_content}
        </body>
        </html>
        """
    except Exception as e:
        logger.error(f"Error reading report {report_file}: {e}")
        return f"Error reading report: {e}", 500

@app.route('/download-report/<report_id>')
def download_report(report_id):
    """Download a report"""
    report_file = f"../reports/update_report_{report_id}.md"
    
    if not os.path.exists(report_file):
        return "Report not found", 404
    
    return send_file(report_file, as_attachment=True)

@app.route('/settings/schedule', methods=['POST'])
def update_schedule():
    """Update the schedule settings"""
    try:
        data = request.json
        schedule_type = data.get('scheduleType')
        schedule_time = data.get('scheduleTime')
        
        if not schedule_type or not schedule_time:
            return jsonify({'success': False, 'error': 'Missing required fields'})
        
        # Update configuration
        config.set('update.schedule', schedule_type)
        config.set('update.time', schedule_time)
        
        return jsonify({'success': True})
    except Exception as e:
        logger.error(f"Error updating schedule: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/settings/email', methods=['POST'])
def update_email():
    """Update the email settings"""
    try:
        data = request.json
        smtp_server = data.get('smtpServer')
        smtp_port = data.get('smtpPort')
        smtp_username = data.get('smtpUsername')
        smtp_password = data.get('smtpPassword')
        from_address = data.get('fromAddress')
        recipients = data.get('recipients')
        use_tls = data.get('useTLS')
        
        if not smtp_server or not smtp_port or not from_address or not recipients:
            return jsonify({'success': False, 'error': 'Missing required fields'})
        
        # Parse recipients
        recipient_list = [r.strip() for r in recipients.split(',')]
        
        # Create notification manager
        notification_manager = NotificationManager()
        
        # Configure email settings
        success = notification_manager.configure_email_settings(
            smtp_server,
            int(smtp_port),
            from_address,
            recipient_list,
            smtp_username,
            smtp_password,
            use_tls
        )
        
        if not success:
            return jsonify({'success': False, 'error': 'Failed to save email settings'})
        
        return jsonify({'success': True})
    except Exception as e:
        logger.error(f"Error updating email settings: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/settings/test-email', methods=['POST'])
def test_email():
    """Send a test email"""
    try:
        # Create notification manager
        notification_manager = NotificationManager()
        
        # Send test email
        success = notification_manager.send_email(
            "Voters Speak Congressional Data Update - Test Email",
            "This is a test email from the Voters Speak Congressional Data Update Service.",
            None,
            "<html><body><h1>Test Email</h1><p>This is a test email from the Voters Speak Congressional Data Update Service.</p></body></html>"
        )
        
        if not success:
            return jsonify({'success': False, 'error': 'Failed to send test email'})
        
        return jsonify({'success': True})
    except Exception as e:
        logger.error(f"Error sending test email: {e}")
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)