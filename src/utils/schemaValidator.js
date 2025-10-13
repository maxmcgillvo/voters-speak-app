import Ajv from 'ajv';
import addFormats from 'ajv-formats';
import concernCategoriesSchema from '../data/concernCategories.schema.json';

/**
 * Validates data against the concern categories schema
 * 
 * @param {Object} data - The data to validate
 * @returns {Object} - Validation result with isValid and errors properties
 */
export const validateConcernsData = (data) => {
  const ajv = new Ajv({ allErrors: true });
  addFormats(ajv);
  
  const validate = ajv.compile(concernCategoriesSchema);
  const isValid = validate(data);
  
  return {
    isValid,
    errors: validate.errors || []
  };
};

/**
 * Checks if a concern has all required fields
 * 
 * @param {Object} concern - The concern object to validate
 * @returns {boolean} - Whether the concern is valid
 */
export const isValidConcern = (concern) => {
  if (!concern) return false;
  
  const requiredFields = ['id', 'title', 'description', 'relevantOfficials', 'isActive'];
  return requiredFields.every(field => concern[field] !== undefined);
};

/**
 * Checks if a news source has all required fields
 * 
 * @param {Object} source - The news source object to validate
 * @returns {boolean} - Whether the news source is valid
 */
export const isValidNewsSource = (source) => {
  if (!source) return false;
  
  const requiredFields = ['name', 'url', 'logoUrl'];
  return requiredFields.every(field => source[field] !== undefined);
};

export default {
  validateConcernsData,
  isValidConcern,
  isValidNewsSource
};