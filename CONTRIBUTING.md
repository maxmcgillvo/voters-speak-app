# Contributing to Voters Speak

Thank you for your interest in contributing to Voters Speak! This document provides guidelines for contributing to the project.

## 🎯 Ways to Contribute

### 1. Data Updates
- Update contact information for elected officials
- Add missing social media links
- Correct any inaccurate information
- Update current issues in media_data.json

### 2. Bug Fixes
- Report bugs via GitHub Issues
- Submit pull requests with fixes
- Improve error handling

### 3. Feature Enhancements
- Propose new features via GitHub Issues
- Implement approved features
- Improve existing functionality

### 4. Documentation
- Improve README and documentation
- Add code comments
- Create tutorials or guides

### 5. Design Improvements
- Enhance UI/UX
- Improve accessibility
- Optimize mobile experience

## 🚀 Getting Started

### Prerequisites
- Basic knowledge of HTML, CSS, and JavaScript
- Git and GitHub account
- Text editor or IDE

### Setup
1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/voters-speak.git
   cd voters-speak
   ```
3. Create a branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. Start a local server:
   ```bash
   python -m http.server 8080
   ```

## 📝 Contribution Guidelines

### Code Style
- Use consistent indentation (2 or 4 spaces)
- Write clear, descriptive variable names
- Add comments for complex logic
- Follow existing code patterns

### Data Format
When updating data files, maintain the existing JSON structure:

```javascript
// Example for officials
{
  name: "Official Name",
  state: "ST",
  party: "Party Name",
  email: "email@example.gov",
  phone: "202-XXX-XXXX",
  office: "Office Address",
  website: "https://official.house.gov",
  socialMedia: {
    x: "https://x.com/username",
    facebook: "https://facebook.com/username",
    instagram: "https://instagram.com/username"
  }
}
```

### Commit Messages
- Use clear, descriptive commit messages
- Start with a verb (Add, Update, Fix, Remove)
- Examples:
  - "Add social media links for California representatives"
  - "Fix phone number formatting in Senate data"
  - "Update Supreme Court contact information"

### Pull Request Process
1. Update your branch with latest main:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```
2. Test your changes thoroughly
3. Commit your changes with clear messages
4. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Create a Pull Request on GitHub
6. Describe your changes clearly
7. Link any related issues

## 🔍 Data Verification

When updating official data:
1. **Verify from official sources only**
   - House.gov for Representatives
   - Senate.gov for Senators
   - WhiteHouse.gov for Executive Branch
   - SupremeCourt.gov for Justices

2. **Check multiple sources** when possible

3. **Include source links** in PR description

4. **Test all links** before submitting

## 🐛 Reporting Bugs

When reporting bugs, include:
- Clear description of the issue
- Steps to reproduce
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Browser and device information

Use this template:
```markdown
**Description:**
Brief description of the bug

**Steps to Reproduce:**
1. Go to '...'
2. Click on '...'
3. See error

**Expected Behavior:**
What should happen

**Actual Behavior:**
What actually happens

**Environment:**
- Browser: [e.g., Chrome 120]
- Device: [e.g., iPhone 12]
- OS: [e.g., iOS 17]
```

## 💡 Feature Requests

When proposing features:
- Check existing issues first
- Describe the feature clearly
- Explain the use case
- Consider implementation complexity
- Discuss potential alternatives

## ✅ Testing

Before submitting:
- [ ] Test on multiple browsers (Chrome, Firefox, Safari, Edge)
- [ ] Test on mobile devices
- [ ] Verify all links work
- [ ] Check for console errors
- [ ] Validate HTML/CSS
- [ ] Test accessibility features

## 📋 Code Review

All contributions go through code review:
- Be open to feedback
- Respond to review comments
- Make requested changes promptly
- Ask questions if unclear

## 🤝 Community Guidelines

- Be respectful and professional
- Welcome newcomers
- Provide constructive feedback
- Focus on the code, not the person
- Maintain non-partisan approach
- Keep discussions on-topic

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙋 Questions?

- Open a GitHub Issue for questions
- Tag with "question" label
- Check existing issues first

## 🎉 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in the project

Thank you for helping make government more accessible to all citizens! 🇺🇸