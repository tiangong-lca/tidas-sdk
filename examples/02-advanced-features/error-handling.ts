#!/usr/bin/env tsx

/**
 * Error Handling Patterns Example
 * 
 * This example demonstrates comprehensive error handling strategies
 * when working with TIDAS objects, including validation errors,
 * property access errors, and recovery mechanisms.
 */

import { createZodContact, createZodFlow } from '../../src/core/zod-factories';

console.log('🚨 TIDAS Error Handling Patterns Example\n');

// 1. Validation Error Handling
console.log('1. Validation Error Handling\n');

const contactResult = createZodContact({
  enableLogging: true,
  throwOnValidationError: false // We'll handle errors manually
});

const contact = contactResult.proxy;

console.log('   a) Handling incomplete object validation:');
// Create minimal object that will fail validation
contact.contactDataSet = {} as any;
contact.contactDataSet.contactInformation = {} as any;

const incompleteValidation = contactResult.validate();
if (!incompleteValidation.success) {
  console.log('   ❌ Validation failed as expected');
  console.log(`   Error count: ${incompleteValidation.error?.issues.length}`);
  
  // Group errors by type
  const errorTypes = incompleteValidation.error?.issues.reduce((acc: any, issue: any) => {
    acc[issue.code] = (acc[issue.code] || 0) + 1;
    return acc;
  }, {});
  
  console.log('   Error breakdown:');
  Object.entries(errorTypes).forEach(([code, count]) => {
    console.log(`   - ${code}: ${count} issues`);
  });
}

console.log('\n   b) Handling specific validation errors:');
contact.contactDataSet.contactInformation.dataSetInformation = {} as any;
contact.contactDataSet.contactInformation.dataSetInformation.email = 'invalid-email';

const emailValidation = contactResult.validate();
if (!emailValidation.success) {
  const emailErrors = emailValidation.error?.issues.filter((issue: any) => 
    issue.path.includes('email')
  );
  
  console.log('   Email-specific errors:');
  emailErrors?.forEach((error: any, index: number) => {
    console.log(`   ${index + 1}. ${error.message}`);
    console.log(`      Path: ${error.path.join('.')}`);
    console.log(`      Code: ${error.code}`);
  });
}

// 2. Property Access Error Handling
console.log('\n\n2. Property Access Error Handling\n');

console.log('   a) Safe property access patterns:');

// Method 1: Try-catch for property access
try {
  const safeEmail = contact.contactDataSet?.contactInformation?.dataSetInformation?.email;
  console.log(`   Email (safe access): ${safeEmail || 'Not set'}`);
} catch (error) {
  console.log('   ❌ Property access error:', (error as Error).message);
}

// Method 2: Defensive programming
function safeGetProperty(obj: any, path: string[]): any {
  try {
    return path.reduce((current, key) => current?.[key], obj);
  } catch (error) {
    console.log(`   ❌ Error accessing path ${path.join('.')}: ${(error as Error).message}`);
    return null;
  }
}

const safeName = safeGetProperty(contact, [
  'contactDataSet', 
  'contactInformation', 
  'dataSetInformation', 
  'common:name'
]);
console.log(`   Name (defensive access): ${safeName || 'Not set'}`);

// Method 3: Using object utilities with error handling
import { get } from '../../src/utils/object-utils';

console.log('\n   b) Using utility functions with error handling:');
try {
  const builtContact = contactResult.buildObject();
  const utilityEmail = get(builtContact, 'contactDataSet.contactInformation.dataSetInformation.email', 'Default email');
  console.log(`   Email (utility with default): ${utilityEmail}`);
} catch (error) {
  console.log('   ❌ Utility function error:', (error as Error).message);
}

// 3. Type Coercion and Conversion Errors
console.log('\n\n3. Type Coercion and Conversion Errors\n');

const flowResult = createZodFlow({
  enableLogging: true,
  throwOnValidationError: false
});

const flow = flowResult.proxy;

console.log('   a) Handling type mismatch errors:');

// Initialize structure
flow.flowDataSet = {} as any;
flow.flowDataSet.flowInformation = {} as any;
flow.flowDataSet.flowInformation.dataSetInformation = {} as any;

