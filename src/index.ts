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

// === Utilities ===
export * from './utils/object-utils';

// === Legacy Validation (Deprecated - Use Zod validation instead) ===
export { validate, isValid } from './validation';

// === Re-export commonly used items for convenience ===
export {
  // Core object classes
  TidasContact,
  TidasProcess, 
  TidasFlow,
  
  // Factory functions
  createContact,
  createProcess,
  createFlow,
  
  // Builder pattern
  buildContact,
  buildProcess, 
  buildFlow,
  
  // JSON conversion
  fromJSON,
  toJSON,
  toJSONObject,
  fromJSONArray,
  toJSONArray,
  
  // Type definitions
  type ValidationOptions,
  type SerializationOptions,
  type CloneOptions,
  type MockOptions,
  
  // Utilities
  createMultiLangText,
  generateUUID,
  TypeAwareHelpers
} from './core';

export {
  // Zod validation functions
  validateWithZod,
  parseWithZod,
  validateBatch,
  
  // Main schemas
  ContactsSchema,
  ProcessesSchema,
  FlowsSchema,
  SourcesSchema,
  FlowpropertiesSchema,
  UnitgroupsSchema,
  LciamethodsSchema,
  LifecyclemodelsSchema,
  
  // Validation result type
  type ValidationResult
} from './schemas';

export {
  // Common types
  type Contacts,
  type Processes,
  type Flows,
  type Sources,
  type Flowproperties,
  type Unitgroups,
  type Lciamethods,
  type Lifecyclemodels,
  type DataSet
} from './types';
