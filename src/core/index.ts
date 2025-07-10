/**
 * Core module exports
 * Provides unified access to all Tidas SDK functionality
 */

// Base classes and types
export { TidasBase, type SerializationOptions, type CloneOptions, type ValidationOptions, type MockOptions } from './base';
export { TypeAwareHelpers } from './type-aware-helpers';

// Import needed for internal use
import { SerializationOptions } from './base';
import { TypeAwareHelpers } from './type-aware-helpers';

// Base object classes
export {
  ContactBaseObject,
  ProcessBaseObject,
  FlowBaseObject,
  SourceBaseObject,
  FlowPropertyBaseObject,
  UnitGroupBaseObject,
  LCIAMethodBaseObject,
  LifeCycleModelBaseObject
} from './base-objects';

// User-friendly object classes (compatible with existing API)
import { ContactBaseObject, ProcessBaseObject, FlowBaseObject } from './base-objects';
import type { Contact, Process, Flow } from '../types';
import type { ValidationOptions } from './base';

/**
 * Contact object - user-friendly alias for ContactBaseObject
 */
export class TidasContact extends ContactBaseObject {
  constructor(data?: Partial<Contact>, options?: ValidationOptions) {
    // Ensure basic structure exists
    const fullData = data || { contactDataSet: {} as any };
    if (!fullData.contactDataSet) {
      fullData.contactDataSet = {} as any;
    }
    super(fullData, options);
  }
}

/**
 * Process object - user-friendly alias for ProcessBaseObject  
 */
export class TidasProcess extends ProcessBaseObject {
  constructor(data?: Partial<Process>, options?: ValidationOptions) {
    super(data, options);
  }
}

/**
 * Flow object - user-friendly alias for FlowBaseObject
 */
export class TidasFlow extends FlowBaseObject {
  constructor(data?: Partial<Flow>, options?: ValidationOptions) {
    super(data, options);
  }
}

// Factory functions
/**
 * Create a new Contact object
 */
export function createContact(data?: Partial<Contact>, options?: ValidationOptions): TidasContact {
  return new TidasContact(data, options);
}

/**
 * Create a new Process object
 */
export function createProcess(data?: Partial<Process>, options?: ValidationOptions): TidasProcess {
  return new TidasProcess(data, options);
}

/**
 * Create a new Flow object
 */
export function createFlow(data?: Partial<Flow>, options?: ValidationOptions): TidasFlow {
  return new TidasFlow(data, options);
}

// Builder functions (fluent API)
/**
 * Build a Contact object with fluent API
 */
export function buildContact(): ContactBuilder {
  return new ContactBuilder();
}

/**
 * Build a Process object with fluent API
 */
export function buildProcess(): ProcessBuilder {
  return new ProcessBuilder();
}

/**
 * Build a Flow object with fluent API
 */
export function buildFlow(): FlowBuilder {
  return new FlowBuilder();
}

// Builder classes
class ContactBuilder {
  private _data: Partial<Contact> = {};
  private _options: ValidationOptions = {};

  withData(data: Partial<Contact>): this {
    this._data = { ...this._data, ...data };
    return this;
  }

  withValidation(options: ValidationOptions = { enableValidation: true }): this {
    this._options = { ...this._options, ...options };
    return this;
  }

  withUUID(): this {
    // Ensure we have a contactDataSet structure first
    if (!this._data.contactDataSet) {
      this._data.contactDataSet = {} as any;
    }
    const contact = new TidasContact(this._data, this._options);
    contact.createWithUUID();
    this._data = contact.data;
    return this;
  }

  withAutoStructure(): this {
    const contact = new TidasContact(this._data, this._options);
    contact.createWithAutoStructure();
    this._data = contact.data;
    return this;
  }

  build(): TidasContact {
    return new TidasContact(this._data, this._options);
  }
}

class ProcessBuilder {
  private _data: Partial<Process> = {};
  private _options: ValidationOptions = {};

  withData(data: Partial<Process>): this {
    this._data = { ...this._data, ...data };
    return this;
  }

  withValidation(options: ValidationOptions = { enableValidation: true }): this {
    this._options = { ...this._options, ...options };
    return this;
  }

  withUUID(): this {
    const process = new TidasProcess(this._data, this._options);
    process.createWithUUID();
    this._data = process.data;
    return this;
  }

  withAutoStructure(): this {
    const process = new TidasProcess(this._data, this._options);
    process.createWithAutoStructure();
    this._data = process.data;
    return this;
  }

  build(): TidasProcess {
    return new TidasProcess(this._data, this._options);
  }
}

class FlowBuilder {
  private _data: Partial<Flow> = {};
  private _options: ValidationOptions = {};

  withData(data: Partial<Flow>): this {
    this._data = { ...this._data, ...data };
    return this;
  }

  withValidation(options: ValidationOptions = { enableValidation: true }): this {
    this._options = { ...this._options, ...options };
    return this;
  }

