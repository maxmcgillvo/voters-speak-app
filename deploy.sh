#!/bin/bash

# Voters Speak Deployment Script
# This script helps deploy the site to various platforms

set -e

echo "🗳️  Voters Speak Deployment Script"
echo "=================================="

# Check if we're in the right directory
if [ ! -f "index.html" ]; then
    echo "❌ Error: index.html not found. Run this from the project root."
    exit 1
fi

# Function to deploy to GitHub Pages
deploy_github() {
    echo "📦 Deploying to GitHub Pages..."
    
    # Check if git is initialized
    if [ ! -d ".git" ]; then
        echo "🔄 Initializing git repository..."
        git init
        git add .
        git commit -m "Initial commit: Voters Speak"
    fi
    
    echo "✅ Ready for GitHub Pages deployment!"
    echo "   1. Push to GitHub"
    echo "   2. Go to Settings → Pages"
    echo "   3. Select 'Deploy from a branch'"
    echo "   4. Choose 'main' branch"
}

# Function to deploy to Netlify
deploy_netlify() {
    echo "🚀 Deploying to Netlify..."
    
    # Check if netlify-cli is installed
    if command -v netlify &> /dev/null; then
        netlify deploy --prod --dir=.
    else
        echo "📋 Manual Netlify deployment:"
        echo "   1. Go to https://netlify.com"
        echo "   2. Drag and drop this folder"
        echo "   3. Your site will be live instantly!"
    fi
}

# Function to validate the build
validate() {
    echo "🔍 Validating build..."
    
    # Check essential files
    files=("index.html" "executive_data.js" "senate_data.js" "house_data.js" "judicial_data.js")
    for file in "${files[@]}"; do
        if [ -f "$file" ]; then
            echo "   ✅ $file exists"
        else
            echo "   ❌ $file missing"
            exit 1
        fi
    done
    
    echo "✅ All essential files present"
}

# Main menu
echo "Choose deployment option:"
echo "1) GitHub Pages"
echo "2) Netlify"
echo "3) Validate only"
echo "4) All options"

read -p "Enter choice (1-4): " choice

case $choice in
    1)
        validate
        deploy_github
        ;;
    2)
        validate
        deploy_netlify
        ;;
    3)
        validate
        ;;
    4)
        validate
        deploy_github
        deploy_netlify
        ;;
    *)
        echo "❌ Invalid choice. Exiting."
        exit 1
        ;;
esac

echo ""
echo "🎉 Deployment complete!"
echo "   GitHub: https://yourusername.github.io/voters-speak"
echo "   Netlify: https://your-site-name.netlify.app"