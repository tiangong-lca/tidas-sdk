#!/usr/bin/env node

/**
 * New TypeScript generation script using our custom JSON Schema converter
 */

import fs from 'fs';
import path from 'path';
import {
  JsonSchemaToTypeScript,
  createTidasConfig,
} from './json-schema-to-typescript.js';

const SCHEMAS_DIR = path.join(__dirname, '../tidas/schemas');
const OUTPUT_DIR = path.join(__dirname, '../src/types');

// 新增：自动生成 multi-lang-types.ts
function generateMultiLangTypesFile() {
  const multiLangPath = path.join(OUTPUT_DIR, 'multi-lang-types.ts');
  const content = `export class MultiLangArray extends Array<{ '@xml:lang': string; '#text': string }> {
  setText(value: string, lang: string = 'en') {
    const existing = this.find(item => item['@xml:lang'] === lang);
    if (existing) {
      existing['#text'] = value;
    } else {
      this.push({ '@xml:lang': lang, '#text': value });
    }
  }
}

export class MultiLangItemClass {
  '@xml:lang': string;
  '#text': string;
  constructor(lang: string, text: string) {
    this['@xml:lang'] = lang;
    this['#text'] = text;
  }
  setText(value: string, lang: string = 'en') {
    this['@xml:lang'] = lang;
    this['#text'] = value;
  }
}

export type MultiLangItem = MultiLangItemClass;
`;
  fs.writeFileSync(multiLangPath, content, 'utf-8');
  console.log(`✓ Generated multi-lang-types file: ${multiLangPath}`);
}

async function main() {
  // Ensure output directory exists
  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }

  // 新增：生成 multi-lang-types.ts
  generateMultiLangTypesFile();

  // Create converter with TIDAS configuration
  const config = createTidasConfig();
  const converter = new JsonSchemaToTypeScript(config);

  // Find all JSON schema files
  const schemaFiles = fs
    .readdirSync(SCHEMAS_DIR)
    .filter((file) => file.endsWith('.json'))
    .sort();

  console.log(`Found ${schemaFiles.length} schema files:`);
  schemaFiles.forEach((file) => console.log(`  - ${file}`));

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

function generateIndexFile(_schemaFiles: string[]) {
  const indexPath = path.join(OUTPUT_DIR, 'index.ts');
  const lines: string[] = [
    '/**',
    ' * Automatically generated index file for all Tidas types',
    ' */',
    '',
  ];

  // Add exports for each generated file
  // for (const schemaFile of schemaFiles) {
  // const moduleName = schemaFile.replace('.json', '');
  // lines.push(`export * from './${moduleName}';`);
  // }

  lines.push('');
  lines.push('// Re-export commonly used types with simpler names');
  lines.push("export { Contacts as Contact } from './tidas_contacts';");
  lines.push("export { Flows as Flow } from './tidas_flows';");
  lines.push("export { Processes as Process } from './tidas_processes';");
  lines.push("export { Sources as Source } from './tidas_sources';");
  lines.push(
    "export { Flowproperties as FlowProperty } from './tidas_flowproperties';"
  );
  lines.push("export { Unitgroups as UnitGroup } from './tidas_unitgroups';");
  lines.push(
    "export { Lciamethods as LCIAMethod } from './tidas_lciamethods';"
  );
  lines.push(
    "export { Lifecyclemodels as LifeCycleModel } from './tidas_lifecyclemodels';"
  );
  lines.push('');
  // lines.push('// Legacy aliases for backward compatibility');
  // lines.push("export { Flows as FlowDataSet } from './tidas_flows';");
  // lines.push("export { Lifecyclemodels as LifeCycleModelDataSet } from './tidas_lifecyclemodels';");
  // lines.push("export { Processes as ProcessDataSet } from './tidas_processes';");
  // lines.push('');
  lines.push('// Import types for union type');
  lines.push("import type { Contacts as Contact } from './tidas_contacts';");
  lines.push("import type { Flows as Flow } from './tidas_flows';");
  lines.push("import type { Processes as Process } from './tidas_processes';");
  lines.push("import type { Sources as Source } from './tidas_sources';");
  lines.push(
    "import type { Flowproperties as FlowProperty } from './tidas_flowproperties';"
  );
  lines.push(
    "import type { Unitgroups as UnitGroup } from './tidas_unitgroups';"
  );
  lines.push(
    "import type { Lciamethods as LCIAMethod } from './tidas_lciamethods';"
  );
  lines.push(
    "import type { Lifecyclemodels as LifeCycleModel } from './tidas_lifecyclemodels';"
  );
  lines.push('');
  lines.push('// Union type for all data sets');
  lines.push('export type DataSet = ');
  lines.push('  | Contact');
  lines.push('  | Flow');
  lines.push('  | Process');
  lines.push('  | Source');
  lines.push('  | FlowProperty');
  lines.push('  | UnitGroup');
  lines.push('  | LCIAMethod');
  lines.push('  | LifeCycleModel;');
  lines.push('');

  fs.writeFileSync(indexPath, lines.join('\n'), 'utf-8');
  console.log(`✓ Generated index file: ${indexPath}`);
}

if (require.main === module) {
  main().catch(console.error);
}
