/**
 * Convert JSON Schema to TypeScript interfaces
 * A clean implementation without dependencies on json-schema-to-typescript
 */

import fs from 'fs';
import path from 'path';
import { format } from 'prettier';

interface TypeScriptConfig {
  /** Type mapping from JSON Schema types to TypeScript types */
  typeMappings: Record<string, string>;
  
  /** Mapping of type names to their source files for imports */
  importMappings: Record<string, string>;
  
  /** Prefix to remove from filenames when generating interface names */
  filenamePrefixToRemove: string;
  
  /** Whether to include descriptions as JSDoc comments */
  includeDescriptions: boolean;
  
  /** Export style: "export" or "declare" */
  exportStyle: string;
  
  /** Quote style for property names that need quotes */
  propertyQuoteStyle: string;
  
  /** Characters that require property names to be quoted */
  propertyQuoteTriggers: string[];
  
  /** Whether to generate imports */
  generateImports: boolean;
  
  /** Import path prefix (e.g., "./" or "@types/") */
  importPathPrefix: string;
  
  /** File extension for imports (e.g., ".js", "", etc.) */
  importExtension: string;
}

class JsonSchemaToTypeScript {
  private config: TypeScriptConfig;
  private interfaces: string[] = [];
  private typeDefinitions: Map<string, string> = new Map();
  private processedRefs: Set<string> = new Set();
  private referencedTypes: Set<string> = new Set();
  private currentFile?: string;

  constructor(config: TypeScriptConfig) {
    this.config = config;
  }

  convertSchemaToTypeScript(schema: any, interfaceName: string = "Root", currentFile?: string): string {
    // Reset state
    this.interfaces = [];
    this.typeDefinitions = new Map();
    this.processedRefs = new Set();
    this.referencedTypes = new Set();
    this.currentFile = currentFile;

    // Process $defs first if they exist
    if (schema.$defs) {
      for (const [defName, defSchema] of Object.entries(schema.$defs)) {
        this.processDefinition(defName, defSchema as any);
      }
    }

    // Process the main schema
    if (schema.properties || schema.type === "object") {
      const interfaceContent = this.processObject(schema, interfaceName);
      this.interfaces.push(interfaceContent);
    } else if (schema.oneOf || schema.anyOf) {
      // Handle top-level union types
      const tsType = this.getTypeScriptType(schema);
      this.typeDefinitions.set(interfaceName, `${this.config.exportStyle} type ${interfaceName} = ${tsType};`);
    } else if (["string", "number", "integer", "boolean", "array"].includes(schema.type)) {
      // Handle simple types at top level
      const tsType = this.getTypeScriptType(schema);
      this.typeDefinitions.set(interfaceName, `${this.config.exportStyle} type ${interfaceName} = ${tsType};`);
    }

    // Generate result
    const result: string[] = [];
    
    // Add file header
    result.push("/**");
    result.push(` * This file was automatically generated from ${currentFile || 'schema'}`);
    result.push(" * DO NOT MODIFY IT BY HAND. Instead, modify the source JSON Schema file,");
    result.push(" * and run the generation script to regenerate this file.");
    result.push(" */");
    result.push("");

    // Generate imports for referenced types
    if (this.referencedTypes.size > 0) {
      const imports = this.generateImports();
      if (imports.length > 0) {
        result.push(...imports);
        result.push("");
      }
    }

    // Add type definitions and interfaces
    if (this.typeDefinitions.size > 0) {
      result.push(...Array.from(this.typeDefinitions.values()));
      result.push("");
    }
    result.push(...this.interfaces);

    return result.join("\n");
  }

  private processDefinition(name: string, schema: any): void {
    if (this.processedRefs.has(name)) {
      return;
    }
    this.processedRefs.add(name);

    const tsType = this.getTypeScriptType(schema);
    if (schema.anyOf || schema.oneOf) {
      // For union types, create a type alias
      this.typeDefinitions.set(name, `${this.config.exportStyle} type ${name} = ${tsType};`);
    } else if (schema.type === "object" && schema.properties) {
      // For objects, create an interface
      const interfaceContent = this.processObject(schema, name);
      this.typeDefinitions.set(name, interfaceContent);
    } else {
      // For simple types, create a type alias
      this.typeDefinitions.set(name, `${this.config.exportStyle} type ${name} = ${tsType};`);
    }
  }

  private processObject(schema: any, interfaceName: string): string {
    const lines: string[] = [`${this.config.exportStyle} interface ${interfaceName} {`];
    
    const properties = schema.properties || {};
    const requiredFields = new Set(schema.required || []);

    for (const [propName, propSchema] of Object.entries(properties)) {
      const propSchemaObj = propSchema as any;
      
      // Handle description
      if (this.config.includeDescriptions && propSchemaObj.description) {
        lines.push(`  /**`);
        lines.push(`   * ${propSchemaObj.description}`);
        lines.push(`   */`);
      }

      // Determine if property is optional
      const isOptional = !requiredFields.has(propName);
      const optionalMarker = isOptional ? "?" : "";

      // Get TypeScript type
      const tsType = this.getTypeScriptType(propSchemaObj);

      // Handle property names that need quotes (e.g., @xmlns)
      const needsQuotes = this.config.propertyQuoteTriggers.some(trigger => 
        propName.startsWith(trigger) || propName.includes(trigger)
      );
      const quotedPropName = needsQuotes ? 
        `${this.config.propertyQuoteStyle}${propName}${this.config.propertyQuoteStyle}` : 
        propName;

      lines.push(`  ${quotedPropName}${optionalMarker}: ${tsType};`);
    }

    lines.push("}");
    return lines.join("\n");
  }

