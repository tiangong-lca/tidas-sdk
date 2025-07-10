import { set } from '../utils/object-utils';
import { TypeAwareHelpers } from './type-aware-helpers';
import { z } from 'zod';
import type { ValidationResult } from '../schemas';
import { generateMock } from '@anatine/zod-mock';
import { createDirectPropertyAccessor } from './typed-accessors';

export interface SerializationOptions {
  pretty?: boolean;
  includeEmpty?: boolean;
  excludeFields?: string[];
}

export interface CloneOptions {
  generateNewUUID?: boolean;
}

export interface ValidationOptions {
  enableValidation?: boolean;
  throwOnValidationError?: boolean;
}

export interface MockOptions {
  fillMissingFields?: boolean;
  useRealData?: boolean;
  customFields?: Record<string, any>;
}

// export interface CreateOptions extends ValidationOptions {
//   // Additional options for object creation
// }

export abstract class TidasBase<T = any> {
  protected _data: T;
  protected _validationOptions: ValidationOptions;

  constructor(data: T, options: ValidationOptions = {}) {
    this._data = data;
    this._validationOptions = options;
  }

  /**
   * Get the raw data object
   */
  get data(): T {
    return this._data;
  }

  /**
   * Create a direct property accessor for seamless property access
   * This allows syntax like: obj.contactDataSet.contactInformation.dataSetInformation.email = 'test@example.com'
   */
  createDirectAccessor(): any {
    return createDirectPropertyAccessor(this._data, '', (newValue: T) => {
      this._data = newValue;
    });
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

  /**
   * Validate the current object using Zod schema
   * Override in subclasses to provide the appropriate schema
   */
  validate(): ValidationResult<T> {
    const schema = this.getSchema();
    if (!schema) {
      return {
        success: true,
        data: this._data
      };
    }

    const result = schema.safeParse(this._data);
    if (result.success) {
      return {
        success: true,
        data: result.data
      };
    } else {
      return {
        success: false,
        error: result.error
      };
    }
  }

  /**
   * Get the Zod schema for this object type
   * Override in subclasses to provide specific schema
   */
  protected getSchema(): z.ZodSchema<T> | null {
    return null;
  }

  /**
   * Validate and throw error if validation fails
   */
  validateOrThrow(): T {
    const result = this.validate();
    if (!result.success) {
      throw new Error(`Validation failed: ${result.error?.message}`);
    }
    return result.data!;
  }

  /**
   * Check if the object is valid
   */
  isValid(): boolean {
    return this.validate().success;
  }

  /**
   * Perform validation if enabled in options
   */
  protected performValidationIfEnabled(): void {
    if (this._validationOptions.enableValidation) {
      const result = this.validate();
      if (!result.success && this._validationOptions.throwOnValidationError) {
        throw new Error(`Validation failed: ${result.error?.message}`);
      }
    }
  }

  /**
   * Update validation options
   */
  setValidationOptions(options: ValidationOptions): this {
    this._validationOptions = { ...this._validationOptions, ...options };
    return this;
  }

  /**
   * Get current validation options
   */
  getValidationOptions(): ValidationOptions {
    return { ...this._validationOptions };
  }

  /**
   * Generate mock data using the object's Zod schema
   */
  generateMock(options: MockOptions = {}): T {
    const schema = this.getSchema();
    if (!schema) {
      throw new Error('No schema available for mock generation. Override getSchema() in the subclass.');
    }

    try {
      // Create stringMap for custom field generation
      const stringMap: Record<string, () => any> = {
        // UUID fields
        'common:UUID': () => TypeAwareHelpers.generateUUID(),
        'UUID': () => TypeAwareHelpers.generateUUID(),
        
        // Email fields
        'email': () => 'mock@example.com',
        'Email': () => 'mock@example.com',
        
        // Phone fields
        'telephoneNumber': () => '+1-555-0123',
        'phone': () => '+1-555-0123',
        
        // URL fields
        'WWWAddress': () => 'https://mock-example.com',
        'uri': () => 'https://mock-example.com',
        
        // Timestamp fields
        'common:timeStamp': () => new Date().toISOString(),
        'timeStamp': () => new Date().toISOString(),
        
        // Version fields
        'common:dataSetVersion': () => '01.00.000',
        'version': () => '01.00.000',
        '@version': () => '1.1',
        
        // Text content fields
        '#text': () => 'Mock Text Content',
        
        // Language fields
        '@xml:lang': () => 'en',
        
        // Classification fields
        '@classId': () => '00.00.00',
        '@level': () => '0',
        
        // Status fields
        'common:workflowAndPublicationStatus': () => 'Data set finalised; entirely published',
        
        // CAS Number
        'CASNumber': () => '123-45-6',
        
        // Location
        '@location': () => 'US',
        
        // Year
        'referenceYear': () => '2024',
        
        // Override with custom fields if provided
        ...this.createStringMapFromCustomFields(options.customFields)
      };

      const mockData = generateMock(schema, { 
        stringMap,
        seed: options.useRealData ? undefined : 12345 // Use fixed seed for reproducible results
      });
      
      // Apply additional custom fields if provided (for deep paths)
      if (options.customFields) {
        for (const [path, value] of Object.entries(options.customFields)) {
          TypeAwareHelpers.safeSet(mockData, path, value);
        }
      }

      return mockData;
    } catch (error) {
      // Fallback to template-based mock generation for complex schemas
      console.warn('Schema-based mock generation failed, using template fallback:', error instanceof Error ? error.message : 'Unknown error');
      return this.generateTemplateMock(options);
    }
  }

  /**
   * Create stringMap from custom fields for direct field mapping
   */
  private createStringMapFromCustomFields(customFields?: Record<string, any>): Record<string, () => any> {
    if (!customFields) return {};
    
    const stringMap: Record<string, () => any> = {};
    for (const [path, value] of Object.entries(customFields)) {
      // Extract the last part of the path as the field name
      const fieldName = path.split('.').pop();
      if (fieldName) {
        stringMap[fieldName] = () => value;
      }
    }
    return stringMap;
  }

  /**
   * Generate template-based mock data as fallback
   */
  protected generateTemplateMock(options: MockOptions = {}): T {
    // Simple fallback - create basic structure and let subclasses override if needed
    const template = this.getDefaultTemplate();
    
    // Apply custom fields if provided
    if (options.customFields) {
      for (const [path, value] of Object.entries(options.customFields)) {
        TypeAwareHelpers.safeSet(template, path, value);
      }
    }

    return template as T;
  }

  /**
   * Get default template for the object type (override in subclasses if needed)
   * Most cases should work with stringMap in generateMock()
   */
  protected getDefaultTemplate(): any {
    // Return empty object - the stringMap approach should handle most cases
    return {};
  }

  /**
   * Create a new instance with mock data
   */
  static createMock<T extends TidasBase>(
    this: new (data: any, options?: ValidationOptions) => T,
    options: MockOptions = {}
  ): T {
    const instance = new this({} as any);
    const mockData = instance.generateMock(options);
    return new this(mockData);
  }

  /**
   * Replace current data with mock data
   */
  fillWithMockData(options: MockOptions = {}): this {
    const mockData = this.generateMock(options);
    this._data = mockData;
    return this;
  }

  /**
   * Generate mock data for a specific field schema
   */
  generateMockForField<F>(fieldSchema: z.ZodSchema<F>): F {
    return generateMock(fieldSchema);
  }

  /**
   * Fill missing fields with mock data
   */
  fillMissingFields(): this {
    const schema = this.getSchema();
    if (!schema) {
      return this;
    }

    try {
      const fullMockData = generateMock(schema);
      this._data = this.deepMergeWithMock(this._data, fullMockData);
    } catch (error) {
      console.warn('Failed to generate mock data for missing fields:', error);
    }

    return this;
  }

  /**
   * Deep merge current data with mock data, only filling missing fields
   */
  private deepMergeWithMock(current: any, mock: any): any {
    if (current === null || current === undefined) {
      return mock;
    }

    if (typeof current !== 'object' || typeof mock !== 'object') {
      return current; // Keep existing primitive values
    }

    if (Array.isArray(current) || Array.isArray(mock)) {
      return current.length > 0 ? current : mock;
    }

    const result = { ...current };
    for (const key in mock) {
      if (!(key in result) || result[key] === null || result[key] === undefined) {
        result[key] = mock[key];
      } else if (typeof result[key] === 'object' && typeof mock[key] === 'object') {
        result[key] = this.deepMergeWithMock(result[key], mock[key]);
      }
    }

    return result;
  }
}