import { TidasBase, type ValidationOptions } from './base';
import type { 
  Contacts, 
  Processes, 
  Flows, 
  Sources, 
  Flowproperties, 
  Unitgroups, 
  Lciamethods, 
  Lifecyclemodels 
} from '../types';
import { 
  ContactsSchema, 
  ProcessesSchema, 
  FlowsSchema, 
  SourcesSchema, 
  FlowpropertiesSchema, 
  UnitgroupsSchema, 
  LciamethodsSchema, 
  LifecyclemodelsSchema 
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
export class ContactBaseObject extends TypedTidasBase<Contacts> {
  constructor(data?: Partial<Contacts>, options?: ValidationOptions) {
    const fullData = data || { contactDataSet: {} };
    super(fullData as Contacts, options);
  }
  
  protected getRootKey(): string {
    return 'contactDataSet';
  }
  
  protected getSchema(): z.ZodSchema<Contacts> {
    return ContactsSchema;
  }
}

/**
 * Process object
 */
export class ProcessBaseObject extends TypedTidasBase<Processes> {
  constructor(data?: Partial<Processes>, options?: ValidationOptions) {
    const fullData = data || { processDataSet: {} };
    super(fullData as Processes, options);
  }
  
  protected getRootKey(): string {
    return 'processDataSet';
  }
  
  protected getSchema(): z.ZodSchema<Processes> {
    return ProcessesSchema;
  }
}

/**
 * Flow object
 */
export class FlowBaseObject extends TypedTidasBase<Flows> {
  constructor(data?: Partial<Flows>, options?: ValidationOptions) {
    const fullData = data || { flowDataSet: {} };
    super(fullData as Flows, options);
  }
  
  protected getRootKey(): string {
    return 'flowDataSet';
  }
  
  protected getSchema(): z.ZodSchema<Flows> {
    return FlowsSchema;
  }
}

/**
 * Source object
 */
export class SourceBaseObject extends TypedTidasBase<Sources> {
  constructor(data?: Partial<Sources>, options?: ValidationOptions) {
    const fullData = data || { sourceDataSet: {} };
    super(fullData as Sources, options);
  }
  
  protected getRootKey(): string {
    return 'sourceDataSet';
  }
  
  protected getSchema(): z.ZodSchema<Sources> {
    return SourcesSchema;
  }
}

/**
 * Flow Property object
 */
export class FlowPropertyBaseObject extends TypedTidasBase<Flowproperties> {
  constructor(data?: Partial<Flowproperties>, options?: ValidationOptions) {
    const fullData = data || { flowPropertyDataSet: {} };
    super(fullData as Flowproperties, options);
  }
  
  protected getRootKey(): string {
    return 'flowPropertyDataSet';
  }
  
  protected getSchema(): z.ZodSchema<Flowproperties> {
    return FlowpropertiesSchema;
  }
}

/**
 * Unit Group object
 */
export class UnitGroupBaseObject extends TypedTidasBase<Unitgroups> {
  constructor(data?: Partial<Unitgroups>, options?: ValidationOptions) {
    const fullData = data || { unitGroupDataSet: {} };
    super(fullData as Unitgroups, options);
  }
  
  protected getRootKey(): string {
    return 'unitGroupDataSet';
  }
  
  protected getSchema(): z.ZodSchema<Unitgroups> {
    return UnitgroupsSchema;
  }
}

/**
 * LCIA Method object
 */
export class LCIAMethodBaseObject extends TypedTidasBase<Lciamethods> {
  constructor(data?: Partial<Lciamethods>, options?: ValidationOptions) {
    const fullData = data || { LCIAMethodDataSet: {} };
    super(fullData as Lciamethods, options);
  }
  
  protected getRootKey(): string {
    return 'LCIAMethodDataSet';
  }
  
  protected getSchema(): z.ZodSchema<Lciamethods> {
    return LciamethodsSchema;
  }
}

/**
 * Life Cycle Model object
 */
export class LifeCycleModelBaseObject extends TypedTidasBase<Lifecyclemodels> {
  constructor(data?: Partial<Lifecyclemodels>, options?: ValidationOptions) {
    const fullData = data || { lifeCycleModelDataSet: {} };
    super(fullData as Lifecyclemodels, options);
  }
  
  protected getRootKey(): string {
    return 'lifeCycleModelDataSet';
  }
  
  protected getSchema(): z.ZodSchema<Lifecyclemodels> {
    return LifecyclemodelsSchema;
  }
}