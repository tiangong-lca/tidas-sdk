/**
 * Typed accessor system for providing code hints and property access
 * to nested interface fields in TIDAS objects
 */

import { TypeAwareHelpers } from './type-aware-helpers';

/**
 * Simplified path type for better TypeScript performance
 */
export type NestedKeyOf<T> = {
  [K in keyof T & (string | number)]: T[K] extends object
    ? T[K] extends any[]
      ? `${K}` | `${K}.${number}`
      : `${K}` | `${K}.${NestedKeyOf<T[K]>}`
    : `${K}`;
}[keyof T & (string | number)];

/**
 * Get the value type at a specific path (simplified)
 */
export type PathValue<T, P extends string> = P extends keyof T
  ? T[P]
  : P extends `${infer K}.${infer Rest}`
  ? K extends keyof T
    ? PathValue<T[K], Rest>
    : unknown
  : unknown;

/**
 * Typed accessor interface that provides code hints for nested properties
 */
export interface TypedAccessor<T> {
  /**
   * Get a value at a typed path with IntelliSense support
   */
  get(path: string): any;
  
  /**
   * Set a value at a typed path with IntelliSense support
   */
  set(path: string, value: any): this;
  
  /**
   * Get the raw data object
   */
  readonly data: T;
  
  /**
   * Check if a path exists and has a value
   */
  has(path: string): boolean;
  
  /**
   * Delete a value at a path
   */
  delete(path: string): boolean;
  
  /**
   * Get all available paths (for discovery)
   */
  getAvailablePaths(): string[];
}

/**
 * Create a dynamic proxy object that provides typed property access
 */
