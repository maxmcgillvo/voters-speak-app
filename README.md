# Your Concerns Feature - Voters Speak

This package contains the implementation of the "Your Concerns" feature for the Voters Speak application. The feature connects current events to relevant officials, helping users understand who to contact about issues that matter to them.

## Contents

- `src/` - Source code for the React components
- `public/` - Public assets (images, etc.)
- `integration-example.html` - Example HTML file showing how to integrate the components
- `demo.html` - Interactive demo of the components
- `INTEGRATION_GUIDE.md` - Detailed guide for integrating the components with the existing site
- `package.json` - Node.js package configuration
- `vite.config.js` - Vite build configuration

## Quick Start

1. Install dependencies:

```bash
npm install
```

2. Start the development server:

```bash
npm start
```

3. Build for production:

```bash
npm run build
```

## Integration

See `INTEGRATION_GUIDE.md` for detailed instructions on integrating the components with the existing Voters Speak site.

## Components

### NewsSources

A responsive component that displays news source logos in a grid (desktop) or carousel (mobile). Each logo links to the politics section of the respective news source.

### ConcernCard

A card component that displays information about a political concern and provides a button to contact relevant officials.

### ConcernsPage

The main page component that displays the "Your Concerns" feature. It loads concern data and renders the NewsSources and ConcernCard components.

## Data Structure

The components use the following data files:

- `src/data/concernsData.json` - Data for the concerns and news sources
- `src/data/officialMapping.json` - Mapping between concerns and officials
- `src/data/concernCategories.schema.json` - JSON schema for the concerns data

## Demo

Open `demo.html` in your browser to see an interactive demo of the components.

## License

MIT