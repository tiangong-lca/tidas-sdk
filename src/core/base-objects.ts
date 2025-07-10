import { TidasBase, type ValidationOptions } from './base';
import type { 
  Contact, 
  Process, 
  Flow, 
  Source, 
  FlowProperty, 
  UnitGroup, 
  LCIAMethod, 
  LifeCycleModel 
} from '../types';
import { 
  ContactSchema, 
  ProcessSchema, 
  FlowSchema, 
  SourceSchema, 
  FlowPropertySchema, 
  UnitGroupSchema, 
  LCIAMethodSchema, 
  LifeCycleModelSchema 
} from '../schemas';
import { z } from 'zod';

/**
 * Base class for all TIDAS objects with auto-detection capabilities
 */
abstract class TypedTidasBase<T> extends TidasBase<T> {
  protected abstract getRootKey(): string;
  
  constructor(data?: Partial<T>, options?: ValidationOptions) {
    const fullData = data || {} as T;
    super(fullData as T, options);
    
    // Perform initial validation if enabled
    this.performValidationIfEnabled();
  }
  
  /**
   * Create a default/empty object with minimal structure
   */
  static createDefault<U extends TypedTidasBase<any>>(
    this: new (data?: any, options?: ValidationOptions) => U,
    options?: ValidationOptions
  ): U {
    return new this({}, options);
  }
  
  /**
   * Create object with validation enabled
   */
  static createWithValidation<U extends TypedTidasBase<any>>(
    this: new (data?: any, options?: ValidationOptions) => U,
    data?: any
  ): U {
    return new this(data, { enableValidation: true, throwOnValidationError: true });
  }
  
  /**
   * Create object with auto-generated UUID at detected path
   */
  createWithUUID(): this {
    const uuidPath = this.getUUIDPath();
    if (uuidPath) {
      const uuid = this.generateUUID();
      this.set(uuidPath, uuid);
    }
    return this;
  }
  
  /**
   * Create object with auto-detected default structure
   */
  createWithAutoStructure(): this {
    // Find UUID path and set UUID if found
    const uuidPath = this.getUUIDPath();
    if (uuidPath) {
      this.set(uuidPath, this.generateUUID());
    }
    
    // Find multi-language paths and set empty multi-lang structure
    const multiLangPaths = this.findMultiLangPaths();
    for (const path of multiLangPaths) {
      this.set(path, {
        '@xml:lang': 'en',
        '#text': ''
      });
    }
    
    return this;
  }
  
  /**
   * Auto-detect UUID path
   */
  protected getUUIDPath(): string | null {
    return this.findPathsWithKey('common:UUID')[0] || null;
  }
  
  /**
   * Find all paths that contain a specific key
   */
  findPathsWithKey(targetKey: string): string[] {
    const paths: string[] = [];
    
    const search = (obj: any, currentPath: string = '') => {
      if (obj && typeof obj === 'object') {
        for (const [key, value] of Object.entries(obj)) {
          const fullPath = currentPath ? `${currentPath}.${key}` : key;
          
          if (key === targetKey || key.endsWith(targetKey)) {
            paths.push(fullPath);
          }
          
          if (value && typeof value === 'object') {
            search(value, fullPath);
          }
        }
      }
    };
    
    search(this._data);
    return paths;
  }
  
  /**
   * Get all available property paths
   */
  getAvailablePaths(): string[] {
    const paths: string[] = [];
    
    const traverse = (obj: any, currentPath: string = '') => {
      if (obj && typeof obj === 'object' && !Array.isArray(obj)) {
        for (const [key, value] of Object.entries(obj)) {
          const fullPath = currentPath ? `${currentPath}.${key}` : key;
          paths.push(fullPath);
          
          if (value && typeof value === 'object') {
            traverse(value, fullPath);
          }
        }
      }
    };
    
    traverse(this._data);
    return paths;
  }
  
  /**
   * Get the type name of this object
   */
  getTypeName(): string {
    return this.getRootKey().replace('DataSet', '').toLowerCase();
  }
  
  /**w
   * Get schema information
   */
  getSchemaInfo(): {
    rootKey: string;
    typeName: string;
    uuidPath: string | null;
    availablePaths: string[];
    multiLangPaths: string[];
  } {
    return {
      rootKey: this.getRootKey(),
      typeName: this.getTypeName(),
      uuidPath: this.getUUIDPath(),
      availablePaths: this.getAvailablePaths(),
      multiLangPaths: this.findMultiLangPaths()
    };
  }
  
