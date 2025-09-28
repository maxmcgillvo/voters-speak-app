import React from 'react';
import styles from './ConcernCard.module.css';

/**
 * ConcernCard component displays information about a political concern
 * and provides a button to contact relevant officials
 * 
 * @param {Object} props
 * @param {Object} props.concern - The concern data object
 * @param {Function} props.onContactClick - Function to call when contact button is clicked
 * @param {boolean} props.isRotating - Whether this is the rotating concern slot
 */
const ConcernCard = ({ concern, onContactClick, isRotating = false }) => {
  if (!concern) return null;
  
  const handleContactClick = () => {
    if (onContactClick) {
      onContactClick(concern.id, concern.relevantOfficials);
    }
  };
  
  return (
    <div className={`${styles.card} ${isRotating ? styles.rotating : ''}`}>
      {isRotating && (
        <div className={styles.rotatingBadge}>
          Current Issue
        </div>
      )}
      
      <h3 className={styles.title}>{concern.title}</h3>
      
      {concern.subtitle && (
        <h4 className={styles.subtitle}>{concern.subtitle}</h4>
      )}
      
      <p className={styles.description}>{concern.description}</p>
      
      {concern.relatedLinks && concern.relatedLinks.length > 0 && (
        <div className={styles.links}>
          <h5 className={styles.linksHeading}>Related Resources:</h5>
          <ul className={styles.linksList}>
            {concern.relatedLinks.map((link, index) => (
              <li key={index}>
                <a 
                  href={link.url} 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className={styles.link}
                >
                  {link.title}
                  {link.source && <span className={styles.source}> ({link.source})</span>}
                </a>
              </li>
            ))}
          </ul>
        </div>
      )}
      
      <button 
        className={styles.contactButton}
        onClick={handleContactClick}
        aria-label={`Contact officials about ${concern.title}`}
      >
        CONTACT OFFICIALS
      </button>
    </div>
  );
};

export default ConcernCard;