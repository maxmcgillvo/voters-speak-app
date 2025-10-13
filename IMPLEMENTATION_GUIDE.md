# Your Concerns Feature - Technical Implementation Guide

This guide provides detailed technical instructions for implementing the "Your Concerns" feature in the Voters Speak application.

## Architecture Overview

The "Your Concerns" feature consists of three main components:

1. **Data Layer**: JSON data structures for concerns and officials mapping
2. **UI Components**: Responsive layouts for desktop and mobile
3. **Integration Layer**: Connection to the existing officials directory

## Data Layer Implementation

### Data Files

- `concerns.json`: Main data file following the schema in `your_concerns_schema.json`
- `officials_mapping.json`: Maps officials to concerns

### Data Loading

```javascript
// Example code for loading the concerns data
async function loadConcernsData() {
  try {
    const response = await fetch('/data/concerns.json');
    if (!response.ok) throw new Error('Failed to load concerns data');
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error loading concerns data:', error);
    return { concerns: [], newsSources: [], metadata: {} };
  }
}
```

### Data Validation

Implement validation to ensure the data follows the schema:

```javascript
function validateConcernsData(data) {
  // Required top-level properties
  if (!data.concerns || !Array.isArray(data.concerns)) return false;
  if (!data.newsSources || !Array.isArray(data.newsSources)) return false;
  if (!data.metadata || typeof data.metadata !== 'object') return false;
  
  // Validate each concern
  for (const concern of data.concerns) {
    if (!concern.id || !concern.title || !concern.description) return false;
    if (!Array.isArray(concern.relevantOfficials)) return false;
    if (typeof concern.isActive !== 'boolean') return false;
  }
  
  // Validate news sources
  for (const source of data.newsSources) {
    if (!source.name || !source.url || !source.logoUrl) return false;
  }
  
  return true;
}
```

## UI Components Implementation

### News Sources Component

```javascript
function renderNewsSources(sources, isMobile = false) {
  const container = document.createElement('div');
  container.className = 'news-sources-container';
  
  const heading = document.createElement('h2');
  heading.textContent = "WHAT'S HAPPENING RIGHT NOW";
  container.appendChild(heading);
  
  const subheading = document.createElement('p');
  subheading.textContent = "Stay informed with coverage from multiple perspectives";
  container.appendChild(subheading);
  
  const sourcesContainer = document.createElement('div');
  sourcesContainer.className = isMobile ? 'news-sources-carousel' : 'news-sources-grid';
  
  sources.forEach(source => {
    const sourceElement = document.createElement('a');
    sourceElement.href = source.url;
    sourceElement.target = '_blank';
    sourceElement.rel = 'noopener noreferrer';
    sourceElement.className = 'news-source';
    
    const logo = document.createElement('img');
    logo.src = source.logoUrl;
    logo.alt = `${source.name} logo`;
    
    const name = document.createElement('span');
    name.textContent = source.name;
    
    sourceElement.appendChild(logo);
    sourceElement.appendChild(name);
    sourcesContainer.appendChild(sourceElement);
  });
  
  container.appendChild(sourcesContainer);
  
  if (isMobile) {
    // Add carousel navigation
    const nav = document.createElement('div');
    nav.className = 'carousel-nav';
    // Implement carousel navigation logic here
    container.appendChild(nav);
  }
  
  return container;
}
```

### Concern Card Component

```javascript
function renderConcernCard(concern) {
  const card = document.createElement('div');
  card.className = 'concern-card';
  card.dataset.concernId = concern.id;
  
  const title = document.createElement('h3');
  title.textContent = concern.title;
  card.appendChild(title);
  
  if (concern.subtitle) {
    const subtitle = document.createElement('h4');
    subtitle.textContent = concern.subtitle;
    card.appendChild(subtitle);
  }
  
  const description = document.createElement('p');
  description.textContent = concern.description;
  card.appendChild(description);
  
  const button = document.createElement('button');
  button.className = 'contact-officials-btn';
  button.textContent = 'CONTACT OFFICIALS';
  button.addEventListener('click', () => {
    // Navigate to officials directory with filter
    window.location.href = `/officials?concerns=${concern.id}`;
  });
  
  card.appendChild(button);
  
  return card;
}
```

### Responsive Layout

