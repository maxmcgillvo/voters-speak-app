# Voters Speak API Integration - Troubleshooting Guide

This guide provides solutions for common issues that may arise when using the Voters Speak API Integration system.

## Table of Contents

1. [Update Process Issues](#1-update-process-issues)
2. [Data Validation Issues](#2-data-validation-issues)
3. [Email Notification Issues](#4-email-notification-issues)
4. [Web Interface Issues](#5-web-interface-issues)
5. [Systemd Service Issues](#6-systemd-service-issues)
6. [Path and File Issues](#7-path-and-file-issues)

## 1. Update Process Issues

### 1.1 Update Process Fails to Start

**Symptoms:**
- Running `run_update.py` results in an error
- No logs are generated in the logs directory

**Possible Causes:**
- Python environment issues
- Missing dependencies
- Incorrect file permissions

**Solutions:**
1. Verify Python version:
   ```bash
   python3 --version
   ```
   Ensure you have Python 3.8 or higher.

2. Reinstall dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Check file permissions:
   ```bash
   chmod +x run_update.py
   ```

### 1.2 Update Process Fails During Execution

**Symptoms:**
- Error messages in the logs
- Update process exits with a non-zero status code

**Possible Causes:**
- Network connectivity issues
- Data source unavailability
- Invalid data format

**Solutions:**
1. Check network connectivity:
   ```bash
   ping unitedstates.github.io
   ```

2. Verify data source availability:
   ```bash
   curl -I https://unitedstates.github.io/congress-legislators/legislators-current.json
   ```

3. Check the logs for specific error messages:
   ```bash
   cat api_implementation/logs/update_congress_data.log
   ```

4. Run the update with verbose logging:
   ```bash
   python run_update.py --now --verbose
   ```

### 1.3 Update Process Completes But No Data is Updated

**Symptoms:**
- Update process completes successfully
- No changes are made to the data file

**Possible Causes:**
- No new data available
- Data file path is incorrect
- Insufficient permissions to write to the data file

**Solutions:**
1. Verify the data file path in the configuration:
   ```bash
   cat config.json | grep data_file
   ```

2. Run the path verification script:
   ```bash
   python src/verify_paths.py
   ```

3. Check file permissions on the data file:
   ```bash
   ls -la /path/to/complete_congress_dataset.js
   ```

4. Force an update even if no changes are detected:
   ```bash
   python run_update.py --now --force
   ```

## 2. Data Validation Issues

### 2.1 Validation Errors

**Symptoms:**
- Update fails with validation errors
- Error messages about missing or invalid data

**Possible Causes:**
- Data source format has changed
- Incomplete or corrupted data download
- Strict validation rules

**Solutions:**
1. Check the validation error messages in the logs:
   ```bash
   cat api_implementation/logs/data_validator.log
   ```

2. Verify the downloaded data files:
   ```bash
   cat api_implementation/data/legislators-current.json | jq
   ```

3. Update the data validator to handle the new format:
   ```bash
   nano src/data_validator.py
   ```

4. Temporarily disable strict validation (for testing only):
   ```bash
   # Edit the data_validator.py file to set strict mode to False
   nano src/data_validator.py
   ```

### 2.2 Large Data Changes Detected

**Symptoms:**
- Update fails with a message about large changes in member counts
- Verification errors in the logs

**Possible Causes:**
- Actual large changes in Congress membership
- Data source format has changed
- Incorrect comparison with old data

**Solutions:**
1. Check the verification error messages in the logs:
   ```bash
   cat api_implementation/logs/update_verifier.log
   ```

2. Compare the old and new data manually:
   ```bash
   # Create a backup of the old data
   cp /path/to/complete_congress_dataset.js /path/to/complete_congress_dataset.js.old
   
   # Run the update with the force flag
   python run_update.py --now --force
   
   # Compare the old and new data
   diff /path/to/complete_congress_dataset.js.old /path/to/complete_congress_dataset.js
   ```

3. Adjust the verification thresholds in the update verifier:
   ```bash
   nano src/update_verifier.py
   ```

## 3. Email Notification Issues

### 3.1 Email Notifications Not Sent

**Symptoms:**
- No email notifications received
- Error messages in the notification manager logs

**Possible Causes:**
- Incorrect SMTP settings
- Network connectivity issues
- Email server restrictions

**Solutions:**
1. Check the notification manager logs:
   ```bash
   cat api_implementation/logs/notification_manager.log
   ```

2. Verify SMTP settings in the configuration:
   ```bash
   cat config.json | grep smtp
   ```

3. Test the SMTP connection:
   ```bash
   python -c "
   import smtplib
   server = smtplib.SMTP('smtp.example.com', 587)
   server.starttls()
   server.login('username', 'password')
   server.quit()
   "
   ```

4. Send a test email using the notification manager:
   ```bash
   python -c "
   import sys
   sys.path.append('.')
   from src.notification_manager import NotificationManager
   nm = NotificationManager()
   nm.send_email('Test Subject', 'Test Body', ['recipient@example.com'])
   "
   ```

### 3.2 Email Notifications Contain Incorrect Information

**Symptoms:**
- Email notifications are sent but contain incorrect or incomplete information
- Missing or malformed report content

**Possible Causes:**
- Report generation issues
- Template rendering problems
- Character encoding issues

**Solutions:**
1. Check the report generator logs:
   ```bash
   cat api_implementation/logs/report_generator.log
   ```

2. Verify the report files:
   ```bash
   cat api_implementation/reports/update_report_*.md
   ```

3. Update the email templates in the notification manager:
   ```bash
   nano src/notification_manager.py
   ```

## 4. Web Interface Issues

### 4.1 Web Interface Not Starting

**Symptoms:**
- Unable to access the web interface
- Error messages when running `run_web_interface.py`

**Possible Causes:**
- Port already in use
- Missing dependencies
- Incorrect file permissions

**Solutions:**
1. Check if the port is already in use:
   ```bash
   netstat -tuln | grep 5000
   ```

2. Try a different port:
   ```bash
   python run_web_interface.py --port 5001
   ```

3. Check for Flask and Waitress dependencies:
   ```bash
   pip install flask waitress
   ```

4. Check file permissions:
   ```bash
   chmod +x run_web_interface.py
   ```

### 4.2 Web Interface Shows Incorrect Data

**Symptoms:**
- Web interface loads but displays incorrect or outdated information
- Charts or tables are empty or contain wrong values

**Possible Causes:**
- Caching issues
- Data file path is incorrect
- JavaScript errors

**Solutions:**
1. Clear your browser cache and reload the page

2. Check the web interface logs:
   ```bash
   cat api_implementation/logs/web_interface.log
   ```

3. Verify the data file path in the configuration:
   ```bash
   cat config.json | grep data_file
   ```

4. Check browser console for JavaScript errors

### 4.3 Unable to Trigger Updates from Web Interface

**Symptoms:**
- Clicking the "Run Update Now" button does nothing
- Error message when trying to run an update

**Possible Causes:**
- Permission issues
- Path configuration problems
- AJAX request failures

**Solutions:**
1. Check the web interface logs:
   ```bash
   cat api_implementation/logs/web_interface.log
   ```

2. Verify that the web interface has permission to run the update script:
   ```bash
   # If running as www-data user
   sudo -u www-data python run_update.py --now
   ```

3. Check browser console for AJAX errors

4. Try running the update manually:
   ```bash
   python run_update.py --now
   ```

## 5. Systemd Service Issues

### 5.1 Service Fails to Start

**Symptoms:**
- Service status shows "failed" or "inactive"
- Error messages in the systemd journal

**Possible Causes:**
- Incorrect paths in the service file
- Missing dependencies
- Permission issues

**Solutions:**
1. Check the systemd journal for error messages:
   ```bash
   sudo journalctl -u voters-speak-update.service
   ```

2. Verify the paths in the service file:
   ```bash
   cat /etc/systemd/system/voters-speak-update.service
   ```

3. Test the command manually:
   ```bash
   # If the ExecStart is: /usr/bin/python3 run_update.py --daemon
   cd /path/to/api_implementation
   /usr/bin/python3 run_update.py --daemon
   ```

4. Check file permissions:
   ```bash
   # Ensure the service user has access to the files
   sudo chown -R www-data:www-data /path/to/api_implementation
   ```

### 5.2 Service Starts But Keeps Restarting

**Symptoms:**
- Service status shows multiple restarts
- Service is active but keeps restarting

**Possible Causes:**
- Errors in the application code
- Resource limitations
- Configuration issues

**Solutions:**
1. Check the systemd journal for error messages:
   ```bash
   sudo journalctl -u voters-speak-update.service
   ```

2. Check the application logs:
   ```bash
   cat api_implementation/logs/update_congress_data.log
   ```

3. Increase the restart delay in the service file:
   ```bash
   sudo nano /etc/systemd/system/voters-speak-update.service
   # Change RestartSec=5 to RestartSec=60
   sudo systemctl daemon-reload
   sudo systemctl restart voters-speak-update.service
   ```

4. Run the application in the foreground to debug:
   ```bash
   cd /path/to/api_implementation
   python run_update.py --now --verbose
   ```

## 6. Path and File Issues

### 6.1 File Not Found Errors

**Symptoms:**
- Error messages about files not being found
- Application fails to start or run correctly

**Possible Causes:**
- Incorrect paths in the configuration
- Missing files or directories
- Permission issues

**Solutions:**
1. Run the path verification script:
   ```bash
   python src/verify_paths.py
   ```

2. Check the configuration file for correct paths:
   ```bash
   cat config.json | grep path
   ```

3. Verify that all required directories exist:
   ```bash
   mkdir -p api_implementation/data
   mkdir -p api_implementation/logs
   mkdir -p api_implementation/backups
   mkdir -p api_implementation/reports
   ```

4. Check file permissions:
   ```bash
   ls -la api_implementation/
   ```

### 6.2 Permission Denied Errors

**Symptoms:**
- Error messages about permission denied
- Unable to write to files or directories

**Possible Causes:**
- Incorrect file ownership
- Restrictive file permissions
- SELinux or AppArmor restrictions

**Solutions:**
1. Check file ownership:
   ```bash
   ls -la api_implementation/
   ```

2. Update file ownership to match the service user:
   ```bash
   # If the service runs as www-data
   sudo chown -R www-data:www-data api_implementation/
   ```

3. Update file permissions:
   ```bash
   sudo chmod -R 755 api_implementation/
   sudo chmod -R 644 api_implementation/*.py
   sudo chmod +x api_implementation/run_*.py
   ```

4. Check for SELinux or AppArmor restrictions:
   ```bash
   # For SELinux
   sudo sestatus
   
   # For AppArmor
   sudo aa-status
   ```

## Getting Additional Help

If you're still experiencing issues after trying the solutions in this guide, please:

1. Collect all relevant logs:
   ```bash
   tar -czf voters-speak-logs.tar.gz api_implementation/logs/
   ```

2. Export your configuration (remove sensitive information):
   ```bash
   cat config.json | grep -v password | grep -v key > config-sanitized.json
   ```

3. Contact the development team with:
   - A detailed description of the issue
   - Steps to reproduce the problem
   - The collected logs and sanitized configuration
   - Any error messages you're seeing