import type { StringMultiLang, STMultiLang, FTMultiLang, GlobalReferenceType } from '../types/tidas_data_types';
import { get, set } from '../utils/object-utils';

/**
 * Type-aware helper methods for working with TIDAS data structures
 */
export class TypeAwareHelpers {
  /**
   * Extract text from multi-language string structure
   */
  static extractMultiLangText(
    multiLangText: StringMultiLang | STMultiLang | FTMultiLang | undefined,
    preferredLang: string = 'en'
  ): string {
    if (!multiLangText) return '';
    
    // Handle array format
    if (Array.isArray(multiLangText)) {
      // Try to find preferred language
      const preferred = multiLangText.find(item => item['@xml:lang'] === preferredLang);
      if (preferred) return preferred['#text'];
      
      // Fall back to first available
      return multiLangText[0]?.['#text'] || '';
    }
    
    // Handle single object format
    if (multiLangText['@xml:lang'] && multiLangText['#text']) {
      return multiLangText['#text'];
    }
    
    return '';
  }

  /**
   * Create or update multi-language string structure
   */
  static createOrUpdateMultiLangText(
    existing: StringMultiLang | STMultiLang | FTMultiLang | undefined,
    newText: string,
    lang: string = 'en'
  ): StringMultiLang {
    const newItem = { '@xml:lang': lang, '#text': newText };
    
    if (!existing) {
      return newItem;
    }
    
    // Handle array format
    if (Array.isArray(existing)) {
      const existingIndex = existing.findIndex(item => item['@xml:lang'] === lang);
      if (existingIndex >= 0) {
        const updated = [...existing];
        updated[existingIndex] = newItem;
        return updated;
      } else {
        return [...existing, newItem];
      }
    }
    
    // Handle single object format
    if (existing['@xml:lang'] === lang) {
      return newItem;
    } else {
      return [existing, newItem];
    }
  }

  /**
   * Extract reference information from GlobalReferenceType
   */
  static extractReferenceInfo(reference: GlobalReferenceType | undefined): {
    id: string;
    type: string;
    uri: string;
    version: string;
    description: string;
  } | null {
    if (!reference) return null;
    
    // Handle array format
    if (Array.isArray(reference)) {
      const ref = reference[0];
      if (!ref) return null;
      
      return {
        id: ref['@refObjectId'],
        type: ref['@type'],
        uri: ref['@uri'],
        version: ref['@version'],
        description: this.extractMultiLangText(ref['common:shortDescription'])
      };
    }
    
    // Handle single object format
    return {
      id: reference['@refObjectId'],
      type: reference['@type'],
      uri: reference['@uri'],
      version: reference['@version'],
      description: this.extractMultiLangText(reference['common:shortDescription'])
    };
  }

  /**
   * Create a GlobalReferenceType object
   */
  static createGlobalReference(options: {
    refObjectId: string;
    type: string;
    uri: string;
    version?: string;
    description: string;
    lang?: string;
  }): GlobalReferenceType {
    return {
      '@refObjectId': options.refObjectId,
      '@type': options.type,
      '@uri': options.uri,
      '@version': options.version || '01.00.000',
      'common:shortDescription': {
        '@xml:lang': options.lang || 'en',
        '#text': options.description
      }
    };
  }

  /**
   * Safely get nested property with type-aware fallback
   */
  static safeGet<T>(obj: any, path: string, defaultValue?: T): T {
    const result = get(obj, path, defaultValue);
    return result !== undefined ? result : defaultValue as T;
  }

  /**
   * Safely set nested property with type validation
   */
  static safeSet(obj: any, path: string, value: any): void {
    set(obj, path, value);
  }

  /**
   * Generate a UUID
   */
  static generateUUID(): string {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
      const r = Math.random() * 16 | 0;
      const v = c === 'x' ? r : (r & 0x3 | 0x8);
      return v.toString(16);
    });
  }

  /**
   * Get current ISO timestamp
   */
  static getCurrentTimestamp(): string {
    return new Date().toISOString();
  }

  /**
   * Validate UUID format
   */
  static isValidUUID(uuid: string): boolean {
    const uuidRegex = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
    return uuidRegex.test(uuid);
  }

  /**
   * Normalize language code
   */
  static normalizeLanguageCode(lang: string): string {
    return lang.toLowerCase().substring(0, 2);
  }

  /**
   * Deep clone with type preservation
   */
  static deepClone<T>(obj: T): T {
    if (obj === null || typeof obj !== 'object') {
      return obj;
    }

    if (obj instanceof Date) {
      return new Date(obj.getTime()) as any;
    }

    if (obj instanceof Array) {
      return obj.map(item => this.deepClone(item)) as any;
    }

    if (typeof obj === 'object') {
      const cloned = {} as any;
      for (const key in obj) {
        if (Object.prototype.hasOwnProperty.call(obj, key)) {
          cloned[key] = this.deepClone(obj[key]);
        }
      }
      return cloned;
    }

    return obj;
  }

  /**
   * Compare two objects for deep equality
   */
  static deepEquals(obj1: any, obj2: any): boolean {
    if (obj1 === obj2) return true;
    
    if (obj1 === null || obj2 === null) return false;
    if (typeof obj1 !== typeof obj2) return false;
    
    if (typeof obj1 !== 'object') return obj1 === obj2;
    
    if (Array.isArray(obj1) !== Array.isArray(obj2)) return false;
    
    if (Array.isArray(obj1)) {
      if (obj1.length !== obj2.length) return false;
      for (let i = 0; i < obj1.length; i++) {
        if (!this.deepEquals(obj1[i], obj2[i])) return false;
      }
      return true;
    }
    
    const keys1 = Object.keys(obj1);
    const keys2 = Object.keys(obj2);
    
    if (keys1.length !== keys2.length) return false;
    
    for (const key of keys1) {
      if (!keys2.includes(key)) return false;
      if (!this.deepEquals(obj1[key], obj2[key])) return false;
    }
    
    return true;
  }

  /**
   * Extract all multi-language texts from an object
   */
  static extractAllMultiLangTexts(obj: any): { path: string; texts: Array<{ lang: string; text: string }> }[] {
    const results: { path: string; texts: Array<{ lang: string; text: string }> }[] = [];
    
    const extract = (current: any, currentPath: string = '') => {
      if (current && typeof current === 'object') {
        // Check if this is a multi-language structure
        if (current['@xml:lang'] && current['#text']) {
          results.push({
            path: currentPath,
            texts: [{ lang: current['@xml:lang'], text: current['#text'] }]
          });
        } else if (Array.isArray(current) && current.length > 0 && current[0]['@xml:lang']) {
          results.push({
            path: currentPath,
            texts: current.map(item => ({ lang: item['@xml:lang'], text: item['#text'] }))
          });
        } else {
          // Recurse into object properties
          for (const [key, value] of Object.entries(current)) {
            const newPath = currentPath ? `${currentPath}.${key}` : key;
            extract(value, newPath);
          }
        }
      }
    };
    
    extract(obj);
    return results;
  }

  /**
   * Update all multi-language texts in an object for a specific language
   */
  static updateAllMultiLangTexts(
    obj: any,
    updates: { path: string; text: string }[],
    lang: string = 'en'
  ): any {
    const result = this.deepClone(obj);
    
    for (const update of updates) {
      const current = get(result, update.path);
      if (current) {
        const updated = this.createOrUpdateMultiLangText(current, update.text, lang);
        set(result, update.path, updated);
      }
    }
    
    return result;
  }
}