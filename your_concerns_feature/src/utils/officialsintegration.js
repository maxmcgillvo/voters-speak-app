/**
 * Filters officials based on concern ID and relevant officials
 * 
 * @param {string} concernId - The ID of the selected concern
 * @param {Array} relevantOfficials - Array of official IDs relevant to the concern
 * @param {Array} allOfficials - Array of all officials data
 * @returns {Array} - Filtered officials
 */
export const filterOfficialsByConcern = (concernId, relevantOfficials, allOfficials) => {
  if (!concernId || !relevantOfficials || !allOfficials) {
    return [];
  }
  
  return allOfficials.filter(official => 
    relevantOfficials.includes(official.id)
  );
};

/**
 * Navigates to the officials directory with concern filter
 * This function can be customized based on the integration approach
 * 
 * @param {string} concernId - The ID of the selected concern
 * @param {Array} relevantOfficials - Array of official IDs relevant to the concern
 */
export const navigateToOfficials = (concernId, relevantOfficials) => {
  // For integration with the static HTML site
  // We'll use URL parameters to pass the filter information
  
  const params = new URLSearchParams();
  params.append('concernId', concernId);
  
  if (relevantOfficials && relevantOfficials.length) {
    params.append('officials', relevantOfficials.join(','));
  }
  
  // Redirect to the officials page with the filter parameters
  window.location.href = `/officials.html?${params.toString()}`;
};

/**
 * Attaches the navigation function to the window object
 * This allows the static HTML site to call this function
 */
export const setupGlobalNavigation = () => {
  window.navigateToOfficials = navigateToOfficials;
};

export default {
  filterOfficialsByConcern,
  navigateToOfficials,
  setupGlobalNavigation
};