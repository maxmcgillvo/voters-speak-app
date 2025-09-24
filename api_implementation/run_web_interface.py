#!/usr/bin/env python3
"""
Run Web Interface Script

This script provides a simple command-line interface to run the web interface
for the congressional data update system.
"""

import os
import sys
import argparse
import logging
import subprocess
from waitress import serve

# Add web_interface directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'web_interface'))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("api_implementation/logs/web_interface.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("run_web_interface")

def main():
    """
    Main function to parse arguments and run the web interface
    """
    parser = argparse.ArgumentParser(description='Run the web interface for the congressional data update system')
    parser.add_argument('--port', type=int, default=5000, help='Port to run the web interface on')
    parser.add_argument('--host', default='0.0.0.0', help='Host to run the web interface on')
    parser.add_argument('--debug', action='store_true', help='Run in debug mode')
    
    args = parser.parse_args()
    
    # Create directories if they don't exist
    os.makedirs("api_implementation/logs", exist_ok=True)
    os.makedirs("api_implementation/web_interface/static", exist_ok=True)
    os.makedirs("api_implementation/web_interface/templates", exist_ok=True)
    
    try:
        # Import the Flask app
        from web_interface.app import app
        
        logger.info(f"Starting web interface on {args.host}:{args.port}")
        
        if args.debug:
            # Run in debug mode
            app.run(debug=True, host=args.host, port=args.port)
        else:
            # Run in production mode with waitress
            serve(app, host=args.host, port=args.port)
    except Exception as e:
        logger.error(f"Error running web interface: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()