export function createTypedAccessor<T extends Record<string, any>>(
  data: Partial<T>,
  onChange?: (data: T) => void
): TypedAccessor<T> & T {
  const internalData = { ...data } as T;
  
  // Helper function to get nested value
  const getByPath = (obj: any, path: string): any => {
    return path.split('.').reduce((current, key) => {
      return current && typeof current === 'object' ? current[key] : undefined;
    }, obj);
  };
  
  // Helper function to set nested value
  const setByPath = (obj: any, path: string, value: any): void => {
    const keys = path.split('.');
    const lastKey = keys.pop()!;
    const target = keys.reduce((current, key) => {
      if (!current[key] || typeof current[key] !== 'object') {
        current[key] = {};
      }
      return current[key];
    }, obj);
    target[lastKey] = value;
    
    // Notify change if callback provided
    if (onChange) {
      onChange(internalData);
    }
  };
  
  // Helper function to delete nested value
  const deleteByPath = (obj: any, path: string): boolean => {
    const keys = path.split('.');
    const lastKey = keys.pop()!;
    const target = keys.reduce((current, key) => {
      return current && typeof current === 'object' ? current[key] : undefined;
    }, obj);
    
    if (target && typeof target === 'object' && lastKey in target) {
      delete target[lastKey];
      if (onChange) {
        onChange(internalData);
      }
      return true;
    }
    return false;
  };
  
  // Helper function to extract all possible paths from an object
  const extractPaths = (obj: any, prefix = ''): string[] => {
    const paths: string[] = [];
    
    if (obj && typeof obj === 'object' && !Array.isArray(obj)) {
      for (const key in obj) {
        const currentPath = prefix ? `${prefix}.${key}` : key;
        paths.push(currentPath);
        
        if (obj[key] && typeof obj[key] === 'object' && !Array.isArray(obj[key])) {
          paths.push(...extractPaths(obj[key], currentPath));
        }
      }
    }
    
    return paths;
  };
  
  // Create the typed accessor object
  const accessor: TypedAccessor<T> = {
    get(path: string): any {
      return getByPath(internalData, path);
    },
    
    set(path: string, value: any): TypedAccessor<T> & T {
      setByPath(internalData, path, value);
      return proxy;
    },
    
    get data(): T {
      return internalData;
    },
    
    has(path: string): boolean {
      return getByPath(internalData, path) !== undefined;
    },
    
    delete(path: string): boolean {
      return deleteByPath(internalData, path);
    },
    
    getAvailablePaths(): string[] {
      return extractPaths(internalData);
    }
  };
  
  // Create a proxy that combines typed accessor with direct property access
  const proxy = new Proxy(accessor as TypedAccessor<T> & T, {
    get(_target: any, prop: string | symbol, receiver: any): any {
      // First check if it's a method on the accessor
      if (prop in accessor) {
        return Reflect.get(accessor, prop, receiver);
      }
      
      // Handle direct property access
      if (typeof prop === 'string') {
        // Check if property exists directly on the data
        if (prop in internalData) {
          const value = internalData[prop];
          // If the value is an object, create a nested proxy accessor
          if (value && typeof value === 'object' && !Array.isArray(value)) {
            return createDirectPropertyAccessor(value, prop, (newValue) => {
              (internalData as any)[prop] = newValue;
              if (onChange) {
                onChange(internalData);
              }
            });
          }
          return value;
        }
        
        // If property doesn't exist, create empty object to support chaining
        // This allows syntax like: obj.a.b.c = value where a, b don't exist yet
        const emptyObj = {};
        (internalData as any)[prop] = emptyObj;
        return createDirectPropertyAccessor(emptyObj, prop, (newValue) => {
          (internalData as any)[prop] = newValue;
          if (onChange) {
            onChange(internalData);
          }
        });
      }
      
      return undefined;
    },
    
    set(_target: any, prop: string | symbol, value: any): boolean {
      if (typeof prop === 'string') {
        (internalData as any)[prop] = value;
        if (onChange) {
          onChange(internalData);
        }
        return true;
      }
      return false;
    },
    
    has(_target: any, prop: string | symbol): boolean {
      if (prop in accessor) {
        return true;
      }
      if (typeof prop === 'string') {
        return prop in internalData;
      }
      return false;
    },
    
    deleteProperty(_target: any, prop: string | symbol): boolean {
      if (typeof prop === 'string') {
        const existed = prop in internalData;
        delete (internalData as any)[prop];
        if (existed && onChange) {
          onChange(internalData);
        }
        return existed;
      }
      return false;
    },
    
    ownKeys(_target: any): ArrayLike<string | symbol> {
      // Return both accessor methods and data properties
      const accessorKeys = Object.keys(accessor);
      const dataKeys = Object.keys(internalData);
      return [...accessorKeys, ...dataKeys];
    },
    
    getOwnPropertyDescriptor(_target: any, prop: string | symbol): PropertyDescriptor | undefined {
      if (prop in accessor) {
        return Reflect.getOwnPropertyDescriptor(accessor, prop);
      }
      
      if (typeof prop === 'string' && prop in internalData) {
        return {
          enumerable: true,
          configurable: true,
          writable: true,
          value: internalData[prop]
        };
      }
      
      return undefined;
    }
  });
  
  return proxy;
}

/**
 * Create a direct property accessor for seamless property access
 */
