#!/usr/bin/env tsx

/**
 * Validation Modes Example
 * 
 * This example demonstrates different validation configurations
 * and error handling strategies in the TIDAS SDK.
 */

import { createZodContact } from '../../src/core/zod-factories';

console.log('✅ TIDAS Validation Modes Example\n');

// 1. Strict Validation Mode (throws on error)
console.log('1. Strict Validation Mode (throws on validation error)\n');

const strictResult = createZodContact({
  enableLogging: true,
  throwOnValidationError: true,
  defaultLanguage: 'en'
});

const strictContact = strictResult.proxy;

// Initialize structure
strictContact.contactDataSet = {} as any;
strictContact.contactDataSet.contactInformation = {} as any;
strictContact.contactDataSet.contactInformation.dataSetInformation = {} as any;

console.log('   Setting valid data:');
try {
  strictContact.contactDataSet.contactInformation.dataSetInformation.email = 'valid@example.com';
  console.log('   ✅ Valid email accepted');
} catch (error) {
  console.log('   ❌ Unexpected error:', error);
}

console.log('\n   Attempting invalid data:');
try {
  strictContact.contactDataSet.contactInformation.dataSetInformation.email = 'invalid-email';
  console.log('   ⚠️ Invalid email was accepted (validation may not be working)');
} catch (error) {
  console.log('   ✅ Invalid email properly rejected');
  console.log('   Error:', (error as Error).message);
}

// 2. Lenient Validation Mode (logs but doesn't throw)
console.log('\n\n2. Lenient Validation Mode (logs errors but continues)\n');

const lenientResult = createZodContact({
  enableLogging: true,
  throwOnValidationError: false,
  defaultLanguage: 'en'
});

const lenientContact = lenientResult.proxy;

// Initialize structure
lenientContact.contactDataSet = {} as any;
lenientContact.contactDataSet.contactInformation = {} as any;
lenientContact.contactDataSet.contactInformation.dataSetInformation = {} as any;

console.log('   Setting valid data:');
lenientContact.contactDataSet.contactInformation.dataSetInformation.email = 'valid@example.com';
console.log('   ✅ Valid email accepted');

console.log('\n   Setting invalid data:');
lenientContact.contactDataSet.contactInformation.dataSetInformation.email = 'invalid-email';
console.log('   ✅ Invalid email was set (validation warnings may appear in console)');

// Check validation status
const lenientValidation = lenientResult.validate();
if (!lenientValidation.success) {
  console.log('   ❌ Object validation failed as expected');
  console.log('   Issues found:', lenientValidation.error?.issues.length);
}

// 3. Validation with Custom Options
console.log('\n\n3. Custom Validation Configuration\n');

const customResult = createZodContact({
  enableLogging: true,
  throwOnValidationError: false,
  autoCreateArrays: true,
  autoGenerateUUID: true,
  autoGenerateTimestamp: true,
  defaultLanguage: 'en'
});

const customContact = customResult.proxy;

console.log('   Auto-features enabled:');
console.log('   - Auto-create arrays: ✅');
console.log('   - Auto-generate UUID: ✅');
console.log('   - Auto-generate timestamp: ✅');

// Initialize minimal structure
customContact.contactDataSet = {} as any;
customContact.contactDataSet.contactInformation = {} as any;
customContact.contactDataSet.contactInformation.dataSetInformation = {} as any;

// Basic data
customContact.contactDataSet.contactInformation.dataSetInformation.email = 'custom@example.com';

// Use auto-generation features
customResult.generateUUID('contactDataSet.contactInformation.dataSetInformation.common:UUID');
customResult.setCurrentTimestamp('contactDataSet.administrativeInformation.dataEntryBy.common:timeStamp');

console.log('   ✅ Auto-features utilized');

// 4. Manual Validation and Error Analysis
console.log('\n\n4. Manual Validation and Error Analysis\n');

const manualResult = createZodContact({
  enableLogging: true,
  throwOnValidationError: false
});

