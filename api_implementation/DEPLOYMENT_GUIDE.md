# Voters Speak API Integration - Deployment Guide

This guide provides step-by-step instructions for deploying the Voters Speak API Integration system to a production environment.

## Prerequisites

- Linux server with systemd (Ubuntu 20.04+ or similar)
- Python 3.8 or higher
- Access to an SMTP server for email notifications
- Sudo/root access for service installation

## 1. System Installation

### 1.1 Create Application Directory

```bash
# Create application directory
sudo mkdir -p /opt/voters-speak/api_integration

# Set appropriate permissions
sudo chown -R www-data:www-data /opt/voters-speak
```

### 1.2 Copy Files

Copy the entire `api_implementation` directory to the server:

```bash
# Using scp (run from your local machine)
scp -r api_implementation/* user@server:/opt/voters-speak/api_integration/

# OR using rsync (recommended for large files)
rsync -avz --progress api_implementation/ user@server:/opt/voters-speak/api_integration/
```

### 1.3 Install Dependencies

```bash
# Navigate to the application directory
cd /opt/voters-speak/api_integration

# Install required packages
sudo pip3 install -r requirements.txt
```

## 2. Configuration

### 2.1 Update Configuration File

Edit the configuration file to match your production environment:

```bash
# Navigate to the application directory
cd /opt/voters-speak/api_integration

# Edit the configuration file
nano config.json
```

Update the following settings:

```json
{
  "api": {
    "base_url": "https://api.data.gov/congress/v3",
    "rate_limit": 5000,
    "rate_limit_window": 3600,
    "max_retries": 3
  },
  "update": {
    "schedule": "daily",
    "time": "02:00",
    "backup": true,
    "backup_dir": "backups"
  },
  "logging": {
    "level": "INFO",
    "file": "/opt/voters-speak/api_integration/logs/api_integration.log",
    "max_size": 10485760,
    "backup_count": 5
  },
  "paths": {
    "data_file": "/path/to/your/complete_congress_dataset.js",
    "backup_dir": "/opt/voters-speak/api_integration/backups",
    "log_dir": "/opt/voters-speak/api_integration/logs"
  },
  "notification": {
    "smtp_server": "smtp.example.com",
    "smtp_port": 587,
    "smtp_username": "your_username",
    "smtp_password": "your_password",
    "smtp_use_tls": true,
    "from_address": "voters-speak@example.com",
    "email_recipients": ["admin@example.com"]
  }
}
```

### 2.2 Verify Paths

Run the path verification script to ensure all paths are correct:

```bash
# Navigate to the application directory
cd /opt/voters-speak/api_integration

# Run the path verification script
python3 src/verify_paths.py
```

## 3. Systemd Service Setup

### 3.1 Create Systemd Service File

Edit the systemd service file to match your environment:

```bash
# Copy the service file to the systemd directory
sudo cp voters-speak-update.service /etc/systemd/system/
```

Edit the service file:

```bash
sudo nano /etc/systemd/system/voters-speak-update.service
```

Update the paths in the service file:

```
[Unit]
Description=Voters Speak Congressional Data Update Service
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/opt/voters-speak/api_integration
ExecStart=/usr/bin/python3 run_update.py --daemon
Restart=on-failure
RestartSec=5
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=voters-speak-update

[Install]
WantedBy=multi-user.target
```

### 3.2 Enable and Start the Service

```bash
# Reload systemd to recognize the new service
sudo systemctl daemon-reload

# Enable the service to start on boot
sudo systemctl enable voters-speak-update.service

# Start the service
sudo systemctl start voters-speak-update.service

# Check the status of the service
sudo systemctl status voters-speak-update.service
```

## 4. Web Interface Setup

### 4.1 Configure Web Server (Nginx)

Install Nginx:

```bash
sudo apt update
sudo apt install nginx
```

Create a Nginx configuration file:

```bash
sudo nano /etc/nginx/sites-available/voters-speak
```

Add the following configuration:

```nginx
server {
    listen 80;
    server_name your_domain.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable the site:

```bash
sudo ln -s /etc/nginx/sites-available/voters-speak /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 4.2 Set Up Web Interface Service

Create a systemd service file for the web interface:

```bash
sudo nano /etc/systemd/system/voters-speak-web.service
```

Add the following content:

