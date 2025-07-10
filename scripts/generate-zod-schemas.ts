#!/usr/bin/env ts-node

import fs from 'fs';
import path from 'path';
import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

// Types for dependency analysis
interface DependencyGraph {
  [fileName: string]: string[];
}

interface TypeFileInfo {
  fileName: string;
  filePath: string;
  dependencies: string[];
  isMainType: boolean;
}

// Configuration
const TYPES_DIR = 'src/types';
const SCHEMAS_DIR = 'src/schemas';
const CONFIG_FILE = 'ts-to-zod.config.js';
const CONFIG_SAVE_DIR = 'src/schemas/ts-to-zod-configs';

// Main types to generate schemas for - these are the primary interfaces we want to validate
const MAIN_TYPES = [
  'tidas_contacts',
  'tidas_processes', 
  'tidas_flows',
  'tidas_sources',
  'tidas_flowproperties',
  'tidas_unitgroups',
  'tidas_lciamethods',
  'tidas_lifecyclemodels'
];

// Core dependency types that other types depend on
const CORE_DEPENDENCY_TYPES = [
  'tidas_data_types'
];

// Category/enum types that are dependencies
const CATEGORY_DEPENDENCY_TYPES = [
  'tidas_locations_category',
  'tidas_contacts_category',
  'tidas_flowproperties_category',
  'tidas_flows_elementary_category',
  'tidas_flows_product_category',
  'tidas_lciamethods_category',
  'tidas_processes_category',
  'tidas_sources_category',
  'tidas_unitgroups_category'
];

// All types that need to be processed (main + dependencies)
const ALL_PROCESSABLE_TYPES = [...CORE_DEPENDENCY_TYPES, ...CATEGORY_DEPENDENCY_TYPES, ...MAIN_TYPES];

async function generateZodSchemas(): Promise<void> {
  console.log('🚀 Generating Zod schemas from TypeScript types...\n');
  
  // Generate ts-to-zod configuration
  await generateTsToZodConfig();
  
  // Ensure schemas directory exists
  if (!fs.existsSync(SCHEMAS_DIR)) {
    fs.mkdirSync(SCHEMAS_DIR, { recursive: true });
  }
  
  // Clean existing schemas
  console.log('🧹 Cleaning existing schemas...');
  const existingSchemas = fs.readdirSync(SCHEMAS_DIR).filter(file => file.endsWith('.schema.ts'));
  for (const schema of existingSchemas) {
    fs.unlinkSync(path.join(SCHEMAS_DIR, schema));
    console.log(`   🗑️  Removed: ${schema}`);
  }
  
  // Get dependency-sorted types for processing
  const sortedTypes = await analyzeTypeDependencies();
  const typeNames = sortedTypes.map(t => t.fileName);
  
  // Run ts-to-zod with configuration, processing each type in dependency order
  console.log('\n📦 Running ts-to-zod for each type in dependency order...');
  
  // Process all types using standard config approach
  for (const typeName of typeNames) {
    const configName = typeName.replace('tidas_', '');
    console.log(`🔄 Processing ${typeName}...`);
    
    try {
      const { stderr } = await execAsync(`npx ts-to-zod --config=${configName} --skipValidation`);
      
      const outputFile = path.join(SCHEMAS_DIR, `${typeName}.schema.ts`);
      if (fs.existsSync(outputFile)) {
        console.log(`   ✅ ${typeName}.schema.ts generated successfully`);
        
        // Post-process the generated schema to fix constraint placement
        await postProcessZodSchema(outputFile);
      } else {
        console.log(`   ❌ ${typeName}.schema.ts failed to generate`);
        if (stderr) {
          console.log(`   📋 Error details:`, stderr);
        }
      }
      
    } catch (error) {
      console.log(`   ❌ Failed to process ${typeName}:`, (error as Error).message);
      
      // If ts-to-zod fails, try fallback approach
      console.log(`   🔄 Trying fallback approach for ${typeName}...`);
      await generateFallbackSchema(typeName);
    }
  }
  
  // Final verification
  console.log('\n✅ Final verification of generated schemas:');
  // Need to include tidas_data_types back for verification
  const allTypeNames = sortedTypes.map(t => t.fileName);
  const successCount = allTypeNames.filter(typeName => {
    const outputFile = path.join(SCHEMAS_DIR, `${typeName}.schema.ts`);
    const exists = fs.existsSync(outputFile);
    console.log(`   ${exists ? '✅' : '❌'} ${typeName}.schema.ts`);
    return exists;
  }).length;
  
  console.log(`\n📊 Generated ${successCount}/${allTypeNames.length} schemas successfully`)
  
  // Generate enhanced index file
  await generateSchemasIndex();
  
  // Clean up config file
  if (fs.existsSync(CONFIG_FILE)) {
    fs.unlinkSync(CONFIG_FILE);
    console.log(`🧹 Cleaned up: ${CONFIG_FILE}`);
  }
  
  console.log('\n🎉 Zod schema generation completed successfully!');
}

