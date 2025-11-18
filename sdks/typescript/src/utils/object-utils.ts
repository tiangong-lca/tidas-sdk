/**
 * Get nested property using dot notation
 */
export function get(obj: any, path: string, defaultValue?: any): any {
  const keys = path.split('.');
  let current = obj;

  for (const key of keys) {
    if (current === null || current === undefined) {
      return defaultValue;
    }

    // Handle array access like "items[0]"
    if (key.includes('[') && key.includes(']')) {
      const [arrayKey, indexStr] = key.split('[');
      const index = parseInt(indexStr.replace(']', ''), 10);

      current = current[arrayKey];
      if (Array.isArray(current) && current.length > index) {
        current = current[index];
      } else {
        return defaultValue;
      }
    } else {
      current = current[key];
    }
  }

  return current !== undefined ? current : defaultValue;
}

/**
 * Set nested property using dot notation
 */
export function set(obj: any, path: string, value: any): void {
  const keys = path.split('.');
  let current = obj;

  for (let i = 0; i < keys.length - 1; i++) {
    const key = keys[i];

    // Handle array access like "items[0]"
    if (key.includes('[') && key.includes(']')) {
      const [arrayKey, indexStr] = key.split('[');
      const index = parseInt(indexStr.replace(']', ''), 10);

      if (!current[arrayKey]) {
        current[arrayKey] = [];
      }

      if (!current[arrayKey][index]) {
        current[arrayKey][index] = {};
      }

      current = current[arrayKey][index];
    } else {
      if (!current[key]) {
        current[key] = {};
      }
      current = current[key];
    }
  }

  const lastKey = keys[keys.length - 1];

  // Handle array access for the last key
  if (lastKey.includes('[') && lastKey.includes(']')) {
    const [arrayKey, indexStr] = lastKey.split('[');
    const index = parseInt(indexStr.replace(']', ''), 10);

    if (!current[arrayKey]) {
      current[arrayKey] = [];
    }

    current[arrayKey][index] = value;
  } else {
    current[lastKey] = value;
  }
}

/**
 * Deep clone an object
 */
export function deepClone<T>(obj: T): T {
  if (obj === null || typeof obj !== 'object') {
    return obj;
  }

  if (obj instanceof Date) {
    return new Date(obj.getTime()) as any;
  }

  if (obj instanceof Array) {
    return obj.map((item) => deepClone(item)) as any;
  }

  if (typeof obj === 'object') {
    const cloned = {} as any;
    for (const key in obj) {
      if (Object.prototype.hasOwnProperty.call(obj, key)) {
        cloned[key] = deepClone(obj[key]);
      }
    }
    return cloned;
  }

  return obj;
}

/**
 * Deep merge two objects
 */
export function merge<T>(target: T, source: Partial<T>): T {
  const result = deepClone(target);

  for (const key in source) {
    if (Object.prototype.hasOwnProperty.call(source, key)) {
      const sourceValue = source[key];
      const targetValue = (result as any)[key];

      if (
        sourceValue !== undefined &&
        isObject(sourceValue) &&
        isObject(targetValue)
      ) {
        (result as any)[key] = merge(targetValue, sourceValue as Partial<any>);
      } else if (sourceValue !== undefined) {
        (result as any)[key] = sourceValue;
      }
    }
  }

  return result;
}

/**
 * Update nested properties using path notation
 */
export function updatePath<T>(obj: T, updates: Record<string, any>): T {
  const result = deepClone(obj);

  for (const [path, value] of Object.entries(updates)) {
    set(result, path, value);
  }

  return result;
}

/**
 * Check if value is a plain object
 */
export function isObject(obj: any): boolean {
  return obj !== null && typeof obj === 'object' && !Array.isArray(obj);
}

/**
 * Check if value is empty
 */
