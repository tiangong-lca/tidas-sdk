import { z } from 'zod';
import {
  ValidationConfig,
  EnhancedValidationResult,
  ValidationUtils,
  ValidationMode,
} from '../config/ValidationConfig';
import { globalConfig } from '../config/GlobalConfig';
import {
  MultiLangArray,
  MultiLangItemClass,
} from '../../types/multi-lang-types';
import { suggestEntireObject } from '../methodology/ai';
import type { ModelConfig } from '../methodology/ai';
import { generateDiffHTML, generateDiffSummary } from '../../utils/diff';

/**
 * Legacy validation result type (maintained for backward compatibility)
 */
export type ValidationResult<T> =
  | {
      success: true;
      data: T;
    }
  | {
      success: false;
      error: z.ZodError;
    };

/**
 * Result type for suggest operation with diff output
 */
export interface SuggestResult<T extends TidasEntity> {
  data: T;
  diffSummary?: string;
  diffHTML?: string;
}

/**
 * Abstract base class for all TIDAS entities
 * Provides basic validation and data container functionality without property mapping
 */
export abstract class TidasEntity<T = any> {
  protected _schema: z.ZodSchema<T>;
  protected _data: Partial<T> = {};
  protected _proxy: any;
  protected _validationConfig: ValidationConfig;

  constructor(
    schema: z.ZodSchema<T>,
    initialData?: Partial<T>,
    validationConfig?: Partial<ValidationConfig>
  ) {
    this._schema = schema;
    this._data = initialData || {};
    this._validationConfig = {
      ...globalConfig.getDefaultValidationConfig(),
      ...validationConfig,
    };
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
          let value = (target._data as any)[prop];
          if (TidasEntity.isMultiLang(value)) {
            value = TidasEntity.wrapMultiLang(value);
            // 懒包装：回写，保证下次访问直接是class实例
            (target._data as any)[prop] = value;
          }
          return value;
        }

        // 3. Dynamic path access (supports dot notation)
        if (
          typeof prop === 'string' &&
          (prop.includes('.') || prop.includes('['))
        ) {
          let value = target.getNestedValue(prop);
          if (TidasEntity.isMultiLang(value)) {
            value = TidasEntity.wrapMultiLang(value);
            // 懒包装：回写
            target.setNestedValue(prop, value);
          }
          return value;
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
          // 懒包装：如果是多语言字段，wrap
          if (TidasEntity.isMultiLang(value)) {
            value = TidasEntity.wrapMultiLang(value);
          }
          target.setNestedValue(prop, value);
          return true;
        }

