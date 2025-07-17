/**
 * Comprehensive Validation Configuration Demo
 *
 * This example demonstrates the new validation configuration options:
 * - Strict validation (default behavior)
 * - Weak validation (warnings for non-critical issues)
 * - Ignore validation (skip validation entirely)
 * - Global configuration management
 * - Per-entity configuration override
 */

import {
  createContact,
  createFlow,
  createProcess,
  createContactsBatch,
} from '@tiangong-lca/tidas-sdk/core';

import {
  setGlobalValidationMode,
  getGlobalValidationMode,
  setGlobalValidationConfig,
  resetGlobalConfig,
} from '@tiangong-lca/tidas-sdk/core';

console.log('=== TIDAS Validation Configuration Demo ===\n');

// Example 1: Default Strict Validation
console.log('1. DEFAULT STRICT VALIDATION');
console.log('Current global validation mode:', getGlobalValidationMode());

const strictContact = createContact();
strictContact.contactDataSet.contactInformation.dataSetInformation[
  'common:name'
] = { '@xml:lang': 'en', '#text': 'Dr. Strict Validation' };

const strictValidation = strictContact.validate();
const strictEnhanced = strictContact.validateEnhanced();

console.log(
  'Strict validation result:',
  strictValidation.success ? 'PASSED' : 'FAILED'
);
console.log('Enhanced validation mode:', strictEnhanced.mode);
console.log(
  'Enhanced validation warnings:',
  strictEnhanced.warnings?.length || 0
);
console.log();

// Example 2: Per-Entity Weak Validation
console.log('2. PER-ENTITY WEAK VALIDATION');

const weakContact = createContact({}, { mode: 'weak', includeWarnings: true });
weakContact.contactDataSet.contactInformation.dataSetInformation[
  'common:name'
] = [{ '@xml:lang': 'en', '#text': 'Dr. Weak Validation' }];

// Set some potentially problematic data
weakContact.contactDataSet.contactInformation.dataSetInformation.email =
  'invalid-email'; // Invalid format
weakContact.contactDataSet.contactInformation.dataSetInformation.WWWAddress =
  'not-a-url'; // Invalid URL

const weakValidation = weakContact.validate();
const weakEnhanced = weakContact.validateEnhanced();

console.log(
  'Weak validation result:',
  weakValidation.success ? 'PASSED' : 'FAILED'
);
console.log('Enhanced validation mode:', weakEnhanced.mode);
console.log(
  'Enhanced validation warnings:',
  weakEnhanced.warnings?.length || 0
);

if (weakEnhanced.warnings && weakEnhanced.warnings.length > 0) {
  console.log('Validation warnings:');
  weakEnhanced.warnings.forEach((warning, index) => {
    console.log(
      `  ${index + 1}. [${warning.severity.toUpperCase()}] ${warning.path.join('.')}: ${warning.message}`
    );
  });
}
console.log();

// Example 3: Ignore Validation for Performance
console.log('3. IGNORE VALIDATION MODE');

const ignoreContact = createContact({}, { mode: 'ignore' });
// Note: Even with invalid data, ignore mode will always pass
ignoreContact.contactDataSet.contactInformation.dataSetInformation[
  'common:name'
] = [{ '@xml:lang': 'en', '#text': 'Ignore Validation Demo' }];

const ignoreValidation = ignoreContact.validate();
const ignoreEnhanced = ignoreContact.validateEnhanced();

console.log(
  'Ignore validation result:',
  ignoreValidation.success ? 'PASSED' : 'FAILED'
);
console.log('Enhanced validation mode:', ignoreEnhanced.mode);
console.log('Data processing time: instantaneous (no validation performed)');
console.log();

// Example 4: Global Configuration Management
console.log('4. GLOBAL CONFIGURATION MANAGEMENT');

// Set global weak validation
setGlobalValidationMode('weak');
console.log('Set global validation mode to: weak');

const globalWeakContact = createContact(); // Uses global config
globalWeakContact.contactDataSet.contactInformation.dataSetInformation[
  'common:name'
] = [{ '@xml:lang': 'en', '#text': 'Global Weak Config' }];

const globalValidation = globalWeakContact.validateEnhanced();
console.log('Global config validation mode:', globalValidation.mode);

// Override global config for specific entity
const overrideContact = createContact({}, { mode: 'strict' }); // Override to strict
const overrideValidation = overrideContact.validateEnhanced();
console.log('Override validation mode:', overrideValidation.mode);

// Reset global config
resetGlobalConfig();
console.log('Reset to default global config');
console.log('Current global validation mode:', getGlobalValidationMode());
console.log();

// Example 5: Runtime Configuration Changes
console.log('5. RUNTIME CONFIGURATION CHANGES');

const runtimeContact = createContact();
console.log(
  'Initial validation mode:',
  runtimeContact.getValidationConfig().mode
);

// Change validation mode at runtime
runtimeContact.setValidationMode('weak');
console.log(
  'Changed to validation mode:',
  runtimeContact.getValidationConfig().mode
);

