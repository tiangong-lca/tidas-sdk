import type { SerializationOptions } from './base';
import { TypeAwareHelpers } from './type-aware-helpers';
import { z } from 'zod';

/**
 * Field metadata for schema discovery
 */
export interface FieldMetadata {
  path: string;
  type: 'string' | 'number' | 'boolean' | 'object' | 'array' | 'uuid' | 'timestamp' | 'multilang' | 'reference';
  required: boolean;
  description?: string;
  example?: any;
  children?: FieldMetadata[];
}

/**
 * Conversion options for toComplete()
 */
export interface ConversionOptions {
  fillMissingWithDefaults?: boolean;
  fillMissingWithMocks?: boolean;
  validateOnConversion?: boolean;
  throwOnValidationError?: boolean;
  autoGenerateUUIDs?: boolean;
  autoGenerateTimestamps?: boolean;
}

/**
 * Validation result for incomplete objects
 */
export interface IncompleteValidationResult {
  missingRequired: string[];
  invalidFields: Array<{ path: string; error: string }>;
  suggestions: Array<{ path: string; suggestion: string }>;
  canConvert: boolean;
}

/**
 * Schema introspection utility
 */
export class SchemaIntrospector {
  /**
   * Extract field metadata from Zod schema
   */
  static extractFieldsFromSchema(schema: z.ZodSchema, rootPath: string = ''): FieldMetadata[] {
    const fields: FieldMetadata[] = [];
    
    try {
      // Try to parse with empty object to get validation errors
      const result = schema.safeParse({});
      if (!result.success) {
        for (const issue of result.error.issues) {
          const path = rootPath ? `${rootPath}.${issue.path.join('.')}` : issue.path.join('.');
          fields.push({
            path,
            type: this.inferTypeFromIssue(issue),
            required: issue.code === 'invalid_type' && issue.expected !== 'undefined',
            description: this.generateDescription(path),
            example: this.generateExample(path)
          });
        }
      }
    } catch {
      // Fallback: analyze schema structure if available
      fields.push(...this.extractFromSchemaStructure(schema, rootPath));
    }
    
    return fields;
  }

  /**
   * Find UUID paths in schema
   */
  static findUUIDPaths(schema: z.ZodSchema): string[] {
    const fields = this.extractFieldsFromSchema(schema);
    return fields
      .filter(f => f.type === 'uuid' || f.path.includes('UUID') || f.path.includes('common:UUID'))
      .map(f => f.path);
  }

  /**
   * Find timestamp paths in schema
   */
  static findTimestampPaths(schema: z.ZodSchema): string[] {
    const fields = this.extractFieldsFromSchema(schema);
    return fields
      .filter(f => f.type === 'timestamp' || f.path.includes('timeStamp') || f.path.includes('common:timeStamp'))
      .map(f => f.path);
  }

  /**
   * Find multi-language text paths
   */
  static findMultiLangPaths(schema: z.ZodSchema): string[] {
    const fields = this.extractFieldsFromSchema(schema);
    return fields
      .filter(f => f.type === 'multilang' || f.path.includes('name') || f.path.includes('Name'))
      .map(f => f.path);
  }

  /**
   * Extract root key from schema by analyzing its structure
   */
  static extractRootKey(schema: z.ZodSchema): string | null {
    try {
      // Try to generate a mock and see what root key appears
      const mockData = this.generateSchemaMock(schema);
      const keys = Object.keys(mockData);
      return keys.find(key => key.endsWith('DataSet')) || keys[0] || null;
    } catch {
      return null;
    }
  }

  /**
   * Generate namespace configuration from schema
   */
  static extractNamespaces(schema: z.ZodSchema): Record<string, string> {
    const namespaces: Record<string, string> = {};
    
    // Common ILCD namespaces - can be detected from schema validation errors
    const commonNamespaces = {
      '@xmlns': 'http://lca.jrc.it/ILCD',
      '@xmlns:common': 'http://lca.jrc.it/ILCD/Common',
      '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
      '@version': '1.1'
    };

    // Try to determine which namespaces are needed
    const fields = this.extractFieldsFromSchema(schema);
    const hasCommonFields = fields.some(f => f.path.includes('common:'));
    
    if (hasCommonFields) {
      Object.assign(namespaces, commonNamespaces);
    }

    return namespaces;
  }

