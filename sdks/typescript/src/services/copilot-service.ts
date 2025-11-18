/**
 * Suggestion Service
 *
 * Provides a simple API for external modules to suggest improvements for TIDAS/ILCD data
 * using AI-powered methodology rules.
 */

import {
  createProcess,
  createFlow,
  createContact,
  createSource,
  createFlowProperty,
  createUnitGroup,
  createLCIAMethod,
  createLifeCycleModel,
} from '../core/factories';
import { suggestEntireObject } from '../core/copilot/ai';
import type { ModelConfig } from '../core/copilot/ai';
import { generateDiffHTML, generateDiffSummary } from '../utils/diff';

/**
 * Supported data types for suggestions
 */
export type DataType =
  | 'process'
  | 'processes'
  | 'flow'
  | 'flows'
  | 'contact'
  | 'contacts'
  | 'source'
  | 'sources'
  | 'flowproperty'
  | 'flowproperties'
  | 'unitgroup'
  | 'unitgroups'
  | 'lciamethod'
  | 'lciamethods'
  | 'lifecyclemodel'
  | 'lifecyclemodels';

/**
 * Options for suggestions
 */
export interface SuggestOptions {
  /** Paths to skip during suggestion */
  skipPaths?: string[];
  /** Maximum retries per rule */
  maxRetries?: number;
  /** Generate text diff summary */
  outputDiffSummary?: boolean;
  /** Generate HTML diff viewer */
  outputDiffHTML?: boolean;
  /** Specific paths to focus on in diff summary */
  diffPaths?: string[];
  /** Model configuration for AI */
  modelConfig?: ModelConfig;
}

/**
 * Result of suggestion
 */
export interface SuggestResult {
  /** The improved data */
  data: any;
  /** Text diff summary (if requested) */
  diffSummary?: string;
  /** HTML diff viewer code (if requested) */
  diffHTML?: string;
  /** Whether the suggestion was successful */
  success: boolean;
  /** Error message if suggestion failed */
  error?: string;
}

/**
 * Factory map for creating entities based on data type
 */
const entityFactories = {
  process: createProcess,
  processes: createProcess,
  flow: createFlow,
  flows: createFlow,
  contact: createContact,
  contacts: createContact,
  source: createSource,
  sources: createSource,
  flowproperty: createFlowProperty,
  flowproperties: createFlowProperty,
  unitgroup: createUnitGroup,
  unitgroups: createUnitGroup,
  lciamethod: createLCIAMethod,
  lciamethods: createLCIAMethod,
  lifecyclemodel: createLifeCycleModel,
  lifecyclemodels: createLifeCycleModel,
};

/**
 * Methodology type mapping for suggestions
 */
const methodologyTypeMap: Record<DataType, string> = {
  process: 'processes',
  processes: 'processes',
  flow: 'flows',
  flows: 'flows',
  contact: 'contacts',
  contacts: 'contacts',
  source: 'sources',
  sources: 'sources',
  flowproperty: 'flowproperties',
  flowproperties: 'flowproperties',
  unitgroup: 'unitgroups',
  unitgroups: 'unitgroups',
  lciamethod: 'lciamethods',
  lciamethods: 'lciamethods',
  lifecyclemodel: 'lifecyclemodels',
  lifecyclemodels: 'lifecyclemodels',
};

/**
 * Suggest improvements for TIDAS/ILCD data using AI-powered methodology rules
 *
 * This function can work in three modes:
 * 1. Entity instance: If a TIDAS entity is passed, uses its suggest method directly
 * 2. Entity mode (default): Creates proper TIDAS entities for validation and structure
 * 3. Raw mode: Directly processes data without entity creation (use `raw: true` option)
 *
 * @param data - The data to improve (can be TIDAS entity, JSON string, or object)
 * @param dataType - The type of data (e.g., 'process', 'flow', etc.) or methodology name for raw mode
 * @param options - Optional configuration for suggestions
 * @returns Promise<SuggestResult> - The suggestion result
 *
 * @example
 * ```typescript
 * // With TIDAS entity
 * const process = createProcess({ processDataSet: { ... } });
 * const result = await suggestData(process, 'process');
 *
 * // Entity mode - with proper validation and structure
 * const result = await suggestData(
 *   { processDataSet: { ... } },
 *   'process'
 * );
 *
 * // Raw mode - direct processing without entity creation
 * const result = await suggestData(
 *   { name: 'test', description: 'sample' },
 *   'processes',
 *   { raw: true }
 * );
 *
 * // With JSON string and diff outputs
 * const result = await suggestData(
 *   '{"processDataSet": {...}}',
 *   'process',
 *   {
 *     outputDiffHTML: true,
 *     outputDiffSummary: true
 *   }
 * );
 *
 * // Access results
 * console.log(result.data);        // Improved data
 * console.log(result.diffHTML);    // HTML diff viewer
 * console.log(result.diffSummary); // Text diff summary
 * ```
 */
