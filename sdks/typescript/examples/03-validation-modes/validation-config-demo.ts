/**
 * Validation demo focused on `validate()` and `validateEnhanced()`.
 * Reads real data from test-data/tidas-example-process.json to show:
 * - strict mode: fails with errors
 * - weak mode: critical errors fail, non-critical issues become warnings
 * - ignore mode: always passes
 *
 * When to use:
 * - strict: production/publishing/import steps that must be schema-clean
 * - weak: iterative data entry/cleaning where you still want warnings
 * - ignore: quick browse/demo/perf paths validated elsewhere
 */

import fs from 'node:fs';
import path from 'node:path';

import type { ZodIssue } from 'zod';
import { createProcessFromJSON, type ValidationMode } from '@tiangong-lca/tidas-sdk/core';

type ValidationWarning = {
  severity: string;
  message: string;
  path: string[];
  code?: string;
};

const samplePath = path.resolve(
  __dirname,
  '../../../../test-data/tidas-example-process.json'
);
const outputPath = path.resolve(__dirname, 'validation-errors.json');
const baseProcessData = JSON.parse(fs.readFileSync(samplePath, 'utf-8'));
const collectedResults: Array<{
  label: string;
  mode: ValidationMode;
  validate: { success: boolean; issues?: ZodIssue[] };
  validateEnhanced: {
    success: boolean;
    mode: ValidationMode;
    issues?: ZodIssue[];
    warnings?: ValidationWarning[];
  };
}> = [];

const cloneData = () => JSON.parse(JSON.stringify(baseProcessData));

const logIssues = (label: string, issues?: ZodIssue[]) => {
  if (!issues || issues.length === 0) return;
  console.log(label, issues.length);
  issues.forEach((issue, index) => {
    const pathText = issue.path.join('.') || '(root)';
    console.log(
      `  ${index + 1}. [${issue.code}] ${pathText}: ${issue.message}`
    );
    // Dump full issue object to keep complete context (including union details)
    console.log(`      details: ${JSON.stringify(issue, null, 2)}`);
  });
};

const logWarnings = (warnings?: ValidationWarning[]) => {
  if (!warnings || warnings.length === 0) return;
  console.log('Warnings:', warnings.length);
  warnings.forEach((warning, index) => {
    const pathText = warning.path.join('.') || '(root)';
    console.log(
      `  ${index + 1}. [${warning.severity.toUpperCase()}] ${pathText}: ${warning.message}`
    );
  });
};

const toPlainIssue = (issue: ZodIssue) => JSON.parse(JSON.stringify(issue));

const showValidation = (
  label: string,
  mode: 'strict' | 'weak' | 'ignore',
  mutate?: (data: any) => void
) => {
  console.log(`\n${label} (${mode.toUpperCase()})`);
  const data = cloneData();
  mutate?.(data);

  const process = createProcessFromJSON(data, {
    mode,
    includeWarnings: true,
  });

  // Legacy validate()
  const legacy = process.validate();
  console.log('validate():', legacy.success ? 'PASSED' : 'FAILED');
  if (!legacy.success) {
    logIssues('Errors (validate):', legacy.error.issues);
  }

  // Enhanced validateEnhanced()
  const enhanced = process.validateEnhanced();
  console.log(
    'validateEnhanced():',
    enhanced.success ? 'PASSED' : 'FAILED',
    `mode=${enhanced.mode}`
  );
  if (!enhanced.success) {
    logIssues('Errors (validateEnhanced):', enhanced.error.issues);
  }
  logWarnings(enhanced.warnings);

  collectedResults.push({
    label,
    mode,
    validate: {
      success: legacy.success,
      issues: legacy.success ? undefined : legacy.error.issues.map(toPlainIssue),
    },
    validateEnhanced: {
      success: enhanced.success,
      mode: enhanced.mode,
      issues: enhanced.success ? undefined : enhanced.error.issues.map(toPlainIssue),
      warnings: enhanced.warnings,
    },
  });
};

console.log('=== TIDAS Validation Demo (process JSON) ===');
console.log('Sample data:', samplePath);

// 1) Strict: show failing errors
showValidation('Strict validation with raw data', 'strict');

// 2) Weak: inject some non-critical issues to highlight warnings
showValidation('Weak validation with injected issues', 'weak', (data) => {
  const exchange = data.processDataSet?.exchanges?.exchange?.[0];
  if (exchange) {
    exchange.meanAmount = 'not-a-number';
  }
});

// 3) Ignore: even invalid data passes
showValidation('Ignore validation (always passes)', 'ignore', (data) => {
  delete data.processDataSet?.processInformation?.dataSetInformation
    ?.classificationInformation;
});

console.log('\nKey takeaways:');
console.log('- use validate() for legacy success/error shape');
console.log('- use validateEnhanced() to also get warnings and current mode');
console.log('- mode can be set per-entity when creating from JSON');
fs.writeFileSync(outputPath, JSON.stringify(collectedResults, null, 2));
console.log('Validation details saved to:', outputPath);