// Try to set wrong type (this should be handled gracefully)
try {
  // Attempt to set non-string value where string expected
  (flow.flowDataSet.flowInformation.dataSetInformation as any).CASNumber = 12345; // Should be string
  console.log('   ⚠️ Number set as CAS number (may cause validation issues)');
} catch (error) {
  console.log('   ✅ Type error caught:', (error as Error).message);
}

const typeValidation = flowResult.validate();
if (!typeValidation.success) {
  const typeErrors = typeValidation.error?.issues.filter((issue: any) => 
    issue.code === 'invalid_type'
  );
  
  if (typeErrors && typeErrors.length > 0) {
    console.log('   Type validation errors found:');
    typeErrors.forEach((error: any, index: number) => {
      console.log(`   ${index + 1}. Expected ${error.expected}, got ${error.received} at ${error.path.join('.')}`);
    });
  }
}

// 4. Error Recovery Strategies
console.log('\n\n4. Error Recovery Strategies\n');

console.log('   a) Automatic error correction:');

function autoCorrectContact(contactResult: any): { corrected: boolean; errors: string[] } {
  const errors: string[] = [];
  let corrected = false;
  
  const validation = contactResult.validate();
  if (!validation.success) {
    validation.error?.issues.forEach((issue: any) => {
      const path = issue.path.join('.');
      
      // Auto-correct common issues
      if (issue.code === 'invalid_string' && path.includes('email')) {
        if (issue.message.includes('Invalid email')) {
          // Set a default valid email
          contactResult.proxy.contactDataSet.contactInformation.dataSetInformation.email = 'corrected@example.com';
          errors.push(`Corrected invalid email to default value`);
          corrected = true;
        }
      }
      
      if (issue.code === 'required' && path.includes('common:UUID')) {
        contactResult.generateUUID('contactDataSet.contactInformation.dataSetInformation.common:UUID');
        errors.push('Generated missing UUID');
        corrected = true;
      }
      
      if (issue.code === 'required' && path.includes('common:name')) {
        contactResult.setMultiLangText(
          'contactDataSet.contactInformation.dataSetInformation.common:name',
          'Auto-generated Contact',
          'en'
        );
        errors.push('Set default contact name');
        corrected = true;
      }
    });
  }
  
  return { corrected, errors };
}

const recoveryResult = createZodContact({ enableLogging: true, throwOnValidationError: false });
const recoveryContact = recoveryResult.proxy;

// Create problematic object
recoveryContact.contactDataSet = {} as any;
recoveryContact.contactDataSet.contactInformation = {} as any;
recoveryContact.contactDataSet.contactInformation.dataSetInformation = {} as any;
recoveryContact.contactDataSet.contactInformation.dataSetInformation.email = 'bad-email';

console.log('   Initial validation status:', recoveryResult.validate().success ? 'PASS' : 'FAIL');

const recovery = autoCorrectContact(recoveryResult);
if (recovery.corrected) {
  console.log('   ✅ Auto-corrections applied:');
  recovery.errors.forEach((error, index) => {
    console.log(`   ${index + 1}. ${error}`);
  });
  
  const postRecoveryValidation = recoveryResult.validate();
  console.log('   Post-recovery validation:', postRecoveryValidation.success ? 'PASS' : 'FAIL');
} else {
  console.log('   No auto-corrections needed');
}

// 5. Custom Error Types and Handling
console.log('\n\n5. Custom Error Types and Handling\n');

class TidasValidationError extends Error {
  constructor(
    message: string,
    public path: string,
    public expectedType: string,
    public receivedValue: any
  ) {
    super(message);
    this.name = 'TidasValidationError';
  }
}

class TidasPropertyError extends Error {
  constructor(
    message: string,
    public property: string,
    public operation: 'get' | 'set'
  ) {
    super(message);
    this.name = 'TidasPropertyError';
  }
}

function validateWithCustomErrors(result: any): void {
  const validation = result.validate();
  
  if (!validation.success) {
    validation.error?.issues.forEach((issue: any) => {
      const path = issue.path.join('.');
      
      if (issue.code === 'invalid_type') {
        throw new TidasValidationError(
          issue.message,
          path,
          issue.expected,
          issue.received
        );
      }
      
      if (issue.code === 'invalid_string') {
        throw new TidasValidationError(
          issue.message,
          path,
          'valid string',
          issue.received
        );
      }
    });
  }
}