export async function suggestData(
  data: any,
  dataType: DataType | string,
  options?: SuggestOptions & { raw?: boolean }
): Promise<SuggestResult> {
  try {
    // Check if data is a TIDAS entity (has suggest method)
    if (data && typeof data.suggest === 'function') {
      // It's a TIDAS entity, use its suggest method directly
      const result = await data.suggest({
        skipPaths: options?.skipPaths,
        maxRetries: options?.maxRetries,
        modelConfig: options?.modelConfig,
        outputDiffSummary: options?.outputDiffSummary,
        outputDiffHTML: options?.outputDiffHTML,
        diffPaths: options?.diffPaths,
      });

      // Extract the improved data
      const improvedData = result.data.toJSON();

      return {
        success: true,
        data: improvedData,
        diffSummary: result.diffSummary,
        diffHTML: result.diffHTML,
      };
    }

    // Parse JSON if string is provided
    const parsedData = typeof data === 'string' ? JSON.parse(data) : data;

    // Check if raw mode is requested
    if (options?.raw) {
      // Raw mode: directly process without entity creation
      const methodologyType =
        methodologyTypeMap[dataType as DataType] || dataType;

      // Store original data for diff if needed
      const originalData =
        options?.outputDiffSummary || options?.outputDiffHTML
          ? JSON.parse(JSON.stringify(parsedData))
          : null;

      // Apply suggestion directly
      const improvedData = await suggestEntireObject(
        parsedData,
        methodologyType,
        {
          skipPaths: options?.skipPaths,
          maxRetries: options?.maxRetries,
        }
      );

      // Generate diffs if requested
      let diffSummary: string | undefined;
      let diffHTML: string | undefined;

      if (originalData) {
        if (options?.outputDiffSummary) {
          diffSummary = generateDiffSummary(
            originalData,
            improvedData,
            options.diffPaths
          );
        }

        if (options?.outputDiffHTML) {
          diffHTML = generateDiffHTML(originalData, improvedData);
        }
      }

      return {
        success: true,
        data: improvedData,
        diffSummary,
        diffHTML,
      };
    }

    // Entity mode: use proper entity creation and validation
    if (!entityFactories[dataType as DataType]) {
      return {
        success: false,
        data: parsedData,
        error: `Unsupported data type: ${dataType}. Supported types: ${Object.keys(entityFactories).join(', ')}`,
      };
    }

    // Create entity from data
    const factory = entityFactories[dataType as DataType];
    const entity = factory(parsedData);

    // Use entity's suggest method for improvement
    const result = await entity.suggest({
      skipPaths: options?.skipPaths,
      maxRetries: options?.maxRetries,
      modelConfig: options?.modelConfig,
      outputDiffSummary: options?.outputDiffSummary,
      outputDiffHTML: options?.outputDiffHTML,
      diffPaths: options?.diffPaths,
    });

    // Extract the improved data
    const improvedData = result.data.toJSON();

    return {
      success: true,
      data: improvedData,
      diffSummary: result.diffSummary,
      diffHTML: result.diffHTML,
    };
  } catch (error) {
    console.error('Suggestion failed:', error);
    return {
      success: false,
      data: data,
      error: (error as Error).message,
    };
  }
}

/**
 * @deprecated Use suggestData with { raw: true } option instead
 *
 * This function is kept for backward compatibility but will be removed in future versions.
 * Please use suggestData with the raw option:
 *
 * @example
 * ```typescript
 * // Instead of:
 * const result = await suggestRawData(data, 'processes');
 *
 * // Use:
 * const result = await suggestData(data, 'processes', { raw: true });
 * ```
 */
export async function suggestRawData(
  data: any,
  dataType: DataType | string,
  options?: SuggestOptions
): Promise<SuggestResult> {
  console.warn(
    'suggestRawData is deprecated. Use suggestData with { raw: true } option instead.'
  );
  return suggestData(data, dataType, { ...options, raw: true });
}

/**
 * Batch suggest improvements for multiple data items
 *
 * @param items - Array of items to improve
 * @param options - Optional configuration
 * @returns Promise<SuggestResult[]> - Array of suggestion results
 *
 * @example
 * ```typescript
 * const results = await batchSuggest([
 *   { data: processData1, type: 'process' },
 *   { data: flowData, type: 'flow' },
 *   { data: contactData, type: 'contact' }
 * ]);
 * ```
 */
export async function batchSuggest(
  items: Array<{ data: any; type: DataType }>,
  options?: SuggestOptions
): Promise<SuggestResult[]> {
  const results = await Promise.all(
    items.map((item) => suggestData(item.data, item.type, options))
  );
  return results;
}

/**
 * Validate if the provided API key is configured
 */
export function validateApiKey(): boolean {
  return !!process.env.OPENAI_API_KEY;
}

/**
 * Get available data types for optimization
 */
export function getAvailableDataTypes(): string[] {
  return Object.keys(entityFactories);
}

// Default export for convenience
export default {
  suggestData,
  suggestRawData, // Deprecated, kept for backward compatibility
  batchSuggest,
  validateApiKey,
  getAvailableDataTypes,
};
