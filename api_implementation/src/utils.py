"""
Utility functions for the Congress API integration

This module provides utility functions for the API integration,
including file operations, data transformation, and logging.
"""

import os
import re
import json
import logging
import shutil
from datetime import datetime
from typing import Dict, List, Any, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("utils")

def ensure_directory(directory: str) -> None:
    """
    Ensure directory exists
    
    Args:
        directory (str): Directory path
    """
    os.makedirs(directory, exist_ok=True)
    logger.debug(f"Ensured directory exists: {directory}")

def backup_file(file_path: str, backup_dir: Optional[str] = None) -> str:
    """
    Create backup of file
    
    Args:
        file_path (str): Path to file
        backup_dir (str, optional): Directory to store backup
        
    Returns:
        str: Path to backup file
        
    Raises:
        FileNotFoundError: If file doesn't exist
        IOError: If backup fails
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Create backup directory if not provided
    if not backup_dir:
        backup_dir = os.path.join(os.path.dirname(file_path), "backups")
    
    # Ensure backup directory exists
    ensure_directory(backup_dir)
    
    # Create backup filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = os.path.basename(file_path)
    backup_filename = f"{os.path.splitext(filename)[0]}_{timestamp}{os.path.splitext(filename)[1]}"
    backup_path = os.path.join(backup_dir, backup_filename)
    
    # Copy file to backup
    try:
        shutil.copy2(file_path, backup_path)
        logger.info(f"Created backup of {file_path} at {backup_path}")
        return backup_path
    except Exception as e:
        raise IOError(f"Failed to create backup: {e}")

def load_js_data(file_path: str) -> Dict[str, Any]:
    """
    Load data from JavaScript file
    
    This function extracts data from a JavaScript file that defines
    objects or arrays. It handles both completeCongressData and
    completeHouseData/completeSenateData formats.
    
    Args:
        file_path (str): Path to JavaScript file
        
    Returns:
        dict: Dictionary with 'house' and 'senate' keys containing lists of members
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file format is not supported
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Read file content
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Initialize result
    result = {
        'house': [],
        'senate': []
    }
    
    # Check file format
    if 'completeCongressData' in content:
        # Extract house data
        house_match = re.search(r'house:\s*\[(.*?)\]', content, re.DOTALL)
        if house_match:
            house_content = house_match.group(1)
            house_items = re.findall(r'{(.*?)}', house_content, re.DOTALL)
            for item in house_items:
                # Convert to valid JSON
                item = '{' + item + '}'
                item = re.sub(r'(\w+):', r'"\1":', item)  # Add quotes to keys
                item = re.sub(r'\'(.*?)\'', r'"\1"', item)  # Replace single quotes with double quotes
                item = re.sub(r',\s*}', '}', item)  # Remove trailing commas
                
                try:
                    member = json.loads(item)
                    result['house'].append(member)
                except json.JSONDecodeError as e:
                    logger.warning(f"Failed to parse house member: {e}")
        
        # Extract senate data
        senate_match = re.search(r'senate:\s*\[(.*?)\]', content, re.DOTALL)
        if senate_match:
            senate_content = senate_match.group(1)
            senate_items = re.findall(r'{(.*?)}', senate_content, re.DOTALL)
            for item in senate_items:
                # Convert to valid JSON
                item = '{' + item + '}'
                item = re.sub(r'(\w+):', r'"\1":', item)  # Add quotes to keys
                item = re.sub(r'\'(.*?)\'', r'"\1"', item)  # Replace single quotes with double quotes
                item = re.sub(r',\s*}', '}', item)  # Remove trailing commas
                
                try:
                    member = json.loads(item)
                    result['senate'].append(member)
                except json.JSONDecodeError as e:
                    logger.warning(f"Failed to parse senate member: {e}")
    
    elif 'completeHouseData' in content and 'completeSenateData' in content:
        # Extract house data
        house_match = re.search(r'completeHouseData\s*=\s*\[(.*?)\];', content, re.DOTALL)
        if house_match:
            house_content = house_match.group(1)
            house_items = re.findall(r'{(.*?)}', house_content, re.DOTALL)
            for item in house_items:
                # Convert to valid JSON
                item = '{' + item + '}'
                item = re.sub(r'(\w+):', r'"\1":', item)  # Add quotes to keys
                item = re.sub(r'\'(.*?)\'', r'"\1"', item)  # Replace single quotes with double quotes
                item = re.sub(r',\s*}', '}', item)  # Remove trailing commas
                
                try:
                    member = json.loads(item)
                    result['house'].append(member)
                except json.JSONDecodeError as e:
                    logger.warning(f"Failed to parse house member: {e}")
        
        # Extract senate data
        senate_match = re.search(r'completeSenateData\s*=\s*\[(.*?)\];', content, re.DOTALL)
        if senate_match:
            senate_content = senate_match.group(1)
            senate_items = re.findall(r'{(.*?)}', senate_content, re.DOTALL)
            for item in senate_items:
                # Convert to valid JSON
                item = '{' + item + '}'
                item = re.sub(r'(\w+):', r'"\1":', item)  # Add quotes to keys
                item = re.sub(r'\'(.*?)\'', r'"\1"', item)  # Replace single quotes with double quotes
                item = re.sub(r',\s*}', '}', item)  # Remove trailing commas
                
                try:
                    member = json.loads(item)
                    result['senate'].append(member)
                except json.JSONDecodeError as e:
                    logger.warning(f"Failed to parse senate member: {e}")
    
    else:
        raise ValueError("Unsupported file format")
    
    logger.info(f"Loaded {len(result['house'])} House members and {len(result['senate'])} Senate members from {file_path}")
    return result

