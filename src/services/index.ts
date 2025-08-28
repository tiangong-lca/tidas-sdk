/**
 * Services module index
 * 
 * Exports the suggestion service for external use
 */

export {
  // Main functions
  suggestData,
  batchSuggest,
  
  // Utility functions
  validateApiKey,
  getAvailableDataTypes,
  
  // Types
  type DataType,
  type SuggestOptions,
  type SuggestResult,
  
  // Deprecated (for backward compatibility)
  suggestRawData,
} from './suggestion-service';

// Default export
import suggestionService from './suggestion-service';
export default suggestionService;