```
[Unit]
Description=Voters Speak Web Interface
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/opt/voters-speak/api_integration
ExecStart=/usr/bin/python3 run_web_interface.py --port 5000
Restart=on-failure
RestartSec=5
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=voters-speak-web

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable voters-speak-web.service
sudo systemctl start voters-speak-web.service
sudo systemctl status voters-speak-web.service
```

## 5. Testing the Deployment

### 5.1 Test the Update Process

Run a manual update to verify that the system is working correctly:

```bash
cd /opt/voters-speak/api_integration
python3 run_update.py --now
```

Check the logs for any errors:

```bash
cat logs/update_congress_data.log
```

### 5.2 Test Email Notifications

Run a manual update with email notifications:

```bash
cd /opt/voters-speak/api_integration
python3 run_update.py --now --notify
```

Verify that you receive an email notification.

### 5.3 Test the Web Interface

Open a web browser and navigate to your server's domain or IP address. You should see the Voters Speak API Integration dashboard.

## 6. Security Considerations

### 6.1 Secure the Web Interface

For production use, it's recommended to secure the web interface with HTTPS and authentication:

1. **HTTPS Setup**:
   - Obtain an SSL certificate (e.g., using Let's Encrypt)
   - Update the Nginx configuration to use HTTPS

2. **Authentication**:
   - Implement basic authentication in Nginx or add authentication to the Flask application

### 6.2 Secure Configuration

1. **API Keys and Passwords**:
   - Ensure that API keys and passwords are stored securely
   - Consider using environment variables instead of storing sensitive information in configuration files

2. **File Permissions**:
   - Ensure that configuration files and logs have appropriate permissions
   - Restrict access to sensitive files to only the necessary users

## 7. Monitoring and Maintenance

### 7.1 Log Rotation

Configure log rotation to prevent logs from growing too large:

```bash
sudo nano /etc/logrotate.d/voters-speak
```

Add the following configuration:

```
/opt/voters-speak/api_integration/logs/*.log {
    daily
    missingok
    rotate 14
    compress
    delaycompress
    notifempty
    create 0640 www-data www-data
}
```

### 7.2 Regular Backups

Set up regular backups of the application data:

```bash
# Create a backup script
sudo nano /opt/voters-speak/backup.sh
```

Add the following content:

```bash
#!/bin/bash
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backup/voters-speak"
mkdir -p $BACKUP_DIR
tar -czf $BACKUP_DIR/voters-speak-$TIMESTAMP.tar.gz -C /opt/voters-speak .
find $BACKUP_DIR -name "voters-speak-*.tar.gz" -mtime +30 -delete
```

Make the script executable:

```bash
sudo chmod +x /opt/voters-speak/backup.sh
```

Add a cron job to run the backup script:

```bash
sudo crontab -e
```

Add the following line to run the backup daily at 3:00 AM:

```
0 3 * * * /opt/voters-speak/backup.sh
```

### 7.3 Monitoring

Set up monitoring to ensure the services are running correctly:

1. **Service Monitoring**:
   - Use a monitoring tool like Nagios, Zabbix, or Prometheus to monitor the systemd services

2. **Log Monitoring**:
   - Set up log monitoring to alert on errors in the application logs

## 8. Troubleshooting

### 8.1 Service Not Starting

If the service fails to start:

1. Check the systemd logs:
   ```bash
   sudo journalctl -u voters-speak-update.service
   ```

2. Check the application logs:
   ```bash
   cat /opt/voters-speak/api_integration/logs/update_congress_data.log
   ```

### 8.2 Web Interface Not Accessible

If the web interface is not accessible:

1. Check if the web interface service is running:
   ```bash
   sudo systemctl status voters-speak-web.service
   ```

2. Check the Nginx logs:
   ```bash
   sudo cat /var/log/nginx/error.log
   ```

3. Check if the port is open:
   ```bash
   sudo netstat -tuln | grep 5000
   ```

### 8.3 Email Notifications Not Working

If email notifications are not working:

1. Check the notification manager logs:
   ```bash
   cat /opt/voters-speak/api_integration/logs/notification_manager.log
   ```

2. Verify SMTP settings in the configuration file

3. Test the SMTP connection:
   ```bash
   python3 -m smtplib -d smtp.example.com:587
   ```