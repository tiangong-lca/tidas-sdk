/**
 * Test official @anatine/zod-mock example
 */

import { generateMock } from '@anatine/zod-mock';
import { z } from 'zod';

console.log('🧪 Testing Official @anatine/zod-mock Example\n');

const schema = z.object({
  uid: z.string().nonempty(),
  theme: z.enum(['light', 'dark']),
  email: z.string().email().optional(),
  phoneNumber: z.string().min(10).optional(),
  avatar: z.string().url().optional(),
  jobTitle: z.string().optional(),
  otherUserEmails: z.array(z.string().email()),
  stringArrays: z.array(z.string()),
  stringLength: z.string().transform((val) => val.length),
  numberCount: z.number().transform((item) => `total value = ${item}`),
  age: z.number().min(18).max(120),
});

try {
  console.log('Generating mock data...');
  const mockData = generateMock(schema);
  console.log('✅ Mock data generated successfully:');
  console.log(JSON.stringify(mockData, null, 2));
  
  console.log('\nTesting with custom stringMap...');
  const customMockData = generateMock(schema, {
    stringMap: {
      email: () => 'custom@example.com',
      phoneNumber: () => '+1-555-123-4567'
    }
  });
  console.log('✅ Custom mock data generated:');
  console.log(JSON.stringify(customMockData, null, 2));
  
} catch (error) {
  console.error('❌ Mock generation failed:', error.message);
  console.error('Stack:', error.stack);
}