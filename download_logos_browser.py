#!/usr/bin/env python3
"""
Script to download news source logos using browser automation
"""

import os
import time
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from io import BytesIO

# Create directory if it doesn't exist
logo_dir = "public/assets/images/news-logos"
os.makedirs(logo_dir, exist_ok=True)

# News sources with their search terms
news_sources = [
    {"name": "reuters", "search": "reuters logo transparent png"},
    {"name": "nytimes", "search": "new york times logo transparent png"},
    {"name": "washingtonpost", "search": "washington post logo transparent png"},
    {"name": "bloomberg", "search": "bloomberg logo transparent png"},
    {"name": "googlenews", "search": "google news logo transparent png"},
    {"name": "cnbc", "search": "cnbc logo transparent png"},
    {"name": "npr", "search": "npr logo transparent png"},
    {"name": "msn", "search": "msn logo transparent png"},
    {"name": "politico", "search": "politico logo transparent png"},
    {"name": "substack", "search": "substack logo transparent png"},
    {"name": "yahoo", "search": "yahoo news logo transparent png"},
    {"name": "usatoday", "search": "usa today logo transparent png"}
]

def download_logo_via_browser(name, search_term):
    try:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Initialize the driver
        driver = webdriver.Chrome(options=chrome_options)
        
        # Go to Google Images
        driver.get(f"https://www.google.com/search?q={search_term}&tbm=isch")
        
        # Wait for images to load
        time.sleep(2)
        
        # Find the first image
        images = driver.find_elements(By.CSS_SELECTOR, "img.rg_i")
        if not images:
            print(f"No images found for {name}")
            driver.quit()
            return False
        
        # Click on the first image
        images[0].click()
        
        # Wait for the larger image to load
        time.sleep(2)
        
        # Find the large image
        large_image = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img.r48jcc"))
        )
        
        # Get the image source
        img_src = large_image.get_attribute("src")
        
        # Check if it's a base64 encoded image
        if img_src.startswith("data:image"):
            # Extract the base64 data
            img_data = img_src.split(",")[1]
            img_bytes = base64.b64decode(img_data)
            
            # Save the image
            filename = f"{logo_dir}/{name}.png"
            with open(filename, "wb") as f:
                f.write(img_bytes)
        else:
            # Download the image
            import requests
            response = requests.get(img_src)
            
            # Save the image
            filename = f"{logo_dir}/{name}.png"
            with open(filename, "wb") as f:
                f.write(response.content)
        
        # Close the browser
        driver.quit()
        
        # Verify the image
        try:
            img = Image.open(filename)
            print(f"Successfully downloaded {name} logo: {img.format}, {img.size}, {img.mode}")
            return True
        except Exception as e:
            print(f"Warning: Downloaded file for {name} may not be a valid image: {e}")
            return False
            
    except Exception as e:
        print(f"Error downloading {name} logo: {e}")
        try:
            driver.quit()
        except:
            pass
        return False

# Download each logo
success_count = 0
for source in news_sources:
    if download_logo_via_browser(source["name"], source["search"]):
        success_count += 1

print(f"Downloaded {success_count} of {len(news_sources)} logos successfully")