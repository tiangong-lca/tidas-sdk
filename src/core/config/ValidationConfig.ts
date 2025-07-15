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
export type EnhancedValidationResult<T> = {
  success: true;
  data: T;
  warnings?: ValidationWarning[];
  mode: ValidationMode;
} | {
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
  INFO = 'info'
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
        // If received is undefined/null for required field, it's critical
        if (error.received === 'undefined' || error.received === 'null') {
          return ErrorSeverity.CRITICAL;
        }
        return ErrorSeverity.WARNING;
      
      case 'too_small':
      case 'too_big':
        return ErrorSeverity.WARNING;
      
      case 'invalid_string':
        return ErrorSeverity.WARNING;
      
      case 'invalid_enum_value':
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
      path: issue.path.map(p => String(p)),
      message: issue.message,
      code: issue.code,
      severity: severity === ErrorSeverity.CRITICAL ? 'high' : 
               severity === ErrorSeverity.WARNING ? 'medium' : 'low'
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
        mode: config.mode
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
        mode: config.mode
      };
    }
    
    // No critical errors - weak validation passes with warnings
    return {
      success: true,
      data: data as T, // Accept data as-is for weak validation
      warnings: config.includeWarnings ? warnings : undefined,
      mode: config.mode
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
    switch (config.mode) {
      case 'strict': {
        const strictResult = schema.safeParse(data);
        if (strictResult.success) {
          return {
            success: true,
            data: strictResult.data,
            mode: config.mode
          };
        } else {
          return {
            success: false,
            error: strictResult.error,
            mode: config.mode
          };
        }
      }
      
      case 'weak':
        return this.performWeakValidation(schema, data, config);
      
      case 'ignore':
        return {
          success: true,
          data: data as T,
          mode: config.mode
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
  includeWarnings: true
};