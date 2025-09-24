# Voters Speak API Integration - Deployment Package

This package contains all the necessary files to deploy the Voters Speak API Integration system.

## Contents

- `api_implementation/`: The main implementation directory
  - `src/`: Source code files
  - `web_interface/`: Web interface files
  - `run_update.py`: Script to run updates
  - `run_web_interface.py`: Script to run the web interface
  - `requirements.txt`: Python dependencies
  - `config.json`: Configuration file
  - `voters-speak-update.service`: Systemd service file
  - Documentation files:
    - `README.md`: Main documentation
    - `DEPLOYMENT_GUIDE.md`: Deployment instructions
    - `TROUBLESHOOTING_GUIDE.md`: Troubleshooting guide
    - `WEB_INTERFACE_USER_GUIDE.md`: Web interface guide
    - `PROJECT_SUMMARY.md`: Project overview
    - `IMPLEMENTATION_REPORT_PHASE2.md`: Implementation report

- `PULL_REQUEST.md`: Pull request description and deployment checklist

## Deployment Instructions

Please refer to `api_implementation/DEPLOYMENT_GUIDE.md` for detailed deployment instructions.

## Quick Start

1. Install dependencies: `pip install -r api_implementation/requirements.txt`
2. Update configuration in `api_implementation/config.json`
3. Run path verification: `python api_implementation/src/verify_paths.py`
4. Test a manual update: `python api_implementation/run_update.py --now`
5. Set up systemd service for automated updates

