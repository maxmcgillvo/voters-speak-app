#!/bin/bash

# GitHub Integration Deployment Script
# This script deploys the GitHub integration to the "Your Concerns" feature on the main site

echo "Starting GitHub integration deployment..."

# Check if the main site directory is provided
if [ -z "$1" ]; then
  echo "Error: Main site directory not provided"
  echo "Usage: ./deploy.sh <main_site_directory>"
  exit 1
fi

MAIN_SITE_DIR=$1
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Create GitHub logo directory if it doesn't exist
echo "Creating GitHub logo directory..."
mkdir -p "$MAIN_SITE_DIR/public/assets/images/news-logos/github"

# Copy GitHub logo
echo "Copying GitHub logo..."
cp "$SCRIPT_DIR/public/assets/images/news-logos/github/github-logo.png" "$MAIN_SITE_DIR/public/assets/images/news-logos/github/"

# Update CSS
echo "Updating CSS..."
# Check if the logos.css file exists in the main site
if [ -f "$MAIN_SITE_DIR/public/assets/images/news-logos/logos.css" ]; then
  # Check if GitHub styles are already in the CSS file
  if grep -q "logo-github" "$MAIN_SITE_DIR/public/assets/images/news-logos/logos.css"; then
    echo "GitHub styles already exist in logos.css, skipping..."
  else
    # Extract GitHub-specific styles and append to the main CSS file
    grep -A 5 "logo-github" "$SCRIPT_DIR/public/assets/images/news-logos/logos.css" >> "$MAIN_SITE_DIR/public/assets/images/news-logos/logos.css"
    echo "GitHub styles added to logos.css"
  fi
else
  # If logos.css doesn't exist, copy the entire file
  cp "$SCRIPT_DIR/public/assets/images/news-logos/logos.css" "$MAIN_SITE_DIR/public/assets/images/news-logos/"
  echo "Created new logos.css file with GitHub styles"
fi

# Update HTML templates
echo "Updating HTML templates..."
# This part depends on the structure of the main site
# For now, we'll just copy the demo files as reference
mkdir -p "$MAIN_SITE_DIR/reference"
cp "$SCRIPT_DIR/demo.html" "$MAIN_SITE_DIR/reference/"
cp "$SCRIPT_DIR/vanilla-demo.html" "$MAIN_SITE_DIR/reference/"
cp "$SCRIPT_DIR/integrated_template.html" "$MAIN_SITE_DIR/reference/"
cp "$SCRIPT_DIR/github-logo-test.html" "$MAIN_SITE_DIR/reference/"

# Copy documentation
echo "Copying documentation..."
mkdir -p "$MAIN_SITE_DIR/docs/github_integration"
cp "$SCRIPT_DIR/github_integration_guide.md" "$MAIN_SITE_DIR/docs/github_integration/"
cp "$SCRIPT_DIR/github_civic_tech_examples.md" "$MAIN_SITE_DIR/docs/github_integration/"
cp "$SCRIPT_DIR/github_integration_deployment.md" "$MAIN_SITE_DIR/docs/github_integration/"
cp "$SCRIPT_DIR/README.md" "$MAIN_SITE_DIR/docs/github_integration/"

echo "GitHub integration deployment completed!"
echo "Please verify the integration by checking the following:"
echo "1. The GitHub logo appears in the news sources grid"
echo "2. Clicking on the GitHub logo navigates to the civic tech topics page"
echo "3. The integration is responsive on mobile devices"