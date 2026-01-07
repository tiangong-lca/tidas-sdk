#!/usr/bin/env tsx

/**
 * LifeCycle Model Validation Demo
 * 
 * This example demonstrates:
 * 1. Deep validation for nested fields (enabled by default)
 * 2. How validation detects missing required fields in nested structures
 * 3. Different validation modes (strict, weak, ignore)
 */

import { readFileSync } from 'fs';
import { join } from 'path';
import { createLifeCycleModel } from '@tiangong-lca/tidas-sdk/core';

console.log('=== LifeCycle Model Validation Demo ===\n');

// Load test data with incomplete name field
const testDataPath = join(__dirname, '../../../../test-data/tidas-example-model.json');
const exampleData = JSON.parse(readFileSync(testDataPath, 'utf-8'));

console.log('Current name structure in test data:');
console.log(JSON.stringify(
  exampleData.lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.name,
  null,
  2
));
console.log('\nNote: Missing required fields "treatmentStandardsRoutes" and "mixAndLocationTypes"\n');

// =============================================================================
// Test 1: Default validation (strict mode with deep validation enabled)
// =============================================================================
console.log('─'.repeat(70));
console.log('Test 1: Default Validation (strict + deepValidation)');
console.log('─'.repeat(70));

const model1 = createLifeCycleModel(exampleData);
const result1 = model1.validateEnhanced();

console.log(`\nValidation result: ${result1.success ? '✅ PASSED' : '❌ FAILED'}`);

if (!result1.success) {
  console.log(`Total errors found: ${result1.error.issues.length}\n`);
  
  // Show all errors
  console.log('All validation errors:');
  result1.error.issues.forEach((err, idx) => {
    console.log(`  ${idx + 1}. ${err.path.join('.')}`);
    console.log(`     → ${err.message}`);
  });
  
  // Highlight name field errors
  const nameErrors = result1.error.issues.filter(issue =>
    issue.path.includes('treatmentStandardsRoutes') ||
    issue.path.includes('mixAndLocationTypes')
  );
  
  if (nameErrors.length > 0) {
    console.log(`\n✅ Deep validation detected ${nameErrors.length} missing name field(s):`);
    nameErrors.forEach(err => {
      console.log(`  • ${err.path.slice(-1)[0]}`);
    });
  }
}

// =============================================================================
// Test 2: Weak validation mode
// =============================================================================
console.log('\n' + '─'.repeat(70));
console.log('Test 2: Weak Validation Mode');
console.log('─'.repeat(70));

const model2 = createLifeCycleModel(exampleData, { 
  mode: 'weak',
  includeWarnings: true
});
const result2 = model2.validateEnhanced();

console.log(`\nValidation result: ${result2.success ? '✅ PASSED' : '❌ FAILED'}`);

if (result2.success) {
  console.log('Weak mode allows non-critical validation issues');
  if (result2.warnings && result2.warnings.length > 0) {
    console.log(`\nWarnings (${result2.warnings.length}):`);
    result2.warnings.forEach((warn, idx) => {
      console.log(`  ${idx + 1}. [${warn.severity}] ${warn.path.join('.')}`);
      console.log(`     → ${warn.message}`);
    });
  }
} else {
  console.log(`Critical errors found: ${result2.error.issues.length}`);
  console.log('Even weak mode rejects data with critical validation errors');
}

// =============================================================================
// Test 3: Validation with complete name fields
// =============================================================================
console.log('\n' + '─'.repeat(70));
console.log('Test 3: Validation with Complete Name Fields');
console.log('─'.repeat(70));

// Add missing required fields
const completeData = JSON.parse(JSON.stringify(exampleData));
completeData.lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.name = {
  baseName: {
    '#text': 'Example Model',
    '@xml:lang': 'en'
  },
  treatmentStandardsRoutes: {
    '#text': 'Standard treatment',
    '@xml:lang': 'en'
  },
  mixAndLocationTypes: {
    '#text': 'Production mix, at plant',
    '@xml:lang': 'en'
  }
};

const model3 = createLifeCycleModel(completeData);
const result3 = model3.validateEnhanced();

console.log(`\nValidation result: ${result3.success ? '✅ PASSED' : '❌ FAILED'}`);

// Check specifically for name field errors
const nameErrors3 = result3.success ? [] : result3.error.issues.filter(issue =>
  issue.path.includes('treatmentStandardsRoutes') ||
  issue.path.includes('mixAndLocationTypes')
);

console.log(`Name field errors: ${nameErrors3.length}`);

if (nameErrors3.length === 0) {
  console.log('✅ All name fields are now valid!');
  console.log('\nCompleted name structure:');
  console.log(JSON.stringify(
    completeData.lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.name,
    null,
    2
  ));

  if (!result3.success) {
    console.log(`\nNote: There are ${result3.error.issues.length} other validation errors unrelated to name fields.`);
  }
} else {
  console.log('Name field errors still present:');
  nameErrors3.forEach(err => {
    console.log(`  • ${err.path.join('.')}: ${err.message}`);
  });
}

// =============================================================================
// Test 4: Disable deep validation
// =============================================================================
console.log('\n' + '─'.repeat(70));
console.log('Test 4: Standard Validation (deepValidation disabled)');
console.log('─'.repeat(70));

const model4 = createLifeCycleModel(exampleData, {
  mode: 'strict',
  deepValidation: false
});
const result4 = model4.validateEnhanced();

console.log(`\nValidation result: ${result4.success ? '✅ PASSED' : '❌ FAILED'}`);

if (!result4.success) {
  console.log(`Errors found: ${result4.error.issues.length}`);
  
  // Compare with deep validation
  const nameErrorsCount = result4.error.issues.filter(issue =>
    issue.path.includes('treatmentStandardsRoutes') ||
    issue.path.includes('mixAndLocationTypes')
  ).length;
  
  console.log(`\nName field errors: ${nameErrorsCount}`);
  console.log('Note: With fixed StringMultiLangSchema, name errors are detected');
  console.log('even without deep validation enabled.');
}

// =============================================================================
// Summary
// =============================================================================
console.log('\n' + '='.repeat(70));
console.log('Summary');
console.log('='.repeat(70));

console.log('\n✅ Key Features Demonstrated:');
console.log('  1. Deep validation is enabled by default');
console.log('  2. Detects missing required fields in nested structures');
console.log('  3. Weak validation mode for non-critical errors');
console.log('  4. StringMultiLangSchema properly validates required fields');

console.log('\n💡 Configuration Options:');
console.log('  • Default: { mode: "strict", deepValidation: true }');
console.log('  • Environment: TIDAS_DEEP_VALIDATION=false to disable');
console.log('  • Per-model: createLifeCycleModel(data, { deepValidation: false })');

console.log('\n=== Demo Completed ===\n');
