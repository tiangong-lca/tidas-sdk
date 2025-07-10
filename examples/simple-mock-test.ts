/**
 * Simple test to debug mock generation
 */

import { generateMock } from '@anatine/zod-mock';
import { z } from 'zod';
import { ContactsSchema } from '../src/schemas';

console.log('🔍 Simple Mock Test\n');

// Test 1: Simple schema
console.log('1. Testing simple schema...');
const simpleSchema = z.object({
  name: z.string(),
  email: z.string().email(),
  age: z.number().min(18)
});

try {
  const simpleMock = generateMock(simpleSchema);
  console.log('✅ Simple mock:', simpleMock);
} catch (error) {
  console.log('❌ Simple mock failed:', error.message);
}

// Test 2: TIDAS ContactsSchema directly
console.log('\n2. Testing TIDAS ContactsSchema...');
try {
  const tidasMock = generateMock(ContactsSchema, {
    stringMap: {
      'common:UUID': () => '123e4567-e89b-12d3-a456-426614174000',
      '#text': () => 'Mock Text',
      '@xml:lang': () => 'en',
      'email': () => 'mock@example.com'
    }
  });
  console.log('✅ TIDAS mock created');
  console.log('TIDAS mock keys:', Object.keys(tidasMock));
  if (tidasMock.contactDataSet) {
    console.log('contactDataSet keys:', Object.keys(tidasMock.contactDataSet));
  }
} catch (error) {
  console.log('❌ TIDAS mock failed:', error.message);
  console.log('Error stack:', error.stack);
}

// Test 3: Simplified TIDAS-like schema
console.log('\n3. Testing simplified TIDAS-like schema...');
const simplifiedTidasSchema = z.object({
  contactDataSet: z.object({
    '@xmlns': z.literal('http://lca.jrc.it/ILCD/Contact'),
    '@version': z.literal('1.1'),
    contactInformation: z.object({
      dataSetInformation: z.object({
        'common:UUID': z.string(),
        'common:name': z.object({
          '@xml:lang': z.string(),
          '#text': z.string()
        })
      })
    })
  })
});

try {
  const simplifiedMock = generateMock(simplifiedTidasSchema, {
    stringMap: {
      'common:UUID': () => '123e4567-e89b-12d3-a456-426614174000',
      '#text': () => 'Mock Contact Name',
      '@xml:lang': () => 'en',
      '@xmlns': () => 'http://lca.jrc.it/ILCD/Contact',
      '@version': () => '1.1'
    }
  });
  console.log('✅ Simplified TIDAS mock created');
  console.log('Simplified mock:', JSON.stringify(simplifiedMock, null, 2));
} catch (error) {
  console.log('❌ Simplified TIDAS mock failed:', error.message);
}