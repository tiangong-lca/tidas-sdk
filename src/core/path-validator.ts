/**
 * Path validation system for TIDAS typed accessors
 * Prevents usage of invalid paths and provides suggestions for correct paths
 */

import type { DataSet, Contact, Flow, Process, Source, FlowProperty, UnitGroup, LCIAMethod, LifeCycleModel } from '../types';

/**
 * Path validation error types
 */
export interface PathValidationError {
  path: string;
  error: string;
  suggestion?: string;
  possiblePaths?: string[];
}

/**
 * Path validation result
 */
export interface PathValidationResult {
  isValid: boolean;
  errors: PathValidationError[];
  normalizedPath?: string;
}

/**
 * Configuration for path validation
 */
export interface PathValidationConfig {
  /** Enable strict mode - throws errors for invalid paths */
  strict?: boolean;
  /** Maximum suggestion count */
  maxSuggestions?: number;
  /** Enable fuzzy matching for suggestions */
  fuzzyMatch?: boolean;
  /** Case sensitivity for path matching */
  caseSensitive?: boolean;
}

/**
 * Default path validation configuration
 */
const DEFAULT_CONFIG: Required<PathValidationConfig> = {
  strict: false,
  maxSuggestions: 5,
  fuzzyMatch: true,
  caseSensitive: false,
};

/**
 * Known valid path patterns for different data types
 */
const VALID_PATH_PATTERNS = {
  contact: [
    'contactDataSet',
    'contactDataSet.contactInformation',
    'contactDataSet.contactInformation.dataSetInformation',
    'contactDataSet.contactInformation.dataSetInformation.common:UUID',
    'contactDataSet.contactInformation.dataSetInformation.common:shortName',
    'contactDataSet.contactInformation.dataSetInformation.common:name',
    'contactDataSet.contactInformation.dataSetInformation.classificationInformation',
    'contactDataSet.contactInformation.dataSetInformation.contactAddress',
    'contactDataSet.contactInformation.dataSetInformation.email',
    'contactDataSet.contactInformation.dataSetInformation.telephone',
    'contactDataSet.contactInformation.dataSetInformation.telefax',
    'contactDataSet.contactInformation.dataSetInformation.WWWAddress',
    'contactDataSet.contactInformation.dataSetInformation.centralContactPoint',
    'contactDataSet.contactInformation.dataSetInformation.contactDescriptionOrComment',
    'contactDataSet.contactInformation.dataSetInformation.referenceToContact',
    'contactDataSet.contactInformation.dataSetInformation.referenceToLogo',
    'contactDataSet.administrativeInformation',
    'contactDataSet.administrativeInformation.dataEntryBy',
    'contactDataSet.administrativeInformation.dataEntryBy.common:timeStamp',
    'contactDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat',
    'contactDataSet.administrativeInformation.publicationAndOwnership',
    'contactDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion',
    'contactDataSet.administrativeInformation.publicationAndOwnership.referenceToPrecedingDataSetVersion',
    'contactDataSet.administrativeInformation.publicationAndOwnership.common:permanentDataSetURI',
    'contactDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet',
  ],
  flow: [
    'flowDataSet',
    'flowDataSet.flowInformation',
    'flowDataSet.flowInformation.dataSetInformation',
    'flowDataSet.flowInformation.dataSetInformation.common:UUID',
    'flowDataSet.flowInformation.dataSetInformation.name',
    'flowDataSet.flowInformation.dataSetInformation.name.baseName',
    'flowDataSet.flowInformation.dataSetInformation.name.treatmentStandardsRoutes',
    'flowDataSet.flowInformation.dataSetInformation.name.mixAndLocationTypes',
    'flowDataSet.flowInformation.dataSetInformation.name.flowProperties',
    'flowDataSet.flowInformation.dataSetInformation.classificationInformation',
    'flowDataSet.flowInformation.dataSetInformation.CASNumber',
    'flowDataSet.flowInformation.dataSetInformation.common:generalComment',
    'flowDataSet.flowInformation.dataSetInformation.typeOfDataSet',
    'flowDataSet.flowInformation.quantitativeReference',
    'flowDataSet.flowInformation.quantitativeReference.referenceToReferenceFlowProperty',
    'flowDataSet.modellingAndValidation',
    'flowDataSet.modellingAndValidation.LCIMethod',
    'flowDataSet.modellingAndValidation.LCIMethod.typeOfDataSet',
    'flowDataSet.modellingAndValidation.complianceDeclarations',
    'flowDataSet.administrativeInformation',
    'flowDataSet.administrativeInformation.dataEntryBy',
    'flowDataSet.administrativeInformation.publicationAndOwnership',
    'flowDataSet.flowProperties',
    'flowDataSet.flowProperties.flowProperty',
  ],
  process: [
    'processDataSet',
    'processDataSet.processInformation',
    'processDataSet.processInformation.dataSetInformation',
    'processDataSet.processInformation.dataSetInformation.common:UUID',
    'processDataSet.processInformation.dataSetInformation.name',
    'processDataSet.processInformation.dataSetInformation.name.baseName',
    'processDataSet.processInformation.dataSetInformation.name.treatmentStandardsRoutes',
    'processDataSet.processInformation.dataSetInformation.name.mixAndLocationTypes',
    'processDataSet.processInformation.dataSetInformation.classificationInformation',
    'processDataSet.processInformation.dataSetInformation.common:generalComment',
    'processDataSet.processInformation.quantitativeReference',
    'processDataSet.processInformation.time',
    'processDataSet.processInformation.time.referenceYear',
    'processDataSet.processInformation.time.dataSetValidUntil',
    'processDataSet.processInformation.geography',
    'processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction',
    'processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction.@location',
    'processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction.descriptionOfRestrictions',
    'processDataSet.processInformation.technology',
    'processDataSet.processInformation.technology.technologyDescriptionAndIncludedProcesses',
    'processDataSet.processInformation.technology.technologicalApplicability',
    'processDataSet.processInformation.technology.referenceToTechnologyFlowDiagrammOrPicture',
    'processDataSet.modellingAndValidation',
    'processDataSet.modellingAndValidation.LCIMethodAndAllocation',
    'processDataSet.modellingAndValidation.dataSourcesTreatmentAndRepresentativeness',
    'processDataSet.modellingAndValidation.completeness',
    'processDataSet.modellingAndValidation.validation',
    'processDataSet.modellingAndValidation.complianceDeclarations',
    'processDataSet.administrativeInformation',
    'processDataSet.administrativeInformation.dataEntryBy',
    'processDataSet.administrativeInformation.publicationAndOwnership',
    'processDataSet.exchanges',
    'processDataSet.exchanges.exchange',
    'processDataSet.LCIAResults',
    'processDataSet.LCIAResults.LCIAResult',
  ],
};

