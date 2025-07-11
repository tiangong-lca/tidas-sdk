/**
 * Core module exports
 * Provides unified access to all Tidas SDK functionality
 */


// Zod Proxy for true property access with Schema validation
export {
  ZodProxy,
  createZodProxy,
  type PathInfo,
  type AccessLogEntry,
  type ZodProxyOptions,
  type ZodProxyValidationResult
} from './zod-proxy';

// TIDAS-specific Zod factories
export {
  createZodContact,
  createZodFlow,
  createZodProcess,
  createZodTidasProxy,
  ContactSchema,
  FlowSchema,
  ProcessSchema,
  type ZodContact,
  type ZodFlow,
  type ZodProcess
} from './zod-factories';

// Utility functions
export { deepClone, merge, get, set, updatePath } from '../utils/object-utils';
