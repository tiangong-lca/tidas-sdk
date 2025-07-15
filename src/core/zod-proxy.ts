/**
 * Zod Proxy implementation for true property access with Schema validation
 * Based on the advanced Zod Proxy approach from docs/zod-proxy.md
 */

import { z } from 'zod';

/**
 * Path information for complex path parsing
 */
export interface PathInfo {
  segments: string[];
  arrayIndices: number[];
  fullPath: string;
  isArrayAccess: boolean;
}

/**
 * Access log entry for debugging and tracking
 */
export interface AccessLogEntry {
  type: 'get' | 'set' | 'push' | 'delete';
  path: string;
  value?: any;
  timestamp: number;
}

/**
 * Configuration options for ZodProxy
 */
export interface ZodProxyOptions {
  enableLogging?: boolean;
  throwOnValidationError?: boolean;
  autoCreateArrays?: boolean;
}

/**
 * Result of ZodProxy validation
 */
export interface ZodProxyValidationResult<T> {
  success: boolean;
  data?: T;
  error?: z.ZodError;
}

/**
 * Parse array path like "posts[0].comments[1].text"
 */
function parseArrayPath(path: string): PathInfo {
  const segments: string[] = [];
  const arrayIndices: number[] = [];
  let isArrayAccess = false;

  // Parse path, e.g., "posts[0].comments[1].replies[2].text"
  const parts = path.split(/[.[\]]/).filter((part) => part !== '');

  for (let i = 0; i < parts.length; i++) {
    const part = parts[i];

    if (/^\d+$/.test(part)) {
      // This is an array index
      arrayIndices.push(parseInt(part));
      isArrayAccess = true;
    } else {
      // This is a property name
      segments.push(part);
    }
  }

  return {
    segments,
    arrayIndices,
    fullPath: path,
    isArrayAccess,
  };
}

/**
 * Get schema at a specific path within the main schema
 */
function getSchemaAtPath(
  currentSchema: z.ZodSchema,
  pathSegments: string[]
): z.ZodSchema | null {
  let schema = currentSchema;

  for (const segment of pathSegments) {
    if (schema instanceof z.ZodObject) {
      const shape = schema.shape;
      if (shape[segment]) {
        schema = shape[segment];
      } else {
        return null;
      }
    } else if (schema instanceof z.ZodArray) {
      // If it's an array, get element type
      schema = schema.element as unknown as z.ZodSchema;
      // Continue processing remaining path after array access
      continue;
    } else {
      return null;
    }
  }

  return schema;
}

/**
 * Set nested property in an object using path segments
 */
function setNestedProperty(obj: any, path: string[], value: any): void {
  let current = obj;

  for (let i = 0; i < path.length - 1; i++) {
    const key = path[i];
    if (!(key in current)) {
      current[key] = {};
    }
    current = current[key];
  }

  current[path[path.length - 1]] = value;
}

/**
 * Set nested array property using complex path like "posts[0].comments[1].text"
 */
function setNestedArrayProperty(obj: any, fullPath: string, value: any): void {
  // Parse complex path like "posts[0].comments[1].text"
  const parts = fullPath.split(/[.[\]]/).filter((part) => part !== '');
  let current = obj;

  for (let i = 0; i < parts.length - 1; i++) {
    const part = parts[i];

    if (/^\d+$/.test(part)) {
      // Array index
      const index = parseInt(part);
      if (!Array.isArray(current)) {
        current = [];
      }
      if (!current[index]) {
        current[index] = {};
      }
      current = current[index];
    } else {
      // Property name
      if (!(part in current)) {
        // Check if next part is array index
        const nextPart = parts[i + 1];
        if (nextPart && /^\d+$/.test(nextPart)) {
          current[part] = [];
        } else {
          current[part] = {};
        }
      }
      current = current[part];
    }
  }

  const lastPart = parts[parts.length - 1];
  if (/^\d+$/.test(lastPart)) {
    const index = parseInt(lastPart);
    if (!Array.isArray(current)) {
      current = [];
    }
    current[index] = value;
  } else {
    current[lastPart] = value;
  }
}