/**
 * Common path mistakes and their corrections
 */
const COMMON_PATH_MISTAKES = {
  // Missing dataSetInformation
  'contactDataSet.contactInformation.email': 'contactDataSet.contactInformation.dataSetInformation.email',
  'contactDataSet.contactInformation.common:name': 'contactDataSet.contactInformation.dataSetInformation.common:name',
  'contactDataSet.contactInformation.common:shortName': 'contactDataSet.contactInformation.dataSetInformation.common:shortName',
  'contactDataSet.contactInformation.common:UUID': 'contactDataSet.contactInformation.dataSetInformation.common:UUID',
  'contactDataSet.contactInformation.telephone': 'contactDataSet.contactInformation.dataSetInformation.telephone',
  'contactDataSet.contactInformation.WWWAddress': 'contactDataSet.contactInformation.dataSetInformation.WWWAddress',
  
  // Flow paths
  'flowDataSet.flowInformation.common:UUID': 'flowDataSet.flowInformation.dataSetInformation.common:UUID',
  'flowDataSet.flowInformation.name': 'flowDataSet.flowInformation.dataSetInformation.name',
  'flowDataSet.flowInformation.name.baseName': 'flowDataSet.flowInformation.dataSetInformation.name.baseName',
  'flowDataSet.flowInformation.CASNumber': 'flowDataSet.flowInformation.dataSetInformation.CASNumber',
  'flowDataSet.flowInformation.typeOfDataSet': 'flowDataSet.flowInformation.dataSetInformation.typeOfDataSet',
  
  // Process paths
  'processDataSet.processInformation.common:UUID': 'processDataSet.processInformation.dataSetInformation.common:UUID',
  'processDataSet.processInformation.name': 'processDataSet.processInformation.dataSetInformation.name',
  'processDataSet.processInformation.name.baseName': 'processDataSet.processInformation.dataSetInformation.name.baseName',
  'processDataSet.processInformation.referenceYear': 'processDataSet.processInformation.time.referenceYear',
  'processDataSet.processInformation.location': 'processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction.@location',
  
  // Common namespace mistakes
  'contactDataSet.contactInformation.dataSetInformation.name': 'contactDataSet.contactInformation.dataSetInformation.common:name',
  'contactDataSet.contactInformation.dataSetInformation.shortName': 'contactDataSet.contactInformation.dataSetInformation.common:shortName',
  'contactDataSet.contactInformation.dataSetInformation.UUID': 'contactDataSet.contactInformation.dataSetInformation.common:UUID',
  'flowDataSet.flowInformation.dataSetInformation.UUID': 'flowDataSet.flowInformation.dataSetInformation.common:UUID',
  'processDataSet.processInformation.dataSetInformation.UUID': 'processDataSet.processInformation.dataSetInformation.common:UUID',
};