export function createDirectPropertyAccessor<T>(value: T, path: string, onChange: (newValue: T) => void): any {
  return new Proxy(value as any, {
    get(target: any, prop: string | symbol): any {
      if (typeof prop === 'string') {
        // If the property exists, return it (with nested proxy if needed)
        if (prop in target) {
          const nestedValue = target[prop];
          if (nestedValue && typeof nestedValue === 'object' && !Array.isArray(nestedValue)) {
            return createDirectPropertyAccessor(nestedValue, `${path}.${prop}`, (newValue) => {
              target[prop] = newValue;
              onChange(target);
            });
          }
          return nestedValue;
        }
        
        // If the property doesn't exist, create an empty object for chaining
        const emptyObj = {};
        target[prop] = emptyObj;
        return createDirectPropertyAccessor(emptyObj, `${path}.${prop}`, (newValue) => {
          target[prop] = newValue;
          onChange(target);
        });
      }
      return target[prop];
    },
    
    set(target: any, prop: string | symbol, value: any): boolean {
      if (typeof prop === 'string') {
        target[prop] = value;
        onChange(target);
        return true;
      }
      return false;
    },
    
    has(target: any, prop: string | symbol): boolean {
      if (typeof prop === 'string') {
        return prop in target;
      }
      return false;
    },
    
    deleteProperty(target: any, prop: string | symbol): boolean {
      if (typeof prop === 'string') {
        const existed = prop in target;
        delete target[prop];
        if (existed) {
          onChange(target);
        }
        return existed;
      }
      return false;
    },
    
    ownKeys(target: any): ArrayLike<string | symbol> {
      return Object.keys(target);
    },
    
    getOwnPropertyDescriptor(target: any, prop: string | symbol): PropertyDescriptor | undefined {
      if (typeof prop === 'string' && prop in target) {
        return {
          enumerable: true,
          configurable: true,
          writable: true,
          value: target[prop]
        };
      }
      return undefined;
    }
  });
}

/**
 * Multi-language text helper with typed access
 */
export interface MultiLangTextAccessor {
  /**
   * Get text in a specific language
   */
  getText(lang?: string): string;
  
  /**
   * Set text for a specific language
   */
  setText(text: string, lang?: string): this;
  
  /**
   * Get all available languages
   */
  getLanguages(): string[];
  
  /**
   * Get raw multi-language object
   */
  getRaw(): any;
  
  /**
   * Set from raw multi-language object
   */
  setRaw(value: any): this;
}

/**
 * Create a multi-language text accessor
 */
export function createMultiLangAccessor(
  getValue: () => any,
  setValue: (value: any) => void
): MultiLangTextAccessor {
  return {
    getText(lang = 'en'): string {
      const value = getValue();
      return TypeAwareHelpers.extractMultiLangText(value, lang);
    },
    
    setText(text: string, lang = 'en'): MultiLangTextAccessor {
      const currentValue = getValue();
      const newValue = TypeAwareHelpers.createOrUpdateMultiLangText(currentValue, text, lang);
      setValue(newValue);
      return this;
    },
    
    getLanguages(): string[] {
      const value = getValue();
      if (!value) return [];
      
      if (Array.isArray(value)) {
        return value.map(item => item['@xml:lang']).filter(Boolean);
      } else if (value['@xml:lang']) {
        return [value['@xml:lang']];
      }
      
      return [];
    },
    
    getRaw(): any {
      return getValue();
    },
    
    setRaw(value: any): MultiLangTextAccessor {
      setValue(value);
      return this;
    }
  };
}

/**
 * Enhanced typed accessor that includes special handling for common TIDAS field types
 */
export interface EnhancedTypedAccessor<T> extends TypedAccessor<T> {
  /**
   * Get a multi-language text accessor for a path
   */
  getMultiLang(path: string): MultiLangTextAccessor;
  
  /**
   * Get UUID at a path
   */
  getUUID(path: string): string | undefined;
  
  /**
   * Set UUID at a path
   */
  setUUID(path: string, uuid?: string): this;
  
  /**
   * Get timestamp at a path
   */
  getTimestamp(path: string): string | undefined;
  
  /**
   * Set current timestamp at a path
   */
  setCurrentTimestamp(path: string): this;
  
  /**
   * Clone the entire object
   */
  clone(): EnhancedTypedAccessor<T> & T;
  
  /**
   * Create a direct property accessor for seamless property access
   */
  createDirectAccessor(): any;
}

/**
 * Create an enhanced typed accessor with special TIDAS field handling
 */
