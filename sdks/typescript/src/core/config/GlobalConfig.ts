import { ValidationConfig, ValidationMode, DEFAULT_VALIDATION_CONFIG } from './ValidationConfig';

/**
 * Global configuration for TIDAS SDK
 */
class TidasGlobalConfig {
  private _defaultValidationConfig: ValidationConfig = { ...DEFAULT_VALIDATION_CONFIG };

  /**
   * Get the current default validation configuration
   */
  getDefaultValidationConfig(): ValidationConfig {
    return { ...this._defaultValidationConfig };
  }

  /**
   * Set the default validation mode globally
   */
  setDefaultValidationMode(mode: ValidationMode): void {
    this._defaultValidationConfig.mode = mode;
  }

  /**
   * Set the complete default validation configuration
   */
  setDefaultValidationConfig(config: Partial<ValidationConfig>): void {
    this._defaultValidationConfig = {
      ...this._defaultValidationConfig,
      ...config
    };
  }

  /**
   * Reset to default configuration
   */
  resetToDefaults(): void {
    this._defaultValidationConfig = { ...DEFAULT_VALIDATION_CONFIG };
  }

  /**
   * Load configuration from environment variables
   */
  loadFromEnvironment(): void {
    const envMode = process.env.TIDAS_VALIDATION_MODE as ValidationMode;
    if (envMode && ['strict', 'weak', 'ignore'].includes(envMode)) {
      this._defaultValidationConfig.mode = envMode;
    }

    const envThrowOnError = process.env.TIDAS_THROW_ON_ERROR;
    if (envThrowOnError !== undefined) {
      this._defaultValidationConfig.throwOnError = envThrowOnError === 'true';
    }

    const envIncludeWarnings = process.env.TIDAS_INCLUDE_WARNINGS;
    if (envIncludeWarnings !== undefined) {
      this._defaultValidationConfig.includeWarnings = envIncludeWarnings === 'true';
    }

    const envDeepValidation = process.env.TIDAS_DEEP_VALIDATION;
    if (envDeepValidation !== undefined) {
      this._defaultValidationConfig.deepValidation = envDeepValidation === 'true';
    }
  }
}

/**
 * Global configuration instance
 */
export const globalConfig = new TidasGlobalConfig();

/**
 * Convenience functions for global configuration
 */

/**
 * Set global validation mode
 */
export function setGlobalValidationMode(mode: ValidationMode): void {
  globalConfig.setDefaultValidationMode(mode);
}

/**
 * Get current global validation mode
 */
export function getGlobalValidationMode(): ValidationMode {
  return globalConfig.getDefaultValidationConfig().mode;
}

/**
 * Set global validation configuration
 */
export function setGlobalValidationConfig(config: Partial<ValidationConfig>): void {
  globalConfig.setDefaultValidationConfig(config);
}

/**
 * Get current global validation configuration
 */
export function getGlobalValidationConfig(): ValidationConfig {
  return globalConfig.getDefaultValidationConfig();
}

/**
 * Reset global configuration to defaults
 */
export function resetGlobalConfig(): void {
  globalConfig.resetToDefaults();
}

/**
 * Load configuration from environment variables
 */
export function loadConfigFromEnvironment(): void {
  globalConfig.loadFromEnvironment();
}

// Auto-load from environment on module initialization
if (typeof process !== 'undefined' && process.env) {
  loadConfigFromEnvironment();
}