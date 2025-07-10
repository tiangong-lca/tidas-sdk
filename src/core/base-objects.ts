import { TidasBase } from './base';
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

/**
 * Base class for all TIDAS objects with auto-detection capabilities
 */
abstract class TypedTidasBase<T> extends TidasBase<T> {
  protected abstract getRootKey(): string;
  
  /**
   * Create a default/empty object with minimal structure
   */
  static createDefault<U extends TypedTidasBase<any>>(
    this: new (data?: any) => U
  ): U {
    return new this();
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
    // Auto-detect available paths and create minimal valid structure
    const availablePaths = this.getAvailablePaths();
    
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
  constructor(data?: Partial<Contacts>) {
    const fullData = data || { contactDataSet: {} };
    super(fullData as Contacts);
  }
  
  protected getRootKey(): string {
    return 'contactDataSet';
  }
}

/**
 * Process object
 */
export class ProcessBaseObject extends TypedTidasBase<Processes> {
  constructor(data?: Partial<Processes>) {
    const fullData = data || { processDataSet: {} };
    super(fullData as Processes);
  }
  
  protected getRootKey(): string {
    return 'processDataSet';
  }
}

/**
 * Flow object
 */
export class FlowBaseObject extends TypedTidasBase<Flows> {
  constructor(data?: Partial<Flows>) {
    const fullData = data || { flowDataSet: {} };
    super(fullData as Flows);
  }
  
  protected getRootKey(): string {
    return 'flowDataSet';
  }
}

/**
 * Source object
 */
export class SourceBaseObject extends TypedTidasBase<Sources> {
  constructor(data?: Partial<Sources>) {
    const fullData = data || { sourceDataSet: {} };
    super(fullData as Sources);
  }
  
  protected getRootKey(): string {
    return 'sourceDataSet';
  }
}

/**
 * Flow Property object
 */
export class FlowPropertyBaseObject extends TypedTidasBase<Flowproperties> {
  constructor(data?: Partial<Flowproperties>) {
    const fullData = data || { flowPropertyDataSet: {} };
    super(fullData as Flowproperties);
  }
  
  protected getRootKey(): string {
    return 'flowPropertyDataSet';
  }
}

/**
 * Unit Group object
 */
export class UnitGroupBaseObject extends TypedTidasBase<Unitgroups> {
  constructor(data?: Partial<Unitgroups>) {
    const fullData = data || { unitGroupDataSet: {} };
    super(fullData as Unitgroups);
  }
  
  protected getRootKey(): string {
    return 'unitGroupDataSet';
  }
}

/**
 * LCIA Method object
 */
export class LCIAMethodBaseObject extends TypedTidasBase<Lciamethods> {
  constructor(data?: Partial<Lciamethods>) {
    const fullData = data || { LCIAMethodDataSet: {} };
    super(fullData as Lciamethods);
  }
  
  protected getRootKey(): string {
    return 'LCIAMethodDataSet';
  }
}

/**
 * Life Cycle Model object
 */
export class LifeCycleModelBaseObject extends TypedTidasBase<Lifecyclemodels> {
  constructor(data?: Partial<Lifecyclemodels>) {
    const fullData = data || { lifeCycleModelDataSet: {} };
    super(fullData as Lifecyclemodels);
  }
  
  protected getRootKey(): string {
    return 'lifeCycleModelDataSet';
  }
}