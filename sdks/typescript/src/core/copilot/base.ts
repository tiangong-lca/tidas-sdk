// Browser-compatible imports - no Node.js file system dependencies
import bundledMethodologies from '../../data/bundled-methodologies.json';

/**
 * Tag used to identify rules in the methodology yaml files.
 */
const RULES_TAG = '<rules>';

/**
 * Available methodology types based on bundled data
 */
const availableMethodologies = Object.keys(bundledMethodologies.methodologies);

/**
 * Get methodology data by type.
 * @param methodologyType - The type of methodology to retrieve (e.g., 'processes', 'flows')
 * @returns The methodology data object, or null if not found
 */
function getMethodologyData(methodologyType: string): Record<string, any> | null {
  const data = bundledMethodologies.methodologies[methodologyType as keyof typeof bundledMethodologies.methodologies];
  return data || null;
}

/**
 * List all available methodology types.
 * @returns An array of available methodology type names
 */
function getAvailableMethodologyTypes(): string[] {
  return [...availableMethodologies];
}

/**
 * Get metadata about the bundled methodologies.
 * @returns Metadata about when the bundle was created and what it contains
 */
function getBundleMetadata() {
  return bundledMethodologies._metadata;
}

/**
 * List all rule paths from a methodology object.
 * This function recursively traverses the methodology object and finds all paths
 * that contain the <rules> tag.
 *
 * @param methodology - The methodology object
 * @returns An array of dot-notation paths to rules locations
 * @example
 * // Given a methodology object like:
 * // {
 * //   processDataSet: {
 * //     processInformation: {
 * //       dataSetInformation: {
 * //         name: {
 * //           baseName: {
 * //             '<rules>': [...]
 * //           }
 * //         }
 * //       }
 * //     }
 * //   }
 * // }
 * // Returns: ['processDataSet.processInformation.dataSetInformation.name.baseName']
 */
function listRulePathsFromMethodology(
  methodology: Record<string, any>
): string[] {
  const rulePaths: string[] = [];

  /**
   * Recursively traverse the object to find all paths containing <rules>
   * @param obj - Current object being traversed
   * @param currentPath - Array representing the current path in the object tree
   */
  function traverse(obj: any, currentPath: string[] = []): void {
    // Skip if not an object
    if (!obj || typeof obj !== 'object') {
      return;
    }

    // Skip arrays
    if (Array.isArray(obj)) {
      return;
    }

    // Check if current object has the <rules> tag
    if (RULES_TAG in obj) {
      // Add the path to this rules location
      const pathString = currentPath.join('.');
      if (pathString) {
        rulePaths.push(pathString);
      }
    }

    // Continue traversing nested objects
    for (const key in obj) {
      // Skip the <rules> tag itself as we've already recorded this path
      if (key === RULES_TAG) {
        continue;
      }

      const value = obj[key];
      if (value && typeof value === 'object' && !Array.isArray(value)) {
        // Recursively traverse nested objects (but not arrays)
        traverse(value, [...currentPath, key]);
      }
    }
  }

  // Start traversal from the root
  traverse(methodology);

  // Sort paths for consistent output
  return rulePaths.sort();
}

/**
 * Get a specific rule from methodology by its path.
 * @param methodology - The methodology object
 * @param path - The dot-notation path to the rule (e.g., 'processDataSet.processInformation.dataSetInformation.name.baseName')
 * @returns The rule object at the specified path, or null if not found
 */
function getRuleFromMethodologyByPath(
  methodology: Record<string, any>,
  path: string
): any | null {
  // First, verify the path exists in the rule paths
  const rulePaths = listRulePathsFromMethodology(methodology);
  const rulePathExists = rulePaths.includes(path);

  if (!rulePathExists) {
    throw new Error(
      `Rule path not found: ${path}. Available paths: ${rulePaths.join(', ')}`
    );
  }

  // Navigate to the rule using the path
  const pathParts = path.split('.');
  let current: any = methodology;

  // Traverse the object using the path parts
  for (const part of pathParts) {
    if (current && typeof current === 'object' && part in current) {
      current = current[part];
    } else {
      // Path doesn't exist in the object
      return null;
    }
  }

  // Return the rules at this path
  if (current && typeof current === 'object' && RULES_TAG in current) {
    const rules = current[RULES_TAG];

    // Return the rules with additional context
    return {
      path,
      rules,
      // Include any other properties at this level (excluding the rules tag itself)
      ...Object.keys(current)
        .filter((key) => key !== RULES_TAG)
        .reduce(
          (acc, key) => {
            acc[key] = current[key];
            return acc;
          },
          {} as Record<string, any>
        ),
    };
  }

  return null;
}

/**
 * Get methodology data by type - convenience wrapper.
 * @param methodologyType - The type of methodology to retrieve
 * @returns The methodology data object, or null if not found
 */
async function readMethodologyFile(methodologyType: string): Promise<Record<string, any> | null> {
  return getMethodologyData(methodologyType);
}

/**
 * Get all rule paths for a specific methodology type.
 * @param methodologyType - The type of methodology (e.g., 'processes', 'flows')
 * @returns An array of dot-notation paths to rules locations
 */
function getRulePathsForMethodologyType(methodologyType: string): string[] {
  const methodologyData = getMethodologyData(methodologyType);
  if (!methodologyData) {
    throw new Error(`Methodology type '${methodologyType}' not found. Available types: ${availableMethodologies.join(', ')}`);
  }
  return listRulePathsFromMethodology(methodologyData);
}

/**
 * Get a specific rule for a methodology type and path.
 * @param methodologyType - The type of methodology (e.g., 'processes', 'flows')
 * @param rulePath - The dot-notation path to the rule
 * @returns The rule object at the specified path, or null if not found
 */
function getRuleForMethodologyType(methodologyType: string, rulePath: string): any | null {
  const methodologyData = getMethodologyData(methodologyType);
  if (!methodologyData) {
    throw new Error(`Methodology type '${methodologyType}' not found. Available types: ${availableMethodologies.join(', ')}`);
  }
  return getRuleFromMethodologyByPath(methodologyData, rulePath);
}

export {
  getMethodologyData,
  getAvailableMethodologyTypes,
  getBundleMetadata,
  listRulePathsFromMethodology,
  getRuleFromMethodologyByPath,
  readMethodologyFile,
  getRulePathsForMethodologyType,
  getRuleForMethodologyType,
  RULES_TAG,
  availableMethodologies,
};