def save_js_data(file_path: str, data: Dict[str, List[Dict[str, Any]]], format_type: str = 'completeCongressData') -> None:
    """
    Save data to JavaScript file
    
    Args:
        file_path (str): Path to JavaScript file
        data (dict): Dictionary with 'house' and 'senate' keys containing lists of members
        format_type (str): Format type ('completeCongressData' or 'separate')
        
    Raises:
        ValueError: If format_type is not supported
    """
    if format_type not in ['completeCongressData', 'separate']:
        raise ValueError("Unsupported format_type. Must be 'completeCongressData' or 'separate'")
    
    # Create backup of existing file
    if os.path.exists(file_path):
        backup_file(file_path)
    
    # Ensure directory exists
    ensure_directory(os.path.dirname(file_path))
    
    # Generate JavaScript content
    if format_type == 'completeCongressData':
        content = "// Complete 119th Congress Dataset - All 435 House + 100 Senate + 5 Delegates\n"
        content += "const completeCongressData = {\n"
        
        # Add house members
        content += "    house: [\n"
        for i, member in enumerate(data['house']):
            content += "        { "
            for key, value in member.items():
                if isinstance(value, str):
                    content += f'{key}: "{value}", '
                else:
                    content += f'{key}: {value}, '
            content = content.rstrip(', ')
            content += " }"
            if i < len(data['house']) - 1:
                content += ",\n"
            else:
                content += "\n"
        content += "    ],\n"
        
        # Add senate members
        content += "    senate: [\n"
        for i, member in enumerate(data['senate']):
            content += "        { "
            for key, value in member.items():
                if isinstance(value, str):
                    content += f'{key}: "{value}", '
                else:
                    content += f'{key}: {value}, '
            content = content.rstrip(', ')
            content += " }"
            if i < len(data['senate']) - 1:
                content += ",\n"
            else:
                content += "\n"
        content += "    ]\n"
        content += "};"
    
    else:  # separate
        content = "// Complete 119th Congress Data (2025-2026)\n"
        content += "// Generated from official Congress.gov data\n"
        content += "// This includes all 435 House members + 5 Delegates + 100 Senators\n\n"
        
        # Add house members
        content += "const completeHouseData = [\n"
        for i, member in enumerate(data['house']):
            content += "    { "
            for key, value in member.items():
                if isinstance(value, str):
                    content += f'{key}: "{value}", '
                else:
                    content += f'{key}: {value}, '
            content = content.rstrip(', ')
            content += " }"
            if i < len(data['house']) - 1:
                content += ",\n"
            else:
                content += "\n"
        content += "];\n\n"
        
        # Add senate members
        content += "const completeSenateData = [\n"
        for i, member in enumerate(data['senate']):
            content += "    { "
            for key, value in member.items():
                if isinstance(value, str):
                    content += f'{key}: "{value}", '
                else:
                    content += f'{key}: {value}, '
            content = content.rstrip(', ')
            content += " }"
            if i < len(data['senate']) - 1:
                content += ",\n"
            else:
                content += "\n"
        content += "];"
    
    # Write content to file
    with open(file_path, 'w') as f:
        f.write(content)
    
    logger.info(f"Saved {len(data['house'])} House members and {len(data['senate'])} Senate members to {file_path}")

