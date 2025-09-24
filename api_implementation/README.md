# Congressional Data Integration for Voters Speak

This directory contains the implementation of the congressional data integration for the Voters Speak application. Due to the unavailability of the Congress.gov API, this implementation uses the United States Project's GitHub repository as a data source.

## Directory Structure

```
api_implementation/
├── config.json           # Configuration file (created automatically)
├── data/                 # Downloaded data files
├── logs/                 # Log files
├── backups/              # Backup files
├── reports/              # Update reports
├── test_results/         # Test results
├── web_interface/        # Web interface for monitoring and management
└── src/                  # Source code
    ├── congress_api_client.py  # API client (for future use with Congress.gov API)
    ├── config.py         # Configuration module
    ├── utils.py          # Utility functions
    ├── update_congress_data.py # Main update script
    ├── scheduler.py      # Update scheduler
    ├── data_validator.py # Data validation module
    ├── notification_manager.py # Email notification module
    ├── verify_paths.py   # Path verification module
    ├── test_update.py    # Test script for update process
    └── test_api_client.py      # Test script for API client
```

## Implementation Approach

Due to the Congress.gov API being unavailable (as of August 2025), this implementation uses the United States Project's GitHub repository as a data source. The United States Project maintains comprehensive data on members of Congress in YAML, JSON, and CSV formats, which is regularly updated by volunteers.

### Data Sources

This implementation uses the following data sources from the United States Project:

- [legislators-current.json](https://unitedstates.github.io/congress-legislators/legislators-current.json): Currently serving Members of Congress
- [legislators-historical.json](https://unitedstates.github.io/congress-legislators/legislators-historical.json): Historical Members of Congress
- [legislators-social-media.json](https://unitedstates.github.io/congress-legislators/legislators-social-media.json): Social media accounts for Members of Congress

## Modules

### Update Congress Data (`update_congress_data.py`)

The main module responsible for updating congressional data in the Voters Speak application. It downloads the latest data from the United States Project, transforms it to match the application format, compares it with existing data, and updates the application's data files.

### Scheduler (`scheduler.py`)

The Scheduler module handles scheduling regular updates of congressional data. It can be configured to run updates daily, weekly, or monthly at a specified time.

### Data Validator (`data_validator.py`)

The Data Validator module provides enhanced validation for congressional data, ensuring that the data is complete, consistent, and correctly formatted before it is used to update the application.

### Notification Manager (`notification_manager.py`)

The Notification Manager module handles email notifications for successful and failed updates, allowing administrators to stay informed about the status of the update process.

### Path Verification (`verify_paths.py`)

The Path Verification module ensures that all required directories exist and that file paths are correct, making the system more robust and easier to deploy in different environments.

### Congress API Client (`congress_api_client.py`)

The Congress API Client is designed for interacting with the Congress.gov API when it becomes available again. It handles authentication, rate limiting, error handling, and logging. The client provides methods for accessing various endpoints of the API.

### Configuration (`config.py`)

The Configuration module handles configuration settings for the data integration, including API keys, rate limits, and other settings. It provides methods for loading and saving configuration, getting and setting configuration values, and managing API keys.

### Utilities (`utils.py`)

The Utilities module provides utility functions for the data integration, including file operations, data transformation, and logging. It includes functions for:

- Loading and saving JavaScript data files
- Creating backups of files
- Transforming data to application format
- Comparing data to identify differences
- Generating update reports

## Web Interface

The web interface provides a user-friendly way to monitor and manage the congressional data update process. It includes:

- Dashboard with system status and recent updates
- Update history with detailed reports
- Log viewer for monitoring the update process
- Settings for configuring the update schedule and email notifications
- Manual update trigger for immediate updates

### Running the Web Interface

To run the web interface:

```bash
python run_web_interface.py
```

By default, the web interface runs on port 5000. You can access it at http://localhost:5000.

## Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Usage

#### Running a Manual Update

To run a manual update:

```bash
python run_update.py --now
```

To run a manual update with email notifications:

```bash
python run_update.py --now --notify
```

#### Scheduling Updates

To schedule regular updates:

```bash
# Run daily updates at 2:00 AM
python run_update.py --daemon

# Run weekly updates on Mondays at 3:30 AM
python run_update.py --schedule weekly --time 03:30 --daemon

# Run monthly updates on the 1st of each month at 4:00 AM
python run_update.py --schedule monthly --time 04:00 --daemon
```

#### Running as a System Service

To run the update process as a system service, you can use the provided systemd service file:

1. Copy the service file to the systemd directory:
   ```bash
   sudo cp voters-speak-update.service /etc/systemd/system/
   ```

2. Edit the service file to set the correct paths:
   ```bash
   sudo nano /etc/systemd/system/voters-speak-update.service
   ```

3. Enable and start the service:
   ```bash
   sudo systemctl enable voters-speak-update.service
   sudo systemctl start voters-speak-update.service
   ```

4. Check the status of the service:
   ```bash
   sudo systemctl status voters-speak-update.service
   ```

#### Running Tests

To test the implementation:

```bash
# Test data transformation only
python src/test_update.py --transform-only

# Test full update process in test mode (no actual file updates)
python src/test_update.py --full-update

# Test full update process on live data files
python src/test_update.py --full-update --live
```

## Future Improvements

1. Integrate with the Congress.gov API when it becomes available again
2. Add support for committee data
3. Implement more detailed data validation
4. Enhance the web interface with more features
5. Add support for more notification methods (SMS, Slack, etc.)

## Congress.gov API Integration (Future)

When the Congress.gov API becomes available again, this implementation can be updated to use it as the primary data source. The existing Congress API Client module is designed to work with the Congress.gov API and can be integrated with the update process.

### Getting a Congress.gov API Key

To use the Congress.gov API when it becomes available:

1. Visit [api.congress.gov/sign-up/](https://api.congress.gov/sign-up/)
2. Fill out the form to request an API key
3. You will receive your API key via email
4. Set the API key as an environment variable:
   ```
   export CONGRESS_API_KEY="your_api_key_here"
   ```
   or add it to the configuration file:
   ```
   {
     "api": {
       "key": "your_api_key_here",
       ...
     },
     ...
   }
   ```

## License

This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the CC0 1.0 Universal public domain dedication.