/**
 * Main ZodProxy class for creating proxies with Schema validation
 */
export class ZodProxy<T extends z.ZodSchema> {
  private schema: T;
  private options: ZodProxyOptions;
  private accessLog: AccessLogEntry[] = [];
  private values = new Map<string, any>();
  private arrayLengths = new Map<string, number>();

  constructor(schema: T, options: ZodProxyOptions = {}) {
    this.schema = schema;
    this.options = {
      enableLogging: true,
      throwOnValidationError: false,
      autoCreateArrays: true,
      ...options,
    };
  }

  /**
   * Log access for debugging
   */
  private log(
    type: 'get' | 'set' | 'push' | 'delete',
    path: string,
    value?: any
  ): void {
    if (this.options.enableLogging) {
      this.accessLog.push({
        type,
        path,
        value,
        timestamp: Date.now(),
      });
    }
  }

  /**
   * Validate value against schema at specific path
   */
  private validateValue(path: string, value: any): boolean {
    const pathInfo = parseArrayPath(path);

    try {
      // Get schema for this path
      const targetSchema = getSchemaAtPath(this.schema, pathInfo.segments);

      if (targetSchema) {
        targetSchema.parse(value);
        return true;
      }

      return false;
    } catch (error) {
      if (this.options.throwOnValidationError) {
        throw error;
      }
      console.error(`Validation failed for ${path}:`, error);
      return false;
    }
  }

  /**
   * Ensure array path has correct length
   */
  private ensureArrayPath(path: string, index: number): void {
    const arrayPath = path;
    const currentLength = this.arrayLengths.get(arrayPath) || 0;

    if (index >= currentLength) {
      this.arrayLengths.set(arrayPath, index + 1);
    }
  }

  /**
   * Create the main proxy object
   */
  createProxy(currentPath: string[] = []): any {
    return new Proxy(
      {},
      {
        get: (_target, prop: string | symbol) => {
          if (typeof prop === 'symbol') {
            return undefined;
          }

          const newPath = [...currentPath, prop];
          const pathStr = newPath.join('.');

          // Handle special array properties
          if (prop === 'length' && currentPath.length > 0) {
            const arrayPath = currentPath.join('.');
            const length = this.arrayLengths.get(arrayPath) || 0;
            this.log('get', `${arrayPath}.length`, length);
            return length;
          }

          if (prop === 'push') {
            return (...items: any[]) => {
              const arrayPath = currentPath.join('.');
              const currentLength = this.arrayLengths.get(arrayPath) || 0;

              items.forEach((item, index) => {
                const itemPath = `${arrayPath}[${currentLength + index}]`;
                if (this.validateValue(itemPath, item)) {
                  this.values.set(itemPath, item);
                  this.log('push', itemPath, item);
                }
              });

              const newLength = currentLength + items.length;
              this.arrayLengths.set(arrayPath, newLength);
              return newLength;
            };
          }

          if (prop === 'pop') {
            return () => {
              const arrayPath = currentPath.join('.');
              const currentLength = this.arrayLengths.get(arrayPath) || 0;

              if (currentLength > 0) {
                const lastIndex = currentLength - 1;
                const itemPath = `${arrayPath}[${lastIndex}]`;
                const value = this.values.get(itemPath);
                this.values.delete(itemPath);
                this.arrayLengths.set(arrayPath, lastIndex);
                this.log('delete', itemPath, value);
                return value;
              }
              return undefined;
            };
          }

          // Handle array index access
          if (/^\d+$/.test(prop)) {
            const index = parseInt(prop);
            const arrayPath = currentPath.join('.');
            const itemPath = `${arrayPath}[${index}]`;

            this.ensureArrayPath(arrayPath, index);
            this.log('get', itemPath);

            if (this.values.has(itemPath)) {
              const value = this.values.get(itemPath);
              // If value is object, return proxy
              if (typeof value === 'object' && value !== null) {
                return this.createProxy([...currentPath, prop]);
              }
              return value;
            }

            return this.createProxy([...currentPath, prop]);
          }

          this.log('get', pathStr);

          if (this.values.has(pathStr)) {
            return this.values.get(pathStr);
          }

          return this.createProxy(newPath);
        },

        set: (_target, prop: string | symbol, value: any) => {
          if (typeof prop !== 'string') {
            return false;
          }

          const newPath = [...currentPath, prop];
          const pathStr = newPath.join('.');

          // Handle array index assignment
          if (/^\d+$/.test(prop)) {
            const index = parseInt(prop);
            const arrayPath = currentPath.join('.');
            const itemPath = `${arrayPath}[${index}]`;

            if (this.validateValue(itemPath, value)) {
              this.values.set(itemPath, value);
              this.ensureArrayPath(arrayPath, index);
              this.log('set', itemPath, value);
              return true;
            }
            return false;
          }

          if (this.validateValue(pathStr, value)) {
            this.values.set(pathStr, value);
            this.log('set', pathStr, value);
            return true;
          }

          return false;
        },

        has: (_target, prop) => {
          const newPath = [...currentPath, prop as string];
          const pathStr = newPath.join('.');
          return this.values.has(pathStr);
        },

        deleteProperty: (_target, prop) => {
          const newPath = [...currentPath, prop as string];
          const pathStr = newPath.join('.');
          const existed = this.values.has(pathStr);
          this.values.delete(pathStr);

          if (existed) {
            this.log('delete', pathStr);
          }

          return true;
        },
      }
    );
  }