        // 2. Top-level property setting
        if (TidasEntity.isMultiLang(value)) {
          value = TidasEntity.wrapMultiLang(value);
        }
        (target._data as any)[prop] = value;
        return true;
      },

      has(target, prop: string) {
        return prop in target._data || prop in target;
      },

      ownKeys(target) {
        return [
          ...Object.keys(target._data),
          ...Object.getOwnPropertyNames(target),
        ];
      },
    });
  }

  /**
   * Helper: 判断是否为多语言字段（数组或单对象）
   */
  private static isMultiLang(val: any): boolean {
    return (
      (Array.isArray(val) &&
        val.length > 0 &&
        typeof val[0] === 'object' &&
        val[0] !== null &&
        '@xml:lang' in val[0] &&
        '#text' in val[0]) ||
      (val &&
        typeof val === 'object' &&
        !Array.isArray(val) &&
        '@xml:lang' in val &&
        '#text' in val)
    );
  }

  /**
   * Helper: 包装多语言字段，返回class实例
   */
  private static wrapMultiLang(val: any): any {
    if (val instanceof MultiLangArray || val instanceof MultiLangItemClass) {
      return val;
    }
    if (Array.isArray(val)) {
      const arr = new MultiLangArray();
      for (const item of val) {
        arr.push(
          item instanceof MultiLangItemClass
            ? item
            : new MultiLangItemClass(item['@xml:lang'], item['#text'])
        );
      }
      return arr;
    } else if (
      val &&
      typeof val === 'object' &&
      '@xml:lang' in val &&
      '#text' in val
    ) {
      return new MultiLangItemClass(val['@xml:lang'], val['#text']);
    }
    return val;
  }

  /**
   * Get nested value using dot notation path
   */
  protected getNestedValue(path: string): any {
    const value = this.resolvePath(this._data, path);
    if (TidasEntity.isMultiLang(value)) {
      return TidasEntity.wrapMultiLang(value);
    }
    return value;
  }

  /**
   * Get value using dot notation path
   */
  public getValue(path: string): any {
    return this.getNestedValue(path);
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
    paths.forEach((path) => {
      if (!this.getNestedValue(path)) {
        this.setNestedValue(path, {});
      }
    });
  }

  /**
   * Get current validation configuration
   */
  getValidationConfig(): ValidationConfig {
    return { ...this._validationConfig };
  }

  /**
   * Set validation mode
   */
  setValidationMode(mode: ValidationMode): void {
    this._validationConfig.mode = mode;
  }

  /**
   * Set validation configuration
   */
  setValidationConfig(config: Partial<ValidationConfig>): void {
    this._validationConfig = {
      ...this._validationConfig,
      ...config,
    };
  }

  /**
   * Enhanced validation with configurable modes
   */
  validateEnhanced(): EnhancedValidationResult<T> {
    return ValidationUtils.performValidation(
      this._schema,
      this._data,
      this._validationConfig
    );
  }

  /**
   * Legacy validation method (maintained for backward compatibility)
   * Uses current validation configuration but returns legacy result format
   */
  validate(): ValidationResult<T> {
    const enhancedResult = this.validateEnhanced();

    if (enhancedResult.success) {
      return {
        success: true,
        data: enhancedResult.data,
      };
    } else {
      return {
        success: false,
        error: enhancedResult.error,
      };
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
   * Removes undefined values, functions, empty objects, and ensures proper structure
   */
  private cleanForJSON(obj: any): any {
    if (obj === null || obj === undefined) {
      return null;
    }

    if (typeof obj === 'function') {
      return undefined;
    }

    if (Array.isArray(obj)) {
      return obj
        .map((item) => this.cleanForJSON(item))
        .filter((item) => item !== undefined && item !== null);
    }

    if (typeof obj === 'object') {
      const cleaned: any = {};
      for (const [key, value] of Object.entries(obj)) {
        const cleanedValue = this.cleanForJSON(value);
        if (cleanedValue !== undefined && cleanedValue !== null) {
          cleaned[key] = cleanedValue;
        }
      }
      if (cleaned instanceof Object) {
        return Object.keys(cleaned).length > 0 ? cleaned : undefined;
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
    return new Constructor(
      structuredClone(this._data),
      this._validationConfig
    );
  }

  /**
   * Get the methodology type based on the entity class name
   * Maps entity class names to their corresponding methodology types
   */
  protected getMethodologyType(): string {
    const className = this.constructor.name;
    const methodologyMapping: Record<string, string> = {
      'TidasProcess': 'processes',
      'TidasFlow': 'flows',
      'TidasContact': 'contacts',
      'TidasSource': 'sources',
      'TidasFlowProperty': 'flowproperties',
      'TidasUnitGroup': 'unitgroups',
      'TidasLCIAMethod': 'lciamethods',
      'TidasLifeCycleModel': 'lifecyclemodels'
    };
    
    const methodologyType = methodologyMapping[className];
    if (!methodologyType) {
      throw new Error(`Unknown entity type: ${className}. Cannot determine methodology type.`);
    }
    
    return methodologyType;
  }

  /**
   * Suggest improvements for the entire entity using AI-powered methodology rules
   * 
   * This method applies all applicable TIDAS methodology rules to improve the data quality
   * and compliance. It always returns a unified result structure containing the improved entity
   * and optional diff outputs.
   * 
   * @param options - Optional configuration for the suggestion process
   * @param options.skipPaths - Array of dot-notation paths to skip during improvement
   * @param options.maxRetries - Maximum number of retries per rule (default: 1)
   * @param options.modelConfig - Optional AI model configuration
   * @param options.outputDiffSummary - Whether to output a text diff summary (default: false)
   * @param options.outputDiffHTML - Whether to output an HTML diff visualization (default: false)
   * @param options.diffPaths - Specific paths to focus on in diff summary (optional)
   * @returns Promise<SuggestResult<this>> - Result object with improved entity and optional diffs
   * 
   * @example
   * ```typescript
   * // Basic usage
   * const process = createProcess({ ... });
   * const result = await process.suggestEntireObject();
   * const improvedProcess = result.data;
   * 
   * // With diff outputs
   * const result = await process.suggestEntireObject({
   *   skipPaths: ['processDataSet.administrativeInformation'],
   *   maxRetries: 2,
   *   outputDiffSummary: true,
   *   outputDiffHTML: true
   * });
   * console.log(result.data);        // The improved entity
   * console.log(result.diffSummary); // Text diff summary
   * console.log(result.diffHTML);    // HTML diff viewer code
   * ```
   */
  async suggestEntireObject(
    options?: {
      skipPaths?: string[];
      maxRetries?: number;
      modelConfig?: ModelConfig;
      outputDiffSummary?: boolean;
      outputDiffHTML?: boolean;
      diffPaths?: string[];
    }
  ): Promise<SuggestResult<this>> {
    try {
      // Get the methodology type for this entity
      const methodologyType = this.getMethodologyType();
      
      console.log(`Starting AI improvement for ${this.constructor.name}...`);
      
      // Store original data for diff if needed
      const originalData = options?.outputDiffSummary || options?.outputDiffHTML 
        ? this.toJSON() 
        : null;
      
      // Apply suggestions to the current data
      const improvedData = await suggestEntireObject(
        this._data,
        methodologyType,
        {
          skipPaths: options?.skipPaths,
          maxRetries: options?.maxRetries
        }
      );
      
      // Create a new instance of the same type with improved data
      const Constructor = this.constructor as new (...args: any[]) => this;
      const improvedEntity = new Constructor(
        improvedData,
        this._validationConfig
      );
      
      console.log(`✓ Successfully improved ${this.constructor.name}`);
      
      // Create unified result structure
      const result: SuggestResult<this> = {
        data: improvedEntity
      };
      
      // Generate diff outputs if requested
      if (options?.outputDiffSummary && originalData) {
        result.diffSummary = generateDiffSummary(
          originalData,
          improvedEntity.toJSON(),
          options.diffPaths
        );
        console.log('✓ Generated diff summary');
      }
      
      if (options?.outputDiffHTML && originalData) {
        result.diffHTML = generateDiffHTML(
          originalData,
          improvedEntity.toJSON()
        );
        console.log('✓ Generated diff HTML');
      }
      
      return result;
    } catch (error) {
      console.error(`Failed to suggest improvements: ${(error as Error).message}`);
      throw error;
    }
  }

  /**
   * Alias for suggestEntireObject for shorter syntax
   * 
   * @example
   * ```typescript
   * const result = await process.suggest();
   * const improvedProcess = result.data;
   * 
   * // With diff outputs
   * const result = await process.suggest({
   *   outputDiffHTML: true
   * });
   * console.log(result.data);      // The improved entity
   * console.log(result.diffHTML);  // HTML diff viewer code
   * ```
   */
  async suggest(options?: {
    skipPaths?: string[];
    maxRetries?: number;
    modelConfig?: ModelConfig;
    outputDiffSummary?: boolean;
    outputDiffHTML?: boolean;
    diffPaths?: string[];
  }): Promise<SuggestResult<this>> {
    return this.suggestEntireObject(options);
  }
}
