/**
 * Compile-time type checking helpers for path validation
 * Provides TypeScript IntelliSense support for valid paths
 */

import type { Contact, Flow, Process, Source, FlowProperty, UnitGroup, LCIAMethod, LifeCycleModel } from '../types';

/**
 * Helper type to get all valid paths from a type
 */
export type ValidPaths<T> = T extends Record<string, any>
  ? {
      [K in keyof T]: K extends string
        ? T[K] extends Record<string, any>
          ? K | `${K}.${ValidPaths<T[K]>}`
          : K
        : never;
    }[keyof T]
  : never;

/**
 * Specific path types for each data type
 */
export type ContactPaths = ValidPaths<Contact>;
export type FlowPaths = ValidPaths<Flow>;
export type ProcessPaths = ValidPaths<Process>;
export type SourcePaths = ValidPaths<Source>;
export type FlowPropertyPaths = ValidPaths<FlowProperty>;
export type UnitGroupPaths = ValidPaths<UnitGroup>;
export type LCIAMethodPaths = ValidPaths<LCIAMethod>;
export type LifeCycleModelPaths = ValidPaths<LifeCycleModel>;

/**
 * Union of all possible paths
 */
export type AnyDataSetPath = 
  | ContactPaths
  | FlowPaths
  | ProcessPaths
  | SourcePaths
  | FlowPropertyPaths
  | UnitGroupPaths
  | LCIAMethodPaths
  | LifeCycleModelPaths;

/**
 * Get the value type at a specific path
 */
export type PathValue<T, P extends string> = P extends keyof T
  ? T[P]
  : P extends `${infer K}.${infer Rest}`
  ? K extends keyof T
    ? T[K] extends Record<string, any>
      ? PathValue<T[K], Rest>
      : never
    : never
  : never;

/**
 * Type-safe path validation function
 */
export function isValidPath<T extends Record<string, any>>(
  _obj: T,
  path: string
): path is ValidPaths<T> {
  // This is a runtime check, the type constraint is compile-time
  return typeof path === 'string' && path.length > 0;
}

/**
 * Common path patterns for different data types
 */
export const CONTACT_PATHS = {
  UUID: 'contactDataSet.contactInformation.dataSetInformation.common:UUID',
  NAME: 'contactDataSet.contactInformation.dataSetInformation.common:name',
  SHORT_NAME: 'contactDataSet.contactInformation.dataSetInformation.common:shortName',
  EMAIL: 'contactDataSet.contactInformation.dataSetInformation.email',
  PHONE: 'contactDataSet.contactInformation.dataSetInformation.telephone',
  WEBSITE: 'contactDataSet.contactInformation.dataSetInformation.WWWAddress',
  ADDRESS: 'contactDataSet.contactInformation.dataSetInformation.contactAddress',
  DESCRIPTION: 'contactDataSet.contactInformation.dataSetInformation.contactDescriptionOrComment',
  TIMESTAMP: 'contactDataSet.administrativeInformation.dataEntryBy.common:timeStamp',
  VERSION: 'contactDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion',
} as const;

export const FLOW_PATHS = {
  UUID: 'flowDataSet.flowInformation.dataSetInformation.common:UUID',
  BASE_NAME: 'flowDataSet.flowInformation.dataSetInformation.name.baseName',
  TREATMENT_ROUTES: 'flowDataSet.flowInformation.dataSetInformation.name.treatmentStandardsRoutes',
  LOCATION_TYPES: 'flowDataSet.flowInformation.dataSetInformation.name.mixAndLocationTypes',
  FLOW_PROPERTIES: 'flowDataSet.flowInformation.dataSetInformation.name.flowProperties',
  CAS_NUMBER: 'flowDataSet.flowInformation.dataSetInformation.CASNumber',
  GENERAL_COMMENT: 'flowDataSet.flowInformation.dataSetInformation.common:generalComment',
  TYPE_OF_DATASET: 'flowDataSet.flowInformation.dataSetInformation.typeOfDataSet',
  REFERENCE_FLOW_PROPERTY: 'flowDataSet.flowInformation.quantitativeReference.referenceToReferenceFlowProperty',
  TIMESTAMP: 'flowDataSet.administrativeInformation.dataEntryBy.common:timeStamp',
  VERSION: 'flowDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion',
} as const;