  /**
   * Find paths that contain multi-language text structures
   */
  private findMultiLangPaths(): string[] {
    const paths: string[] = [];
    
    const search = (obj: any, currentPath: string = '') => {
      if (obj && typeof obj === 'object') {
        // Check if this is a multi-language structure
        if (obj['@xml:lang'] && obj['#text']) {
          paths.push(currentPath);
        } else if (Array.isArray(obj) && obj.length > 0 && obj[0]['@xml:lang']) {
          paths.push(currentPath);
        } else {
          // Continue searching
          for (const [key, value] of Object.entries(obj)) {
            const fullPath = currentPath ? `${currentPath}.${key}` : key;
            search(value, fullPath);
          }
        }
      }
    };
    
    search(this._data);
    return paths;
  }
}

/**
 * Contact object
 */
export class ContactBaseObject extends TypedTidasBase<Contact> {
  constructor(data?: Partial<Contact>, options?: ValidationOptions) {
    const fullData = data || { contactDataSet: {} };
    super(fullData as Contact, options);
  }
  
  protected getRootKey(): string {
    return 'contactDataSet';
  }
  
  protected getSchema(): z.ZodSchema<Contact> {
    return ContactSchema;
  }
}

/**
 * Process object
 */
export class ProcessBaseObject extends TypedTidasBase<Process> {
  constructor(data?: Partial<Process>, options?: ValidationOptions) {
    const fullData = data || { processDataSet: {} };
    super(fullData as Process, options);
  }
  
  protected getRootKey(): string {
    return 'processDataSet';
  }
  
  protected getSchema(): z.ZodSchema<Process> {
    return ProcessSchema as any;
  }
}

/**
 * Flow object
 */
export class FlowBaseObject extends TypedTidasBase<Flow> {
  constructor(data?: Partial<Flow>, options?: ValidationOptions) {
    const fullData = data || { flowDataSet: {} };
    super(fullData as Flow, options);
  }
  
  protected getRootKey(): string {
    return 'flowDataSet';
  }
  
  protected getSchema(): z.ZodSchema<Flow> {
    return FlowSchema as any;
  }
}

/**
 * Source object
 */
export class SourceBaseObject extends TypedTidasBase<Source> {
  constructor(data?: Partial<Source>, options?: ValidationOptions) {
    const fullData = data || { sourceDataSet: {} };
    super(fullData as Source, options);
  }
  
  protected getRootKey(): string {
    return 'sourceDataSet';
  }
  
  protected getSchema(): z.ZodSchema<Source> {
    return SourceSchema;
  }
}

/**
 * Flow Property object
 */
export class FlowPropertyBaseObject extends TypedTidasBase<FlowProperty> {
  constructor(data?: Partial<FlowProperty>, options?: ValidationOptions) {
    const fullData = data || { flowPropertyDataSet: {} };
    super(fullData as FlowProperty, options);
  }
  
  protected getRootKey(): string {
    return 'flowPropertyDataSet';
  }
  
  protected getSchema(): z.ZodSchema<FlowProperty> {
    return FlowPropertySchema;
  }
}

/**
 * Unit Group object
 */
export class UnitGroupBaseObject extends TypedTidasBase<UnitGroup> {
  constructor(data?: Partial<UnitGroup>, options?: ValidationOptions) {
    const fullData = data || { unitGroupDataSet: {} };
    super(fullData as UnitGroup, options);
  }
  
  protected getRootKey(): string {
    return 'unitGroupDataSet';
  }
  
  protected getSchema(): z.ZodSchema<UnitGroup> {
    return UnitGroupSchema;
  }
}

/**
 * LCIA Method object
 */
export class LCIAMethodBaseObject extends TypedTidasBase<LCIAMethod> {
  constructor(data?: Partial<LCIAMethod>, options?: ValidationOptions) {
    const fullData = data || { LCIAMethodDataSet: {} };
    super(fullData as LCIAMethod, options);
  }
  
  protected getRootKey(): string {
    return 'LCIAMethodDataSet';
  }
  
  protected getSchema(): z.ZodSchema<LCIAMethod> {
    return LCIAMethodSchema;
  }
}

/**
 * Life Cycle Model object
 */
export class LifeCycleModelBaseObject extends TypedTidasBase<LifeCycleModel> {
  constructor(data?: Partial<LifeCycleModel>, options?: ValidationOptions) {
    const fullData = data || { lifeCycleModelDataSet: {} };
    super(fullData as LifeCycleModel, options);
  }
  
  protected getRootKey(): string {
    return 'lifeCycleModelDataSet';
  }
  
  protected getSchema(): z.ZodSchema<LifeCycleModel> {
    return LifeCycleModelSchema;
  }
}