/**
 * Extract object structure to generate valid paths
 */
export function extractObjectPaths(obj: any, prefix = '', maxDepth = 10): string[] {
  const paths: string[] = [];
  
  if (maxDepth <= 0 || obj === null || obj === undefined) {
    return paths;
  }
  
  if (typeof obj === 'object' && !Array.isArray(obj)) {
    for (const key in obj) {
      if (obj.hasOwnProperty(key)) {
        const currentPath = prefix ? `${prefix}.${key}` : key;
        paths.push(currentPath);
        
        if (typeof obj[key] === 'object' && obj[key] !== null) {
          paths.push(...extractObjectPaths(obj[key], currentPath, maxDepth - 1));
        }
      }
    }
  } else if (Array.isArray(obj)) {
    // For arrays, add numeric indices
    for (let i = 0; i < Math.min(obj.length, 3); i++) {
      const currentPath = `${prefix}[${i}]`;
      paths.push(currentPath);
      
      if (typeof obj[i] === 'object' && obj[i] !== null) {
        paths.push(...extractObjectPaths(obj[i], currentPath, maxDepth - 1));
      }
    }
  }
  
  return paths;
}

/**
 * Detect data type from object structure
 */
export function detectDataType(obj: any): string {
  if (!obj || typeof obj !== 'object') return 'unknown';
  
  if (obj.contactDataSet) return 'contact';
  if (obj.flowDataSet) return 'flow';
  if (obj.processDataSet) return 'process';
  if (obj.sourceDataSet) return 'source';
  if (obj.flowPropertyDataSet) return 'flowProperty';
  if (obj.unitGroupDataSet) return 'unitGroup';
  if (obj.LCIAMethodDataSet) return 'lciaMethod';
  if (obj.lifeCycleModelDataSet) return 'lifeCycleModel';
  
  return 'unknown';
}

/**
 * Calculate string similarity using Levenshtein distance
 */
function calculateSimilarity(str1: string, str2: string): number {
  const matrix = [];
  const len1 = str1.length;
  const len2 = str2.length;
  
  for (let i = 0; i <= len2; i++) {
    matrix[i] = [i];
  }
  
  for (let j = 0; j <= len1; j++) {
    matrix[0][j] = j;
  }
  
  for (let i = 1; i <= len2; i++) {
    for (let j = 1; j <= len1; j++) {
      if (str2.charAt(i - 1) === str1.charAt(j - 1)) {
        matrix[i][j] = matrix[i - 1][j - 1];
      } else {
        matrix[i][j] = Math.min(
          matrix[i - 1][j - 1] + 1,
          matrix[i][j - 1] + 1,
          matrix[i - 1][j] + 1
        );
      }
    }
  }
  
  const maxLength = Math.max(len1, len2);
  return maxLength === 0 ? 1 : (maxLength - matrix[len2][len1]) / maxLength;
}

/**
 * Find similar paths using fuzzy matching
 */
function findSimilarPaths(
  targetPath: string,
  validPaths: string[],
  config: Required<PathValidationConfig>
): string[] {
  const similarities = validPaths.map(path => ({
    path,
    similarity: calculateSimilarity(
      config.caseSensitive ? targetPath : targetPath.toLowerCase(),
      config.caseSensitive ? path : path.toLowerCase()
    )
  }));
  
  return similarities
    .filter(item => item.similarity > 0.5) // Threshold for similarity
    .sort((a, b) => b.similarity - a.similarity)
    .slice(0, config.maxSuggestions)
    .map(item => item.path);
}

/**
 * Create path validator for a specific data type
 */
export class PathValidator {
  private config: Required<PathValidationConfig>;
  private validPaths: string[] = [];
  private dataType: string = 'unknown';
  
  constructor(config: PathValidationConfig = {}) {
    this.config = { ...DEFAULT_CONFIG, ...config };
  }
  
  /**
   * Set the data object for validation context
   */
  setDataContext(obj: any): void {
    this.dataType = detectDataType(obj);
    this.validPaths = this.generateValidPaths(obj);
  }
  