  withUUID(): this {
    const flow = new TidasFlow(this._data, this._options);
    flow.createWithUUID();
    this._data = flow.data;
    return this;
  }

  withAutoStructure(): this {
    const flow = new TidasFlow(this._data, this._options);
    flow.createWithAutoStructure();
    this._data = flow.data;
    return this;
  }

  build(): TidasFlow {
    return new TidasFlow(this._data, this._options);
  }
}

// JSON conversion functions
import { validateWithZod } from '../schemas';
import { ContactSchema, ProcessSchema, FlowSchema } from '../schemas';

/**
 * Convert JSON to Tidas object with validation
 */
export function fromJSON<T>(
  jsonData: string | object,
  type: 'contact' | 'process' | 'flow',
  options?: ValidationOptions
): T {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  
  switch (type) {
    case 'contact':
      if (options?.enableValidation) {
        const result = validateWithZod(data, ContactSchema);
        if (!result.success) {
          throw new Error(`Validation failed: ${result.error?.message}`);
        }
        return new TidasContact(result.data, options) as unknown as T;
      }
      return new TidasContact(data, options) as unknown as T;
      
    case 'process':
      if (options?.enableValidation) {
        const result = validateWithZod(data, ProcessSchema);
        if (!result.success) {
          throw new Error(`Validation failed: ${result.error?.message}`);
        }
        return new TidasProcess(result.data as Partial<Process>, options) as unknown as T;
      }
      return new TidasProcess(data as any, options) as unknown as T;
      
    case 'flow':
      if (options?.enableValidation) {
        const result = validateWithZod(data, FlowSchema);
        if (!result.success) {
          throw new Error(`Validation failed: ${result.error?.message}`);
        }
        return new TidasFlow(result.data as Partial<Flow>, options) as unknown as T;
      }
      return new TidasFlow(data, options) as unknown as T;
      
    default:
      throw new Error(`Unknown type: ${type}`);
  }
}

/**
 * Convert Tidas object to JSON string
 */
export function toJSON(obj: TidasContact | TidasProcess | TidasFlow, options?: SerializationOptions): string {
  return obj.toJSON(options);
}

/**
 * Convert Tidas object to JSON object
 */
export function toJSONObject(obj: TidasContact | TidasProcess | TidasFlow, options?: SerializationOptions): any {
  return obj.toJSONObject(options);
}

/**
 * Convert JSON array to Tidas objects
 */
export function fromJSONArray<T>(
  jsonArray: string | object[],
  type: 'contact' | 'process' | 'flow',
  options?: ValidationOptions
): T[] {
  const array = typeof jsonArray === 'string' ? JSON.parse(jsonArray) : jsonArray;
  return array.map((item: any) => fromJSON<T>(item, type, options));
}

/**
 * Convert Tidas objects array to JSON string
 */
export function toJSONArray(objects: (TidasContact | TidasProcess | TidasFlow)[], options?: SerializationOptions): string {
  return JSON.stringify(objects.map(obj => obj.toJSONObject(options)), null, options?.pretty ? 2 : 0);
}

// Simplified object classes for easy creation with schema discovery
export {
  SimplifiedTidasObject,
  SchemaIntrospector,
  UniversalTidasBuilder,
  createSimplified,
  buildObject,
  registerSchema,
  getSchemaFromRegistry,
  type FieldMetadata,
  type ConversionOptions,
  type IncompleteValidationResult
} from './simplified-objects';

// Typed accessors for property-style access with code hints
export {
  createTypedAccessor,
  createEnhancedTypedAccessor,
  createMultiLangAccessor,
  createTypedContact,
  createTypedProcess,
  createTypedFlow,
  type TypedAccessor,
  type EnhancedTypedAccessor,
  type MultiLangTextAccessor,
  type ContactAccessor,
  type ProcessAccessor,
  type FlowAccessor,
  type NestedKeyOf,
  type PathValue
} from './typed-accessors';

// Zod Proxy for true property access with Schema validation
export {
  ZodProxy,
  createZodProxy,
  type PathInfo,
  type AccessLogEntry,
  type ZodProxyOptions,
  type ZodProxyValidationResult
} from './zod-proxy';

// TIDAS-specific Zod factories
export {
  createZodContact,
  createZodFlow,
  createZodProcess,
  createZodTidasProxy,
  ContactSchema,
  FlowSchema,
  ProcessSchema,
  type ZodContact,
  type ZodFlow,
  type ZodProcess
} from './zod-factories';

// Utility functions
export { deepClone, merge, get, set, updatePath } from '../utils/object-utils';

/**
 * Create multi-language text helper
 */
export function createMultiLangText(text: string, lang: string = 'en') {
  return TypeAwareHelpers.createOrUpdateMultiLangText(undefined, text, lang);
}

/**
 * Generate UUID helper
 */
export function generateUUID(): string {
  return TypeAwareHelpers.generateUUID();
}