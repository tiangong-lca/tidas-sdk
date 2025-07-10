/**
 * Path Validation System Demo
 * 
 * This example demonstrates how to use the path validation system
 * to prevent common path mistakes and get helpful suggestions.
 */

import { 
  createTypedContact, 
  createTypedFlow, 
  createTypedProcess,
  type PathValidationConfig 
} from '../src/core/typed-accessors';
import { 
  CONTACT_PATHS, 
  FLOW_PATHS, 
  PROCESS_PATHS 
} from '../src/core/typed-path-helpers';
import { setGlobalPathValidatorConfig } from '../src/core/path-validator';

console.log('=== Path Validation System Demo ===\n');

// 1. Basic Usage - Non-strict Mode (Default)
console.log('1. Basic Usage - Non-strict Mode (Default)');
const contact = createTypedContact();

// This will work but show a warning
console.log('Setting email with incorrect path (missing dataSetInformation)...');
contact.set('contactDataSet.contactInformation.email', 'john@example.com');

// Check if it was auto-corrected
const retrievedEmail = contact.get('contactDataSet.contactInformation.dataSetInformation.email');
console.log('Retrieved email:', retrievedEmail);
console.log('Auto-correction worked!\n');

// 2. Using Path Constants (Recommended)
console.log('2. Using Path Constants (Recommended)');
contact.set(CONTACT_PATHS.EMAIL, 'john.doe@example.com');
contact.set(CONTACT_PATHS.NAME, { '@xml:lang': 'en', '#text': 'John Doe' });
contact.set(CONTACT_PATHS.PHONE, '+1-555-0123');

console.log('Email:', contact.get(CONTACT_PATHS.EMAIL));
console.log('Name:', contact.get(CONTACT_PATHS.NAME));
console.log('Phone:', contact.get(CONTACT_PATHS.PHONE));
console.log('Using path constants prevents mistakes!\n');

// 3. Path Suggestions
console.log('3. Path Suggestions');
const emailSuggestions = contact.getPathSuggestions('email');
console.log('Suggestions for "email":', emailSuggestions);

const nameSuggestions = contact.getPathSuggestions('name');
console.log('Suggestions for "name":', nameSuggestions);

const partialSuggestions = contact.getPathSuggestions('contact');
console.log('Suggestions for "contact":', partialSuggestions.slice(0, 5));
console.log('\n');

// 4. Path Validation
console.log('4. Path Validation');
const validResult = contact.validatePath(CONTACT_PATHS.EMAIL);
console.log('Valid path result:', validResult);

const invalidResult = contact.validatePath('contactDataSet.contactInformation.email');
console.log('Invalid path result:', invalidResult);
console.log('\n');

// 5. Strict Mode
console.log('5. Strict Mode');
const strictConfig: PathValidationConfig = { strict: true };
const strictContact = createTypedContact({}, strictConfig);

console.log('Trying to set with invalid path in strict mode...');
try {
  strictContact.set('contactDataSet.contactInformation.email', 'test@example.com');
} catch (error) {
  console.log('Error caught:', (error as Error).message);
}
console.log('\n');

// 6. Flow Example
console.log('6. Flow Example');
const flow = createTypedFlow();

// Common mistake: missing dataSetInformation
console.log('Setting flow name with incorrect path...');
flow.set('flowDataSet.flowInformation.name.baseName', 
  { '@xml:lang': 'en', '#text': 'Steel' });

// Check if corrected
const flowName = flow.get('flowDataSet.flowInformation.dataSetInformation.name.baseName');
console.log('Retrieved flow name:', flowName);

// Using constants (recommended)
flow.set(FLOW_PATHS.BASE_NAME, { '@xml:lang': 'en', '#text': 'Steel - High Quality' });
flow.set(FLOW_PATHS.CAS_NUMBER, '7439-89-6');
flow.set(FLOW_PATHS.TYPE_OF_DATASET, 'Elementary flow');

console.log('Flow base name:', flow.get(FLOW_PATHS.BASE_NAME));
console.log('Flow CAS number:', flow.get(FLOW_PATHS.CAS_NUMBER));
console.log('Flow type:', flow.get(FLOW_PATHS.TYPE_OF_DATASET));
console.log('\n');

// 7. Process Example
console.log('7. Process Example');
const process = createTypedProcess();

// Common mistake: wrong location path
console.log('Setting process location with incorrect path...');
process.set('processDataSet.processInformation.location', 'CN');

// Check if corrected
const location = process.get('processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction.@location');
console.log('Retrieved location:', location);

// Using constants (recommended)
process.set(PROCESS_PATHS.BASE_NAME, { '@xml:lang': 'en', '#text': 'Steel Production' });
process.set(PROCESS_PATHS.LOCATION, 'CN');
process.set(PROCESS_PATHS.REFERENCE_YEAR, '2024');

console.log('Process base name:', process.get(PROCESS_PATHS.BASE_NAME));
console.log('Process location:', process.get(PROCESS_PATHS.LOCATION));
console.log('Reference year:', process.get(PROCESS_PATHS.REFERENCE_YEAR));
console.log('\n');

// 8. Global Configuration
console.log('8. Global Configuration');
setGlobalPathValidatorConfig({ 
  strict: false,
  maxSuggestions: 3,
  fuzzyMatch: true 
});

const globalContact = createTypedContact();
console.log('Global configuration applied');
console.log('Max suggestions for "email":', globalContact.getPathSuggestions('email'));
console.log('\n');

// 9. Dynamic Path Validation
console.log('9. Dynamic Path Validation');
const dynamicValidator = (path: string) => {
  const result = contact.validatePath(path);
  if (result.isValid) {
    console.log(`✓ Path "${path}" is valid`);
  } else {
    console.log(`✗ Path "${path}" is invalid: ${result.errors[0].error}`);
    if (result.errors[0].suggestion) {
      console.log(`  Suggestion: ${result.errors[0].suggestion}`);
    }
  }
};

dynamicValidator(CONTACT_PATHS.EMAIL); // Valid
dynamicValidator('contactDataSet.contactInformation.email'); // Invalid
dynamicValidator('contactDataSet.invalidSection.field'); // Invalid
console.log('\n');

// 10. Best Practices
console.log('10. Best Practices');
console.log('✓ Always use path constants when available');
console.log('✓ Enable strict mode during development');
console.log('✓ Use path suggestions for discovery');
console.log('✓ Validate paths in dynamic scenarios');
console.log('✓ Check validation results before proceeding');
console.log('\n');

console.log('=== Demo Complete ===');

// Example of advanced usage with TypeScript IntelliSense
console.log('\n=== Advanced TypeScript Usage ===');

// This will provide IntelliSense for path constants
const contactPaths = CONTACT_PATHS;
console.log('Available contact paths:', Object.keys(contactPaths));

// Type-safe operations
const typeAwareContact = createTypedContact();
const validationConfig = typeAwareContact.getValidationConfig();
console.log('Current validation config:', validationConfig);

// Toggle strict mode
typeAwareContact.setStrictMode(true);
console.log('Strict mode enabled');

// Get all available paths
const allPaths = typeAwareContact.getAvailablePaths();
console.log('Total available paths:', allPaths.length);
console.log('First 5 paths:', allPaths.slice(0, 5));

console.log('\n=== Path Validation System Demo Complete ===');