console.log('   Testing custom error types:');
try {
  const errorTestResult = createZodContact({ enableLogging: false, throwOnValidationError: false });
  const errorTestContact = errorTestResult.proxy;
  
  errorTestContact.contactDataSet = {} as any;
  errorTestContact.contactDataSet.contactInformation = {} as any;
  errorTestContact.contactDataSet.contactInformation.dataSetInformation = {} as any;
  errorTestContact.contactDataSet.contactInformation.dataSetInformation.email = 'invalid';
  
  validateWithCustomErrors(errorTestResult);
  console.log('   No custom errors thrown');
} catch (error) {
  if (error instanceof TidasValidationError) {
    console.log('   ✅ Custom validation error caught:');
    console.log(`   Type: ${error.name}`);
    console.log(`   Message: ${error.message}`);
    console.log(`   Path: ${error.path}`);
    console.log(`   Expected: ${error.expectedType}`);
  } else {
    console.log('   Unexpected error type:', error);
  }
}

// 6. Error Logging and Monitoring
console.log('\n\n6. Error Logging and Monitoring\n');

class ErrorLogger {
  private errors: Array<{
    timestamp: number;
    type: string;
    message: string;
    path?: string;
    context?: any;
  }> = [];
  
  logValidationError(validation: any, context: string) {
    if (!validation.success) {
      validation.error?.issues.forEach((issue: any) => {
        this.errors.push({
          timestamp: Date.now(),
          type: 'validation',
          message: issue.message,
          path: issue.path.join('.'),
          context
        });
      });
    }
  }
  
  logPropertyError(error: Error, property: string, operation: 'get' | 'set') {
    this.errors.push({
      timestamp: Date.now(),
      type: 'property',
      message: error.message,
      path: property,
      context: { operation }
    });
  }
  
  getErrorSummary() {
    const summary = this.errors.reduce((acc: any, error) => {
      acc[error.type] = (acc[error.type] || 0) + 1;
      return acc;
    }, {});
    
    return {
      total: this.errors.length,
      byType: summary,
      recent: this.errors.slice(-5)
    };
  }
  
  clearErrors() {
    this.errors = [];
  }
}

const errorLogger = new ErrorLogger();

console.log('   Testing error logging:');

const logTestResult = createZodContact({ enableLogging: false, throwOnValidationError: false });
const logTestContact = logTestResult.proxy;

// Generate some errors
logTestContact.contactDataSet = {} as any;
errorLogger.logValidationError(logTestResult.validate(), 'Initial incomplete object');

logTestContact.contactDataSet.contactInformation = {} as any;
logTestContact.contactDataSet.contactInformation.dataSetInformation = {} as any;
logTestContact.contactDataSet.contactInformation.dataSetInformation.email = 'invalid';
errorLogger.logValidationError(logTestResult.validate(), 'Invalid email set');

// Property access error simulation
try {
  throw new Error('Simulated property access error');
} catch (error) {
  errorLogger.logPropertyError(error as Error, 'contactDataSet.someProperty', 'get');
}

const summary = errorLogger.getErrorSummary();
console.log('   Error Summary:');
console.log(`   Total errors: ${summary.total}`);
console.log('   By type:', summary.byType);
console.log('   Recent errors:');
summary.recent.forEach((error, index) => {
  console.log(`   ${index + 1}. [${error.type}] ${error.message} (${error.path || 'no path'})`);
});

console.log('\n🎉 Error handling patterns example completed!');
console.log('\n📋 Error Handling Strategies Demonstrated:');
console.log('✅ Validation error analysis and categorization');
console.log('✅ Safe property access patterns');
console.log('✅ Type coercion error handling');
console.log('✅ Automatic error recovery strategies');
console.log('✅ Custom error types and throwing');
console.log('✅ Comprehensive error logging and monitoring');
console.log('✅ Defensive programming techniques');
console.log('✅ Error grouping and summary reporting');