const manualContact = manualResult.proxy;

// Create intentionally incomplete/invalid object
manualContact.contactDataSet = {} as any;
manualContact.contactDataSet.contactInformation = {} as any;
manualContact.contactDataSet.contactInformation.dataSetInformation = {} as any;

// Set some invalid data
manualContact.contactDataSet.contactInformation.dataSetInformation.email = 'not-an-email';
manualContact.contactDataSet.contactInformation.dataSetInformation.WWWAddress = 'not-a-url';

console.log('   Manually validating incomplete object:');
const manualValidation = manualResult.validate();

if (!manualValidation.success) {
  console.log('   ❌ Validation failed (as expected)');
  console.log('   \n   Detailed error analysis:');
  
  manualValidation.error?.issues.forEach((issue: any, index: number) => {
    console.log(`   ${index + 1}. Path: ${issue.path.join('.')}`);
    console.log(`      Code: ${issue.code}`);
    console.log(`      Message: ${issue.message}`);
    if (issue.received) {
      console.log(`      Received: ${issue.received}`);
    }
    if (issue.expected) {
      console.log(`      Expected: ${issue.expected}`);
    }
    console.log();
  });
} else {
  console.log('   ✅ Validation passed unexpectedly');
}

// 5. Validation Recovery Patterns
console.log('\n\n5. Validation Recovery Patterns\n');

const recoveryResult = createZodContact({
  enableLogging: true,
  throwOnValidationError: false
});

const recoveryContact = recoveryResult.proxy;

// Start with invalid data
recoveryContact.contactDataSet = {} as any;
recoveryContact.contactDataSet.contactInformation = {} as any;
recoveryContact.contactDataSet.contactInformation.dataSetInformation = {} as any;

console.log('   a) Setting invalid email:');
recoveryContact.contactDataSet.contactInformation.dataSetInformation.email = 'invalid';

const firstValidation = recoveryResult.validate();
console.log(`   Initial validation: ${firstValidation.success ? 'PASS' : 'FAIL'}`);

console.log('\n   b) Correcting the email:');
recoveryContact.contactDataSet.contactInformation.dataSetInformation.email = 'corrected@example.com';

const secondValidation = recoveryResult.validate();
console.log(`   After correction: ${secondValidation.success ? 'PASS' : 'FAIL'}`);

console.log('\n   c) Adding required fields:');
recoveryResult.generateUUID('contactDataSet.contactInformation.dataSetInformation.common:UUID');
recoveryResult.setMultiLangText(
  'contactDataSet.contactInformation.dataSetInformation.common:name',
  'Recovery Contact',
  'en'
);

const finalValidation = recoveryResult.validate();
console.log(`   Final validation: ${finalValidation.success ? 'PASS' : 'FAIL'}`);

if (!finalValidation.success) {
  console.log('   Remaining issues:');
  finalValidation.error?.issues.slice(0, 3).forEach((issue: any, index: number) => {
    console.log(`   ${index + 1}. ${issue.message} at ${issue.path.join('.')}`);
  });
}

// 6. Validation Best Practices
console.log('\n\n6. Validation Best Practices\n');

const bestPracticeResult = createZodContact({
  enableLogging: true,
  throwOnValidationError: false,
  defaultLanguage: 'en'
});

const bestPracticeContact = bestPracticeResult.proxy;

console.log('   Best Practice 1: Validate incrementally');
// Build object step by step, validating at each major step

// Step 1: Basic structure
bestPracticeContact.contactDataSet = {} as any;
bestPracticeContact.contactDataSet.contactInformation = {} as any;
bestPracticeContact.contactDataSet.contactInformation.dataSetInformation = {} as any;

// Step 2: Required identification
bestPracticeResult.generateUUID('contactDataSet.contactInformation.dataSetInformation.common:UUID');
bestPracticeResult.setMultiLangText(
  'contactDataSet.contactInformation.dataSetInformation.common:name',
  'Best Practice Contact',
  'en'
);

