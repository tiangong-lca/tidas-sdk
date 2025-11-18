/**
 * Utility functions index
 * Provides unified access to all utility functions
 */

// Object manipulation utilities
export * from './object-utils';

// Re-export commonly used functions with cleaner names
export { deepClone, merge, get, set, updatePath } from './object-utils';