// Main exports
export * from './core';
export * from './utils/object-utils';

// Types re-export
export * from './types';

// Validation (placeholder - to be implemented in phase 4)
export { validate, isValid } from './validation';

// Convenience exports - Type-driven and schema-independent
export {
  // Core classes
  TidasContact,
  TidasProcess,
  TidasFlow,
  
  // Type-driven factory functions (RECOMMENDED - adapts to schema changes)
  createContact,
  createProcess,
  createFlow,
  
  // Type-safe builders (RECOMMENDED - fluent API with compile-time checking)
  buildContact,
  buildProcess,
  buildFlow,
  
  // JSON conversion
  fromJSON,
  toJSON,
  toJSONObject,
  fromJSONArray,
  toJSONArray,
  
  // Type-aware helpers
  TypeAwareHelpers,
  
  // Utilities
  deepClone,
  merge,
  get,
  set,
  updatePath,
  
  // Helper functions
  createMultiLangText,
  generateUUID
} from './core';