/**
 * Get correct dataset key for each type
 */
function getDataSetKeyForType(typeName: string): string {
  switch (typeName) {
    case 'tidas_contacts': return 'contactDataSet';
    case 'tidas_processes': return 'processDataSet';  
    case 'tidas_flows': return 'flowDataSet';
    case 'tidas_sources': return 'sourceDataSet';
    case 'tidas_flowproperties': return 'flowPropertyDataSet';
    case 'tidas_unitgroups': return 'unitGroupDataSet';
    case 'tidas_lciamethods': return 'LCIAMethodDataSet';
    case 'tidas_lifecyclemodels': return 'lifeCycleModelDataSet';
    default: return typeName.replace('tidas_', '') + 'DataSet';
  }
}


/**
 * Post-process generated Zod schema to fix constraint placement
 */
async function postProcessZodSchema(schemaFile: string): Promise<void> {
  const content = fs.readFileSync(schemaFile, 'utf8');
  let fixedContent = content;
  
  // For tidas_data_types, apply specific constraint fixes
  if (schemaFile.includes('tidas_data_types')) {
    // Fix StringMultiLang schemas - should have max(500)
    fixedContent = fixedContent.replace(
      /StringMultiLangSchema = z\.union\(\[([\s\S]*?)\]\);/g,
      (match, unionContent) => {
        const fixedUnion = unionContent.replace(/('#text':\s*z\.string\(\)),/g, "'#text': z.string().max(500),");
        return `StringMultiLangSchema = z.union([${fixedUnion}]);`;
      }
    );
    
    // Fix STMultiLang schemas - should have max(1000)  
    fixedContent = fixedContent.replace(
      /STMultiLangSchema = z\.union\(\[([\s\S]*?)\]\);/g,
      (match, unionContent) => {
        const fixedUnion = unionContent.replace(/('#text':\s*z\.string\(\)),/g, "'#text': z.string().max(1000),");
        return `STMultiLangSchema = z.union([${fixedUnion}]);`;
      }
    );
  }
  
  // Apply intelligent constraint fixes for all schemas
  // Pattern 1: Fix object-level constraints and move them to #text property
  const newContent1 = fixedContent.replace(
    /('#text':\s*z\.string\(\)),(\s*\}\)\s*\.max\((\d+)\))/g,
    "'#text': z.string().max($3),\n    }))"
  );
  
  // Pattern 2: Fix array-level constraints and move them to #text property within objects
  const newContent2 = newContent1.replace(
    /('#text':\s*z\.string\(\)),(\s*\}\)\s*\)\s*\.max\((\d+)\))/g,
    "'#text': z.string().max($3),\n    })\n  )"
  );
  
  // Pattern 3: Fix union-level constraints by identifying and replacing them
  const unionMaxPattern = /(\w+Schema = z\.union\(\[[\s\S]*?'#text':\s*z\.string\(\)[\s\S]*?\]\))\.max\((\d+)\);/g;
  const newContent3 = newContent2.replace(unionMaxPattern, (match, unionPart, maxValue) => {
    const fixedUnion = unionPart.replace(/('#text':\s*z\.string\(\))/g, `'#text': z.string().max(${maxValue})`);
    return `${fixedUnion};`;
  });
  
  fixedContent = newContent3;
  const hasChanges = fixedContent !== content;
  
  if (hasChanges) {
    fs.writeFileSync(schemaFile, fixedContent, 'utf8');
    console.log(`   🔧 Applied constraint fixes to ${path.basename(schemaFile)}`);
  }
}

/**
 * Generate fallback schema when ts-to-zod fails
 */
