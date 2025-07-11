#!/usr/bin/env tsx

/**
 * Debugging Tools and Techniques Example
 * 
 * This example demonstrates various debugging tools and techniques
 * available in the TIDAS SDK for troubleshooting and development.
 */

import { createZodContact, createZodFlow } from '../../src/core/zod-factories';

console.log('🔍 TIDAS Debugging Tools and Techniques Example\n');

// 1. Access Logging and Analysis
console.log('1. Access Logging and Analysis\n');

const debugContactResult = createZodContact({
  enableLogging: true, // Enable detailed access logging
  throwOnValidationError: false,
  defaultLanguage: 'en'
});

const debugContact = debugContactResult.proxy;

console.log('   Setting up contact with logging enabled:');

// Initialize structure
debugContact.contactDataSet = {} as any;
debugContact.contactDataSet.contactInformation = {} as any;
debugContact.contactDataSet.contactInformation.dataSetInformation = {} as any;

// Perform various operations that will be logged
debugContact.contactDataSet.contactInformation.dataSetInformation.email = 'debug@example.com';
debugContact.contactDataSet.contactInformation.dataSetInformation.telephone = '+1-555-DEBUG';
debugContactResult.generateUUID('contactDataSet.contactInformation.dataSetInformation.common:UUID');
debugContactResult.setMultiLangText(
  'contactDataSet.contactInformation.dataSetInformation.common:name',
  'Debug Contact',
  'en'
);

// Read back some values (generates GET operations)
const email = debugContact.contactDataSet.contactInformation.dataSetInformation.email;
const name = debugContactResult.getMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:name', 'en');

console.log(`   Email: ${email}`);
console.log(`   Name: ${name}`);

// Analyze access log
const accessLog = debugContactResult.getAccessLog();
console.log(`\n   Access Log Analysis (${accessLog.length} total operations):`);

// Group operations by type
const operationsByType = accessLog.reduce((acc: any, entry) => {
  acc[entry.type] = (acc[entry.type] || 0) + 1;
  return acc;
}, {});

console.log('   Operation breakdown:');
Object.entries(operationsByType).forEach(([type, count]) => {
  console.log(`   - ${type.toUpperCase()}: ${count} operations`);
});

// Show recent operations
console.log('\n   Recent operations (last 5):');
accessLog.slice(-5).forEach((entry, index) => {
  const timestamp = new Date(entry.timestamp).toISOString().split('T')[1].split('.')[0];
  console.log(`   ${index + 1}. [${timestamp}] ${entry.type.toUpperCase()}: ${entry.path}`);
  if (entry.value !== undefined) {
    console.log(`      Value: ${JSON.stringify(entry.value)}`);
  }
});

// 2. Internal State Inspection
console.log('\n\n2. Internal State Inspection\n');

console.log('   Inspecting internal proxy state:');

// Get stored values
const storedValues = debugContactResult.getValues();
console.log(`   Stored values count: ${Object.keys(storedValues).length}`);

console.log('   Stored value paths:');
Object.keys(storedValues).forEach((path, index) => {
  console.log(`   ${index + 1}. ${path}`);
});

// Get debug information
const debugInfo = debugContactResult.debug();
console.log('\n   Debug information summary:');
console.log(`   - Values tracked: ${Object.keys(debugInfo.values).length}`);
console.log(`   - Array lengths tracked: ${Object.keys(debugInfo.arrayLengths).length}`);
console.log(`   - Recent access entries: ${debugInfo.accessLog.length}`);

// Show built object structure
console.log('\n   Built object structure analysis:');
const builtObject = debugContactResult.buildObject();

function analyzeObjectStructure(obj: any, path = '', depth = 0): any {
  const analysis = {
    totalProperties: 0,
    maxDepth: depth,
    propertyTypes: {} as Record<string, number>,
    arrays: [] as string[],
    objects: [] as string[]
  };

  if (obj && typeof obj === 'object') {
    const keys = Object.keys(obj);
    analysis.totalProperties = keys.length;

    keys.forEach(key => {
      const value = obj[key];
      const currentPath = path ? `${path}.${key}` : key;
      const valueType = Array.isArray(value) ? 'array' : typeof value;
      
      analysis.propertyTypes[valueType] = (analysis.propertyTypes[valueType] || 0) + 1;

      if (Array.isArray(value)) {
        analysis.arrays.push(currentPath);
      } else if (value && typeof value === 'object') {
        analysis.objects.push(currentPath);
        const childAnalysis = analyzeObjectStructure(value, currentPath, depth + 1);
        analysis.maxDepth = Math.max(analysis.maxDepth, childAnalysis.maxDepth);
        analysis.totalProperties += childAnalysis.totalProperties;
        
        // Merge property types
        Object.entries(childAnalysis.propertyTypes).forEach(([type, count]) => {
          analysis.propertyTypes[type] = (analysis.propertyTypes[type] || 0) + count;
        });
        
        analysis.arrays.push(...childAnalysis.arrays);
        analysis.objects.push(...childAnalysis.objects);
      }
    });
  }

  return analysis;
}

