/**
 * @tidas-typescript-sdk
 * TypeScript SDK for ILCD/Tidas data management
 * 
 * @example
 * ```typescript
 * import { TidasContact, createContact, validateWithZod } from '@tidas-typescript-sdk';
 * 
 * // Create a new contact
 * const contact = createContact({
 *   contactDataSet: {
 *     contactInformation: {
 *       dataSetInformation: {
 *         'common:name': { '@xml:lang': 'en', '#text': 'My Company' }
 *       }
 *     }
 *   }
 * });
 * 
 * // Generate mock data
 * const mockContact = TidasContact.createMock();
 * 
 * // Validate data
 * const result = validateWithZod(contact.data, ContactsSchema);
 * ```
 */

// === Core Classes and Functions ===
export * from './core';

// === Type Definitions ===
export * from './types';

// === Zod Schemas and Validation ===
export * from './schemas';

export {
  // Zod validation functions
  validateWithZod,
  parseWithZod,
  validateBatch,
  
  // Main schemas
  ContactSchema,
  ProcessSchema,
  FlowSchema,
  SourceSchema,
  FlowPropertySchema,
  UnitGroupSchema,
  LCIAMethodSchema,
  LifeCycleModelSchema,
  
  // Validation result type
  type ValidationResult
} from './schemas';

export {
  // Common types
  type Contact,
  type Process,
  type Flow,
  type Source,
  type FlowProperty,
  type UnitGroup,
  type LCIAMethod,
  type LifeCycleModel,
  type DataSet
} from './types';

// === Services ===
export {
  // Suggestion service functions
  suggestData,
  batchSuggest,
  validateApiKey as validateSuggestionApiKey,
  getAvailableDataTypes,
  
  // Types
  type DataType as SuggestionDataType,
  type SuggestOptions,
  type SuggestResult as ServiceSuggestResult,
  
  // Deprecated (for backward compatibility)
  suggestRawData,
} from './services';
