# Your Concerns Feature - Integration Guide

This guide explains how to integrate the "Your Concerns" React components with the existing Voters Speak static HTML site.

## Prerequisites

- Node.js 16+ and npm (for building the React components)
- Basic understanding of HTML, CSS, and JavaScript

## Building the React Components

1. Navigate to the `your_concerns_react` directory:

```bash
cd your_concerns_react
```

2. Install dependencies:

```bash
npm install
```

3. Build the React components:

```bash
npm run build
```

This will create a UMD bundle in the `dist` directory that can be integrated with the existing static HTML site.

## Integration Steps

### 1. Copy the Required Files

Copy the following files to your static site:

- `dist/voters-speak-your-concerns.umd.js` - The bundled React components
- `public/assets/images/news-logos/` - The news source logos (if not already available)

### 2. Create a New HTML Page

Create a new HTML page for the "Your Concerns" feature. You can use the `integration-example.html` file as a starting point.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Voters Speak - Your Concerns</title>
    <!-- Include your existing CSS -->
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Include your existing header and navigation -->
    <header>
        <!-- Your header content -->
    </header>

    <nav>
        <!-- Your navigation content -->
    </nav>

    <!-- Container for the React app -->
    <main>
        <div id="your-concerns-app"></div>
    </main>

    <!-- Include your existing footer -->
    <footer>
        <!-- Your footer content -->
    </footer>

    <!-- Load React and React DOM -->
    <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <script src="https://unpkg.com/react-router-dom@6/umd/react-router-dom.production.min.js"></script>
    
    <!-- Load our bundled React app -->
    <script src="dist/voters-speak-your-concerns.umd.js"></script>
    
    <script>
        // Initialize the React app
        document.addEventListener('DOMContentLoaded', function() {
            // Call the render function exported from our bundle
            window.renderYourConcerns('your-concerns-app');
        });
    </script>
</body>
</html>
```

### 3. Implement the Officials Directory Integration

The "Contact Officials" button in the ConcernCard component needs to navigate to the officials directory with filters applied. There are two ways to implement this:

#### Option 1: URL Parameters

Modify the `navigateToOfficials` function in your HTML page to use URL parameters:

```javascript
window.navigateToOfficials = function(concernId, relevantOfficials) {
    const params = new URLSearchParams();
    params.append('concernId', concernId);
    
    if (relevantOfficials && relevantOfficials.length) {
        params.append('officials', relevantOfficials.join(','));
    }
    
    // Redirect to the officials page with the filter parameters
    window.location.href = `officials.html?${params.toString()}`;
};
```

Then, in your officials directory page, parse the URL parameters and apply the filters:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    const params = new URLSearchParams(window.location.search);
    const concernId = params.get('concernId');
    const officials = params.get('officials');
    
    if (concernId && officials) {
        const officialIds = officials.split(',');
        // Apply filters to your officials directory
        filterOfficialsByIds(officialIds);
    }
});
```

#### Option 2: Session Storage

Alternatively, you can use session storage to pass the filter information:

```javascript
window.navigateToOfficials = function(concernId, relevantOfficials) {
    // Store the filter information in session storage
    sessionStorage.setItem('concernFilter', JSON.stringify({
        concernId,
        relevantOfficials
    }));
    
    // Redirect to the officials page
    window.location.href = 'officials.html';
};
```

Then, in your officials directory page, check for the filter information in session storage:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    const filterJson = sessionStorage.getItem('concernFilter');
    
    if (filterJson) {
        const filter = JSON.parse(filterJson);
        // Apply filters to your officials directory
        filterOfficialsByIds(filter.relevantOfficials);
        
        // Clear the filter information from session storage
        sessionStorage.removeItem('concernFilter');
    }
});
```

### 4. Add News Source Logos

The NewsSources component requires logo images for each news source. Make sure these images are available at the paths specified in the `concernsData.json` file.

Default path: `/assets/images/news-logos/`

You can modify the paths in the `concernsData.json` file if needed.

### 5. Update the Navigation

Add a link to the "Your Concerns" page in your navigation menu:

```html
<nav>
    <a href="index.html">Home</a>
    <a href="officials.html">Officials Directory</a>
    <a href="concerns.html">Your Concerns</a>
    <a href="about.html">About</a>
</nav>
```

### 6. Test the Integration

Open the "Your Concerns" page in your browser and test the following:

- The page loads without errors
- The news sources are displayed correctly
- The concern cards are displayed correctly
- The "Contact Officials" button navigates to the officials directory with filters applied

## Customizing the Content

### Updating the Concerns

The concerns data is stored in the `concernsData.json` file. You can modify this file to update the concerns, add new concerns, or remove existing concerns.

Make sure the data follows the schema defined in `concernCategories.schema.json`.

### Updating the News Sources

The news sources data is also stored in the `concernsData.json` file. You can modify this file to update the news sources, add new sources, or remove existing sources.

### Updating the Officials Mapping

The officials mapping is stored in the `officialMapping.json` file. You can modify this file to update the mapping between concerns and officials.

## Advanced Integration

### Using Individual Components

If you want to use the individual components instead of the full page, you can import them directly:

```javascript
const { NewsSources, ConcernCard } = window.VotersSpeakConcerns;

// Create root for news sources
const newsRoot = ReactDOM.createRoot(document.getElementById('news-sources-container'));
newsRoot.render(
    React.createElement(NewsSources, { 
        sources: newsSources,
        isMobile: false
    })
);

// Create root for concern card
const cardRoot = ReactDOM.createRoot(document.getElementById('concern-card-container'));
cardRoot.render(
    React.createElement(ConcernCard, { 
        concern: concern,
        onContactClick: handleContactClick,
        isRotating: false
    })
);
```

### Customizing the Styling

The components use CSS modules for styling. If you need to customize the styling, you'll need to modify the CSS files and rebuild the React components.

Alternatively, you can override the styles using CSS custom properties (variables) or by adding custom CSS rules with higher specificity.

## Troubleshooting

### React Not Defined

If you see an error like "React is not defined", make sure you've included the React and ReactDOM scripts in your HTML file.

### Component Not Rendering

If the components are not rendering, check the browser console for errors. Make sure the container element exists in the DOM before calling `renderYourConcerns`.

### Missing News Source Logos

If the news source logos are not displaying, check that the image paths in `concernsData.json` are correct and that the images exist at those paths.

### Contact Officials Button Not Working

If the "Contact Officials" button is not navigating to the officials directory, make sure you've implemented the `navigateToOfficials` function correctly.

## Need Help?

If you encounter any issues with the integration, please refer to the README.md file or contact the development team for assistance.