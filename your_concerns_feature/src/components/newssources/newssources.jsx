import React, { useState } from 'react';
import styles from './NewsSources.module.css';

/**
 * NewsSources component displays a grid or carousel of news source logos that link to their websites
 * 
 * @param {Object} props
 * @param {Array} props.sources - Array of news source objects
 * @param {boolean} props.isMobile - Whether to display in mobile mode (carousel)
 */
const NewsSources = ({ sources = [], isMobile = false }) => {
  const [carouselPage, setCarouselPage] = useState(0);
  const sourcesPerPage = isMobile ? 3 : sources.length;
  const totalPages = Math.ceil(sources.length / sourcesPerPage);
  
  const displayedSources = isMobile
    ? sources.slice(carouselPage * sourcesPerPage, (carouselPage + 1) * sourcesPerPage)
    : sources;
    
  const nextPage = () => {
    setCarouselPage((prev) => (prev + 1) % totalPages);
  };
  
  const prevPage = () => {
    setCarouselPage((prev) => (prev - 1 + totalPages) % totalPages);
  };
  
  return (
    <div className={styles.container}>
      <h2 className={styles.heading}>WHAT'S HAPPENING RIGHT NOW</h2>
      <p className={styles.subheading}>Stay informed with coverage from multiple perspectives</p>
      
      <div className={isMobile ? styles.carousel : styles.grid}>
        {displayedSources.map((source) => (
          <a 
            key={source.name}
            href={source.url}
            target="_blank"
            rel="noopener noreferrer"
            className={styles.newsSource}
            aria-label={`Visit ${source.name} website`}
          >
            <img 
              src={source.logoUrl} 
              alt={`${source.name} logo`}
              className={styles.logo}
            />
            <span className={styles.name}>{source.name}</span>
          </a>
        ))}
      </div>
      
      {isMobile && totalPages > 1 && (
        <div className={styles.navigation}>
          <button 
            onClick={prevPage}
            aria-label="Previous page"
            className={styles.navButton}
          >
            &lt;
          </button>
          <span className={styles.pageIndicator}>
            {carouselPage + 1}/{totalPages}
          </span>
          <button 
            onClick={nextPage}
            aria-label="Next page"
            className={styles.navButton}
          >
            &gt;
          </button>
        </div>
      )}
    </div>
  );
};

export default NewsSources;