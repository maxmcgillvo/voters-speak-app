#!/usr/bin/env python3
"""
Script to download news source logos from reliable sources
"""

import os
import requests
from io import BytesIO
from PIL import Image

# Create directory if it doesn't exist
logo_dir = "public/assets/images/news-logos"
os.makedirs(logo_dir, exist_ok=True)

# News sources with their logo URLs
# Using transparent PNG logos from reputable sources
news_sources = [
    # We already have these logos
    # {"name": "cnn", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/CNN.svg/200px-CNN.svg.png"},
    # {"name": "fox", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Fox_News_Channel_logo.svg/200px-Fox_News_Channel_logo.svg.png"},
    # {"name": "nbc", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/NBC_logo.svg/200px-NBC_logo.svg.png"},
    # {"name": "abc", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/ABC_Logo.svg/200px-ABC_Logo.svg.png"},
    # {"name": "bbc", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/BBC.svg/200px-BBC.svg.png"},
    
    # Need to fix empty reuters.png
    {"name": "reuters", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Reuters_logo.svg/200px-Reuters_logo.svg.png"},
    
    # Need to download these logos
    {"name": "nytimes", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/NewYorkTimes.svg/200px-NewYorkTimes.svg.png"},
    {"name": "washingtonpost", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/The_Logo_of_The_Washington_Post_Newspaper.svg/200px-The_Logo_of_The_Washington_Post_Newspaper.svg.png"},
    {"name": "bloomberg", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Bloomberg_logo.svg/200px-Bloomberg_logo.svg.png"},
    {"name": "googlenews", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Google_News_icon.svg/200px-Google_News_icon.svg.png"},
    {"name": "cnbc", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/CNBC_logo.svg/200px-CNBC_logo.svg.png"},
    {"name": "npr", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/National_Public_Radio_logo.svg/200px-National_Public_Radio_logo.svg.png"},
    {"name": "msn", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/MSN_logo.svg/200px-MSN_logo.svg.png"},
    {"name": "politico", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Politico.svg/200px-Politico.svg.png"},
    {"name": "substack", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Substack_logo.svg/200px-Substack_logo.svg.png"},
    {"name": "yahoo", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Yahoo_Finance_Logo_2019.svg/200px-Yahoo_Finance_Logo_2019.svg.png"},
    {"name": "usatoday", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/USA_Today_Logo.svg/200px-USA_Today_Logo.svg.png"}
]

def download_and_save_logo(name, url):
    try:
        response = requests.get(url)
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