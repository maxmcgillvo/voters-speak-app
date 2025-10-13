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
# Using multiple URLs for each logo to increase chances of success
news_sources = [
    {"name": "washingtonpost", "urls": [
        "https://www.washingtonpost.com/wp-stat/assets/favicons/apple-touch-icon.png",
        "https://www.washingtonpost.com/resizer/qlSn54UyODRUKPMCFgm1uFjZSIw=/1484x0/arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/2DMNWCEGVYI6TCBVQKH7XAQ7ZM.jpg"
    ]},
    {"name": "bloomberg", "urls": [
        "https://assets.bbhub.io/company/sites/51/2019/07/bloomberg_black.png",
        "https://assets.bbhub.io/company/sites/51/2019/07/bloomberg_white.png"
    ]},
    {"name": "googlenews", "urls": [
        "https://lh3.googleusercontent.com/J6_coFbogxhRI9iM864NL_liGXvsQp2AupsKei7z0cNNfDvGUmWUy20nuUhkREQyrpY4bEeIBuc=w300-rw",
        "https://play-lh.googleusercontent.com/hB9t3Z-mi284_49HA3nAuhO-W5Cyhje7r2P9McdgORoVCd-0SV1Ra-W0YIIHiUyG_HAa"
    ]},
    {"name": "cnbc", "urls": [
        "https://www.cnbc.com/favicon.ico",
        "https://static-redesign.cnbcfm.com/dist/a54a1c4a56f5608f0a68.svg"
    ]},
    {"name": "npr", "urls": [
        "https://media.npr.org/chrome/npr-logo.png",
        "https://media.npr.org/assets/img/2019/06/17/npr-logo-e1550f5d5c1936054a5299302f1056a2cc1e5c05-s1100-c50.jpg"
    ]},
    {"name": "msn", "urls": [
        "https://static-us-east-2-fastly-a.www.phx.msn.com/statics/icons/microsoft-logo-white-text.svg",
        "https://static-us-east-2-fastly-a.www.phx.msn.com/statics/icons/microsoft-logo.svg"
    ]},
    {"name": "politico", "urls": [
        "https://static.politico.com/da/f5/44342c424c68b675719324b1106b/politico.png",
        "https://www.politico.com/favicon.ico"
    ]},
    {"name": "yahoo", "urls": [
        "https://s.yimg.com/cv/apiv2/default/20200917/logo-yahoo-news.png",
        "https://s.yimg.com/rz/p/yahoo_news_en-US_s_f_pw_351x40_news.png"
    ]},
    {"name": "usatoday", "urls": [
        "https://www.gannett-cdn.com/sites/usatoday/images/site-nav/usatoday-logo-small.svg",
        "https://www.usatoday.com/favicon.ico"
    ]}
]

def download_and_save_logo(name, urls):
    for url in urls:
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
                return True
            except Exception as e:
                print(f"Warning: Downloaded file for {name} may not be a valid image: {e}")
                # Continue to next URL
                
        except Exception as e:
            print(f"Error downloading {name} logo from {url}: {e}")
            # Continue to next URL
    
    return False

# Download each logo
success_count = 0
for source in news_sources:
    if download_and_save_logo(source["name"], source["urls"]):
        success_count += 1

print(f"Downloaded {success_count} of {len(news_sources)} logos successfully")