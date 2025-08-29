import { existsSync } from 'node:fs';
import fs from 'node:fs/promises';
import path from 'path';
import yaml from 'yaml';

const TIDAS_TOOLS_DIR = path.join(
  __dirname,
  '../../../tidas-tools/src/tidas_tools/tidas/'
);

const SDK_ROOT_DIR = path.join(__dirname, '../../../');
const DIST_DIR = path.join(SDK_ROOT_DIR, 'dist');

/**
 * Path to the TIDAS tools directory.
 */
let METHODOLOGY_DIR = path.join(TIDAS_TOOLS_DIR, 'methodologies');

// check METHODOLOGY_DIR exists
if (!existsSync(METHODOLOGY_DIR)) {
  // Use dist path
  METHODOLOGY_DIR = path.join(DIST_DIR, 'methodologies');
}

/**
 * Path to the TIDAS schemas directory.
 */
const SCHEMA_DIR = path.join(TIDAS_TOOLS_DIR, 'schemas');

/**
 * Tag used to identify rules in the methodology yaml files.
 */
const RULES_TAG = '<rules>';

/**
 * Mapping of methodology files to their paths.
 * @type {Record<string, string>}
 */
const methodologyFilesMapping: Record<string, string> = {
  contacts: path.join(METHODOLOGY_DIR, 'tidas_contacts.yaml'),
  contacts_category: path.join(METHODOLOGY_DIR, 'tidas_contacts_category.yaml'),
  data_types: path.join(METHODOLOGY_DIR, 'tidas_data_types.yaml'),
  flowproperties_category: path.join(
    METHODOLOGY_DIR,
    'tidas_flowproperties_category.yaml'
  ),
  flowproperties: path.join(METHODOLOGY_DIR, 'tidas_flowproperties.yaml'),
  flows_elementary_category: path.join(
    METHODOLOGY_DIR,
    'tidas_flows_elementary_category.yaml'
  ),
  flows: path.join(METHODOLOGY_DIR, 'tidas_flows.yaml'),
  lifecyclemodels: path.join(METHODOLOGY_DIR, 'tidas_lifecyclemodels.yaml'),
  lciamethods: path.join(METHODOLOGY_DIR, 'tidas_lciamethods.yaml'),
  lciamethods_category: path.join(
    METHODOLOGY_DIR,
    'tidas_lciamethods_category.yaml'
  ),
  locations_category: path.join(
    METHODOLOGY_DIR,
    'tidas_locations_category.yaml'
  ),
  processes: path.join(METHODOLOGY_DIR, 'tidas_processes.yaml'),
  processes_category: path.join(
    METHODOLOGY_DIR,
    'tidas_processes_category.yaml'
  ),
  sources: path.join(METHODOLOGY_DIR, 'tidas_sources.yaml'),
  sources_category: path.join(METHODOLOGY_DIR, 'tidas_sources_category.yaml'),
  unitgroups: path.join(METHODOLOGY_DIR, 'tidas_unitgroups.yaml'),
  unitgroups_category: path.join(
    METHODOLOGY_DIR,
    'tidas_unitgroups_category.yaml'
  ),
};

/**
 * Read a methodology file and return the data as a JSON object.
 * @param filePath - The path to the methodology file.
 * @returns The data from the methodology file as a JSON object.
 */
async function readMethodologyFile(filePath: string) {
  const file = await fs.readFile(filePath, 'utf8');
  return yaml.parse(file);
}

/**
 * List all rule paths from a methodology object.
 * This function recursively traverses the methodology object and finds all paths
 * that contain the <rules> tag.
 *
 * @param methodology - The methodology object parsed from YAML
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
async function listRulePathsFromMethodology(
  methodology: Record<string, any>
): Promise<string[]> {
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
 * @param methodology - The methodology object parsed from YAML
 * @param path - The dot-notation path to the rule (e.g., 'processDataSet.processInformation.dataSetInformation.name.baseName')
 * @returns The rule object at the specified path, or null if not found
 */
async function getRuleFromMethodologyByPath(
  methodology: Record<string, any>,
  path: string
): Promise<any | null> {
  // First, verify the path exists in the rule paths
  const rulePaths = await listRulePathsFromMethodology(methodology);
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

export {
  readMethodologyFile,
  listRulePathsFromMethodology,
  getRuleFromMethodologyByPath,
  methodologyFilesMapping,
  RULES_TAG,
  TIDAS_TOOLS_DIR,
  METHODOLOGY_DIR,
  SCHEMA_DIR,
};
