#!/bin/bash

# Voters Speak Deployment Script
# This script helps deploy the site to various platforms

# Don't exit on error, handle gracefully
set +e

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
    
    # Check if git is installed
    if ! command -v git &> /dev/null; then
        echo "❌ Git is not installed. Please install git first."
        echo "   Ubuntu/Debian: sudo apt-get install git"
        echo "   macOS: brew install git"
        echo "   Windows: Download from git-scm.com"
        return 1
    fi
    
    # Check if git is initialized
    if [ ! -d ".git" ]; then
        echo "🔄 Initializing git repository..."
        
        # Check if git user is configured
        if ! git config user.name &> /dev/null || ! git config user.email &> /dev/null; then
            echo "⚠️  Git user not configured. Setting up temporary configuration..."
            git config user.name "Voters Speak Deploy"
            git config user.email "deploy@voters-speak.app"
        fi
        
        git init
        git add .
        git commit -m "Initial commit: Voters Speak"
    fi
    
    echo "✅ Ready for GitHub Pages deployment!"
    echo ""
    echo "Next steps:"
    echo "1. Create a new repository on GitHub"
    echo "2. Run: git remote add origin https://github.com/yourusername/voters-speak.git"
    echo "3. Run: git push -u origin master"
    echo "4. Go to repository Settings → Pages"
    echo "5. Select 'Deploy from a branch' and choose 'master'"
}

# Function to deploy to Netlify
deploy_netlify() {
    echo "🚀 Deploying to Netlify..."
    
    # Check if netlify-cli is installed
    if command -v netlify &> /dev/null; then
        echo "Using netlify-cli..."
        netlify deploy --prod --dir=.
    else
        echo "📋 Manual Netlify deployment:"
        echo ""
        echo "Method 1: Web Interface"
        echo "   1. Go to https://netlify.com"
        echo "   2. Drag and drop this folder"
        echo "   3. Your site will be live instantly!"
        echo ""
        echo "Method 2: Netlify CLI (if installed)"
        echo "   1. Install: npm install -g netlify-cli"
        echo "   2. Run: netlify deploy --prod --dir=."
    fi
}

# Function to validate the build
validate() {
    echo "🔍 Validating build..."
    
    # Check essential files
    files=("index.html" "executive_data.js" "senate_data.js" "house_data.js" "judicial_data.js")
    missing_files=()
    
    for file in "${files[@]}"; do
        if [ -f "$file" ]; then
            echo "   ✅ $file exists"
        else
            echo "   ❌ $file missing"
            missing_files+=("$file")
        fi
    done
    
    if [ ${#missing_files[@]} -eq 0 ]; then
        echo "✅ All essential files present"
        return 0
    else
        echo "❌ Missing files: ${missing_files[*]}"
        return 1
    fi
}

# Function to check environment
check_environment() {
    echo "🔧 Checking environment..."
    
    # Check Node.js
    if command -v node &> /dev/null; then
        echo "   ✅ Node.js: $(node --version)"
    else
        echo "   ℹ️  Node.js not found (not required for static deployment)"
    fi
    
    # Check Python
    if command -v python3 &> /dev/null; then
        echo "   ✅ Python3: $(python3 --version)"
    elif command -v python &> /dev/null; then
        echo "   ✅ Python: $(python --version)"
    else
        echo "   ℹ️  Python not found (for local server only)"
    fi
    
    # Check Git
    if command -v git &> /dev/null; then
        echo "   ✅ Git: $(git --version)"
    else
        echo "   ❌ Git not installed"
    fi
}

# Show usage information
show_usage() {
    echo "Usage: $0 [command]"
    echo ""
    echo "Commands:"
    echo "  validate    - Check if all files are present"
    echo "  github      - Set up for GitHub Pages deployment"
    echo "  netlify     - Set up for Netlify deployment"
    echo "  all         - Run all checks and setups"
    echo "  help        - Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 validate"
    echo "  $0 github"
    echo "  $0 all"
}

# Main execution
if [ -n "$1" ]; then
    # Command mode
    check_environment
    echo ""
    
    case "$1" in
        "github")
            if validate; then
                deploy_github
            fi
            ;;
        "netlify")
            if validate; then
                deploy_netlify
            fi
            ;;
        "validate")
            validate
            ;;
        "all")
            if validate; then
                echo ""
                deploy_github
                echo ""
                deploy_netlify
            fi
            ;;
        "help"|"--help"|"-h")
            show_usage
            ;;
        *)
            echo "❌ Unknown command: $1"
            show_usage
            exit 1
            ;;
    esac
else
    # Interactive mode
    check_environment
    echo ""
    
    echo "Choose deployment option:"
    echo "1) Validate build"
    echo "2) GitHub Pages setup"
    echo "3) Netlify setup"
    echo "4) All options"
    echo "5) Help"
    
    # Check if stdin is available
    if [ -t 0 ]; then
        read -p "Enter choice (1-5): " choice
    else
        echo "No input available, running validation..."
        choice="1"
    fi
    
    case $choice in
        1)
            validate
            ;;
        2)
            if validate; then
                deploy_github
            fi
            ;;
        3)
            if validate; then
                deploy_netlify
            fi
            ;;
        4)
            if validate; then
                echo ""
                deploy_github
                echo ""
                deploy_netlify
            fi
            ;;
        5)
            show_usage
            ;;
        *)
            echo "❌ Invalid choice. Use 1-5 or run: $0 help"
            exit 1
            ;;
    esac
fi

echo ""
echo "🎉 Script execution complete!"
echo ""
echo "📚 Quick deployment guide:"
echo ""
echo "GitHub Pages:"
echo "1. Create repository: https://github.com/new"
echo "2. Upload files and push to GitHub"
echo "3. Go to Settings → Pages → Select branch"
echo ""
echo "Netlify:"
echo "1. Go to https://netlify.com"
echo "2. Drag and drop the project folder"
echo "3. Site will be live in seconds!"