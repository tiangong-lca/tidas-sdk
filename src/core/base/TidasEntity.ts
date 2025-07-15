import { z } from 'zod';

/**
 * Validation result type
 */
export type ValidationResult<T> = {
  success: true;
  data: T;
} | {
  success: false;
  error: z.ZodError;
};

/**
 * Abstract base class for all TIDAS entities
 * Provides basic validation and data container functionality without property mapping
 */
export abstract class TidasEntity<T = any> {
  protected _schema: z.ZodSchema<T>;
  protected _data: Partial<T> = {};
  protected _proxy: any;

  constructor(schema: z.ZodSchema<T>, initialData?: Partial<T>) {
    this._schema = schema;
    this._data = initialData || {};
    this._proxy = this.createBasicProxy();
    this.initializeDefaults();
    return this._proxy;
  }

  /**
   * Abstract method to be implemented by subclasses
   * Initializes default values and ensures required structure
   */
  protected abstract initializeDefaults(): void;

  /**
   * Creates a basic proxy that provides direct data access
   */
  private createBasicProxy() {
    return new Proxy(this, {
      get(target, prop: string | symbol) {
        if (typeof prop === 'symbol') {
          return (target as any)[prop];
        }

        // 1. Method calls - return bound methods
        if (typeof (target as any)[prop] === 'function') {
          return (target as any)[prop].bind(target);
        }

        // 2. Direct data access
        if (prop in target._data) {
          return (target._data as any)[prop];
        }

        // 3. Dynamic path access (supports dot notation)
        if (prop.includes('.') || prop.includes('[')) {
          return target.getNestedValue(prop);
        }

        // 4. Other properties
        return (target as any)[prop];
      },

      set(target, prop: string | symbol, value) {
        if (typeof prop === 'symbol') {
          (target as any)[prop] = value;
          return true;
        }

        // 1. Dynamic path setting (supports dot notation)
        if (prop.includes('.') || prop.includes('[')) {
          target.setNestedValue(prop, value);
          return true;
        }

        // 2. Top-level property setting
        (target._data as any)[prop] = value;
        return true;
      },

      has(target, prop: string) {
        return prop in target._data || prop in target;
      },

      ownKeys(target) {
        return [
          ...Object.keys(target._data),
          ...Object.getOwnPropertyNames(target)
        ];
      }
    });
  }

  /**
   * Get nested value using dot notation path
   */
  protected getNestedValue(path: string): any {
    return this.resolvePath(this._data, path);
  }

  /**
   * Set nested value using dot notation path
   */
  protected setNestedValue(path: string, value: any): void {
    this.setPath(this._data, path, value);
  }

  /**
   * Resolve a nested path in an object
   */
  private resolvePath(obj: any, path: string): any {
    return path.split('.').reduce((current, key) => {
      if (key.includes('[') && key.includes(']')) {
        const [arrayKey, indexStr] = key.split('[');
        const index = parseInt(indexStr.replace(']', ''));
        return current?.[arrayKey]?.[index];
      }
      return current?.[key];
    }, obj);
  }

  /**
   * Set a nested path in an object
   */
  private setPath(obj: any, path: string, value: any): void {
    const keys = path.split('.');
    const lastKey = keys.pop()!;
    
    const target = keys.reduce((current, key) => {
      if (key.includes('[') && key.includes(']')) {
        const [arrayKey, indexStr] = key.split('[');
        const index = parseInt(indexStr.replace(']', ''));
        if (!current[arrayKey]) current[arrayKey] = [];
        if (!current[arrayKey][index]) current[arrayKey][index] = {};
        return current[arrayKey][index];
      }
      if (!current[key]) current[key] = {};
      return current[key];
    }, obj);
    
    if (lastKey.includes('[') && lastKey.includes(']')) {
      const [arrayKey, indexStr] = lastKey.split('[');
      const index = parseInt(indexStr.replace(']', ''));
      if (!target[arrayKey]) target[arrayKey] = [];
      target[arrayKey][index] = value;
    } else {
      target[lastKey] = value;
    }
  }

  /**
   * Ensure nested structure exists
   */
  protected ensureNestedStructure(paths: string[]): void {
    paths.forEach(path => {
      if (!this.getNestedValue(path)) {
        this.setNestedValue(path, {});
      }
    });
  }

  /**
   * Validate the current data against the schema
   */
  validate(): ValidationResult<T> {
    const result = this._schema.safeParse(this._data);
    if (result.success) {
      return { success: true, data: result.data };
    } else {
      return { success: false, error: result.error };
    }
  }

  /**
   * Convert to JSON (complete TIDAS structure)
   * Ensures clean JSON output without non-serializable objects
   */
  toJSON(): T {
    return this.cleanForJSON(this._data) as T;
  }

  /**
   * Convert to JSON string
   * Returns a properly formatted JSON string
   */
  toJSONString(indent?: number): string {
    const cleanData = this.cleanForJSON(this._data);
    return JSON.stringify(cleanData, null, indent);
  }

  /**
   * Clean data for JSON serialization
   * Removes undefined values, functions, and ensures proper structure
   */
  private cleanForJSON(obj: any): any {
    if (obj === null || obj === undefined) {
      return null;
    }
    
    if (typeof obj === 'function') {
      return undefined;
    }
    
    if (Array.isArray(obj)) {
      return obj.map(item => this.cleanForJSON(item)).filter(item => item !== undefined);
    }
    
    if (typeof obj === 'object') {
      const cleaned: any = {};
      for (const [key, value] of Object.entries(obj)) {
        const cleanedValue = this.cleanForJSON(value);
        if (cleanedValue !== undefined) {
          cleaned[key] = cleanedValue;
        }
      }
      return cleaned;
    }
    
    // Primitive values
    return obj;
  }

  /**
   * Get raw data access
   */
  get rawData(): Partial<T> {
    return this._data;
  }

  /**
   * Clone the entity
   */
  clone(): this {
    const Constructor = this.constructor as new (...args: any[]) => this;
    return new Constructor(this._schema, structuredClone(this._data));
  }
}