// Change complete validation config
runtimeContact.setValidationConfig({
  mode: 'ignore',
  includeWarnings: false,
});
console.log('Updated validation config:', runtimeContact.getValidationConfig());
console.log();

// Example 6: Batch Operations with Validation Config
console.log('6. BATCH OPERATIONS WITH VALIDATION CONFIG');

const batchData = [
  {}, // Empty data for contact 1
  {}, // Empty data for contact 2
  {}, // Empty data for contact 3
];

// Create batch with weak validation
const weakBatchContacts = createContactsBatch(batchData, { mode: 'weak' });

console.log(
  `Created ${weakBatchContacts.length} contacts with weak validation`
);
weakBatchContacts.forEach((contact, index) => {
  const validation = contact.validateEnhanced();
  console.log(
    `Contact ${index + 1}: ${validation.mode} mode, ${validation.success ? 'valid' : 'invalid'}`
  );
});
console.log();

// Example 7: Performance Comparison
console.log('7. PERFORMANCE COMPARISON');

const performanceTestData = Array(100).fill({});

// Test strict validation performance
const strictStartTime = performance.now();
const strictBatch = createContactsBatch(performanceTestData, {
  mode: 'strict',
});
const strictResults = strictBatch.map((contact) => contact.validate());
const strictEndTime = performance.now();

// Test weak validation performance
const weakStartTime = performance.now();
const weakBatch = createContactsBatch(performanceTestData, { mode: 'weak' });
const weakResults = weakBatch.map((contact) => contact.validate());
const weakEndTime = performance.now();

// Test ignore validation performance
const ignoreStartTime = performance.now();
const ignoreBatch = createContactsBatch(performanceTestData, {
  mode: 'ignore',
});
const ignoreResults = ignoreBatch.map((contact) => contact.validate());
const ignoreEndTime = performance.now();

console.log(
  `Strict validation (100 entities): ${(strictEndTime - strictStartTime).toFixed(2)}ms`
);
console.log(
  `Weak validation (100 entities): ${(weakEndTime - weakStartTime).toFixed(2)}ms`
);
console.log(
  `Ignore validation (100 entities): ${(ignoreEndTime - ignoreStartTime).toFixed(2)}ms`
);

const strictSuccessRate = strictResults.filter((r) => r.success).length;
const weakSuccessRate = weakResults.filter((r) => r.success).length;
const ignoreSuccessRate = ignoreResults.filter((r) => r.success).length;

console.log(
  `Success rates - Strict: ${strictSuccessRate}/100, Weak: ${weakSuccessRate}/100, Ignore: ${ignoreSuccessRate}/100`
);
console.log();

// Example 8: Multi-Entity Type Configuration
console.log('8. MULTI-ENTITY TYPE CONFIGURATION');

// Create different entity types with different validation modes
const entities = [
  { type: 'Contact', entity: createContact({}, { mode: 'strict' }) },
  { type: 'Flow', entity: createFlow({}, { mode: 'weak' }) },
  { type: 'Process', entity: createProcess({}, { mode: 'ignore' }) },
];

entities.forEach(({ type, entity }) => {
  const validation = entity.validateEnhanced();
  console.log(`${type}: ${validation.mode} validation mode`);
});
console.log();

// Example 9: Error Categorization Demo
console.log('9. ERROR CATEGORIZATION DEMO');

const errorTestContact = createContact(
  {},
  { mode: 'weak', includeWarnings: true }
);

// Create data with various types of validation issues
errorTestContact.contactDataSet.contactInformation.dataSetInformation[
  'common:name'
] = [
  { '@xml:lang': 'en', '#text': '' }, // Empty name (could be critical or warning)
];

errorTestContact.contactDataSet.contactInformation.dataSetInformation.email =
  'invalid-email-format';
errorTestContact.contactDataSet.contactInformation.dataSetInformation.telefax =
  'abc123'; // Invalid phone format

const errorValidation = errorTestContact.validateEnhanced();

console.log(
  'Error categorization result:',
  errorValidation.success ? 'PASSED' : 'FAILED'
);
if (errorValidation.warnings) {
  console.log('Categorized issues:');
  errorValidation.warnings.forEach((warning, index) => {
    console.log(
      `  ${index + 1}. [${warning.severity.toUpperCase()}] ${warning.code}: ${warning.message}`
    );
    console.log(`     Path: ${warning.path.join('.')}`);
  });
}
console.log();

console.log('=== Validation Configuration Demo Complete! ===');
console.log('\nKey Features Demonstrated:');
console.log('✅ Strict validation (default) - Full schema validation');
console.log('✅ Weak validation - Non-critical issues become warnings');
console.log('✅ Ignore validation - Skip validation for performance');
console.log('✅ Global configuration management');
console.log('✅ Per-entity configuration override');
console.log('✅ Runtime configuration changes');
console.log('✅ Batch operations with validation config');
console.log('✅ Performance optimization options');
console.log('✅ Error categorization and warning system');
console.log('✅ Backward compatibility maintained');
