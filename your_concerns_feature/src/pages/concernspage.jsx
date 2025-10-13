import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import NewsSources from '../components/NewsSources/NewsSources';
import ConcernCard from '../components/ConcernCard/ConcernCard';
import styles from './ConcernsPage.module.css';

/**
 * ConcernsPage displays the "Your Concerns" feature with news sources
 * and concern cards that connect users to relevant officials
 */
const ConcernsPage = () => {
  const [concernsData, setConcernsData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isMobile, setIsMobile] = useState(window.innerWidth <= 768);
  const navigate = useNavigate();
  
  // Handle window resize for responsive layout
  useEffect(() => {
    const handleResize = () => {
      setIsMobile(window.innerWidth <= 768);
    };
    
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);
  
  // Load concerns data
  useEffect(() => {
    const fetchConcernsData = async () => {
      try {
        setLoading(true);
        // In production, this would be an API call
        // For now, we'll import the data directly
        const data = await import('../data/concernsData.json');
        
        setConcernsData(data.default || data);
        setLoading(false);
      } catch (err) {
        console.error('Error loading concerns data:', err);
        setError('Unable to load concerns information. Please try again later.');
        setLoading(false);
      }
    };
    
    fetchConcernsData();
  }, []);
  
  // Handle contact officials button click
  const handleContactOfficials = (concernId, relevantOfficials) => {
    // Navigate to officials directory with filter
    navigate('/officials', { 
      state: { 
        concernId,
        relevantOfficials 
      }
    });
    
    // For integration with the static site, we might need a different approach
    // such as setting URL parameters or using a global event system
    if (window.navigateToOfficials) {
      window.navigateToOfficials(concernId, relevantOfficials);
    }
  };
  
  if (loading) {
    return (
      <div className={styles.loadingContainer}>
        <div className={styles.loadingSpinner}></div>
        <p>Loading concerns information...</p>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className={styles.errorContainer}>
        <h2>Something went wrong</h2>
        <p>{error}</p>
        <button 
          onClick={() => window.location.reload()}
          className={styles.retryButton}
        >
          Try Again
        </button>
      </div>
    );
  }
  
  // Sort concerns by order property
  const sortedConcerns = concernsData?.concerns
    ? [...concernsData.concerns].sort((a, b) => a.order - b.order)
    : [];
    
  // Find the rotating concern
  const rotatingConcern = sortedConcerns.find(concern => concern.isRotating);
  
  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <h1 className={styles.title}>YOUR CONCERNS</h1>
        <p className={styles.subtitle}>Your voice matters in our democracy</p>
      </header>
      
      {/* News Sources Section */}
      {concernsData?.newsSources && (
        <section className={styles.newsSourcesSection}>
          <NewsSources 
            sources={concernsData.newsSources} 
            isMobile={isMobile} 
          />
        </section>
      )}
      
      {/* Concerns Grid */}
      <section className={styles.concernsSection}>
        <div className={styles.concernsGrid}>
          {sortedConcerns.map(concern => (
            <div key={concern.id} className={styles.concernCardWrapper}>
              <ConcernCard 
                concern={concern}
                onContactClick={handleContactOfficials}
                isRotating={concern.isRotating}
              />
            </div>
          ))}
        </div>
      </section>
      
      {/* Metadata and Last Updated */}
      {concernsData?.metadata && (
        <footer className={styles.footer}>
          <p className={styles.lastUpdated}>
            Last updated: {new Date(concernsData.metadata.lastUpdated).toLocaleDateString()}
          </p>
        </footer>
      )}
    </div>
  );
};

export default ConcernsPage;