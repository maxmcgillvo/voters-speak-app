# GitHub Integration Deployment Guide

This guide provides step-by-step instructions for deploying the GitHub integration to the "Your Concerns" feature using Git.

## Prerequisites

- Git installed on your local machine
- Access to the project repository
- Necessary permissions to create branches and pull requests

## Deployment Steps

### 1. Clone the Repository

```bash
# Clone the repository if you haven't already
git clone https://github.com/your-organization/your-concerns-feature.git
cd your-concerns-feature
```

### 2. Create a New Branch

```bash
# Create a new branch for the GitHub integration
git checkout -b feature/github-integration
```

### 3. Add the GitHub Logo

```bash
# Create the directory for the GitHub logo
mkdir -p public/assets/images/news-logos/github

# Copy the GitHub logo to the directory
# Note: You should download the logo first or copy it from your local files
cp /path/to/github-logo.png public/assets/images/news-logos/github/
```

### 4. Update the CSS File

```bash
# Edit the logos.css file to add GitHub logo styling
nano public/assets/images/news-logos/logos.css
```

Add the following CSS code:

```css
.logo-github {
    background-image: url('github/github-logo.png');
    background-color: white;
    text-indent: -9999px; /* Hide text */
}
```

### 5. Update the Data File

```bash
# Edit the concernsData.json file
nano src/data/concernsData.json
```

Add GitHub to the `newsSources` array:

```json
{
  "name": "GITHUB",
  "url": "https://github.com/topics/civic-tech",
  "logoUrl": "/assets/images/news-logos/github/github-logo.png",
  "isActive": true,
  "order": 18
}
```

### 6. Update JavaScript Files (if applicable)

If you have JavaScript files that contain hardcoded news sources:

```bash
# Edit the vanilla-demo.html file or other JS files
nano vanilla-demo.html
```

Add GitHub to the `newsSourcesData` array:

```javascript
{ name: "GITHUB", url: "https://github.com/topics/civic-tech", logoClass: "logo-github" }
```

### 7. Create Test Files (Optional)

```bash
# Create a test file to verify the GitHub logo integration
nano github-logo-test.html
```

Add the test HTML content as provided in the integration guide.

### 8. Commit Your Changes

```bash
# Add all changes to staging
git add public/assets/images/news-logos/github/github-logo.png
git add public/assets/images/news-logos/logos.css
git add src/data/concernsData.json
git add vanilla-demo.html
git add github-logo-test.html

# Commit the changes
git commit -m "Add GitHub integration to Your Concerns feature"
```

### 9. Push Your Branch

```bash
# Push your branch to the remote repository
git push -u origin feature/github-integration
```

### 10. Create a Pull Request

1. Go to your repository on GitHub
2. Click on "Pull Requests"
3. Click "New Pull Request"
4. Select your branch (`feature/github-integration`) as the compare branch
5. Add a title and description for your pull request
6. Click "Create Pull Request"

## Pull Request Template

When creating your pull request, use the following template:

```markdown
# GitHub Integration Pull Request

## Description
This PR adds GitHub as a news source to the "Your Concerns" feature, recognizing GitHub's role in civic tech and government transparency.

## Changes Made
- Added GitHub logo to news logos directory
- Updated CSS to include GitHub logo styling
- Added GitHub to concernsData.json
- Updated vanilla-demo.html to include GitHub
- Created test file to verify integration

## Rationale
GitHub serves as a platform for civic engagement through:
- Open source civic tech projects
- Government collaboration
- Policy development
- Data transparency initiatives
- Civic hackathons and events

## Testing Completed
- Verified GitHub logo displays correctly
- Tested on desktop and mobile views
- Confirmed link to GitHub civic tech topics works correctly

## Screenshots
[Attach screenshots of the GitHub integration]

## Related Issues
Closes #[issue-number]
```

## After Merge

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

## Troubleshooting

If you encounter issues during deployment:

1. **Logo not displaying**: Check file paths and CSS class names
2. **CSS not applying**: Clear browser cache or check for syntax errors
3. **Git conflicts**: Resolve conflicts by merging the latest main branch into your feature branch
4. **Pull request issues**: Ensure all requested changes are addressed before re-requesting review

## Conclusion

Following these steps will successfully deploy the GitHub integration to the "Your Concerns" feature. This integration enhances the feature by connecting users to civic tech resources and initiatives on GitHub, acknowledging the platform's role in modern civic engagement.