const structure = analyzeObjectStructure(builtObject);
console.log(`   - Total properties: ${structure.totalProperties}`);
console.log(`   - Maximum depth: ${structure.maxDepth}`);
console.log(`   - Property types:`, structure.propertyTypes);
console.log(`   - Arrays found: ${structure.arrays.length}`);
console.log(`   - Objects found: ${structure.objects.length}`);

// 3. Validation Debugging
console.log('\n\n3. Validation Debugging\n');

console.log('   Detailed validation analysis:');

const validation = debugContactResult.validate();
if (!validation.success) {
  console.log('   ❌ Validation failed - analyzing issues:');
  
  // Group issues by error code
  const issuesByCode = validation.error?.issues.reduce((acc: any, issue: any) => {
    if (!acc[issue.code]) acc[issue.code] = [];
    acc[issue.code].push(issue);
    return acc;
  }, {});

  Object.entries(issuesByCode || {}).forEach(([code, issues]: [string, any]) => {
    console.log(`\n   ${code.toUpperCase()} errors (${issues.length}):`);
    issues.forEach((issue: any, index: number) => {
      console.log(`   ${index + 1}. Path: ${issue.path.join('.')}`);
      console.log(`      Message: ${issue.message}`);
      if (issue.expected) console.log(`      Expected: ${issue.expected}`);
      if (issue.received) console.log(`      Received: ${issue.received}`);
    });
  });

  // Show paths with most issues
  const pathCounts = validation.error?.issues.reduce((acc: any, issue: any) => {
    const pathKey = issue.path.slice(0, 3).join('.'); // First 3 levels
    acc[pathKey] = (acc[pathKey] || 0) + 1;
    return acc;
  }, {});

  const sortedPaths = Object.entries(pathCounts || {})
    .sort(([,a], [,b]) => (b as number) - (a as number))
    .slice(0, 5);

  console.log('\n   Paths with most validation issues:');
  sortedPaths.forEach(([path, count], index) => {
    console.log(`   ${index + 1}. ${path}: ${count} issues`);
  });
} else {
  console.log('   ✅ Validation successful - no issues to debug');
}

// 4. Performance Profiling
console.log('\n\n4. Performance Profiling\n');

console.log('   Profiling common operations:');

// Profile object creation
const createStartTime = performance.now();
const perfTestResult = createZodContact({ enableLogging: false });
const createEndTime = performance.now();
console.log(`   Object creation: ${(createEndTime - createStartTime).toFixed(3)}ms`);

// Profile property setting
const perfContact = perfTestResult.proxy;
perfContact.contactDataSet = {} as any;

const setStartTime = performance.now();
for (let i = 0; i < 100; i++) {
  perfContact.contactDataSet[`dynamicProperty${i}`] = `value${i}`;
}
const setEndTime = performance.now();
console.log(`   100 property sets: ${(setEndTime - setStartTime).toFixed(3)}ms`);
console.log(`   Average per set: ${((setEndTime - setStartTime) / 100).toFixed(4)}ms`);

// Profile object building
const buildStartTime = performance.now();
const perfBuiltObject = perfTestResult.buildObject();
const buildEndTime = performance.now();
console.log(`   Object building: ${(buildEndTime - buildStartTime).toFixed(3)}ms`);

// Profile validation
const validateStartTime = performance.now();
const perfValidation = perfTestResult.validate();
const validateEndTime = performance.now();
console.log(`   Validation: ${(validateEndTime - validateStartTime).toFixed(3)}ms`);

// 5. Memory Usage Analysis
console.log('\n\n5. Memory Usage Analysis\n');

console.log('   Analyzing memory usage patterns:');

// Create multiple objects to test memory patterns
const memoryTestObjects = [];
const initialMemory = process.memoryUsage();

console.log('   Creating 100 contact objects...');
for (let i = 0; i < 100; i++) {
  const testResult = createZodContact({ enableLogging: false });
  const testContact = testResult.proxy;
  
  testContact.contactDataSet = {} as any;
  testContact.contactDataSet.contactInformation = {} as any;
  testContact.contactDataSet.contactInformation.dataSetInformation = {} as any;
  testContact.contactDataSet.contactInformation.dataSetInformation.email = `test${i}@example.com`;
  
  memoryTestObjects.push(testResult);
}

const afterCreationMemory = process.memoryUsage();