export const PROCESS_PATHS = {
  UUID: 'processDataSet.processInformation.dataSetInformation.common:UUID',
  BASE_NAME: 'processDataSet.processInformation.dataSetInformation.name.baseName',
  TREATMENT_ROUTES: 'processDataSet.processInformation.dataSetInformation.name.treatmentStandardsRoutes',
  LOCATION_TYPES: 'processDataSet.processInformation.dataSetInformation.name.mixAndLocationTypes',
  GENERAL_COMMENT: 'processDataSet.processInformation.dataSetInformation.common:generalComment',
  REFERENCE_YEAR: 'processDataSet.processInformation.time.referenceYear',
  VALID_UNTIL: 'processDataSet.processInformation.time.dataSetValidUntil',
  LOCATION: 'processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction.@location',
  LOCATION_DESCRIPTION: 'processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction.descriptionOfRestrictions',
  TECHNOLOGY_DESCRIPTION: 'processDataSet.processInformation.technology.technologyDescriptionAndIncludedProcesses',
  TECHNOLOGICAL_APPLICABILITY: 'processDataSet.processInformation.technology.technologicalApplicability',
  TIMESTAMP: 'processDataSet.administrativeInformation.dataEntryBy.common:timeStamp',
  VERSION: 'processDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion',
} as const;

/**
 * Type-safe path constants
 */
export type ContactPathConstants = typeof CONTACT_PATHS[keyof typeof CONTACT_PATHS];
export type FlowPathConstants = typeof FLOW_PATHS[keyof typeof FLOW_PATHS];
export type ProcessPathConstants = typeof PROCESS_PATHS[keyof typeof PROCESS_PATHS];

/**
 * Helper function to get typed path suggestions
 */
export function getTypedPathSuggestions<T extends Record<string, any>>(
  dataType: string,
  partialPath: string = ''
): string[] {
  const pathConstants = {
    contact: Object.values(CONTACT_PATHS),
    flow: Object.values(FLOW_PATHS),
    process: Object.values(PROCESS_PATHS),
  };

  const paths = pathConstants[dataType as keyof typeof pathConstants] || [];
  
  if (!partialPath) {
    return paths;
  }
  
  return paths.filter(path => 
    path.toLowerCase().includes(partialPath.toLowerCase())
  );
}

/**
 * Enhanced typed accessor interface with compile-time path validation
 */
export interface TypedAccessorWithPaths<T extends Record<string, any>> {
  /**
   * Get a value at a typed path with compile-time validation
   */
  get<P extends ValidPaths<T>>(path: P): PathValue<T, P>;
  
  /**
   * Set a value at a typed path with compile-time validation
   */
  set<P extends ValidPaths<T>>(path: P, value: PathValue<T, P>): this;
  
  /**
   * Check if a path exists with compile-time validation
   */
  has<P extends ValidPaths<T>>(path: P): boolean;
  
  /**
   * Delete a value at a typed path with compile-time validation
   */
  delete<P extends ValidPaths<T>>(path: P): boolean;
  
  /**
   * Get all available paths (compile-time typed)
   */
  getTypedPaths(): ValidPaths<T>[];
}

/**
 * Utility type to check if a path is valid for a given type
 */
export type IsValidPath<T, P extends string> = P extends ValidPaths<T> ? true : false;

/**
 * Helper to create a type-safe path validator
 */
export function createTypedPathValidator<T extends Record<string, any>>() {
  return {
    /**
     * Validate a path at compile time
     */
    validatePath<P extends string>(
      path: P
    ): IsValidPath<T, P> extends true ? P : never {
      return path as any;
    },
    
    /**
     * Get suggestions for a given type
     */
    getSuggestions(partialPath: string): string[] {
      // This would be implemented based on the actual type
      return [];
    }
  };
}

/**
 * Common path validation errors and suggestions
 */
export const PATH_VALIDATION_MESSAGES = {
  MISSING_DATA_SET_INFORMATION: {
    error: 'Missing "dataSetInformation" in path',
    suggestion: 'Add "dataSetInformation" between the information section and the field name'
  },
  INCORRECT_NAMESPACE: {
    error: 'Incorrect namespace prefix',
    suggestion: 'Use "common:" prefix for common fields like UUID, name, shortName'
  },
  WRONG_SECTION: {
    error: 'Field not found in specified section',
    suggestion: 'Check if the field belongs to a different section'
  },
  INVALID_FIELD: {
    error: 'Field does not exist',
    suggestion: 'Check the field name spelling and case'
  }
} as const;

/**
 * Export utility functions for runtime use
 */
export {
  isValidPath,
  getTypedPathSuggestions,
  createTypedPathValidator
};