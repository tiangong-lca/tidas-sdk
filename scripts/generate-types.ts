#!/usr/bin/env node

/**
 * New TypeScript generation script using our custom JSON Schema converter
 */

import fs from 'fs';
import path from 'path';
import { JsonSchemaToTypeScript, createTidasConfig } from './json-schema-to-typescript.js';

const SCHEMAS_DIR = path.join(__dirname, '../tidas/schemas');
const OUTPUT_DIR = path.join(__dirname, '../src/types');

async function main() {
  // Ensure output directory exists
  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }

  // Create converter with TIDAS configuration
  const config = createTidasConfig();
  const converter = new JsonSchemaToTypeScript(config);

  // Find all JSON schema files
  const schemaFiles = fs.readdirSync(SCHEMAS_DIR)
    .filter(file => file.endsWith('.json'))
    .sort();

  console.log(`Found ${schemaFiles.length} schema files:`);
  schemaFiles.forEach(file => console.log(`  - ${file}`));

  // Convert each schema file
  for (const schemaFile of schemaFiles) {
    const inputPath = path.join(SCHEMAS_DIR, schemaFile);
    const outputFile = schemaFile.replace('.json', '.ts');
    const outputPath = path.join(OUTPUT_DIR, outputFile);

    console.log(`\nConverting ${schemaFile} -> ${outputFile}`);
    
    try {
      await converter.convertFile(inputPath, outputPath);
      console.log(`✓ Successfully generated ${outputFile}`);
    } catch (error) {
      console.error(`✗ Error converting ${schemaFile}:`, error);
    }
  }

  // Generate index file
  generateIndexFile(schemaFiles);
  
  console.log('\nType generation completed!');
}

function generateIndexFile(schemaFiles: string[]) {
  const indexPath = path.join(OUTPUT_DIR, 'index.ts');
  const lines: string[] = [
    '/**',
    ' * Automatically generated index file for all Tidas types',
    ' */',
    '',
  ];

  // Add exports for each generated file
  for (const schemaFile of schemaFiles) {
    const moduleName = schemaFile.replace('.json', '');
    lines.push(`export * from './${moduleName}';`);
  }

  lines.push('');
  lines.push('// Re-export commonly used types with simpler names');
  lines.push("export { Flows as FlowDataSet } from './tidas_flows';");
  lines.push("export { Lifecyclemodels as LifeCycleModelDataSet } from './tidas_lifecyclemodels';");
  lines.push("export { Processes as ProcessDataSet } from './tidas_processes';");
  lines.push('');
  lines.push('// Import types for union type');
  lines.push("import type { Flows } from './tidas_flows';");
  lines.push("import type { Lifecyclemodels } from './tidas_lifecyclemodels';");
  lines.push("import type { Processes } from './tidas_processes';");
  lines.push('');
  lines.push('// Union type for all data sets');
  lines.push('export type DataSet = ');
  lines.push('  | Flows');
  lines.push('  | Lifecyclemodels');
  lines.push('  | Processes;');
  lines.push('');

  fs.writeFileSync(indexPath, lines.join('\n'), 'utf-8');
  console.log(`✓ Generated index file: ${indexPath}`);
}

if (require.main === module) {
  main().catch(console.error);
}