async function generateFallbackSchema(typeName: string): Promise<void> {
  const outputFile = path.join(SCHEMAS_DIR, `${typeName}.schema.ts`);
  const dataSetKey = getDataSetKeyForType(typeName);
  const schemaName = typeName.split('_').map(part => 
    part.charAt(0).toUpperCase() + part.slice(1)
  ).join('') + 'Schema';
  
  // Create a basic schema that imports from data types and exports a permissive schema
  const fallbackContent = `// Generated fallback schema for ${typeName}
import { z } from 'zod';

// Import base types (this might need manual adjustment)
import {
  UUIDSchema,
  StringMultiLangSchema,
  StringSchema,
  STMultiLangSchema,
  FTMultiLangSchema,
  GlobalReferenceTypeSchema,
  dateTimeSchema
} from './tidas_data_types.schema';

// Fallback schema - allows any structure but provides type checking for common fields
export const ${schemaName} = z.object({
  ${dataSetKey}: z.object({
    // Common XML namespace attributes
    '@xmlns': z.string().optional(),
    '@xmlns:common': z.string().optional(),
    '@xmlns:xsi': z.string().optional(),
    '@version': z.string().optional(),
    '@xsi:schemaLocation': z.string().optional(),
    
    // Allow any additional properties
  }).passthrough()
}).passthrough();

// Note: This is a fallback schema. For full validation, 
// the schema should be manually refined based on the actual type structure.
`;

  try {
    fs.writeFileSync(outputFile, fallbackContent, 'utf8');
    console.log(`   ✅ Generated fallback schema: ${outputFile}`);
  } catch (error) {
    console.log(`   ❌ Failed to generate fallback schema: ${(error as Error).message}`);
  }
}

/**
 * Analyze TypeScript files to understand their import dependencies
 */
async function analyzeTypeDependencies(): Promise<TypeFileInfo[]> {
  console.log('🔍 Analyzing TypeScript dependencies...');
  
  const typesFiles = fs.readdirSync(TYPES_DIR)
    .filter(file => file.startsWith('tidas_') && file.endsWith('.ts'))
    .map(file => file.replace('.ts', ''));
  
  console.log(`   Found ${typesFiles.length} TypeScript files`);
  
  const dependencyGraph: DependencyGraph = {};
  const typeFileInfos: TypeFileInfo[] = [];
  
  // Build dependency graph by parsing import statements
  for (const fileName of typesFiles) {
    const filePath = path.join(TYPES_DIR, `${fileName}.ts`);
    const content = fs.readFileSync(filePath, 'utf8');
    
    const dependencies = parseImportStatements(content, fileName);
    dependencyGraph[fileName] = dependencies;
    
    typeFileInfos.push({
      fileName,
      filePath,
      dependencies,
      isMainType: ALL_PROCESSABLE_TYPES.includes(fileName)
    });
  }
  
  // Filter to only include types we want to process
  const processableTypes = typeFileInfos.filter(info => info.isMainType);
  
  console.log(`   Analyzed dependencies for ${processableTypes.length} processable types`);
  
  // Sort types based on dependencies using topological sort
  const sortedTypes = topologicalSort(processableTypes, dependencyGraph);
  
  // Display dependency information
  console.log('\n📊 Dependency Analysis Results:');
  sortedTypes.forEach((typeInfo, index) => {
    const depsList = typeInfo.dependencies.length > 0 
      ? typeInfo.dependencies.join(', ') 
      : 'none';
    console.log(`   ${index + 1}. ${typeInfo.fileName} (deps: ${depsList})`);
  });
  
  return sortedTypes;
}

/**
 * Parse import statements from TypeScript file content
 */
function parseImportStatements(content: string, currentFileName: string): string[] {
  const dependencies: string[] = [];
  const importRegex = /import\s+(?:type\s+)?{[^}]+}\s+from\s+['"]\.\/([^'"]+)['"]/g;
  
  let match: RegExpExecArray | null;
  while ((match = importRegex.exec(content)) !== null) {
    const importedFile = match[1];
    // Only track dependencies on tidas_ files to avoid circular references
    if (importedFile.startsWith('tidas_') && importedFile !== currentFileName) {
      dependencies.push(importedFile);
    }
  }
  
  return [...new Set(dependencies)]; // Remove duplicates
}

/**
 * Topological sort to determine correct processing order
 */
function topologicalSort(types: TypeFileInfo[], dependencyGraph: DependencyGraph): TypeFileInfo[] {
  const visited = new Set<string>();
  const visiting = new Set<string>();
  const result: TypeFileInfo[] = [];
  const typeMap = new Map(types.map(t => [t.fileName, t]));
  
  function visit(fileName: string): void {
    if (visited.has(fileName)) return;
    
    if (visiting.has(fileName)) {
      console.log(`   ⚠️  Circular dependency detected involving ${fileName}`);
      return;
    }
    
    visiting.add(fileName);
    
    // Visit dependencies first
    const dependencies = dependencyGraph[fileName] || [];
    for (const dep of dependencies) {
      // Only process dependencies that are in our types to process
      if (typeMap.has(dep)) {
        visit(dep);
      }
    }
    
    visiting.delete(fileName);
    visited.add(fileName);
    
    const typeInfo = typeMap.get(fileName);
    if (typeInfo) {
      result.push(typeInfo);
    }
  }
  
  // Visit all types
  for (const typeInfo of types) {
    visit(typeInfo.fileName);
  }
  
  return result;
}