export function isEmpty(value: any): boolean {
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
 * Schema type definitions
 */
export interface Schema {
  type:
    | 'object'
    | 'array'
    | 'string'
    | 'number'
    | 'boolean'
    | 'null'
    | 'undefined';
  properties?: Record<string, Schema>; // for objects
  items?: Schema; // for arrays
  nullable?: boolean; // if the value can be null
}

/**
 * Generate a schema representing the structure of a JSON object
 */
export function generateSchema(obj: any): Schema {
  // Handle null
  if (obj === null) {
    return { type: 'null' };
  }

  // Handle undefined
  if (obj === undefined) {
    return { type: 'undefined' };
  }

  // Handle primitive types
  const typeOf = typeof obj;
  if (typeOf === 'string') {
    return { type: 'string' };
  }
  if (typeOf === 'number') {
    return { type: 'number' };
  }
  if (typeOf === 'boolean') {
    return { type: 'boolean' };
  }

  // Handle arrays and array-like objects
  // Check if it's an array or has array-like characteristics
  if (
    Array.isArray(obj) ||
    (typeOf === 'object' &&
      obj !== null &&
      typeof obj.length === 'number' &&
      obj.length >= 0)
  ) {
    // Treat as array
    if (obj.length === 0) {
      return { type: 'array' };
    }

    // Generate schema for array items (using first non-null item as reference)
    let itemSchema: Schema | undefined;
    for (let i = 0; i < obj.length; i++) {
      const item = obj[i];
      if (item !== null && item !== undefined) {
        itemSchema = generateSchema(item);
        break;
      }
    }

    // Check if array contains null values
    let hasNull = false;
    for (let i = 0; i < obj.length; i++) {
      if (obj[i] === null) {
        hasNull = true;
        break;
      }
    }

    if (itemSchema && hasNull) {
      itemSchema.nullable = true;
    }

    return {
      type: 'array',
      items: itemSchema || { type: 'null' },
    };
  }

  // Handle objects
  if (typeOf === 'object') {
    const properties: Record<string, Schema> = {};

    for (const key in obj) {
      if (Object.prototype.hasOwnProperty.call(obj, key)) {
        properties[key] = generateSchema(obj[key]);
      }
    }

    return {
      type: 'object',
      properties,
    };
  }

  // Fallback (should not reach here for normal JSON)
  return { type: 'undefined' };
}

/**
 * Validate if a JSON object conforms to a given schema
 */
export function validateSchema(obj: any, schema: Schema): boolean {
  // Check for null
  if (obj === null) {
    return schema.type === 'null' || schema.nullable === true;
  }

  // Check for undefined
  if (obj === undefined) {
    return schema.type === 'undefined';
  }

  // Check primitive types
  const typeOf = typeof obj;

  if (schema.type === 'string') {
    return typeOf === 'string';
  }

  if (schema.type === 'number') {
    return typeOf === 'number';
  }

  if (schema.type === 'boolean') {
    return typeOf === 'boolean';
  }

  // Check arrays
  if (schema.type === 'array') {
    // Accept both arrays and array-like objects
    const isArrayLike =
      Array.isArray(obj) ||
      (typeOf === 'object' &&
        obj !== null &&
        typeof obj.length === 'number' &&
        obj.length >= 0);

    if (!isArrayLike) {
      return false;
    }

    // If schema has items definition, validate each item
    if (schema.items) {
      for (let i = 0; i < obj.length; i++) {
        if (!validateSchema(obj[i], schema.items)) {
          return false;
        }
      }
    }

    return true;
  }

  // Check objects
  if (schema.type === 'object') {
    if (typeOf !== 'object' || Array.isArray(obj)) {
      return false;
    }

    // Check if all required properties in schema exist in object
    if (schema.properties) {
      for (const key in schema.properties) {
        if (!Object.prototype.hasOwnProperty.call(obj, key)) {
          // Property is missing - schema doesn't match
          return false;
        }

        // Validate the property value against its schema
        if (!validateSchema(obj[key], schema.properties[key])) {
          return false;
        }
      }

      // Check if object has extra properties not in schema
      for (const key in obj) {
        if (Object.prototype.hasOwnProperty.call(obj, key)) {
          if (!schema.properties[key]) {
            // Object has a property not defined in schema
            return false;
          }
        }
      }
    }

    return true;
  }

  return false;
}

// Helper function to extract all paths from a schema
export function extractPaths(schema: any, prefix = ''): Set<string> {
  const paths = new Set<string>();

  if (schema.type === 'object' && schema.properties) {
    for (const key in schema.properties) {
      const fullPath = prefix ? `${prefix}.${key}` : key;
      paths.add(fullPath);

      const subPaths = extractPaths(schema.properties[key], fullPath);
      subPaths.forEach((path) => paths.add(path));
    }
  } else if (schema.type === 'array' && schema.items) {
    paths.add(prefix);
    const subPaths = extractPaths(schema.items, `${prefix}[]`);
    subPaths.forEach((path) => paths.add(path));
  } else {
    paths.add(prefix);
  }

  return paths;
}
