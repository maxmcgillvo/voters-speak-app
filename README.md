# 🏛️ Voters Speak - Complete Government Contact Directory

## 📋 Project Overview
The most comprehensive publicly accessible government contact directory, featuring **549 total verified contacts** across all branches of the U.S. government.

## 🎯 Coverage
- **100 U.S. Senators** (all 50 states)
- **431 House Representatives** (all 50 states + 6 non-voting delegates)
- **9 Executive Branch Officials** (President, Cabinet, Agencies)
- **9 Supreme Court Justices** (complete current court)

## 🌐 Live Access
**URL**: https://voters-speak-app.vercel.app (or your deployment URL)

## 🚀 Features
- ✅ **Real-time search** across all 549 officials
- ✅ **State filtering** for all 50 states
- ✅ **Party filtering** (Democrat/Republican)
- ✅ **Direct email integration** with anti-spam protection
- ✅ **Mobile-responsive** design
- ✅ **Complete contact details** (email, phone, office, website)

## 📁 Repository Structure
```
voters-speak-government-directory/
├── index.html                    # Main application file
├── assets/
│   ├── css/
│   │   └── styles.css            # Styling
│   └── js/
│       └── app.js               # JavaScript functionality
├── data/
│   ├── house_representatives.js  # House members data
│   ├── senators.js              # Senate data
│   ├── executive.js             # Executive branch data
│   └── judicial.js              # Supreme Court data
├── docs/
│   ├── CONTRIBUTING.md          # Contribution guidelines
│   ├── API.md                   # Data structure documentation
│   └── DEPLOYMENT.md            # Deployment instructions
├── LICENSE
├── README.md
└── package.json                 # NPM configuration for deployment
```

## 🔧 Technical Details
- **Frontend**: Pure HTML5, CSS3, JavaScript (ES6+)
- **Data**: JSON-based, hardcoded for reliability
- **Deployment**: Static site (Netlify, Vercel, GitHub Pages)
- **Dependencies**: None (vanilla web technologies)

## 🚀 Quick Start
1. Clone repository
2. Open `index.html` in browser
3. Or deploy to static hosting

## 📊 Data Sources
All contact information verified from:
- Official House.gov directories
- Senate.gov contact pages
- Whitehouse.gov listings
- Supreme Court official site

## 🔗 Repository URLs
- **Main**: https://github.com/[username]/voters-speak-government-directory
- **Demo**: https://voters-speak-app.vercel.app

## 📝 Contributing
See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines on adding new representatives.

## 📈 Progress
- ✅ **Phase 1**: AL-MI states (131 reps)
- ✅ **Phase 2**: MN-NJ states (43 reps added)
- 🔄 **Next**: NM-SC states (in progress)