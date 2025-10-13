/**
 * This file contains vanilla JavaScript implementations of the components
 * that can be used without requiring a build step.
 */

// Create a news source element
function createNewsSource(source) {
  const newsSource = document.createElement('a');
  newsSource.href = source.url;
  newsSource.className = 'news-source';
  newsSource.target = '_blank';
  newsSource.rel = 'noopener noreferrer';
  
  const name = document.createElement('div');
  name.className = 'news-source-name';
  name.textContent = source.name;
  
  newsSource.appendChild(name);
  return newsSource;
}

// Create a news sources section
function createNewsSources(sources, isMobile = false) {
  const container = document.createElement('div');
  container.className = 'news-sources-container';
  
  const heading = document.createElement('h2');
  heading.className = 'section-title';
  heading.textContent = "WHAT'S HAPPENING RIGHT NOW";
  container.appendChild(heading);
  
  const subheading = document.createElement('p');
  subheading.className = 'section-subtitle';
  subheading.textContent = "Stay informed with coverage from multiple perspectives";
  container.appendChild(subheading);
  
  const newsSourcesGrid = document.createElement('div');
  newsSourcesGrid.className = isMobile ? 'news-sources-carousel' : 'news-sources-grid';
  
  // If mobile, only show a subset of sources
  const displayedSources = isMobile ? sources.slice(0, 3) : sources;
  
  displayedSources.forEach(source => {
    newsSourcesGrid.appendChild(createNewsSource(source));
  });
  
  container.appendChild(newsSourcesGrid);
  
  // If mobile and we have more than 3 sources, add navigation
  if (isMobile && sources.length > 3) {
    const navigation = document.createElement('div');
    navigation.className = 'news-sources-navigation';
    
    const prevButton = document.createElement('button');
    prevButton.textContent = '<';
    prevButton.className = 'nav-button';
    prevButton.setAttribute('aria-label', 'Previous page');
    
    const pageIndicator = document.createElement('span');
    pageIndicator.className = 'page-indicator';
    pageIndicator.textContent = '1/' + Math.ceil(sources.length / 3);
    
    const nextButton = document.createElement('button');
    nextButton.textContent = '>';
    nextButton.className = 'nav-button';
    nextButton.setAttribute('aria-label', 'Next page');
    
    navigation.appendChild(prevButton);
    navigation.appendChild(pageIndicator);
    navigation.appendChild(nextButton);
    
    container.appendChild(navigation);
    
    // Add event listeners for navigation
    let currentPage = 0;
    const totalPages = Math.ceil(sources.length / 3);
    
    prevButton.addEventListener('click', () => {
      currentPage = (currentPage - 1 + totalPages) % totalPages;
      updateCarousel();
    });
    
    nextButton.addEventListener('click', () => {
      currentPage = (currentPage + 1) % totalPages;
      updateCarousel();
    });
    
    function updateCarousel() {
      // Update page indicator
      pageIndicator.textContent = (currentPage + 1) + '/' + totalPages;
      
      // Update displayed sources
      newsSourcesGrid.innerHTML = '';
      const start = currentPage * 3;
      const end = Math.min(start + 3, sources.length);
      
      for (let i = start; i < end; i++) {
        newsSourcesGrid.appendChild(createNewsSource(sources[i]));
      }
    }
  }
  
  return container;
}