export function createEnhancedTypedAccessor<T extends Record<string, any>>(
  data: Partial<T>,
  onChange?: (data: T) => void
): EnhancedTypedAccessor<T> & T {
  const baseAccessor = createTypedAccessor(data, onChange);
  
  const enhanced: EnhancedTypedAccessor<T> = {
    ...baseAccessor,
    
    getMultiLang(path: string): MultiLangTextAccessor {
      return createMultiLangAccessor(
        () => this.get(path),
        (value) => this.set(path, value)
      );
    },
    
    getUUID(path: string): string | undefined {
      return this.get(path) as string | undefined;
    },
    
    setUUID(path: string, uuid?: string): EnhancedTypedAccessor<T> & T {
      const uuidValue = uuid || TypeAwareHelpers.generateUUID();
      this.set(path, uuidValue);
      return proxy;
    },
    
    getTimestamp(path: string): string | undefined {
      return this.get(path) as string | undefined;
    },
    
    setCurrentTimestamp(path: string): EnhancedTypedAccessor<T> & T {
      const timestamp = TypeAwareHelpers.getCurrentTimestamp();
      this.set(path, timestamp);
      return proxy;
    },
    
    clone(): EnhancedTypedAccessor<T> & T {
      const clonedData = TypeAwareHelpers.deepClone(this.data);
      return createEnhancedTypedAccessor(clonedData, onChange);
    },
    
    createDirectAccessor(): any {
      return createDirectPropertyAccessor(this.data, '', (newValue: T) => {
        Object.assign(this.data, newValue);
        if (onChange) {
          onChange(this.data);
        }
      });
    }
  };
  
  // Create enhanced proxy
  const proxy = new Proxy(enhanced as EnhancedTypedAccessor<T> & T, {
    get(_target: any, prop: string | symbol, receiver: any): any {
      // First check enhanced methods
      if (prop in enhanced) {
        return Reflect.get(enhanced, prop, receiver);
      }
      
      // Then delegate to base accessor
      return Reflect.get(baseAccessor, prop, receiver);
    },
    
    set(_target: any, prop: string | symbol, value: any): boolean {
      return Reflect.set(baseAccessor, prop, value);
    },
    
    has(_target: any, prop: string | symbol): boolean {
      return Reflect.has(enhanced, prop) || Reflect.has(baseAccessor, prop);
    },
    
    deleteProperty(_target: any, prop: string | symbol): boolean {
      return Reflect.deleteProperty(baseAccessor, prop);
    },
    
    ownKeys(_target: any): ArrayLike<string | symbol> {
      const enhancedKeys = Object.keys(enhanced);
      const baseKeys = Reflect.ownKeys(baseAccessor);
      return [...enhancedKeys, ...baseKeys];
    },
    
    getOwnPropertyDescriptor(_target: any, prop: string | symbol): PropertyDescriptor | undefined {
      return Reflect.getOwnPropertyDescriptor(enhanced, prop) || 
             Reflect.getOwnPropertyDescriptor(baseAccessor, prop);
    }
  });
  
  return proxy;
}

/**
 * Type-safe factory functions for common TIDAS objects with enhanced IntelliSense
 */
import type { Contact, Process, Flow } from '../types';

/**
 * Contact accessor with type-specific convenience methods
 */
export interface ContactAccessor extends EnhancedTypedAccessor<Contact> {
  // Convenience methods for common Contact fields
  getName(lang?: string): string;
  setName(text: string, lang?: string): this;
  getShortName(lang?: string): string;
  setShortName(text: string, lang?: string): this;
  getEmail(): string | undefined;
  setEmail(email: string): this;
  getPhone(): string | undefined;
  setPhone(phone: string): this;
  getWebsite(): string | undefined;
  setWebsite(url: string): this;
}

/**
 * Process accessor with type-specific convenience methods
 */
export interface ProcessAccessor extends EnhancedTypedAccessor<Process> {
  // Convenience methods for common Process fields
  getBaseName(lang?: string): string;
  setBaseName(text: string, lang?: string): this;
  getLocation(): string | undefined;
  setLocation(location: string): this;
  getReferenceYear(): string | undefined;
  setReferenceYear(year: string): this;
}

/**
 * Flow accessor with type-specific convenience methods
 */
