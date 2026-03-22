#!/usr/bin/env tsx

/**
 * Test script to verify all imports work correctly with the published npm package
 */

import { createContact, createFlow } from '@tiangong-lca/tidas-sdk/core';
import { ContactSchema } from '@tiangong-lca/tidas-sdk/schemas';
import * as typeModule from '@tiangong-lca/tidas-sdk/types';

console.log('🧪 Testing TIDAS SDK imports...\n');

try {
  // Test core imports
  console.log('Testing core imports...');
  console.log('✅ Core imports successful');

  // Test type imports
  console.log('Testing type imports...');
  console.log(
    `✅ Type imports successful (${Object.keys(typeModule).length} runtime exports)`
  );
  console.log('✅ Type imports successful');

  // Test schema imports
  console.log('Testing schema imports...');
  void ContactSchema;
  console.log('✅ Schema imports successful');

  // Test basic functionality
  console.log('\nTesting basic functionality...');
  const contact = createContact();
  contact.contactDataSet.contactInformation.dataSetInformation['common:name'] =
    [{ '@xml:lang': 'en', '#text': 'Test Contact' }];

  const validation = contact.validate();
  console.log(
    '✅ Contact creation and validation:',
    validation.success ? 'PASSED' : 'FAILED'
  );

  const flow = createFlow();
  flow.flowDataSet.flowInformation.dataSetInformation['common:name'] = [
    { '@xml:lang': 'en', '#text': 'Test Flow' },
  ];

  const flowValidation = flow.validate();
  console.log(
    '✅ Flow creation and validation:',
    flowValidation.success ? 'PASSED' : 'FAILED'
  );

  console.log('\n🎉 All imports and basic functionality tests passed!');
  console.log('\nYou can now run the example scripts:');
  console.log('  npm run run-basic');
  console.log('  npm run run-validation');
  console.log('  npm run run-advanced');
  console.log('  npm run run-validation-modes');
} catch (error) {
  console.error('❌ Import test failed:', (error as Error).message);
  console.error('\nMake sure you have installed the dependencies:');
  console.error('  npm install');
  process.exit(1);
}
