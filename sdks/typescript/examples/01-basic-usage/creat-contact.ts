/**
 * Usage example for creating a Contact object using the TIDAS SDK.
 *
 * npx tsx 01-basic-usage/creat-contact.ts
 */
import { createContact } from '@tiangong-lca/tidas-sdk';

import { readFileSync } from 'fs';
import { join } from 'path';
const testDataPath = join(
  __dirname,
  '../../../../test-data/tidas-example-contact.json'
);
const exampleData = JSON.parse(readFileSync(testDataPath, 'utf-8'));

console.log('=== Create Contact Demo ===\n');

const contact = createContact(exampleData);

console.log('Contact created successfully:');
console.log(JSON.stringify(contact.toJSON(), null, 2));