  private static inferTypeFromIssue(issue: z.ZodIssue): FieldMetadata['type'] {
    if (issue.path.some(p => p.toString().includes('UUID'))) return 'uuid';
    if (issue.path.some(p => p.toString().includes('timeStamp'))) return 'timestamp';
    if (issue.path.some(p => p.toString().includes('@xml:lang'))) return 'multilang';
    
    // Type inference based on issue code instead of 'expected' property
    if (issue.code === 'invalid_type') {
      const receivedType = (issue as any).received;
      if (receivedType === 'string') return 'string';
      if (receivedType === 'number') return 'number';
      if (receivedType === 'boolean') return 'boolean';
    }
    
    return 'string';
  }

  private static generateDescription(path: string): string {
    const pathParts = path.split('.');
    const lastPart = pathParts[pathParts.length - 1];
    
    if (lastPart.includes('UUID')) return 'Unique identifier';
    if (lastPart.includes('timeStamp')) return 'Timestamp';
    if (lastPart.includes('name')) return 'Name or title';
    if (lastPart.includes('email')) return 'Email address';
    if (lastPart.includes('version')) return 'Version number';
    
    return `Field: ${lastPart}`;
  }

  private static generateExample(path: string): any {
    if (path.includes('UUID')) return '123e4567-e89b-12d3-a456-426614174000';
    if (path.includes('timeStamp')) return new Date().toISOString();
    if (path.includes('@xml:lang')) return 'en';
    if (path.includes('#text')) return 'Example text';
    if (path.includes('email')) return 'example@example.com';
    if (path.includes('version')) return '01.00.000';
    if (path.includes('name')) return { '@xml:lang': 'en', '#text': 'Example Name' };
    
    return 'example value';
  }

  private static generateSchemaMock(schema: z.ZodSchema): any {
    try {
      // Use existing mock generation if available
      // eslint-disable-next-line @typescript-eslint/no-require-imports
      const { generateMock } = require('@anatine/zod-mock');
      return generateMock(schema);
    } catch {
      // Fallback to empty object
      return {};
    }
  }

  private static extractFromSchemaStructure(_schema: z.ZodSchema, rootPath: string): FieldMetadata[] {
    // Fallback implementation - return common fields structure
    return [
      {
        path: `${rootPath ? rootPath + '.' : ''}common:UUID`,
        type: 'uuid',
        required: true,
        description: 'Unique identifier',
        example: '123e4567-e89b-12d3-a456-426614174000'
      }
    ];
  }
}

/**
 * Dynamic simplified object that discovers its structure from schema
 */
export class SimplifiedTidasObject<T = any> {
  protected _partialData: Partial<T>;
  protected _schema: z.ZodSchema<T> | null;
  protected _fieldMetadata: FieldMetadata[] | null = null;
  protected _rootKey: string | null = null;
  protected _uuidPaths: string[] | null = null;
  protected _timestampPaths: string[] | null = null;
  protected _multiLangPaths: string[] | null = null;

  constructor(schema?: z.ZodSchema<T>, data?: Partial<T>) {
    this._schema = schema || null;
    this._partialData = data ? { ...data } : {};
    
    // Initialize schema-based discovery if schema is provided
    if (this._schema) {
      this.initializeFromSchema();
    }
  }

  /**
   * Set schema and re-initialize discovery
   */
  setSchema(schema: z.ZodSchema<T>): this {
    this._schema = schema;
    this.initializeFromSchema();
    return this;
  }

  /**
   * Get the raw partial data
   */
  get data(): Partial<T> {
    return this._partialData;
  }

  /**
   * Set a field value using dot notation path
   */
  set<U = any>(path: string, value: U): this {
    this.setByPath(this._partialData, path, value);
    return this;
  }

  /**
   * Get a field value using dot notation path
   */
  get<U = any>(path: string, defaultValue?: U): U {
    return this.getByPath(this._partialData, path, defaultValue);
  }

  /**
   * Set multiple fields at once
   */
  setFields(fields: Record<string, any>): this {
    for (const [path, value] of Object.entries(fields)) {
      this.set(path, value);
    }
    return this;
  }

  /**
   * Set multi-language text field
   */
  setMultiLangText(path: string, text: string, lang: string = 'en'): this {
    const multiLangValue = {
      '@xml:lang': lang,
      '#text': text
    };
    this.set(path, multiLangValue);
    return this;
  }