const step1Validation = bestPracticeResult.validate();
console.log(`   After basic info: ${step1Validation.success ? 'PASS' : 'FAIL'}`);

// Step 3: Contact details
bestPracticeContact.contactDataSet.contactInformation.dataSetInformation.email = 'bestpractice@example.com';
bestPracticeContact.contactDataSet.contactInformation.dataSetInformation.telephone = '+1-555-BEST';
bestPracticeContact.contactDataSet.contactInformation.dataSetInformation.WWWAddress = 'https://bestpractice.example.com';

const step2Validation = bestPracticeResult.validate();
console.log(`   After contact details: ${step2Validation.success ? 'PASS' : 'FAIL'}`);

// Step 4: Administrative info
bestPracticeContact.contactDataSet.administrativeInformation = {} as any;
bestPracticeContact.contactDataSet.administrativeInformation.dataEntryBy = {} as any;
bestPracticeResult.setCurrentTimestamp('contactDataSet.administrativeInformation.dataEntryBy.common:timeStamp');

const finalBestPracticeValidation = bestPracticeResult.validate();
console.log(`   Final validation: ${finalBestPracticeValidation.success ? 'PASS' : 'FAIL'}`);

console.log('\n   Best Practice 2: Use helper functions for consistency');
console.log('   ✅ Used generateUUID() for proper UUID format');
console.log('   ✅ Used setMultiLangText() for internationalization');
console.log('   ✅ Used setCurrentTimestamp() for proper timestamp format');

console.log('\n   Best Practice 3: Handle validation errors gracefully');
if (!finalBestPracticeValidation.success) {
  console.log('   Remaining validation issues to address:');
  finalBestPracticeValidation.error?.issues.forEach((issue: any, index: number) => {
    if (index < 5) { // Limit to first 5 issues
      console.log(`   - ${issue.message} (${issue.path.join('.')})`);
    }
  });
  if (finalBestPracticeValidation.error?.issues.length! > 5) {
    console.log(`   - ... and ${finalBestPracticeValidation.error?.issues.length! - 5} more issues`);
  }
}

// 7. Performance Impact of Validation
console.log('\n\n7. Performance Impact of Validation\n');

console.log('   Measuring validation performance...');

const perfResult = createZodContact({
  enableLogging: false, // Disable logging for performance test
  throwOnValidationError: false
});

const perfContact = perfResult.proxy;

const startTime = performance.now();

// Perform many operations
for (let i = 0; i < 100; i++) {
  perfContact.contactDataSet = {} as any;
  perfContact.contactDataSet.contactInformation = {} as any;
  perfContact.contactDataSet.contactInformation.dataSetInformation = {} as any;
  perfContact.contactDataSet.contactInformation.dataSetInformation.email = `test${i}@example.com`;
}

const endTime = performance.now();
const duration = endTime - startTime;

console.log(`   100 operations completed in ${duration.toFixed(2)}ms`);
console.log(`   Average per operation: ${(duration / 100).toFixed(3)}ms`);

const validationStartTime = performance.now();
const perfValidation = perfResult.validate();
const validationEndTime = performance.now();
const validationDuration = validationEndTime - validationStartTime;

console.log(`   Final validation took: ${validationDuration.toFixed(2)}ms`);
console.log(`   Validation result: ${perfValidation.success ? 'PASS' : 'FAIL'}`);

console.log('\n🎉 Validation modes example completed!');
console.log('\n📋 Validation Strategies Demonstrated:');
console.log('✅ Strict validation (throws on error)');
console.log('✅ Lenient validation (logs warnings)');
console.log('✅ Custom validation configuration');
console.log('✅ Manual validation and error analysis');
console.log('✅ Validation recovery patterns');
console.log('✅ Incremental validation best practices');
console.log('✅ Performance considerations');
console.log('✅ Graceful error handling');