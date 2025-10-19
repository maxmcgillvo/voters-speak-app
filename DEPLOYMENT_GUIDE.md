# Deployment Guide for Voters Speak

This guide will help you deploy Voters Speak to GitHub Pages or other hosting platforms.

## 📦 What's Included

Your deployment package contains:
- All HTML pages (index, media, about, privacy, terms)
- All data files (executive, senate, house, judicial, media)
- Assets (icons, images)
- JavaScript components
- Configuration files (manifest, robots.txt, sitemap)
- Documentation (README, CHANGELOG, CONTRIBUTING)

## 🚀 Deployment Options

### Option 1: GitHub Pages (Recommended)

#### Step 1: Create GitHub Repository
1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon → "New repository"
3. Name it: `voters-speak` (or your preferred name)
4. Make it Public
5. Don't initialize with README (we have one)
6. Click "Create repository"

#### Step 2: Upload Files
**Method A: Using GitHub Web Interface**
1. On your new repository page, click "uploading an existing file"
2. Drag and drop all files from the `voters-speak-github-deployment` folder
3. Write commit message: "Initial commit - Voters Speak v1.0.0"
4. Click "Commit changes"

**Method B: Using Git Command Line**
```bash
# Navigate to the deployment folder
cd voters-speak-github-deployment

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Voters Speak v1.0.0"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/voters-speak.git

# Push to GitHub
git branch -M main
git push -u origin main
```

#### Step 3: Enable GitHub Pages
1. Go to your repository on GitHub
2. Click "Settings" tab
3. Scroll to "Pages" in left sidebar
4. Under "Source", select "main" branch
5. Click "Save"
6. Wait 1-2 minutes for deployment
7. Your site will be live at: `https://YOUR_USERNAME.github.io/voters-speak/`

#### Step 4: Verify Deployment
1. Visit your GitHub Pages URL
2. Test all sections (Executive, Senate, House, Supreme Court)
3. Click "Today's Issues" to verify media page
4. Test footer links (About, Privacy, Terms)
5. Verify all contact information displays correctly

### Option 2: Netlify

#### Quick Deploy
1. Go to [Netlify](https://www.netlify.com)
2. Sign up or log in
3. Drag and drop the `voters-speak-github-deployment` folder
4. Your site will be live instantly!
5. Optional: Connect to GitHub for continuous deployment

#### Custom Domain (Optional)
1. Go to Site Settings → Domain Management
2. Add custom domain
3. Follow DNS configuration instructions

### Option 3: Vercel

#### Deploy Steps
1. Go to [Vercel](https://vercel.com)
2. Sign up or log in
3. Click "New Project"
4. Import from GitHub or upload folder
5. Deploy!

### Option 4: Traditional Web Hosting

#### Upload via FTP/SFTP
1. Connect to your web host via FTP client (FileZilla, Cyberduck)
2. Upload all files to your public_html or www directory
3. Ensure index.html is in the root
4. Set proper file permissions (644 for files, 755 for directories)
5. Visit your domain to verify

## 🔧 Configuration

### Update URLs in README.md
After deployment, update these in README.md:
```markdown
## 🚀 Live Demo
Visit the live site: https://YOUR_USERNAME.github.io/voters-speak/

## 📧 Contact
- Issues: https://github.com/YOUR_USERNAME/voters-speak/issues
```

### Update Sitemap.xml
Replace the domain in sitemap.xml:
```xml
<loc>https://YOUR_USERNAME.github.io/voters-speak/</loc>
```

### Custom Domain (Optional)
If using a custom domain:
1. Create a `CNAME` file in root with your domain:
   ```
   www.yourdomain.com
   ```
2. Configure DNS with your domain provider:
   - Add CNAME record pointing to GitHub Pages
   - Or A records pointing to GitHub's IPs

## ✅ Post-Deployment Checklist

- [ ] Site loads correctly
- [ ] All sections display data (Executive, Senate, House, Supreme Court)
- [ ] "Today's Issues" page works
- [ ] Footer links work (About, Privacy, Terms)
- [ ] Logo/header returns to home page
- [ ] Search and filter functions work
- [ ] Phone numbers are clickable
- [ ] Email links work
- [ ] Social media links open correctly
- [ ] Mobile responsive design works
- [ ] No console errors in browser

## 🔄 Updating Your Site

### Update Data
1. Edit the relevant data file (e.g., `senate_data.js`)
2. Commit and push changes:
   ```bash
   git add senate_data.js
   git commit -m "Update Senate contact information"
   git push
   ```
3. GitHub Pages will automatically redeploy

### Add New Features
1. Create a new branch:
   ```bash
   git checkout -b feature/new-feature
   ```
2. Make your changes
3. Test locally
4. Commit and push
5. Create Pull Request on GitHub
6. Merge when ready

## 🐛 Troubleshooting

### Site Not Loading
- Check GitHub Pages is enabled in Settings
- Verify branch is set to "main"
- Wait 2-3 minutes after first deployment
- Clear browser cache

### 404 Errors
- Ensure index.html is in root directory
- Check file names are correct (case-sensitive)
- Verify all links use relative paths

### Data Not Displaying
- Check browser console for errors
- Verify data files are uploaded
- Ensure JSON syntax is valid
- Check file paths in HTML

### Images Not Loading
- Verify assets folder is uploaded
- Check image paths are relative
- Ensure file names match exactly

## 📊 Analytics (Optional)

### Add Google Analytics
Add before `</head>` in index.html:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR_GA_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR_GA_ID');
</script>
```

## 🔒 Security

- All data is static (no server-side processing)
- No user data collection
- HTTPS enabled by default on GitHub Pages
- No API keys or secrets needed

## 📱 PWA Installation

Users can install as Progressive Web App:
1. Visit site on mobile
2. Browser will prompt to "Add to Home Screen"
3. App icon appears on device
4. Works offline (basic functionality)

## 🎉 Success!

Your Voters Speak site is now live and helping citizens connect with their elected officials!

## 📞 Support

- GitHub Issues: Report bugs or request features
- Documentation: Check README.md and CONTRIBUTING.md
- Community: Engage with other contributors

---

**Thank you for deploying Voters Speak and supporting civic engagement!** 🇺🇸