// Create a concern card
function createConcernCard(concern, onContactClick, isRotating = false) {
  const card = document.createElement('div');
  card.className = 'concern-card';
  if (isRotating) {
    card.classList.add('rotating');
  }
  
  // Add rotating badge if needed
  if (isRotating) {
    const badge = document.createElement('div');
    badge.className = 'rotating-badge';
    badge.textContent = 'Current Issue';
    card.appendChild(badge);
  }
  
  // Add title
  const title = document.createElement('h3');
  title.className = 'concern-title';
  title.textContent = concern.title;
  card.appendChild(title);
  
  // Add subtitle if present
  if (concern.subtitle) {
    const subtitle = document.createElement('h4');
    subtitle.className = 'concern-subtitle';
    subtitle.textContent = concern.subtitle;
    card.appendChild(subtitle);
  }
  
  // Add description
  const description = document.createElement('p');
  description.className = 'concern-description';
  description.textContent = concern.description;
  card.appendChild(description);
  
  // Add related links if present
  if (concern.relatedLinks && concern.relatedLinks.length > 0) {
    const linksContainer = document.createElement('div');
    linksContainer.className = 'concern-links';
    
    const linksHeading = document.createElement('h5');
    linksHeading.className = 'links-heading';
    linksHeading.textContent = 'Related Resources:';
    linksContainer.appendChild(linksHeading);
    
    const linksList = document.createElement('ul');
    linksList.className = 'links-list';
    
    concern.relatedLinks.forEach(link => {
      const listItem = document.createElement('li');
      
      const linkElement = document.createElement('a');
      linkElement.href = link.url;
      linkElement.target = '_blank';
      linkElement.rel = 'noopener noreferrer';
      linkElement.className = 'concern-link';
      linkElement.textContent = link.title;
      
      if (link.source) {
        const sourceSpan = document.createElement('span');
        sourceSpan.className = 'link-source';
        sourceSpan.textContent = ` (${link.source})`;
        linkElement.appendChild(sourceSpan);
      }
      
      listItem.appendChild(linkElement);
      linksList.appendChild(listItem);
    });
    
    linksContainer.appendChild(linksList);
    card.appendChild(linksContainer);
  }
  
  // Add contact button
  const contactButton = document.createElement('button');
  contactButton.className = 'contact-button';
  contactButton.textContent = 'CONTACT OFFICIALS';
  contactButton.setAttribute('aria-label', `Contact officials about ${concern.title}`);
  
  contactButton.addEventListener('click', () => {
    if (onContactClick) {
      onContactClick(concern.id, concern.relevantOfficials);
    }
  });
  
  card.appendChild(contactButton);
  
  return card;
}

// Create the concerns page
function createConcernsPage(concernsData, onContactClick) {
  const container = document.createElement('div');
  container.className = 'concerns-page';
  
  // Add header
  const header = document.createElement('header');
  header.className = 'concerns-header';
  
  const title = document.createElement('h1');
  title.className = 'concerns-title';
  title.textContent = 'YOUR CONCERNS';
  header.appendChild(title);
  
  const subtitle = document.createElement('p');
  subtitle.className = 'concerns-subtitle';
  subtitle.textContent = 'Your voice matters in our democracy';
  header.appendChild(subtitle);
  
  container.appendChild(header);
  
  // Add news sources section if data is available
  if (concernsData.newsSources && concernsData.newsSources.length > 0) {
    const isMobile = window.innerWidth <= 768;
    const newsSourcesSection = document.createElement('section');
    newsSourcesSection.className = 'news-sources-section';
    newsSourcesSection.appendChild(createNewsSources(concernsData.newsSources, isMobile));
    container.appendChild(newsSourcesSection);
  }
  
  // Add concerns grid
  const concernsSection = document.createElement('section');
  concernsSection.className = 'concerns-section';
  
  const concernsGrid = document.createElement('div');
  concernsGrid.className = 'concerns-grid';
  
  // Sort concerns by order property
  const sortedConcerns = concernsData.concerns
    ? [...concernsData.concerns].sort((a, b) => a.order - b.order)
    : [];
  
  // Find the rotating concern
  const rotatingConcern = sortedConcerns.find(concern => concern.isRotating);
  
  sortedConcerns.forEach(concern => {
    const concernCardWrapper = document.createElement('div');
    concernCardWrapper.className = 'concern-card-wrapper';
    concernCardWrapper.appendChild(createConcernCard(
      concern,
      onContactClick,
      concern.isRotating
    ));
    concernsGrid.appendChild(concernCardWrapper);
  });
  
  concernsSection.appendChild(concernsGrid);
  container.appendChild(concernsSection);
  
  // Add footer with metadata if available
  if (concernsData.metadata) {
    const footer = document.createElement('footer');
    footer.className = 'concerns-footer';
    
    const lastUpdated = document.createElement('p');
    lastUpdated.className = 'last-updated';
    lastUpdated.textContent = `Last updated: ${new Date(concernsData.metadata.lastUpdated).toLocaleDateString()}`;
    footer.appendChild(lastUpdated);
    
    container.appendChild(footer);
  }
  
  return container;
}

// Export the components
window.YourConcernsComponents = {
  createNewsSource,
  createNewsSources,
  createConcernCard,
  createConcernsPage
};