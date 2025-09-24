# Voters Speak API Integration - Web Interface User Guide

This guide provides instructions for using the Voters Speak API Integration web interface, which allows you to monitor and manage the congressional data update process.

## Table of Contents

1. [Accessing the Web Interface](#1-accessing-the-web-interface)
2. [Dashboard Overview](#2-dashboard-overview)
3. [Update History](#3-update-history)
4. [Logs](#4-logs)
5. [Settings](#5-settings)
6. [Running Manual Updates](#6-running-manual-updates)
7. [Troubleshooting](#7-troubleshooting)

## 1. Accessing the Web Interface

The web interface is accessible through a web browser at the URL where it's hosted. By default, this is:

```
http://your-server-address:5000
```

If the web interface is hosted behind a reverse proxy or with a domain name, use that URL instead.

## 2. Dashboard Overview

The dashboard is the main page of the web interface and provides an overview of the system status.

### 2.1 System Status

The top section of the dashboard displays the current system status:

- **Status Indicator**: A colored dot indicating the overall system status:
  - **Green**: System is operational
  - **Yellow**: System is operational but has warnings
  - **Red**: System has errors

- **Last Update**: The date and time of the last successful update
- **Next Scheduled Update**: The date and time of the next scheduled update
- **Update Schedule**: The current update schedule (e.g., "Daily at 02:00")
- **House Members**: The current number of House members in the dataset
- **Senate Members**: The current number of Senate members in the dataset

### 2.2 Recent Updates

The Recent Updates section displays information about the most recent updates:

- **Date**: The date and time of the update
- **Status**: The status of the update (Completed, Completed with warnings, or Failed)
- **Changes**: A summary of the changes made during the update
- **Actions**: Links to view the detailed report for the update

### 2.3 Update Statistics

The Update Statistics section displays a chart showing the number of changes over time:

- **X-axis**: Dates of updates
- **Y-axis**: Number of changes
- **Blue Line**: Changes to House members
- **Red Line**: Changes to Senate members

This chart helps you visualize the frequency and magnitude of changes to the congressional data over time.

## 3. Update History

The Update History tab provides a detailed list of all updates that have been performed:

- **Date**: The date and time of the update
- **Status**: The status of the update (Completed, Completed with warnings, or Failed)
- **House Changes**: A summary of changes to House members (new, updated, removed)
- **Senate Changes**: A summary of changes to Senate members (new, updated, removed)
- **Duration**: How long the update took to complete
- **Actions**: Links to view or download the detailed report for the update

You can use this information to track changes to the congressional data over time and investigate any issues that may have occurred during updates.

## 4. Logs

The Logs tab provides access to the system logs, which can be useful for troubleshooting issues:

### 4.1 Log Selection

Use the dropdown menu to select which log to view:

- **Update Process**: Logs from the main update process
- **Scheduler**: Logs from the scheduler
- **Data Validator**: Logs from the data validation process
- **Notifications**: Logs from the email notification system

### 4.2 Log Actions

- **Refresh Logs**: Click this button to refresh the log display with the latest entries
- **Download Logs**: Click this button to download the selected log file

### 4.3 Log Content

The log content is displayed in a scrollable container. The most recent log entries are at the bottom of the display. Each log entry includes:

- **Timestamp**: The date and time of the log entry
- **Log Level**: The severity of the log entry (INFO, WARNING, ERROR, etc.)
- **Message**: The log message

## 5. Settings

The Settings tab allows you to configure the system:

### 5.1 Update Schedule

Configure when updates should run:

- **Schedule Type**: Choose from Daily, Weekly, or Monthly
- **Time**: Set the time of day when updates should run (in 24-hour format)

Click the "Save Schedule" button to apply the changes.

### 5.2 Email Notifications

Configure email notifications for updates:

- **SMTP Server**: The hostname of your SMTP server
- **SMTP Port**: The port number for your SMTP server
- **SMTP Username**: The username for authenticating with your SMTP server
- **SMTP Password**: The password for authenticating with your SMTP server
- **From Address**: The email address that notifications will be sent from
- **Recipients**: A comma-separated list of email addresses to receive notifications
- **Use TLS**: Check this box if your SMTP server requires TLS encryption

Click the "Save Email Settings" button to apply the changes.

Click the "Send Test Email" button to send a test email with the current settings.

## 6. Running Manual Updates

You can run a manual update at any time by clicking the "Run Update Now" button in the top-right corner of the dashboard.

A confirmation dialog will appear asking if you're sure you want to run an update now. Click "OK" to proceed or "Cancel" to abort.

The update will run in the background, and you can monitor its progress by refreshing the dashboard or checking the logs.

## 7. Troubleshooting

If you encounter issues with the web interface, try the following:

### 7.1 Page Not Loading

If the web interface page is not loading:

1. Check that the web interface service is running:
   ```bash
   sudo systemctl status voters-speak-web.service
   ```

2. Verify that you can access the server:
   ```bash
   ping your-server-address
   ```

3. Check if the port is open:
   ```bash
   telnet your-server-address 5000
   ```

### 7.2 Cannot Run Updates

If you cannot run updates from the web interface:

1. Check the web interface logs for error messages:
   ```bash
   cat api_implementation/logs/web_interface.log
   ```

2. Verify that the web interface has permission to run the update script:
   ```bash
   # If running as www-data user
   sudo -u www-data python run_update.py --now
   ```

3. Try running the update manually:
   ```bash
   python run_update.py --now
   ```

### 7.3 Settings Not Saving

If your settings are not saving:

1. Check the web interface logs for error messages:
   ```bash
   cat api_implementation/logs/web_interface.log
   ```

2. Verify that the web interface has permission to write to the configuration file:
   ```bash
   ls -la config.json
   ```

3. Try updating the configuration file manually:
   ```bash
   nano config.json
   ```

### 7.4 Charts or Tables Not Displaying

If charts or tables are not displaying:

1. Check your browser's developer console for JavaScript errors

2. Clear your browser cache and reload the page

3. Verify that the data files exist and are accessible:
   ```bash
   ls -la api_implementation/reports/
   ```

For more detailed troubleshooting, please refer to the [Troubleshooting Guide](TROUBLESHOOTING_GUIDE.md).