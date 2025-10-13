# GitHub Integration - Final Deployment Instructions

## Overview

This document provides the final instructions for deploying the GitHub integration to the "Your Concerns" feature on the main site. The integration adds GitHub as a news source, recognizing its important role in civic tech and government transparency.

## Deployment Package

We have created a comprehensive deployment package that includes all the necessary files and documentation:

1. **github_integration_final_deployment.zip** - Contains all files needed for deployment
2. **github_integration_deployment_package.zip** - Contains a focused set of files for the GitHub integration
3. **MAIN_SITE_DEPLOYMENT_GUIDE.md** - Step-by-step guide for deploying to the main site
4. **PULL_REQUEST_TEMPLATE.md** - Template for creating a pull request

## Deployment Steps

### Option 1: Using the Deployment Script

1. Extract the `github_integration_deployment_package.zip` file
2. Navigate to the extracted directory
3. Run the deployment script, providing the path to your main site repository:
   ```bash
   ./deploy.sh /path/to/your-main-site
   ```
4. The script will:
   - Copy the GitHub logo to the appropriate directory
   - Update the CSS file with GitHub-specific styles
   - Copy reference HTML templates
   - Copy documentation files

### Option 2: Manual Deployment

1. **Add GitHub Logo**:
   - Create directory: `mkdir -p /path/to/main-site/public/assets/images/news-logos/github`
   - Copy logo: `cp github-logo.png /path/to/main-site/public/assets/images/news-logos/github/`

2. **Update CSS**:
   - Add the following to `logos.css`:
     ```css
     .logo-github {
         background-image: url('github/github-logo.png');
         background-color: white;
         text-indent: -9999px; /* Hide text */
     }
     ```

3. **Update Data Files**:
   - Add GitHub to the `concernsData.json` file:
     ```json
     {
       "name": "GITHUB",
       "url": "https://github.com/topics/civic-tech",
       "logoUrl": "/assets/images/news-logos/github/github-logo.png",
       "isActive": true,
       "order": 18
     }
     ```

4. **Update JavaScript Files**:
   - Add GitHub to the news sources array:
     ```javascript
     { name: "GITHUB", url: "https://github.com/topics/civic-tech", logoClass: "logo-github" }
     ```

## Git Workflow

1. **Create a Branch**:
   ```bash
   git checkout -b feature/github-integration
   ```

2. **Add and Commit Changes**:
   ```bash
   git add .
   git commit -m "Add GitHub integration to Your Concerns feature"
   ```

3. **Push Branch**:
   ```bash
   git push -u origin feature/github-integration
   ```

4. **Create Pull Request**:
   - Use the provided PULL_REQUEST_TEMPLATE.md content
   - Include screenshots of the integration

## Verification

After deployment, verify that:

1. The GitHub logo appears in the news sources grid
2. Clicking on the GitHub logo navigates to the civic tech topics page
3. The integration is responsive on mobile devices

## Support

For any questions or issues with the deployment, please contact the development team.