// Build all objects
console.log('   Building all objects...');
memoryTestObjects.forEach(result => result.buildObject());

const afterBuildingMemory = process.memoryUsage();

console.log('   Memory usage analysis:');
console.log(`   Initial heap used: ${(initialMemory.heapUsed / 1024 / 1024).toFixed(2)} MB`);
console.log(`   After creation: ${(afterCreationMemory.heapUsed / 1024 / 1024).toFixed(2)} MB`);
console.log(`   After building: ${(afterBuildingMemory.heapUsed / 1024 / 1024).toFixed(2)} MB`);
console.log(`   Memory per object: ${((afterBuildingMemory.heapUsed - initialMemory.heapUsed) / 100 / 1024).toFixed(2)} KB`);

// 6. Advanced Debugging Utilities
console.log('\n\n6. Advanced Debugging Utilities\n');

class DebugUtils {
  static createPathTracker() {
    const paths = new Set<string>();
    
    return {
      track: (path: string) => paths.add(path),
      getPaths: () => Array.from(paths).sort(),
      hasPath: (path: string) => paths.has(path),
      getDepth: () => Math.max(...Array.from(paths).map(p => p.split('.').length))
    };
  }
  
  static createValidationReporter() {
    const issues: any[] = [];
    
    return {
      addIssue: (issue: any) => issues.push({...issue, timestamp: Date.now()}),
      getIssues: () => issues,
      getSummary: () => {
        const byCode = issues.reduce((acc: any, issue) => {
          acc[issue.code] = (acc[issue.code] || 0) + 1;
          return acc;
        }, {});
        return { total: issues.length, byCode };
      }
    };
  }
  
  static analyzeProxyUsage(proxyResult: any) {
    const log = proxyResult.getAccessLog();
    const values = proxyResult.getValues();
    
    return {
      operationCount: log.length,
      uniquePaths: new Set(log.map((entry: any) => entry.path)).size,
      valueCount: Object.keys(values).length,
      averagePathDepth: Object.keys(values).reduce((acc, path) => 
        acc + path.split('.').length, 0) / Object.keys(values).length || 0,
      operationTypes: log.reduce((acc: any, entry: any) => {
        acc[entry.type] = (acc[entry.type] || 0) + 1;
        return acc;
      }, {})
    };
  }
}

console.log('   Using advanced debugging utilities:');

const pathTracker = DebugUtils.createPathTracker();
const validationReporter = DebugUtils.createValidationReporter();

// Track paths in our debug contact
Object.keys(debugContactResult.getValues()).forEach(path => {
  pathTracker.track(path);
});

// Add validation issues if any
if (!validation.success) {
  validation.error?.issues.forEach((issue: any) => {
    validationReporter.addIssue(issue);
  });
}

const usageAnalysis = DebugUtils.analyzeProxyUsage(debugContactResult);

console.log('   Path tracking results:');
console.log(`   - Unique paths: ${pathTracker.getPaths().length}`);
console.log(`   - Maximum depth: ${pathTracker.getDepth()}`);
console.log(`   - Sample paths: ${pathTracker.getPaths().slice(0, 3).join(', ')}`);

console.log('\n   Validation reporting:');
const valSummary = validationReporter.getSummary();
console.log(`   - Total issues: ${valSummary.total}`);
console.log(`   - By code:`, valSummary.byCode);

console.log('\n   Proxy usage analysis:');
console.log(`   - Total operations: ${usageAnalysis.operationCount}`);
console.log(`   - Unique paths accessed: ${usageAnalysis.uniquePaths}`);
console.log(`   - Values stored: ${usageAnalysis.valueCount}`);
console.log(`   - Average path depth: ${usageAnalysis.averagePathDepth.toFixed(2)}`);
console.log(`   - Operation breakdown:`, usageAnalysis.operationTypes);

// 7. Debugging Best Practices Summary
console.log('\n\n7. Debugging Best Practices\n');

console.log('🎉 Debugging tools and techniques example completed!');
console.log('\n📋 Debugging Strategies Demonstrated:');
console.log('✅ Access logging and operation analysis');
console.log('✅ Internal state inspection');
console.log('✅ Detailed validation debugging');
console.log('✅ Performance profiling techniques');
console.log('✅ Memory usage analysis');
console.log('✅ Advanced debugging utilities');
console.log('✅ Path tracking and analysis');

console.log('\n🔧 Key Debugging Practices:');
console.log('• Enable logging during development');
console.log('• Use debug() method for quick state inspection');
console.log('• Analyze validation errors by type and path');
console.log('• Profile performance for optimization');
console.log('• Monitor memory usage for large datasets');
console.log('• Track property access patterns');
console.log('• Use utility functions for common debug tasks');
console.log('• Group and categorize issues for easier resolution');