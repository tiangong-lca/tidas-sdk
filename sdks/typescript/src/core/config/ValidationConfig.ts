import { z } from 'zod';

/**
 * Validation mode types
 */
export type ValidationMode = 'strict' | 'weak' | 'ignore';

/**
 * Validation configuration interface
 */
export interface ValidationConfig {
  mode: ValidationMode;
  throwOnError?: boolean;
  includeWarnings?: boolean;
  deepValidation?: boolean; // Enable deep validation to report nested field errors even when parent structure is invalid
}

/**
 * Validation warning interface
 */
export interface ValidationWarning {
  path: string[];
  message: string;
  code: string;
  severity: 'low' | 'medium' | 'high';
}

/**
 * Enhanced validation result type
 */
export type EnhancedValidationResult<T> =
  | {
      success: true;
      data: T;
      warnings?: ValidationWarning[];
      mode: ValidationMode;
    }
  | {
      success: false;
      error: z.ZodError;
      warnings?: ValidationWarning[];
      mode: ValidationMode;
    };

/**
 * Error severity classification
 */
export enum ErrorSeverity {
  CRITICAL = 'critical',
  WARNING = 'warning',
  INFO = 'info',
}

/**
 * Critical error patterns that should always cause validation failure
 */
const CRITICAL_ERROR_PATTERNS = [
  'Required',
  'Expected string, received undefined',
  'Expected number, received undefined',
  'Expected object, received undefined',
  'Expected array, received undefined',
];

/**
 * Validation utilities class
 */
export class ValidationUtils {
  /**
   * Categorize Zod error by severity
   */
  static categorizeError(error: z.ZodIssue): ErrorSeverity {
    const message = error.message;

    // Check for critical patterns
    for (const pattern of CRITICAL_ERROR_PATTERNS) {
      if (message.includes(pattern)) {
        return ErrorSeverity.CRITICAL;
      }
    }

    // Type-specific categorization
    switch (error.code) {
      case 'invalid_type':
        // If input is undefined for required field, it's critical
        if (error.input === undefined) {
          return ErrorSeverity.CRITICAL;
        }
        return ErrorSeverity.WARNING;

      case 'too_small':
      case 'too_big':
        return ErrorSeverity.WARNING;

      case 'invalid_value':
        return ErrorSeverity.WARNING;

      case 'unrecognized_keys':
        return ErrorSeverity.INFO;

      default:
        return ErrorSeverity.WARNING;
    }
  }

  /**
   * Convert Zod issue to validation warning
   */
  static issueToWarning(issue: z.ZodIssue): ValidationWarning {
    const severity = this.categorizeError(issue);

    return {
      path: issue.path.map((p) => String(p)),
      message: issue.message,
      code: issue.code,
      severity:
        severity === ErrorSeverity.CRITICAL
          ? 'high'
          : severity === ErrorSeverity.WARNING
            ? 'medium'
            : 'low',
    };
  }

  /**
   * Perform weak validation that returns warnings instead of errors
   */
  static performWeakValidation<T>(
    schema: z.ZodSchema<T>,
    data: any,
    config: ValidationConfig
  ): EnhancedValidationResult<T> {
    const result = schema.safeParse(data);

    if (result.success) {
      return {
        success: true,
        data: result.data,
        mode: config.mode,
      };
    }

    // Categorize errors
    const criticalErrors: z.ZodIssue[] = [];
    const warnings: ValidationWarning[] = [];

    for (const issue of result.error.issues) {
      const severity = this.categorizeError(issue);

      if (severity === ErrorSeverity.CRITICAL) {
        criticalErrors.push(issue);
      } else {
        warnings.push(this.issueToWarning(issue));
      }
    }

    // If there are critical errors, validation fails
    if (criticalErrors.length > 0) {
      const criticalError = new z.ZodError(criticalErrors);
      return {
        success: false,
        error: criticalError,
        warnings: config.includeWarnings ? warnings : undefined,
        mode: config.mode,
      };
    }

    // No critical errors - weak validation passes with warnings
    return {
      success: true,
      data: data as T, // Accept data as-is for weak validation
      warnings: config.includeWarnings ? warnings : undefined,
      mode: config.mode,
    };
  }

