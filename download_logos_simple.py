#!/usr/bin/env python3
"""
Script to download news source logos from reliable sources with user agent
"""

import os
import requests
from PIL import Image
from io import BytesIO

# Create directory if it doesn't exist
logo_dir = "public/assets/images/news-logos"
os.makedirs(logo_dir, exist_ok=True)

# Set headers to mimic a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# News sources with direct logo URLs from various sources
news_sources = [
    {"name": "reuters", "url": "https://1000logos.net/wp-content/uploads/2017/06/Reuters-Logo.png"},
    {"name": "nytimes", "url": "https://1000logos.net/wp-content/uploads/2017/04/Symbol-New-York-Times.png"},
    {"name": "washingtonpost", "url": "https://1000logos.net/wp-content/uploads/2017/05/Washington-Post-logo.png"},
    {"name": "bloomberg", "url": "https://1000logos.net/wp-content/uploads/2021/04/Bloomberg-logo.png"},
    {"name": "googlenews", "url": "https://upload.wikimedia.org/wikipedia/commons/d/da/Google_News_icon.svg"},
    {"name": "cnbc", "url": "https://1000logos.net/wp-content/uploads/2021/04/CNBC-logo.png"},
    {"name": "npr", "url": "https://media.npr.org/chrome/npr-logo.png"},
    {"name": "msn", "url": "https://1000logos.net/wp-content/uploads/2020/08/MSN-Logo.png"},
    {"name": "politico", "url": "https://static.politico.com/cf/05/ee684a274496b04fa20ba2978da1/politico-logo.png"},
    {"name": "substack", "url": "https://substack.com/img/substack.png"},
    {"name": "yahoo", "url": "https://1000logos.net/wp-content/uploads/2017/05/Yahoo-Logo.png"},
    {"name": "usatoday", "url": "https://1000logos.net/wp-content/uploads/2017/04/USA-Today-Logo.png"}
]

def download_and_save_logo(name, url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad responses
        
        # Save the image
        filename = f"{logo_dir}/{name}.png"
        with open(filename, 'wb') as f:
            f.write(response.content)
        
        # Verify the image can be opened
        try:
            img = Image.open(BytesIO(response.content))
            print(f"Successfully downloaded {name} logo: {img.format}, {img.size}, {img.mode}")
        except Exception as e:
            print(f"Warning: Downloaded file for {name} may not be a valid image: {e}")
            
        return True
    except Exception as e:
        print(f"Error downloading {name} logo: {e}")
        return False

# Download each logo
success_count = 0
for source in news_sources:
    if download_and_save_logo(source["name"], source["url"]):
        success_count += 1

print(f"Downloaded {success_count} of {len(news_sources)} logos successfully")