def transform_api_data(api_data: Dict[str, List[Dict[str, Any]]]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Transform API data to application format
    
    Args:
        api_data (dict): API data
        
    Returns:
        dict: Transformed data
    """
    result = {
        'house': [],
        'senate': []
    }
    
    # Transform house members
    for member in api_data.get('house', []):
        transformed = {
            'name': f"{member.get('first_name', '')} {member.get('last_name', '')}".strip(),
            'title': "Representative",
            'state': member.get('state', ''),
            'district': f"{member.get('district', '')}",
            'party': member.get('party', ''),
            'email': member.get('email', f"rep.{member.get('last_name', '').lower()}@mail.house.gov"),
            'phone': member.get('phone', ''),
            'office': member.get('office', ''),
            'website': member.get('url', ''),
            'twitter': member.get('twitter_account', ''),
            'facebook': member.get('facebook_account', '')
        }
        result['house'].append(transformed)
    
    # Transform senate members
    for member in api_data.get('senate', []):
        transformed = {
            'name': f"{member.get('first_name', '')} {member.get('last_name', '')}".strip(),
            'title': "Senator",
            'state': member.get('state', ''),
            'party': member.get('party', ''),
            'email': member.get('email', f"senator@{member.get('last_name', '').lower()}.senate.gov"),
            'phone': member.get('phone', ''),
            'office': member.get('office', ''),
            'website': member.get('url', ''),
            'twitter': member.get('twitter_account', ''),
            'facebook': member.get('facebook_account', '')
        }
        result['senate'].append(transformed)
    
    logger.info(f"Transformed {len(result['house'])} House members and {len(result['senate'])} Senate members")
    return result

def compare_members(existing_data: Dict[str, List[Dict[str, Any]]], 
                   api_data: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Dict[str, List]]:
    """
    Compare existing data with API data to identify differences
    
    Args:
        existing_data (dict): Existing application data
        api_data (dict): Data from the API
        
    Returns:
        dict: Dictionary with 'new', 'updated', and 'removed' keys for both 'house' and 'senate'
    """
    result = {
        'house': {
            'new': [],
            'updated': [],
            'removed': []
        },
        'senate': {
            'new': [],
            'updated': [],
            'removed': []
        }
    }
    
    # Compare House members
    existing_house_names = {member['name']: member for member in existing_data['house']}
    api_house_names = {member['name']: member for member in api_data['house']}
    
    # Find new and updated House members
    for name, member in api_house_names.items():
        if name not in existing_house_names:
            result['house']['new'].append(member)
        else:
            # Check if any fields have changed
            existing_member = existing_house_names[name]
            changes = {}
            for key in ['state', 'district', 'party', 'email', 'phone', 'office', 'website', 'twitter', 'facebook']:
                if key in member and key in existing_member and member[key] != existing_member[key]:
                    changes[key] = {
                        'old': existing_member[key],
                        'new': member[key]
                    }
            
            if changes:
                result['house']['updated'].append({
                    'member': member,
                    'changes': changes
                })
    
    # Find removed House members
    for name, member in existing_house_names.items():
        if name not in api_house_names:
            result['house']['removed'].append(member)
    
    # Compare Senate members
    existing_senate_names = {member['name']: member for member in existing_data['senate']}
    api_senate_names = {member['name']: member for member in api_data['senate']}
    
    # Find new and updated Senate members
    for name, member in api_senate_names.items():
        if name not in existing_senate_names:
            result['senate']['new'].append(member)
        else:
            # Check if any fields have changed
            existing_member = existing_senate_names[name]
            changes = {}
            for key in ['state', 'party', 'email', 'phone', 'office', 'website', 'twitter', 'facebook']:
                if key in member and key in existing_member and member[key] != existing_member[key]:
                    changes[key] = {
                        'old': existing_member[key],
                        'new': member[key]
                    }
            
            if changes:
                result['senate']['updated'].append({
                    'member': member,
                    'changes': changes
                })
    
    # Find removed Senate members
    for name, member in existing_senate_names.items():
        if name not in api_senate_names:
            result['senate']['removed'].append(member)
    
    # Log summary
    logger.info(f"House: {len(result['house']['new'])} new, {len(result['house']['updated'])} updated, {len(result['house']['removed'])} removed")
    logger.info(f"Senate: {len(result['senate']['new'])} new, {len(result['senate']['updated'])} updated, {len(result['senate']['removed'])} removed")
    
    return result

def generate_update_report(changes: Dict[str, Dict[str, List]], output_file: Optional[str] = None) -> str:
    """
    Generate a report of the changes
    
    Args:
        changes (dict): Changes to report
        output_file (str, optional): Path to output file
        
    Returns:
        str: Report text
    """
    report = "# Congressional Data Update Report\n\n"
    report += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    # House changes
    report += "## House of Representatives\n\n"
    
    # New House members
    if changes['house']['new']:
        report += "### New Representatives\n\n"
        for member in changes['house']['new']:
            report += f"- {member['name']} ({member['party']}) - {member['state']}, {member['district']}\n"
        report += "\n"
    
    # Updated House members
    if changes['house']['updated']:
        report += "### Updated Representatives\n\n"
        for update in changes['house']['updated']:
            member = update['member']
            report += f"#### {member['name']} ({member['party']}) - {member['state']}, {member['district']}\n\n"
            report += "Changes:\n"
            for key, change in update['changes'].items():
                report += f"- {key}: {change['old']} -> {change['new']}\n"
            report += "\n"
    
    # Removed House members
    if changes['house']['removed']:
        report += "### Removed Representatives\n\n"
        for member in changes['house']['removed']:
            report += f"- {member['name']} ({member['party']}) - {member['state']}, {member['district']}\n"
        report += "\n"
    
    # Senate changes
    report += "## Senate\n\n"
    
    # New Senate members
    if changes['senate']['new']:
        report += "### New Senators\n\n"
        for member in changes['senate']['new']:
            report += f"- {member['name']} ({member['party']}) - {member['state']}\n"
        report += "\n"
    
    # Updated Senate members
    if changes['senate']['updated']:
        report += "### Updated Senators\n\n"
        for update in changes['senate']['updated']:
            member = update['member']
            report += f"#### {member['name']} ({member['party']}) - {member['state']}\n\n"
            report += "Changes:\n"
            for key, change in update['changes'].items():
                report += f"- {key}: {change['old']} -> {change['new']}\n"
            report += "\n"
    
    # Removed Senate members
    if changes['senate']['removed']:
        report += "### Removed Senators\n\n"
        for member in changes['senate']['removed']:
            report += f"- {member['name']} ({member['party']}) - {member['state']}\n"
        report += "\n"
    
    # Summary
    report += "## Summary\n\n"
    report += f"- House: {len(changes['house']['new'])} new, {len(changes['house']['updated'])} updated, {len(changes['house']['removed'])} removed\n"
    report += f"- Senate: {len(changes['senate']['new'])} new, {len(changes['senate']['updated'])} updated, {len(changes['senate']['removed'])} removed\n"
    
    # Write report to file if output_file is provided
    if output_file:
        # Ensure directory exists
        ensure_directory(os.path.dirname(output_file))
        
        # Write report to file
        with open(output_file, 'w') as f:
            f.write(report)
        
        logger.info(f"Generated update report at {output_file}")
    
    return report

# Example usage
if __name__ == "__main__":
    # Create test data
    test_data = {
        'house': [
            {
                'name': 'John Smith',
                'title': 'Representative',
                'state': 'CA',
                'district': '1st',
                'party': 'Republican',
                'email': 'john.smith@mail.house.gov',
                'phone': '(202) 225-1234',
                'office': '123 Cannon HOB, Washington, DC 20515',
                'website': 'https://smith.house.gov',
                'twitter': 'RepSmith',
                'facebook': 'RepJohnSmith'
            }
        ],
        'senate': [
            {
                'name': 'Jane Doe',
                'title': 'Senator',
                'state': 'CA',
                'party': 'Democrat',
                'email': 'senator@doe.senate.gov',
                'phone': '(202) 224-5678',
                'office': '456 Russell SOB, Washington, DC 20510',
                'website': 'https://doe.senate.gov',
                'twitter': 'SenDoe',
                'facebook': 'SenJaneDoe'
            }
        ]
    }
    
    # Create test file
    test_file = 'api_implementation/test_data.js'
    save_js_data(test_file, test_data, 'completeCongressData')
    
    # Load test file
    loaded_data = load_js_data(test_file)
    print(f"Loaded {len(loaded_data['house'])} House members and {len(loaded_data['senate'])} Senate members")
    
    # Create backup
    backup_path = backup_file(test_file)
    print(f"Created backup at {backup_path}")
    
    # Clean up
    os.remove(test_file)
    os.remove(backup_path)
    os.rmdir(os.path.dirname(backup_path))