  private generateImports(): string[] {
    const imports: string[] = [];
    
    // Group imports by file
    const importsByFile: Record<string, string[]> = {};
    for (const typeName of this.referencedTypes) {
      if (typeName in this.config.importMappings) {
        const fileName = this.config.importMappings[typeName];
        // Don't import from the same file
        const currentFileStem = this.currentFile ? path.parse(this.currentFile).name : "";
        if (fileName !== currentFileStem) {
          if (!importsByFile[fileName]) {
            importsByFile[fileName] = [];
          }
          importsByFile[fileName].push(typeName);
        }
      }
    }

    // Generate import statements
    for (const [fileName, types] of Object.entries(importsByFile).sort()) {
      const typesStr = types.sort().join(", ");
      imports.push(`import type { ${typesStr} } from '${this.config.importPathPrefix}${fileName}${this.config.importExtension}';`);
    }

    return imports;
  }

  private getTypeScriptType(schema: any): string {
    // Handle $ref
    if (schema.$ref) {
      const refPath = schema.$ref;
      if (refPath.startsWith("#/$defs/")) {
        const refName = refPath.split("/").pop();
        // Don't add internal references to referencedTypes
        return refName;
      } else if (refPath.includes(".json#/$defs/")) {
        // External reference with specific definition
        const parts = refPath.split("#/$defs/");
        const typeName = parts[1];
        this.referencedTypes.add(typeName);
        return typeName;
      } else if (refPath.includes(".json")) {
        // External reference - use type name from file
        const fileStem = path.parse(refPath).name;
        const typeName = this.generateInterfaceName(fileStem);
        this.referencedTypes.add(typeName);
        return typeName;
      } else {
        return "any";
      }
    }

    // Handle const
    if (schema.const !== undefined) {
      const constValue = schema.const;
      if (typeof constValue === "string") {
        // Escape quotes and other special characters in string literals
        const escapedValue = constValue
          .replace(/\\/g, '\\\\')  // Escape backslashes first
          .replace(/"/g, '\\"')    // Escape double quotes
          .replace(/'/g, "\\'")    // Escape single quotes
          .replace(/\n/g, '\\n')   // Escape newlines
          .replace(/\r/g, '\\r')   // Escape carriage returns
          .replace(/\t/g, '\\t');  // Escape tabs
        return `"${escapedValue}"`;
      } else {
        return String(constValue);
      }
    }

    // Handle enum
    if (schema.enum) {
      return schema.enum.map((v: any) => {
        if (typeof v === "string") {
          // Escape quotes and other special characters in string literals
          const escapedValue = v
            .replace(/\\/g, '\\\\')  // Escape backslashes first
            .replace(/"/g, '\\"')    // Escape double quotes
            .replace(/'/g, "\\'")    // Escape single quotes
            .replace(/\n/g, '\\n')   // Escape newlines
            .replace(/\r/g, '\\r')   // Escape carriage returns
            .replace(/\t/g, '\\t');  // Escape tabs
          return `"${escapedValue}"`;
        } else {
          return String(v);
        }
      }).join(" | ");
    }

    // Handle anyOf/oneOf
    if (schema.anyOf || schema.oneOf) {
      const options = schema.anyOf || schema.oneOf;
      const types = options.map((option: any) => {
        const optionType = this.getTypeScriptType(option);
        // If it's an inline object, wrap in parentheses for clarity
        if (optionType.startsWith("{") && optionType.endsWith("}")) {
          return `(${optionType})`;
        }
        return optionType;
      });
      return types.join(" | ");
    }

    // Handle arrays
    if (schema.type === "array") {
      const itemsSchema = schema.items || {};
      if (Array.isArray(itemsSchema)) {
        // Tuple type
        const tupleTypes = itemsSchema.map(item => this.getTypeScriptType(item));
        return `[${tupleTypes.join(", ")}]`;
      } else {
        const itemType = this.getTypeScriptType(itemsSchema);
        return `${itemType}[]`;
      }
    }

    // Handle objects
    if (schema.type === "object" || (!schema.type && schema.properties)) {
      if (schema.properties) {
        // Inline object type - format nicely for complex objects
        const properties = schema.properties;
        const requiredFields = new Set(schema.required || []);
        const propCount = Object.keys(properties).length;
        
        // If there are many properties, format as multi-line
        if (propCount > 5) {
          const props: string[] = [];
          for (const [propName, propSchema] of Object.entries(properties)) {
            const isOptional = !requiredFields.has(propName);
            const optionalMarker = isOptional ? "?" : "";
            const tsType = this.getTypeScriptType(propSchema);

            const needsQuotes = this.config.propertyQuoteTriggers.some(trigger => 
              propName.startsWith(trigger) || propName.includes(trigger)
            );
            const quotedPropName = needsQuotes ? 
              `${this.config.propertyQuoteStyle}${propName}${this.config.propertyQuoteStyle}` : 
              propName;

            props.push(`    ${quotedPropName}${optionalMarker}: ${tsType};`);
          }
          return `{\n${props.join('\n')}\n  }`;
        } else {
          // Simple inline object
          const props: string[] = [];
          for (const [propName, propSchema] of Object.entries(properties)) {
            const isOptional = !requiredFields.has(propName);
            const optionalMarker = isOptional ? "?" : "";
            const tsType = this.getTypeScriptType(propSchema);

            const needsQuotes = this.config.propertyQuoteTriggers.some(trigger => 
              propName.startsWith(trigger) || propName.includes(trigger)
            );
            const quotedPropName = needsQuotes ? 
              `${this.config.propertyQuoteStyle}${propName}${this.config.propertyQuoteStyle}` : 
              propName;

            props.push(`${quotedPropName}${optionalMarker}: ${tsType}`);
          }
          return `{ ${props.join("; ")} }`;
        }
      } else {
        return "Record<string, any>";
      }
    }

    // Handle basic types
    const jsonType = schema.type || "any";
    return this.config.typeMappings[jsonType] || "any";
  }

  private generateInterfaceName(filename: string): string {
    // Remove tidas_ prefix if present
    let name = filename;
    if (name.startsWith(`${this.config.filenamePrefixToRemove}_`)) {
      name = name.substring(this.config.filenamePrefixToRemove.length + 1);
    }

    // Convert to PascalCase
    const parts = name.split("_");
    return parts.map(part => part.charAt(0).toUpperCase() + part.slice(1)).join("");
  }

  async convertFile(inputPath: string, outputPath?: string): Promise<void> {
    const schema = JSON.parse(fs.readFileSync(inputPath, 'utf-8'));
    
    // Generate interface name from filename
    const interfaceName = this.generateInterfaceName(path.parse(inputPath).name);
    
    // Convert to TypeScript
    let typescriptCode = this.convertSchemaToTypeScript(schema, interfaceName, path.parse(inputPath).name);
    
    // Format with Prettier
    try {
      typescriptCode = await format(typescriptCode, {
        parser: 'typescript',
        semi: true,
        singleQuote: true,
        trailingComma: 'es5',
        tabWidth: 2,
        printWidth: 80,
      });
    } catch (error) {
      console.warn(`Warning: Could not format ${inputPath} with Prettier:`, error);
      // Continue with unformatted code
    }
    
    // Determine output path
    const output = outputPath || inputPath.replace('.json', '.ts');
    
    // Write output
    fs.writeFileSync(output, typescriptCode, 'utf-8');
    
    console.log(`Generated TypeScript interface: ${output}`);
  }
}

function createTidasConfig(): TypeScriptConfig {
  return {
    typeMappings: {
      "string": "string",
      "number": "number", 
      "integer": "number",
      "boolean": "boolean",
      "null": "null"
    },
    importMappings: {
      // Data types
      "UUID": "tidas_data_types",
      "CASNumber": "tidas_data_types", 
      "FT": "tidas_data_types",
      "StringMultiLang": "tidas_data_types",
      "Int1": "tidas_data_types",
      "Int5": "tidas_data_types",
      "Int6": "tidas_data_types",
      "LevelType": "tidas_data_types",
      "Perc": "tidas_data_types",
      "MatR": "tidas_data_types",
      "MatV": "tidas_data_types",
      "Real": "tidas_data_types",
      "ST": "tidas_data_types",
      "String": "tidas_data_types",
      "STMultiLang": "tidas_data_types",
      "FTMultiLang": "tidas_data_types",
      "GlobalReferenceType": "tidas_data_types",
      "GIS": "tidas_data_types",
      "Year": "tidas_data_types",
      "dateTime": "tidas_data_types",
      // Category types
      "LocationsCategory": "tidas_locations_category",
      "FlowpropertiesCategory": "tidas_flowproperties_category",
      "ContactsCategory": "tidas_contacts_category",
      "SourcesCategory": "tidas_sources_category",
      "UnitgroupsCategory": "tidas_unitgroups_category",
      "ProcessesCategory": "tidas_processes_category",
      "LciamethodsCategory": "tidas_lciamethods_category",
      "FlowsElementaryCategory": "tidas_flows_elementary_category",
      "FlowsProductCategory": "tidas_flows_product_category",
    },
    filenamePrefixToRemove: "tidas",
    includeDescriptions: true,
    exportStyle: "export",
    propertyQuoteStyle: '"',
    propertyQuoteTriggers: ["@", "#", ":"],
    generateImports: true,
    importPathPrefix: "./",
    importExtension: ""
  };
}

export { JsonSchemaToTypeScript, createTidasConfig, TypeScriptConfig };