export interface FlowAccessor extends EnhancedTypedAccessor<Flow> {
  // Convenience methods for common Flow fields
  getBaseName(lang?: string): string;
  setBaseName(text: string, lang?: string): this;
  getCASNumber(): string | undefined;
  setCASNumber(cas: string): this;
  getTypeOfDataSet(): string | undefined;
  setTypeOfDataSet(type: string): this;
}

export function createTypedContact(data?: Partial<Contact>): ContactAccessor & Contact {
  const base = createEnhancedTypedAccessor<Contact>(data || {});
  const self = Object.assign(base, {
    getName: (lang = 'en') => base.getMultiLang('contactDataSet.contactInformation.dataSetInformation.common:name').getText(lang),
    setName: (text: string, lang = 'en') => { base.getMultiLang('contactDataSet.contactInformation.dataSetInformation.common:name').setText(text, lang); return self; },
    getShortName: (lang = 'en') => base.getMultiLang('contactDataSet.contactInformation.dataSetInformation.common:shortName').getText(lang),
    setShortName: (text: string, lang = 'en') => { base.getMultiLang('contactDataSet.contactInformation.dataSetInformation.common:shortName').setText(text, lang); return self; },
    getEmail: () => base.get('contactDataSet.contactInformation.dataSetInformation.email'),
    setEmail: (email: string) => { base.set('contactDataSet.contactInformation.dataSetInformation.email', email); return self; },
    getPhone: () => base.get('contactDataSet.contactInformation.dataSetInformation.telephone'),
    setPhone: (phone: string) => { base.set('contactDataSet.contactInformation.dataSetInformation.telephone', phone); return self; },
    getWebsite: () => base.get('contactDataSet.contactInformation.dataSetInformation.WWWAddress'),
    setWebsite: (url: string) => { base.set('contactDataSet.contactInformation.dataSetInformation.WWWAddress', url); return self; }
  });
  return self as ContactAccessor & Contact;
}

export function createTypedProcess(data?: Partial<Process>): ProcessAccessor & Process {
  const base = createEnhancedTypedAccessor<Process>(data || {});
  const self = Object.assign(base, {
    getBaseName: (lang = 'en') => base.getMultiLang('processDataSet.processInformation.dataSetInformation.name.baseName').getText(lang),
    setBaseName: (text: string, lang = 'en') => { base.getMultiLang('processDataSet.processInformation.dataSetInformation.name.baseName').setText(text, lang); return self; },
    getLocation: () => base.get('processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction.@location'),
    setLocation: (location: string) => { base.set('processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction.@location', location); return self; },
    getReferenceYear: () => base.get('processDataSet.processInformation.time.referenceYear'),
    setReferenceYear: (year: string) => { base.set('processDataSet.processInformation.time.referenceYear', year); return self; }
  });
  return self as ProcessAccessor & Process;
}

export function createTypedFlow(data?: Partial<Flow>): FlowAccessor & Flow {
  const base = createEnhancedTypedAccessor<Flow>(data || {});
  const self = Object.assign(base, {
    getBaseName: (lang = 'en') => base.getMultiLang('flowDataSet.flowInformation.dataSetInformation.name.baseName').getText(lang),
    setBaseName: (text: string, lang = 'en') => { base.getMultiLang('flowDataSet.flowInformation.dataSetInformation.name.baseName').setText(text, lang); return self; },
    getCASNumber: () => base.get('flowDataSet.flowInformation.dataSetInformation.CASNumber'),
    setCASNumber: (cas: string) => { base.set('flowDataSet.flowInformation.dataSetInformation.CASNumber', cas); return self; },
    getTypeOfDataSet: () => base.get('flowDataSet.flowInformation.dataSetInformation.typeOfDataSet'),
    setTypeOfDataSet: (type: string) => { base.set('flowDataSet.flowInformation.dataSetInformation.typeOfDataSet', type); return self; }
  });
  return self as FlowAccessor & Flow;
}