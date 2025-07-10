/**
 * Automatically generated index file for all Zod schemas
 * Generated with dependency analysis
 */

// Export all schemas

// Re-export commonly used schemas with simpler names
export { ContactsSchema as ContactSchema } from './tidas_contacts.schema';
export { SourcesSchema as SourceSchema } from './tidas_sources.schema';
export { FlowpropertiesSchema as FlowPropertySchema } from './tidas_flowproperties.schema';
export { UnitgroupsSchema as UnitGroupSchema } from './tidas_unitgroups.schema';
export { LciamethodsSchema as LCIAMethodSchema } from './tidas_lciamethods.schema';
export { LifecyclemodelsSchema as LifeCycleModelSchema } from './tidas_lifecyclemodels.schema';
export { FlowsSchema as FlowSchema } from './tidas_flows.schema';
export { ProcessesSchema as ProcessSchema } from './tidas_processes.schema';

// Export category/enum types (if schemas exist)
export { LocationsCategorySchema as LocationCategorySchema } from './tidas_locations_category.schema';
export { ContactsCategorySchema as ContactCategorySchema } from './tidas_contacts_category.schema';
export { FlowpropertiesCategorySchema as FlowPropertyCategorySchema } from './tidas_flowproperties_category.schema';
export { FlowsElementaryCategorySchema as FlowElementaryCategorySchema } from './tidas_flows_elementary_category.schema';
export { FlowsProductCategorySchema as FlowProductCategorySchema } from './tidas_flows_product_category.schema';
export { LciamethodsCategorySchema as LCIAMethodCategorySchema } from './tidas_lciamethods_category.schema';
export { ProcessesCategorySchema as ProcessCategorySchema } from './tidas_processes_category.schema';
export { SourcesCategorySchema as SourceCategorySchema } from './tidas_sources_category.schema';
export { UnitgroupsCategorySchema as UnitGroupCategorySchema } from './tidas_unitgroups_category.schema';

// Export validation helper functions
import { z } from 'zod';

export type ValidationResult<T> = {
  success: boolean;
  data?: T;
  error?: z.ZodError;
};

/**
 * Validate data against a Zod schema
 */
export function validateWithZod<T>(
  data: unknown,
  schema: z.ZodSchema<T>
): ValidationResult<T> {
  const result = schema.safeParse(data);
  
  if (result.success) {
    return {
      success: true,
      data: result.data
    };
  } else {
    return {
      success: false,
      error: result.error
    };
  }
}

/**
 * Parse and validate JSON data
 */
export function parseWithZod<T>(
  jsonData: string,
  schema: z.ZodSchema<T>
): ValidationResult<T> {
  try {
    const parsed = JSON.parse(jsonData);
    return validateWithZod(parsed, schema);
  } catch (error) {
    return {
      success: false,
      error: new z.ZodError([{
        code: 'custom',
        message: `Invalid JSON: ${error instanceof Error ? error.message : 'Unknown error'}`,
        path: []
      }])
    };
  }
}

/**
 * Batch validate multiple objects
 */
export function validateBatch<T>(
  dataArray: unknown[],
  schema: z.ZodSchema<T>
): ValidationResult<T>[] {
  return dataArray.map(data => validateWithZod(data, schema));
}

/**
 * Create a validation method for object classes
 */
export function createValidationMethod<T>(schema: z.ZodSchema<T>) {
  return function validate(this: any): ValidationResult<T> {
    return validateWithZod(this.data || this._data, schema);
  };
}

/**
 * Create a static validation method for object classes
 */
export function createStaticValidationMethod<T>(schema: z.ZodSchema<T>) {
  return function validateWithSchema(data: unknown): ValidationResult<T> {
    return validateWithZod(data, schema);
  };
}