```css
/* Base styles */
.your-concerns-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.concerns-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 30px;
}

.news-sources-grid {
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  gap: 10px;
  margin: 20px 0;
}

/* Mobile styles */
@media (max-width: 768px) {
  .concerns-grid {
    grid-template-columns: 1fr;
  }
  
  .news-sources-grid {
    display: none;
  }
  
  .news-sources-carousel {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    padding: 10px 0;
  }
  
  .news-sources-carousel .news-source {
    flex: 0 0 33.333%;
    scroll-snap-align: start;
  }
}
```

## Integration with Officials Directory

### Filtering Officials by Concern

```javascript
function filterOfficialsByConcern(concernId) {
  // Load officials mapping
  fetch('/data/officials_mapping.json')
    .then(response => response.json())
    .then(mapping => {
      // Find officials relevant to this concern
      const relevantOfficials = mapping.officials.filter(official => 
        official.relevantConcerns.includes(concernId)
      );
      
      // Update the officials directory UI
      displayFilteredOfficials(relevantOfficials);
    })
    .catch(error => {
      console.error('Error loading officials mapping:', error);
    });
}

function displayFilteredOfficials(officials) {
  // Clear existing officials display
  const container = document.getElementById('officials-container');
  container.innerHTML = '';
  
  // Add filtered officials
  officials.forEach(official => {
    const officialElement = createOfficialElement(official);
    container.appendChild(officialElement);
  });
  
  // Update filter status display
  const filterStatus = document.getElementById('filter-status');
  filterStatus.textContent = `Showing ${officials.length} officials relevant to this concern`;
}
```

### Updating the Navigation

```javascript
function addYourConcernsToNavigation() {
  const nav = document.querySelector('nav ul');
  
  const concernsLink = document.createElement('li');
  const link = document.createElement('a');
  link.href = '/your-concerns';
  link.textContent = 'Your Concerns';
  
  concernsLink.appendChild(link);
  nav.appendChild(concernsLink);
}
```

## Rotating Concern Slot Implementation

```javascript
function setupRotatingConcern() {
  // Check if it's time to update the rotating concern
  const lastUpdate = localStorage.getItem('rotatingConcernLastUpdate');
  const now = new Date().toISOString();
  
  if (!lastUpdate || isTimeToUpdate(lastUpdate, now)) {
    // Load concerns data
    loadConcernsData().then(data => {
      // Find the current rotating concern
      const rotatingConcern = data.concerns.find(c => c.isRotating);
      
      // Check if it's time to rotate to a new concern
      if (shouldRotateConcern(rotatingConcern)) {
        // Select a new rotating concern from the pool
        selectNewRotatingConcern(data.concerns);
      }
      
      // Update the UI
      updateRotatingConcernUI(rotatingConcern);
      
      // Save the update time
      localStorage.setItem('rotatingConcernLastUpdate', now);
    });
  }
}

function isTimeToUpdate(lastUpdate, now) {
  // Check if it's been at least 24 hours since the last update
  const lastUpdateDate = new Date(lastUpdate);
  const nowDate = new Date(now);
  
  const diffMs = nowDate - lastUpdateDate;
  const diffHours = diffMs / (1000 * 60 * 60);
  
  return diffHours >= 24;
}

function shouldRotateConcern(concern) {
  // Logic to determine if it's time to rotate to a new concern
  // For example, rotate weekly
  if (!concern.dateAdded) return true;
  
  const addedDate = new Date(concern.dateAdded);
  const now = new Date();
  
  const diffMs = now - addedDate;
  const diffDays = diffMs / (1000 * 60 * 60 * 24);
  
  return diffDays >= 7;
}
```

## Testing Plan

1. **Unit Tests**
   - Test data loading and validation
   - Test UI component rendering
   - Test officials filtering logic

2. **Integration Tests**
   - Test navigation between concerns and officials
   - Test responsive layout transitions
   - Test carousel functionality on mobile

3. **User Acceptance Testing**
   - Verify content neutrality
   - Test accessibility with screen readers
   - Verify all links work correctly

## Performance Considerations

- Lazy load news source logos
- Implement pagination for officials if the list is long
- Cache concerns data to reduce API calls
- Use IntersectionObserver for lazy loading content

## Security Considerations

- Validate all data from external sources
- Sanitize content before rendering to prevent XSS
- Implement proper CORS headers for API requests
- Use HTTPS for all external links

## Deployment Checklist

- Validate all JSON files against their schemas
- Test on multiple browsers and devices
- Verify all links are working
- Check accessibility compliance
- Optimize images and assets
- Update documentation