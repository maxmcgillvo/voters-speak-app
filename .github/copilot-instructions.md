# VotersSpeak - Government Contact Platform

VotersSpeak is a self-contained, static HTML/CSS/JavaScript web application that provides comprehensive contact information for US government officials across all branches. The entire application is contained in a single 68KB `index.html` file with no external dependencies except CDN-hosted libraries.

**ALWAYS reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

## Working Effectively

### Quick Start - Running the Application
- **Start local development**: `python3 -m http.server 8080` (starts in < 1 second)
- **Access application**: Navigate to `http://localhost:8080/`
- **Stop server**: `Ctrl+C` in the terminal running the server

### Validation Requirements
- **ALWAYS test functionality after making changes**: Navigate through tabs, test search, verify contact forms
- **Test major user scenarios**:
  1. Load application → verify all tabs display correctly
  2. Search functionality → type in search boxes, verify filtering works
  3. Contact forms → click email buttons, verify modal opens with all fields
  4. Navigation → test all 6 tabs (House, Senate, Executive, Cabinet, Supreme Court, Agencies)
- **Screenshot validation**: Always take screenshots of UI changes to verify visual correctness

### File Structure and Architecture
```
voters-speak-app/
├── index.html          (complete application - 68KB)
├── README.md          (deployment and usage documentation)  
└── .github/
    └── copilot-instructions.md (this file)
```

### Key Application Components (all in index.html)
- **CSS Styling**: Complete responsive design in `<style>` section (lines ~7-400)
- **HTML Structure**: Bootstrap-based layout with tab navigation (lines ~400-700)
- **JavaScript Data**: Embedded government official data objects (lines ~700-1200)
- **JavaScript Logic**: Search, filtering, and contact form functionality (lines ~1200-1575)

## Technical Specifications

### Dependencies and Requirements
- **No build process required** - application runs directly
- **No package.json or node_modules** - uses CDN dependencies only
- **CDN Dependencies**:
  - Bootstrap 4.6 (CSS framework)
  - Font Awesome (icons)
  - External script: sites.super.myninja.ai (can be removed if needed)
- **Browser Requirements**: All modern browsers (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+)

### Data Management
- **Government Data**: Hardcoded JavaScript objects containing official information
- **Data Categories**: House (435 members), Senate (100 members), Executive, Cabinet (16 members), Supreme Court (9 justices), Agencies (10 major agencies)
- **Data Location**: Lines ~700-1200 in index.html
- **Update Process**: Manual editing of JavaScript data objects

### Performance Characteristics
- **File Size**: 68KB (highly optimized)
- **Load Time**: < 1 second on local server
- **Search Performance**: Real-time filtering (no delays)
- **Memory Usage**: Minimal (all data loaded at startup)

## Common Development Tasks

### Making Code Changes
- **CSS Modifications**: Edit `<style>` section (lines ~7-400)
- **HTML Structure**: Edit main content area (lines ~400-700)  
- **Data Updates**: Edit `governmentData` object (lines ~700-1200)
- **JavaScript Logic**: Edit functions at end of file (lines ~1200-1575)

### Testing Changes
1. **Start server**: `python3 -m http.server 8080`
2. **Open browser**: `http://localhost:8080/`
3. **Test core functionality**:
   - Click all 6 navigation tabs
   - Type in search boxes to test filtering
   - Click email buttons to test contact forms
   - Verify responsive design on different screen sizes

### Deployment Validation
- **GitHub Pages**: Upload `index.html` to repository root, enable Pages in settings
- **Alternative hosting**: Any static file hosting (Netlify, Vercel, Surge.sh)
- **No server configuration needed**

## Debugging and Troubleshooting

### Common Issues
- **CDN blocking**: Some environments block CDN resources - check browser console
- **JavaScript errors**: Open browser DevTools Console to see errors
- **Styling issues**: Inspect element to debug CSS problems
- **Data problems**: Verify `governmentData` object structure

### Browser Developer Tools
- **Console**: Check for JavaScript errors and console.log output
- **Network**: Verify CDN resources load correctly
- **Elements**: Inspect DOM structure and CSS styles
- **Application**: Check local storage for saved officials data

## Validation Scenarios

### Complete End-to-End Testing
After making any changes, ALWAYS perform this validation:

1. **Application Startup**:
   - Start local server
   - Verify page loads without errors
   - Check all statistics display correctly (1,000+ contacts, 535 Congress, etc.)

2. **Navigation Testing**:
   - Click each tab: House → Senate → Executive → Cabinet → Supreme Court → Agencies
   - Verify each tab shows appropriate officials
   - Confirm search boxes appear for each section

3. **Search Functionality**:
   - Type "sanders" in Senate search → should show Bernie Sanders only
   - Type "texas" in House search → should show Texas representatives
   - Clear search → should show all officials again

4. **Contact Form Testing**:
   - Click any "📧 Email" button
   - Verify modal opens with all required fields
   - Check form validation (required fields marked with *)
   - Close modal and verify it disappears

5. **Responsive Design**:
   - Resize browser window to mobile size
   - Verify layout adapts correctly
   - Test touch-friendly button sizes

### Performance Validation
- **Load time**: Should be < 1 second on local server
- **Search response**: Filtering should be instant
- **Memory usage**: Check browser task manager for reasonable memory usage
- **Mobile performance**: Test on mobile devices or browser mobile simulation

## Data Structure and Customization

### Government Data Object Structure
```javascript
const governmentData = {
    house: [
        {
            name: "Official Name",
            title: "Position Title", 
            state: "State",
            district: "District Number",
            party: "Political Party",
            email: "email@house.gov",
            phone: "(202) 225-XXXX",
            office: "Office Address",
            website: "https://official.house.gov",
            twitter: "TwitterHandle",
            facebook: "FacebookPage",
            instagram: "InstagramHandle",
            youtube: "YouTubeChannel"
        }
    ],
    // Similar structure for senate, cabinet, supremeCourt, agencies
};
```

### Adding New Officials
1. Locate the appropriate section in `governmentData` object
2. Copy existing official structure
3. Update all fields with new official's information
4. Test the addition by searching for the new official

### Customization Options
- **Branding**: Change title, colors, logo in HTML/CSS sections
- **Data Sources**: Update official information in JavaScript objects
- **Features**: Add/remove functionality by modifying JavaScript
- **Styling**: Modify CSS variables and Bootstrap classes

## Browser Support and Compatibility

### Supported Browsers
- **Chrome**: 90+ (fully supported)
- **Firefox**: 88+ (fully supported) 
- **Safari**: 14+ (fully supported)
- **Edge**: 90+ (fully supported)
- **Mobile**: All modern mobile browsers

### Known Limitations
- **Internet Explorer**: Not supported (uses modern JavaScript)
- **Very old browsers**: May have CSS/JavaScript compatibility issues
- **CDN dependency**: Requires internet connection for Bootstrap/FontAwesome

## Ready to Deploy
The application is production-ready and requires only static file hosting. No build process, no server setup, no configuration needed - just upload `index.html` and it works!