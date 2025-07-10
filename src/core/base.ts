import { set } from '../utils/object-utils';
import { TypeAwareHelpers } from './type-aware-helpers';

export interface SerializationOptions {
  pretty?: boolean;
  includeEmpty?: boolean;
  excludeFields?: string[];
}

export interface CloneOptions {
  generateNewUUID?: boolean;
}

export abstract class TidasBase<T = any> {
  protected _data: T;

  constructor(data: T) {
    this._data = data;
  }

  /**
   * Get the raw data object
   */
  get data(): T {
    return this._data;
  }

  /**
   * Deep clone the object
   */
  clone(options: CloneOptions = {}): this {
    const cloned = new (this.constructor as new (data: T) => this)(
      TypeAwareHelpers.deepClone(this._data)
    );
    
    if (options.generateNewUUID && this.hasUUID()) {
      cloned.generateNewUUID();
    }
    
    return cloned;
  }

  /**
   * Merge data with current object
   */
  merge(data: Partial<T>): this {
    this._data = this.deepMerge(this._data, data);
    return this;
  }

  /**
   * Update nested property using dot notation
   */
  update(updates: Record<string, any>): this {
    for (const [path, value] of Object.entries(updates)) {
      set(this._data, path, value);
    }
    return this;
  }

  /**
   * Get nested property using dot notation
   */
  get(path: string, defaultValue?: any): any {
    return TypeAwareHelpers.safeGet(this._data, path, defaultValue);
  }

  /**
   * Set nested property using dot notation
   */
  set(path: string, value: any): this {
    TypeAwareHelpers.safeSet(this._data, path, value);
    return this;
  }

  /**
   * Get multi-language text from a specific path
   */
  getMultiLangText(path: string, lang: string = 'en'): string {
    const multiLangText = this.get(path);
    return TypeAwareHelpers.extractMultiLangText(multiLangText, lang);
  }

  /**
   * Set multi-language text at a specific path
   */
  setMultiLangText(path: string, text: string, lang: string = 'en'): this {
    const existing = this.get(path);
    const updated = TypeAwareHelpers.createOrUpdateMultiLangText(existing, text, lang);
    this.set(path, updated);
    return this;
  }

  /**
   * Get reference information from a GlobalReferenceType field
   */
  getReferenceInfo(path: string): {
    id: string;
    type: string;
    uri: string;
    version: string;
    description: string;
  } | null {
    const reference = this.get(path);
    return TypeAwareHelpers.extractReferenceInfo(reference);
  }

  /**
   * Set reference information for a GlobalReferenceType field
   */
  setReferenceInfo(path: string, options: {
    refObjectId: string;
    type: string;
    uri: string;
    version?: string;
    description: string;
    lang?: string;
  }): this {
    const reference = TypeAwareHelpers.createGlobalReference(options);
    this.set(path, reference);
    return this;
  }

  /**
   * Get all multi-language texts in the object
   */
  getAllMultiLangTexts(): { path: string; texts: Array<{ lang: string; text: string }> }[] {
    return TypeAwareHelpers.extractAllMultiLangTexts(this._data);
  }

  /**
   * Update all multi-language texts for a specific language
   */
  updateAllMultiLangTexts(
    updates: { path: string; text: string }[],
    lang: string = 'en'
  ): this {
    this._data = TypeAwareHelpers.updateAllMultiLangTexts(this._data, updates, lang);
    return this;
  }

  /**
   * Convert to JSON string
   */
  toJSON(options: SerializationOptions = {}): string {
    const data = this.processForSerialization(this._data, options);
    return options.pretty 
      ? JSON.stringify(data, null, 2)
      : JSON.stringify(data);
  }

  /**
   * Convert to JSON object
   */
  toJSONObject(options: SerializationOptions = {}): any {
    return this.processForSerialization(this._data, options);
  }

  /**
   * Check if object has UUID field
   */
  protected hasUUID(): boolean {
    return this.getUUIDPath() !== null;
  }

  /**
   * Generate new UUID for the object
   */
  protected generateNewUUID(): void {
    const uuidPath = this.getUUIDPath();
    if (uuidPath) {
      TypeAwareHelpers.safeSet(this._data, uuidPath, TypeAwareHelpers.generateUUID());
    }
  }

  /**
   * Get the path to UUID field (override in subclasses)
   */
  protected getUUIDPath(): string | null {
    return null;
  }

  /**
   * Get the UUID of this object
   */
  getUUID(): string | null {
    const uuidPath = this.getUUIDPath();
    return uuidPath ? this.get(uuidPath) : null;
  }

  /**
   * Generate a new UUID
   */
  protected generateUUID(): string {
    return TypeAwareHelpers.generateUUID();
  }

  /**
   * Deep merge helper using TypeAwareHelpers
   */
  protected deepMerge<U>(target: U, source: Partial<U>): U {
    const result = TypeAwareHelpers.deepClone(target);

    for (const key in source) {
      if (Object.prototype.hasOwnProperty.call(source, key)) {
        const sourceValue = source[key];
        const targetValue = (result as any)[key];

        if (sourceValue !== undefined && this.isObject(sourceValue) && this.isObject(targetValue)) {
          (result as any)[key] = this.deepMerge(targetValue, sourceValue as Partial<any>);
        } else if (sourceValue !== undefined) {
          (result as any)[key] = sourceValue;
        }
      }
    }

    return result;
  }

  /**
   * Check if value is a plain object
   */
  protected isObject(obj: any): boolean {
    return obj !== null && typeof obj === 'object' && !Array.isArray(obj);
  }

  /**
   * Process data for serialization
   */
  protected processForSerialization(data: any, options: SerializationOptions): any {
    if (data === null || typeof data !== 'object') {
      return data;
    }

    if (Array.isArray(data)) {
      return data.map(item => this.processForSerialization(item, options));
    }

    const result: any = {};
    for (const key in data) {
      if (Object.prototype.hasOwnProperty.call(data, key)) {
        // Skip excluded fields
        if (options.excludeFields?.includes(key)) {
          continue;
        }

        const value = data[key];
        
        // Skip empty values if requested
        if (!options.includeEmpty && this.isEmpty(value)) {
          continue;
        }

        result[key] = this.processForSerialization(value, options);
      }
    }

    return result;
  }

  /**
   * Check if value is empty
   */
  protected isEmpty(value: any): boolean {
    if (value === null || value === undefined) {
      return true;
    }
    
    if (typeof value === 'string') {
      return value.trim() === '';
    }
    
    if (Array.isArray(value)) {
      return value.length === 0;
    }
    
    if (typeof value === 'object') {
      return Object.keys(value).length === 0;
    }
    
    return false;
  }
}