  /**
   * Recursively collect validation errors from nested objects
   * This validates nested objects independently, even when parent validation fails
   */
  private static collectNestedErrors(
    schema: z.ZodSchema<any>,
    data: any,
    path: string[] = [],
    maxDepth: number = 10
  ): z.ZodIssue[] {
    const issues: z.ZodIssue[] = [];

    // Prevent infinite recursion
    if (path.length >= maxDepth) {
      return issues;
    }

    // Try to get the schema definition (support both _def and def for different Zod versions)
    const schemaDef = (schema as any).def || (schema as any)._def;

    // Handle ZodObject schemas
    if (schemaDef?.type === 'object' || schemaDef?.typeName === 'ZodObject') {
      let shape;

      // Get shape (could be a function or object)
      if (typeof schemaDef.shape === 'function') {
        shape = schemaDef.shape();
      } else if (schemaDef.shape) {
        shape = schemaDef.shape;
      }

      if (shape) {
        // Debug: log the current path
        if (
          process.env.DEBUG_VALIDATION &&
          path.length > 0 &&
          path.length <= 4
        ) {
          console.log(`[Deep Validation] Checking path: ${path.join('.')}`);
          console.log(
            `  Fields at this level: ${Object.keys(shape).join(', ')}`
          );
        }

        // Validate each field independently
        for (const [key, fieldSchema] of Object.entries(shape)) {
          const fieldPath = [...path, key];
          const fieldData = data?.[key];

          // Always validate the field itself first
          const fieldResult = (fieldSchema as z.ZodSchema<any>).safeParse(
            fieldData
          );

          // Debug: log ALL field validations for name-related paths
          if (
            process.env.DEBUG_VALIDATION &&
            fieldPath.join('.').includes('name')
          ) {
            console.log(
              `[Deep Validation] Validating field: ${fieldPath.join('.')}`
            );
            console.log(
              `  Data exists: ${fieldData !== undefined}, Is object: ${typeof fieldData === 'object'}`
            );
            console.log(
              `  Validation result: ${fieldResult.success ? 'PASS' : 'FAIL'}`
            );
            if (!fieldResult.success) {
              console.log(`  Errors: ${fieldResult.error.issues.length}`);
              fieldResult.error.issues.forEach((issue) => {
                console.log(
                  `    - ${issue.path.join('.')}: ${issue.message} [${issue.code}]`
                );
              });
            }
          }

          if (!fieldResult.success) {
            // Add ALL errors with full path
            fieldResult.error.issues.forEach((issue) => {
              issues.push({
                ...issue,
                path: [...fieldPath, ...issue.path],
              });
            });
          }

          // Recursively check nested objects if data exists and is an object
          if (
            fieldData &&
            typeof fieldData === 'object' &&
            !Array.isArray(fieldData)
          ) {
            const nestedIssues = this.collectNestedErrors(
              fieldSchema as z.ZodSchema<any>,
              fieldData,
              fieldPath,
              maxDepth
            );
            issues.push(...nestedIssues);
          }
        }
      }
    }

    return issues;
  }

  /**
   * Perform deep validation on nested objects
   * This attempts to validate nested structures even when parent objects have errors
   */
  static performDeepValidation<T>(
    schema: z.ZodSchema<T>,
    data: any,
    config: ValidationConfig
  ): EnhancedValidationResult<T> {
    // First, perform standard validation
    const standardResult = schema.safeParse(data);

    if (standardResult.success) {
      return {
        success: true,
        data: standardResult.data,
        mode: config.mode,
      };
    }

    // Standard validation failed - now collect additional nested errors
    const allIssues = [...standardResult.error.issues];

    // Collect nested validation errors
    const nestedIssues = this.collectNestedErrors(schema, data);

    // Debug: log how many nested issues were found
    if (process.env.DEBUG_VALIDATION) {
      console.log(
        `[Deep Validation] Standard issues: ${allIssues.length}, Nested issues: ${nestedIssues.length}`
      );
      console.log('[Deep Validation] Standard error paths:');
      allIssues.forEach((issue) =>
        console.log(`  - ${issue.path.join('.')} [${issue.code}]`)
      );
      console.log('[Deep Validation] Nested error paths:');
      nestedIssues.forEach((issue) =>
        console.log(`  - ${issue.path.join('.')} [${issue.code}]`)
      );
    }

    // Merge nested issues, avoiding duplicates
    let addedCount = 0;
    nestedIssues.forEach((nestedIssue) => {
      const isDuplicate = allIssues.some(
        (existing) =>
          JSON.stringify(existing.path) === JSON.stringify(nestedIssue.path) &&
          existing.code === nestedIssue.code
      );

      if (!isDuplicate) {
        allIssues.push(nestedIssue);
        addedCount++;
      }
    });

    if (process.env.DEBUG_VALIDATION) {
      console.log(
        `[Deep Validation] Added ${addedCount} new issues, total: ${allIssues.length}`
      );
    }

    // Create a new ZodError with all collected issues
    const enhancedError = new z.ZodError(allIssues);

    return {
      success: false,
      error: enhancedError,
      mode: config.mode,
    };
  }

  /**
   * Perform validation based on mode
   */
  static performValidation<T>(
    schema: z.ZodSchema<T>,
    data: any,
    config: ValidationConfig
  ): EnhancedValidationResult<T> {
    // If deep validation is enabled, use deep validation for strict mode
    if (config.deepValidation && config.mode === 'strict') {
      return this.performDeepValidation(schema, data, config);
    }

    switch (config.mode) {
      case 'strict': {
        const strictResult = schema.safeParse(data);
        if (strictResult.success) {
          return {
            success: true,
            data: strictResult.data,
            mode: config.mode,
          };
        } else {
          return {
            success: false,
            error: strictResult.error,
            mode: config.mode,
          };
        }
      }

      case 'weak':
        return this.performWeakValidation(schema, data, config);

      case 'ignore':
        return {
          success: true,
          data: data as T,
          mode: config.mode,
        };

      default:
        throw new Error(`Unknown validation mode: ${config.mode}`);
    }
  }
}

/**
 * Default validation configuration
 */
export const DEFAULT_VALIDATION_CONFIG: ValidationConfig = {
  mode: 'strict',
  throwOnError: false,
  includeWarnings: true,
  deepValidation: true, // Enable deep validation by default
};