  /**
   * Build final object from all set values
   */
  buildObject(): any {
    const result: any = {};

    // Process all values
    for (const [path, value] of this.values.entries()) {
      const pathInfo = parseArrayPath(path);

      if (!pathInfo.isArrayAccess) {
        // Simple property path
        setNestedProperty(result, pathInfo.segments, value);
      } else {
        // Array path
        setNestedArrayProperty(result, path, value);
      }
    }

    return result;
  }

  /**
   * Validate the complete object against schema
   */
  validate(): ZodProxyValidationResult<z.infer<T>> {
    try {
      const obj = this.buildObject();
      const result = this.schema.parse(obj);
      return { success: true, data: result };
    } catch (error) {
      return { success: false, error: error as z.ZodError };
    }
  }

  /**
   * Get access log for debugging
   */
  getAccessLog(): AccessLogEntry[] {
    return [...this.accessLog];
  }

  /**
   * Get all stored values
   */
  getValues(): Record<string, any> {
    return Object.fromEntries(this.values.entries());
  }

  /**
   * Get array lengths
   */
  getArrayLengths(): Record<string, number> {
    return Object.fromEntries(this.arrayLengths.entries());
  }

  /**
   * Debug information
   */
  debug(): {
    values: Record<string, any>;
    arrayLengths: Record<string, number>;
    accessLog: AccessLogEntry[];
    builtObject: any;
  } {
    return {
      values: this.getValues(),
      arrayLengths: this.getArrayLengths(),
      accessLog: this.accessLog.slice(-10), // Last 10 entries
      builtObject: this.buildObject(),
    };
  }
}

/**
 * Factory function to create a ZodProxy with convenient API
 */
export function createZodProxy<T extends z.ZodSchema>(
  schema: T,
  options: ZodProxyOptions = {}
): {
  proxy: z.infer<T>;
  getAccessLog: () => AccessLogEntry[];
  getValues: () => Record<string, any>;
  getArrayLengths: () => Record<string, number>;
  buildObject: () => any;
  validate: () => ZodProxyValidationResult<z.infer<T>>;
  debug: () => any;
} {
  const zodProxy = new ZodProxy(schema, options);
  const proxy = zodProxy.createProxy() as z.infer<T>;

  return {
    proxy,
    getAccessLog: () => zodProxy.getAccessLog(),
    getValues: () => zodProxy.getValues(),
    getArrayLengths: () => zodProxy.getArrayLengths(),
    buildObject: () => zodProxy.buildObject(),
    validate: () => zodProxy.validate(),
    debug: () => zodProxy.debug(),
  };
}