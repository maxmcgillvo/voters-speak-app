#!/usr/bin/env python3
"""
Script to create placeholder logo text files for news sources
"""

import os

# Create directory if it doesn't exist
logo_dir = "public/assets/images/news-logos"
os.makedirs(logo_dir, exist_ok=True)

# News sources
news_sources = [
    "CNN", "FOX", "NBC", "ABC", "BBC", "REUTERS", "NYT", "WAPO",
    "BLOOMBERG", "GOOGLENEWS", "CNBC", "NPR", "MSN", "POLITICO",
    "SUBSTACK", "YAHOO", "USATODAY"
]

# Create a placeholder text file for each news source
for source in news_sources:
    filename = f"{logo_dir}/{source.lower()}.txt"
    with open(filename, 'w') as f:
        f.write(f"This is a placeholder for the {source} logo.\n")
        f.write("In production, this would be replaced with an actual logo image.\n")
    print(f"Created {filename}")

print("All placeholder logo files created successfully!")