/**
 * Generate ts-to-zod configuration file using dependency analysis
 */
async function generateTsToZodConfig(): Promise<void> {
  console.log('⚙️  Generating ts-to-zod configuration with dependency analysis...');
  
  // Analyze dependencies to get correct processing order
  const sortedTypes = await analyzeTypeDependencies();
  
  const configs = sortedTypes.map(typeInfo => ({
    name: typeInfo.fileName.replace('tidas_', ''),
    input: `${TYPES_DIR}/${typeInfo.fileName}.ts`,
    output: `${SCHEMAS_DIR}/${typeInfo.fileName}.schema.ts`,
    getSchemaName: '(id) => `${id}Schema`',
    skipValidation: true,
    keepComments: false,
    skipParseJSDoc: false // Enable JSDoc parsing for constraint extraction
  }));
  
  const configContent = `/**
 * ts-to-zod configuration - Auto-generated with dependency analysis
 * Processing order determined by import dependencies
 * @type {import("ts-to-zod").TsToZodConfig}
 */
module.exports = [
${configs.map(config => `  {
    name: "${config.name}",
    input: "${config.input}",
    output: "${config.output}",
    getSchemaName: ${config.getSchemaName},
    skipValidation: ${config.skipValidation},
    keepComments: ${config.keepComments},
    skipParseJSDoc: ${config.skipParseJSDoc}
  }`).join(',\n')}
];`;

  fs.writeFileSync(CONFIG_FILE, configContent, 'utf8');
  
  // Save configuration files for debugging
  if (!fs.existsSync(CONFIG_SAVE_DIR)) {
    fs.mkdirSync(CONFIG_SAVE_DIR, { recursive: true });
  }
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  const savedConfigFile = path.join(CONFIG_SAVE_DIR, `ts-to-zod.config.${timestamp}.js`);
  fs.writeFileSync(savedConfigFile, configContent, 'utf8');
  
  console.log(`   ✅ Generated configuration for ${configs.length} types in dependency order`);
  console.log(`   📁 Configuration saved to: ${savedConfigFile}`);
}

async function generateSchemasIndex(): Promise<void> {
  console.log('📋 Generating enhanced schemas index file...');
  
  // Get all generated schemas
  const allGeneratedTypes = (await analyzeTypeDependencies()).map(t => t.fileName);
  
  const indexContent = `/**
 * Automatically generated index file for all Zod schemas
 * Generated with dependency analysis
 */

// Export all schemas
${allGeneratedTypes.map(typeName => `export * from './${typeName}.schema';`).join('\n')}

// Re-export commonly used schemas with simpler names
export { ContactsSchema } from './tidas_contacts.schema';
export { SourcesSchema } from './tidas_sources.schema';
export { FlowpropertiesSchema } from './tidas_flowproperties.schema';
export { UnitgroupsSchema } from './tidas_unitgroups.schema';
export { LciamethodsSchema } from './tidas_lciamethods.schema';
export { LifecyclemodelsSchema } from './tidas_lifecyclemodels.schema';

// Export category/enum types (if schemas exist)
export { LocationsCategorySchema } from './tidas_locations_category.schema';
export { ContactsCategorySchema } from './tidas_contacts_category.schema';
export { FlowpropertiesCategorySchema } from './tidas_flowproperties_category.schema';
export { FlowsElementaryCategorySchema } from './tidas_flows_elementary_category.schema';
export { FlowsProductCategorySchema } from './tidas_flows_product_category.schema';
export { LciamethodsCategorySchema } from './tidas_lciamethods_category.schema';
export { ProcessesCategorySchema } from './tidas_processes_category.schema';
export { SourcesCategorySchema } from './tidas_sources_category.schema';
export { UnitgroupsCategorySchema } from './tidas_unitgroups_category.schema';

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
        message: \`Invalid JSON: \${error instanceof Error ? error.message : 'Unknown error'}\`,
        path: [],
        input: undefined as any
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
`;
  
  const indexFile = path.join(SCHEMAS_DIR, 'index.ts');
  fs.writeFileSync(indexFile, indexContent, 'utf8');
  console.log(`   ✅ Generated: ${indexFile}`);
}

// Run the generator
generateZodSchemas().catch(console.error);