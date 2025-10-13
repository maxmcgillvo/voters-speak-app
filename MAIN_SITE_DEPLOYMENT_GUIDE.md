# GitHub Integration: Main Site Deployment Guide

This guide provides step-by-step instructions for deploying the GitHub integration to the main site.

## Prerequisites

- Access to the main site repository
- Git installed on your local machine
- Necessary permissions to create branches and pull requests

## Deployment Steps

### 1. Download and Extract the Deployment Package

Download the `github_integration_deployment_package.zip` file and extract it to your local machine.

### 2. Clone the Main Site Repository

```bash
# Clone the repository if you haven't already
git clone https://github.com/your-organization/your-main-site.git
cd your-main-site
```

### 3. Create a New Branch

```bash
# Create a new branch for the GitHub integration
git checkout -b feature/github-integration
```

### 4. Run the Deployment Script

```bash
# Navigate to where you extracted the deployment package
cd path/to/extracted/deployment_package

# Run the deployment script, providing the path to your main site repository
./deploy.sh /path/to/your-main-site
```

The script will:
- Copy the GitHub logo to the appropriate directory
- Update the CSS file with GitHub-specific styles
- Copy reference HTML templates
- Copy documentation files

### 5. Review the Changes

```bash
# Check what files have been modified
git status

# Review the changes
git diff
```

### 6. Commit the Changes

```bash
# Add all changes to staging
git add .

# Commit the changes
git commit -m "Add GitHub integration to Your Concerns feature"
```

### 7. Push Your Branch

```bash
# Push your branch to the remote repository
git push -u origin feature/github-integration
```

### 8. Create a Pull Request

1. Go to your repository on GitHub
2. Click on "Pull Requests"
3. Click "New Pull Request"
4. Select your branch (`feature/github-integration`) as the compare branch
5. Use the provided PULL_REQUEST_TEMPLATE.md content for your pull request
6. Click "Create Pull Request"

### 9. After Merge

Once your pull request is approved and merged:

1. Pull the latest changes from the main branch:
   ```bash
   git checkout main
   git pull
   ```

2. Delete your local feature branch:
   ```bash
   git branch -d feature/github-integration
   ```

3. Delete the remote feature branch (optional):
   ```bash
   git push origin --delete feature/github-integration
   ```

## Verification

After deployment, verify that:

1. The GitHub logo appears in the news sources grid
2. Clicking on the GitHub logo navigates to the civic tech topics page
3. The integration is responsive on mobile devices

## Troubleshooting

If you encounter issues during deployment:

1. **Logo not displaying**: Check file paths and CSS class names
2. **CSS not applying**: Clear browser cache or check for syntax errors
3. **Git conflicts**: Resolve conflicts by merging the latest main branch into your feature branch
4. **Pull request issues**: Ensure all requested changes are addressed before re-requesting review

## Support

For any questions or issues with the deployment, please contact the development team.