import { TidasContact } from '../entities/TidasContact';
import { Contact } from '../../types';

/**
 * Factory functions for creating TIDAS entities
 */

/**
 * Create a new TIDAS Contact entity
 */
export function createContact(data?: Partial<Contact>): TidasContact {
  return new TidasContact(data);
}

/**
 * Create a contact from JSON data
 */
export function createContactFromJSON(jsonData: string | object): TidasContact {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  return createContact(data);
}

/**
 * Create multiple contacts from an array of data
 */
export function createContactsBatch(dataArray: Array<Partial<Contact>>): TidasContact[] {
  return dataArray.map(data => createContact(data));
}

// Export entity classes
export { TidasContact } from '../entities/TidasContact';

// Export base classes
export { TidasEntity } from '../base/TidasEntity';
export type { ValidationResult } from '../base/TidasEntity';