  /**
   * Set reference field
   */
  setReference(path: string, options: {
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
   * Generate and set UUID for detected UUID fields
   */
  generateUUID(pathIndex: number = 0): this {
    const uuidPaths = this.getUUIDPaths();
    if (uuidPaths.length > pathIndex) {
      this.set(uuidPaths[pathIndex], TypeAwareHelpers.generateUUID());
    }
    return this;
  }

  /**
   * Set current timestamp for detected timestamp fields
   */
  setCurrentTimestamp(pathIndex: number = 0): this {
    const timestampPaths = this.getTimestampPaths();
    if (timestampPaths.length > pathIndex) {
      this.set(timestampPaths[pathIndex], TypeAwareHelpers.getCurrentTimestamp());
    }
    return this;
  }

  /**
   * Get all available field paths with metadata
   */
  getAvailableFields(): FieldMetadata[] {
    if (!this._fieldMetadata && this._schema) {
      this._fieldMetadata = SchemaIntrospector.extractFieldsFromSchema(this._schema);
    }
    return this._fieldMetadata || [];
  }

  /**
   * Get detected UUID paths
   */
  getUUIDPaths(): string[] {
    if (!this._uuidPaths && this._schema) {
      this._uuidPaths = SchemaIntrospector.findUUIDPaths(this._schema);
    }
    return this._uuidPaths || [];
  }

  /**
   * Get detected timestamp paths
   */
  getTimestampPaths(): string[] {
    if (!this._timestampPaths && this._schema) {
      this._timestampPaths = SchemaIntrospector.findTimestampPaths(this._schema);
    }
    return this._timestampPaths || [];
  }

  /**
   * Get detected multi-language text paths
   */
  getMultiLangPaths(): string[] {
    if (!this._multiLangPaths && this._schema) {
      this._multiLangPaths = SchemaIntrospector.findMultiLangPaths(this._schema);
    }
    return this._multiLangPaths || [];
  }

  /**
   * Get root key for this object type
   */
  getRootKey(): string | null {
    if (!this._rootKey && this._schema) {
      this._rootKey = SchemaIntrospector.extractRootKey(this._schema);
    }
    return this._rootKey;
  }

  /**
   * Get required fields that are missing
   */
  getMissingRequired(): string[] {
    const fields = this.getAvailableFields();
    const missing: string[] = [];
    
    for (const field of fields) {
      if (field.required && this.get(field.path) === undefined) {
        missing.push(field.path);
      }
    }
    
    return missing;
  }

  /**
   * Get field suggestions based on current data and schema analysis
   */
  getFieldSuggestions(): Array<{ path: string; suggestion: string; reason: string }> {
    const suggestions: Array<{ path: string; suggestion: string; reason: string }> = [];
    
    // UUID suggestions
    const uuidPaths = this.getUUIDPaths();
    for (const uuidPath of uuidPaths) {
      if (!this.get(uuidPath)) {
        suggestions.push({
          path: uuidPath,
          suggestion: `Generate UUID with .generateUUID()`,
          reason: 'Objects need unique identifiers'
        });
      }
    }
    
    // Multi-language field suggestions
    const multiLangPaths = this.getMultiLangPaths();
    for (const path of multiLangPaths.slice(0, 3)) { // Limit suggestions
      if (!this.get(path)) {
        suggestions.push({
          path,
          suggestion: `Set with .setMultiLangText('${path}', 'Your Text')`,
          reason: 'Name/title fields help identify the object'
        });
      }
    }
    
    return suggestions;
  }

  /**
   * Validate current partial data
   */
  validatePartial(): IncompleteValidationResult {
    const missingRequired = this.getMissingRequired();
    const invalidFields: Array<{ path: string; error: string }> = [];
    const suggestions = this.getFieldSuggestions();
    
    // Try validation if schema exists
    if (this._schema) {
      try {
        const result = this._schema.safeParse(this.toCompleteData({ fillMissingWithDefaults: true }));
        if (!result.success) {
          for (const issue of result.error.issues) {
            const path = issue.path.join('.');
            invalidFields.push({
              path,
              error: issue.message
            });
          }
        }
      } catch {
        // Ignore conversion errors during validation
      }
    }
    
    return {
      missingRequired,
      invalidFields,
      suggestions,
      canConvert: missingRequired.length === 0 && invalidFields.length === 0
    };
  }

  /**
   * Convert to complete object with validation
   */
  toComplete(options: ConversionOptions = {}): T {
    const defaultOptions: ConversionOptions = {
      fillMissingWithDefaults: true,
      fillMissingWithMocks: false,
      validateOnConversion: true,
      throwOnValidationError: true,
      autoGenerateUUIDs: true,
      autoGenerateTimestamps: true
    };
    
    const finalOptions = { ...defaultOptions, ...options };
    
    // Auto-generate missing UUIDs
    if (finalOptions.autoGenerateUUIDs) {
      const uuidPaths = this.getUUIDPaths();
      uuidPaths.forEach((path, index) => {
        if (!this.get(path)) {
          this.generateUUID(index);
        }
      });
    }
    
    // Auto-generate missing timestamps
    if (finalOptions.autoGenerateTimestamps) {
      const timestampPaths = this.getTimestampPaths();
      timestampPaths.forEach((path, index) => {
        if (!this.get(path)) {
          this.setCurrentTimestamp(index);
        }
      });
    }
    
    // Convert to complete data structure
    const completeData = this.toCompleteData(finalOptions);
    
    // Validate if requested
    if (finalOptions.validateOnConversion && this._schema) {
      const result = this._schema.safeParse(completeData);
      if (!result.success) {
        const errorMessage = `Validation failed: ${result.error.issues.map(i => `${i.path.join('.')}: ${i.message}`).join(', ')}`;
        if (finalOptions.throwOnValidationError) {
          throw new Error(errorMessage);
        } else {
          console.warn(errorMessage);
        }
      }
    }
    
    return completeData;
  }

  /**
   * Get a preview of what the complete object would look like
   */
  preview(options: ConversionOptions = {}): any {
    try {
      return this.toComplete({ ...options, throwOnValidationError: false });
    } catch {
      return this.toCompleteData(options);
    }
  }

  /**
   * Get completion status
   */
  getCompletionStatus(): {
    totalFields: number;
    completedFields: number;
    missingRequired: number;
    percentage: number;
    isReady: boolean;
  } {
    const fields = this.getAvailableFields();
    const missing = this.getMissingRequired();
    const totalRequired = fields.filter(f => f.required).length;
    const completed = totalRequired - missing.length;
    
    return {
      totalFields: fields.length,
      completedFields: completed,
      missingRequired: missing.length,
      percentage: totalRequired > 0 ? Math.round((completed / totalRequired) * 100) : 100,
      isReady: missing.length === 0
    };
  }

  /**
   * Clone the simplified object
   */
  clone(): this {
    const cloned = new (this.constructor as any)(this._schema, TypeAwareHelpers.deepClone(this._partialData));
    return cloned;
  }

  /**
   * Convert to JSON string
   */
  toJSON(options: SerializationOptions = {}): string {
    const data = options.pretty ? 
      JSON.stringify(this._partialData, null, 2) : 
      JSON.stringify(this._partialData);
    return data;
  }

  /**
   * Convert partial data to complete structure
   */
  protected toCompleteData(options: ConversionOptions): T {
    if (!this._schema) {
      return this._partialData as T;
    }

    // Get root key and create basic structure
    const rootKey = this.getRootKey();
    if (!rootKey) {
      return this._partialData as T;
    }

    // Create complete structure with namespaces
    const namespaces = SchemaIntrospector.extractNamespaces(this._schema);
    const template: any = {
      [rootKey]: {
        ...namespaces,
        ...this.createMinimalRequiredStructure(options)
      }
    };

    // Deep merge with partial data
    return this.deepMergeCompleteData(template, this._partialData);
  }

  /**
   * Create minimal required structure based on schema analysis
   */
  private createMinimalRequiredStructure(options: ConversionOptions): any {
    const structure: any = {};
    const fields = this.getAvailableFields();
    const rootKey = this.getRootKey();
    
    for (const field of fields.filter(f => f.required)) {
      if (!rootKey || !field.path.startsWith(rootKey)) continue;
      
      // Get relative path (remove root key)
      const relativePath = field.path.substring(rootKey.length + 1);
      
      let defaultValue: any;
      if (field.type === 'uuid') {
        defaultValue = this.get(field.path) || (options.fillMissingWithDefaults ? TypeAwareHelpers.generateUUID() : '');
      } else if (field.type === 'timestamp') {
        defaultValue = this.get(field.path) || (options.fillMissingWithDefaults ? TypeAwareHelpers.getCurrentTimestamp() : '');
      } else if (field.type === 'multilang') {
        defaultValue = this.get(field.path) || (options.fillMissingWithDefaults ? { '@xml:lang': 'en', '#text': `Default ${field.description}` } : undefined);
      } else {
        defaultValue = this.get(field.path) || (options.fillMissingWithDefaults ? field.example : undefined);
      }
      
      if (defaultValue !== undefined) {
        this.setByPath(structure, relativePath, defaultValue);
      }
    }
    
    return structure;
  }

  /**
   * Initialize schema-based discovery
   */
  private initializeFromSchema(): void {
    // Reset cached values to force re-discovery
    this._fieldMetadata = null;
    this._rootKey = null;
    this._uuidPaths = null;
    this._timestampPaths = null;
    this._multiLangPaths = null;
  }

  private setByPath(obj: any, path: string, value: any): void {
    const keys = path.split('.');
    let current = obj;
    
    for (let i = 0; i < keys.length - 1; i++) {
      if (!(keys[i] in current) || typeof current[keys[i]] !== 'object') {
        current[keys[i]] = {};
      }
      current = current[keys[i]];
    }
    
    current[keys[keys.length - 1]] = value;
  }

  private getByPath(obj: any, path: string, defaultValue?: any): any {
    const keys = path.split('.');
    let current = obj;
    
    for (const key of keys) {
      if (current === null || current === undefined || !(key in current)) {
        return defaultValue;
      }
      current = current[key];
    }
    
    return current;
  }

  private deepMergeCompleteData(target: any, source: any): any {
    const result = TypeAwareHelpers.deepClone(target);
    
    const merge = (targetObj: any, sourceObj: any) => {
      if (!sourceObj || typeof sourceObj !== 'object') return;
      
      for (const key in sourceObj) {
        if (sourceObj[key] !== undefined) {
          if (targetObj[key] && typeof targetObj[key] === 'object' && typeof sourceObj[key] === 'object') {
            merge(targetObj[key], sourceObj[key]);
          } else {
            targetObj[key] = sourceObj[key];
          }
        }
      }
    };
    
    merge(result, source);
    return result;
  }
}

// Factory functions using schema registry
export function createSimplified<T>(schemaOrName: z.ZodSchema<T> | string, data?: Partial<T>): SimplifiedTidasObject<T> {
  if (typeof schemaOrName === 'string') {
    // Try to load schema from registry if implemented
    const schema = getSchemaFromRegistry<T>(schemaOrName);
    return new SimplifiedTidasObject<T>(schema, data);
  }
  return new SimplifiedTidasObject<T>(schemaOrName, data);
}

// Universal builder that discovers capabilities from schema
export class UniversalTidasBuilder<T = any> {
  private obj: SimplifiedTidasObject<T>;

  constructor(schemaOrName: z.ZodSchema<T> | string, data?: Partial<T>) {
    this.obj = createSimplified(schemaOrName, data);
  }

  set(path: string, value: any): this {
    this.obj.set(path, value);
    return this;
  }

  setMultiLang(path: string, text: string, lang: string = 'en'): this {
    this.obj.setMultiLangText(path, text, lang);
    return this;
  }

  withUUID(index: number = 0): this {
    this.obj.generateUUID(index);
    return this;
  }

  withTimestamp(index: number = 0): this {
    this.obj.setCurrentTimestamp(index);
    return this;
  }

  // Smart setters that use discovered paths
  setName(text: string, lang: string = 'en'): this {
    const namePaths = this.obj.getMultiLangPaths().filter(p => p.includes('name'));
    if (namePaths.length > 0) {
      this.obj.setMultiLangText(namePaths[0], text, lang);
    }
    return this;
  }

  build(): SimplifiedTidasObject<T> {
    return this.obj;
  }

  buildComplete(options?: ConversionOptions): T {
    return this.obj.toComplete(options);
  }

  // Discovery methods
  getAvailableFields(): FieldMetadata[] {
    return this.obj.getAvailableFields();
  }

  getUUIDPaths(): string[] {
    return this.obj.getUUIDPaths();
  }

  getMultiLangPaths(): string[] {
    return this.obj.getMultiLangPaths();
  }

  getSuggestions(): Array<{ path: string; suggestion: string; reason: string }> {
    return this.obj.getFieldSuggestions();
  }
}

// Schema registry (to be extended)
const schemaRegistry = new Map<string, z.ZodSchema>();

export function registerSchema<T>(name: string, schema: z.ZodSchema<T>): void {
  schemaRegistry.set(name, schema);
}

export function getSchemaFromRegistry<T>(name: string): z.ZodSchema<T> | undefined {
  return schemaRegistry.get(name) as z.ZodSchema<T>;
}

// Convenience factory functions
export function buildObject<T>(schemaOrName: z.ZodSchema<T> | string, data?: Partial<T>): UniversalTidasBuilder<T> {
  return new UniversalTidasBuilder<T>(schemaOrName, data);
}