  /**
   * Generate valid paths for the current data object
   */
  private generateValidPaths(obj: any): string[] {
    const extractedPaths = extractObjectPaths(obj);
    const typePaths = VALID_PATH_PATTERNS[this.dataType as keyof typeof VALID_PATH_PATTERNS] || [];
    
    // Combine extracted paths with known patterns
    const allPaths = [...new Set([...extractedPaths, ...typePaths])];
    return allPaths.sort();
  }
  
  /**
   * Validate a path
   */
  validatePath(path: string): PathValidationResult {
    const errors: PathValidationError[] = [];
    
    if (!path || typeof path !== 'string') {
      errors.push({
        path,
        error: 'Path must be a non-empty string',
      });
      return { isValid: false, errors };
    }
    
    // Check for direct correction in common mistakes
    const correction = COMMON_PATH_MISTAKES[path as keyof typeof COMMON_PATH_MISTAKES];
    if (correction) {
      errors.push({
        path,
        error: 'Common path mistake detected',
        suggestion: correction,
      });
      return { isValid: false, errors, normalizedPath: correction };
    }
    
    // Check if path exists in valid paths
    const normalizedPath = this.config.caseSensitive ? path : path.toLowerCase();
    const normalizedValidPaths = this.config.caseSensitive 
      ? this.validPaths 
      : this.validPaths.map(p => p.toLowerCase());
    
    if (!normalizedValidPaths.includes(normalizedPath)) {
      const suggestions = this.config.fuzzyMatch 
        ? findSimilarPaths(path, this.validPaths, this.config)
        : [];
      
      errors.push({
        path,
        error: `Invalid path for ${this.dataType} data type`,
        suggestion: suggestions.length > 0 ? suggestions[0] : undefined,
        possiblePaths: suggestions,
      });
      return { isValid: false, errors };
    }
    
    return { isValid: true, errors: [] };
  }
  
  /**
   * Get all valid paths for current data type
   */
  getValidPaths(): string[] {
    return [...this.validPaths];
  }
  
  /**
   * Get path suggestions for a partial path
   */
  getPathSuggestions(partialPath: string): string[] {
    if (!partialPath) return this.validPaths.slice(0, this.config.maxSuggestions);
    
    const filtered = this.validPaths.filter(path => 
      path.toLowerCase().includes(partialPath.toLowerCase())
    );
    
    return filtered.slice(0, this.config.maxSuggestions);
  }
  
  /**
   * Validate and throw error in strict mode
   */
  validateOrThrow(path: string): PathValidationResult {
    const result = this.validatePath(path);
    
    if (!result.isValid && this.config.strict) {
      const error = result.errors[0];
      const message = `Invalid path: ${error.error}${error.suggestion ? `. Did you mean: ${error.suggestion}` : ''}`;
      throw new Error(message);
    }
    
    return result;
  }
  
  /**
   * Set strict mode for validation
   */
  setStrictMode(enabled: boolean): void {
    this.config.strict = enabled;
  }
  
  /**
   * Get current validation configuration
   */
  getValidationConfig(): Required<PathValidationConfig> {
    return { ...this.config };
  }
}

/**
 * Global path validator instance
 */
let globalValidator: PathValidator | null = null;

/**
 * Get or create global path validator
 */
export function getGlobalPathValidator(): PathValidator {
  if (!globalValidator) {
    globalValidator = new PathValidator();
  }
  return globalValidator;
}

/**
 * Set global path validator configuration
 */
export function setGlobalPathValidatorConfig(config: PathValidationConfig): void {
  globalValidator = new PathValidator(config);
}

/**
 * Validate a path using global validator
 */
export function validatePath(path: string, dataContext?: any): PathValidationResult {
  const validator = getGlobalPathValidator();
  if (dataContext) {
    validator.setDataContext(dataContext);
  }
  return validator.validatePath(path);
}

/**
 * Get path suggestions using global validator
 */
export function getPathSuggestions(partialPath: string, dataContext?: any): string[] {
  const validator = getGlobalPathValidator();
  if (dataContext) {
    validator.setDataContext(dataContext);
  }
  return validator.getPathSuggestions(partialPath);
}

/**
 * Validate path or throw error
 */
export function validatePathOrThrow(path: string, dataContext?: any): PathValidationResult {
  const validator = getGlobalPathValidator();
  if (dataContext) {
    validator.setDataContext(dataContext);
  }
  return validator.validateOrThrow(path);
}