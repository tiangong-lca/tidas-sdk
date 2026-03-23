/**
 * Utility functions index
 * Provides unified access to all utility functions
 */

// Object manipulation utilities
export * from './object-utils';
export * from './markdown';
export * from './uuid';

// Re-export commonly used functions with cleaner names
export { deepClone, merge, get, set, updatePath } from './object-utils';
