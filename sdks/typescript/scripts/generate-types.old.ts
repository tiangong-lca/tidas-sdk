#!/usr/bin/env ts-node

import { compileFromFile } from 'json-schema-to-typescript';
import * as fs from 'fs';
import * as path from 'path';

const SCHEMA_DIR = path.join(
  __dirname,
  '../../../tidas-tools/src/tidas_tools/tidas/schemas'
);
const OUTPUT_DIR = path.join(__dirname, '../src/types/generated');

interface SchemaInfo {
  inputPath: string;
  outputPath: string;
  name: string;
}

// 特殊处理的属性映射
const ATTRIBUTE_MAPPING: Record<string, string> = {
  '@xmlns': 'xmlns',
  '@xmlns:common': 'xmlnsCommon',
  '@xmlns:xsi': 'xmlnsXsi',
  '@xmlns:ecn': 'xmlnsEcn',
  '@version': 'version',
  '@xsi:schemaLocation': 'xsiSchemaLocation',
  '@xml:lang': 'lang',
  '#text': 'value',
  '@level': 'level',
  '@classId': 'classId',
  '@catId': 'catId',
  '@location': 'location',
  '@latitudeAndLongitude': 'latitudeAndLongitude',
  '@dataSetInternalID': 'dataSetInternalID',
  '@type': 'type',
  '@name': 'name',
  '@value': 'value',
  '@allocatedFraction': 'allocatedFraction',
  '@internalReferenceToCoProduct': 'internalReferenceToCoProduct',
  '@subLocation': 'subLocation',
  '@locations': 'locations',
};

// 后处理数据类型引用，将内联的类型替换为对 tidas_data_types.ts 的引用
function postProcessDataTypeReferences(content: string, originalSchema?: any): string {
  if (!originalSchema) return content;
  
  // 获取所有可用的数据类型
  const availableDataTypes = [
    'STMultiLang', 'CASNumber', 'FT', 'StringMultiLang', 'Int1', 'Int5', 'Int6', 
    'LevelType', 'Perc', 'MatR', 'MatV', 'Real', 'ST', 'String', 'FTMultiLang', 
    'GlobalReferenceType', 'GIS', 'UUID', 'Year', 'DateTime'
  ];
  
  // 收集需要导入的类型和字段映射
  const neededImports = new Set<string>();
  const fieldTypeMap = new Map<string, string>();
  
  // 检查原始schema中是否有对tidas_data_types.json的引用
  const schemaString = JSON.stringify(originalSchema);
  const hasDataTypesRef = schemaString.includes('tidas_data_types.json#/$defs/');
  
  if (hasDataTypesRef) {
    let processed = content;
    
    // 收集所有字段名及其对应的数据类型
    availableDataTypes.forEach(typeName => {
      const refPattern = `tidas_data_types.json#/$defs/${typeName}`;
      if (schemaString.includes(refPattern)) {
        neededImports.add(typeName);
        
        // 找到所有引用此类型的字段
        const fieldRefRegex = new RegExp(`"([^"]+)":\\s*{[^}]*"\\$ref":\\s*"tidas_data_types\\.json#/\\$defs/${typeName}"[^}]*}`, 'g');
        let fieldMatch;
        
        while ((fieldMatch = fieldRefRegex.exec(schemaString)) !== null) {
          const fieldName = fieldMatch[1];
          fieldTypeMap.set(fieldName, typeName);
        }
      }
    });
    
    // 深度替换字段类型
    if (fieldTypeMap.size > 0) {
      // 替换简单的字符串类型字段
      fieldTypeMap.forEach((typeName, fieldName) => {
        const escapedFieldName = fieldName.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        
        // 模式1: 简单的字符串字段 - 处理带引号的字段名
        const quotedPattern = new RegExp(`(\\s+)(['"]${escapedFieldName}['"]):\\s*string;`, 'g');
        processed = processed.replace(quotedPattern, `$1$2: ${typeName};`);
        
        // 模式2: 简单的字符串字段 - 处理不带引号的字段名  
        const unquotedPattern = new RegExp(`(\\s+)(${escapedFieldName}):\\s*string;`, 'g');
        processed = processed.replace(unquotedPattern, `$1$2: ${typeName};`);
        
        // 模式3: 可选的字符串字段 - 带引号
        const optionalQuotedPattern = new RegExp(`(\\s+)(['"]${escapedFieldName}['"])\\?:\\s*string;`, 'g');
        processed = processed.replace(optionalQuotedPattern, `$1$2?: ${typeName};`);
        
        // 模式4: 可选的字符串字段 - 不带引号
        const optionalUnquotedPattern = new RegExp(`(\\s+)(${escapedFieldName})\\?:\\s*string;`, 'g');
        processed = processed.replace(optionalUnquotedPattern, `$1$2?: ${typeName};`);
        
        // 模式5: 数字字段 - 带引号
        const quotedNumberPattern = new RegExp(`(\\s+)(['"]${escapedFieldName}['"]):\\s*number;`, 'g');
        processed = processed.replace(quotedNumberPattern, `$1$2: ${typeName};`);
        
        // 模式6: 数字字段 - 不带引号
        const unquotedNumberPattern = new RegExp(`(\\s+)(${escapedFieldName}):\\s*number;`, 'g');
        processed = processed.replace(unquotedNumberPattern, `$1$2: ${typeName};`);
      });
      
      // 额外处理: 直接根据imports查找和替换常见的未捕获字段
      if (neededImports.has('UUID')) {
        processed = processed.replace(/(\\s+)(['"]common:UUID['"]):\\s*string;/g, '$1$2: UUID;');
        // 再试一次更直接的替换
        processed = processed.replace(/(\s+)(['"]common:UUID['"]):\s*string;/g, '$1$2: UUID;');
      }
      
      // 特殊处理复杂的多语言字段（StringMultiLang, FTMultiLang等）
      const multiLangFields = ['StringMultiLang', 'FTMultiLang', 'STMultiLang'];
      
      multiLangFields.forEach(multiLangType => {
        if (neededImports.has(multiLangType)) {
          fieldTypeMap.forEach((typeName, fieldName) => {
            if (typeName === multiLangType) {
              const escapedFieldName = fieldName.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
              
              // 替换复杂的多语言字段结构
              const multiLangPattern = new RegExp(
                `(\\s+)(['"]?${escapedFieldName}['"]?):\\s*` +
                `\\|?\\s*\\{[^}]*'@xml:lang':[^}]*\\}\\[\\]\\s*` +
                `\\|\\s*\\{[^}]*'@xml:lang':[^}]*\\};?`,
                'g'
              );
              
              processed = processed.replace(multiLangPattern, `$1$2: ${typeName};`);
              
              // 更通用的模式 - 匹配任何以 @xml:lang 开头的复杂结构
              const complexMultiLangPattern = new RegExp(
                `(\\s+)(['"]?${escapedFieldName}['"]?):\\s*` +
                `(\\|\\s*)?\\{[\\s\\S]*?'@xml:lang':[\\s\\S]*?\\}[\\s\\S]*?;`,
                'g'
              );
              
              processed = processed.replace(complexMultiLangPattern, `$1$2: ${typeName};`);
            }
          });
        }
      });
      
      // 特殊处理GlobalReferenceType字段
      if (neededImports.has('GlobalReferenceType')) {
        fieldTypeMap.forEach((typeName, fieldName) => {
          if (typeName === 'GlobalReferenceType') {
            const escapedFieldName = fieldName.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
            
            // 替换GlobalReferenceType的复杂结构
            const globalRefPattern = new RegExp(
              `(\\s+)(['"]?${escapedFieldName}['"]?):\\s*` +
              `(\\|\\s*)?\\{[\\s\\S]*?'@type':[\\s\\S]*?'@refObjectId':[\\s\\S]*?\\}[\\s\\S]*?;`,
              'g'
            );
            
            processed = processed.replace(globalRefPattern, `$1$2: ${typeName};`);
          }
        });
      }
    }
    
    // 如果有需要导入的类型，添加import语句
    if (neededImports.size > 0) {
      const importStatement = `import type { ${Array.from(neededImports).sort().join(', ')} } from './tidas_data_types';\n\n`;
      processed = processed.replace(/(\/\*\*[\s\S]*?\*\/\n\n)/, `$1${importStatement}`);
    }
    
    return processed;
  }
  
  return content;
}

// 后处理生成的TypeScript代码
function postProcessTypeScript(content: string, _schema?: any, _typeName?: string): string {
  let processed = content;

  // 替换属性名称
  Object.entries(ATTRIBUTE_MAPPING).forEach(([from, to]) => {
    const propertyRegex = new RegExp(`"${from.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}"??: *`, 'g');
    processed = processed.replace(propertyRegex, `${to}$1: `);
  });

  // 添加索引签名到主要接口
  processed = processed.replace(
    /export interface (\w+DataSet) \{/g,
    'export interface $1 {\n  [key: string]: any; // Allow arbitrary extension fields'
  );

  // 应用属性名称映射到生成的类型
  Object.entries(ATTRIBUTE_MAPPING).forEach(([from, to]) => {
    const attrRegex = new RegExp(`"${from.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}"\\??: *`, 'g');
    processed = processed.replace(attrRegex, `${to}?: `);
  });

  return processed;
}


// 创建修复后的schema副本
async function createFixedSchema(schemaPath: string): Promise<string> {
  const content = await fs.promises.readFile(schemaPath, 'utf8');
  let schema = JSON.parse(content);

  // 如果是 _category.json 文件，直接使用原始结构（oneOf 在顶层）
  if (schemaPath.endsWith('_category.json')) {
    // 对于 category 文件，直接使用原始结构，json-schema-to-typescript 能够正确处理
    return schemaPath;
  }

  // 特殊处理 tidas_data_types.json，它只有 $defs 没有根结构
  if (schemaPath.endsWith('tidas_data_types.json')) {
    // 创建一个具有所有 $defs 作为属性的根 schema
    const rootSchema = {
      $schema: schema.$schema,
      title: 'TidasDataTypes',
      description: 'All data types used in TIDAS schemas',
      type: 'object',
      properties: Object.fromEntries(
        Object.entries(schema.$defs).map(([key, value]) => [key, value])
      ),
      $defs: schema.$defs
    };
    
    const fixedPath = schemaPath.replace('.json', '.fixed.json');
    fs.writeFileSync(fixedPath, JSON.stringify(rootSchema, null, 2));
    return fixedPath;
  }

  // 对于其他文件，检查是否有主要对象嵌套在 properties 下
  if (schema.type === 'object' && schema.properties) {
    // 查找主要数据集对象（通常以 DataSet 结尾）
    const mainObjectKeys = Object.keys(schema.properties).filter(key => 
      key.endsWith('DataSet') || key.endsWith('dataSet')
    );
    
    if (mainObjectKeys.length === 1) {
      // 提取主要对象作为根 schema
      const mainObjectKey = mainObjectKeys[0];
      const mainObject = schema.properties[mainObjectKey];
      
      // 保持顶级元数据，但使用主要对象的结构
      schema = {
        $schema: schema.$schema,
        ...(schema.title && { title: schema.title }),
        ...(schema.description && { description: schema.description }),
        ...mainObject
      };
    } else if (!schema.$defs) {
      // 如果没有明确的主要对象，则将整个 schema 包装为 $defs
      const { $schema, title, description, ...rest } = schema;
      schema = {
        ...($schema && { $schema }),
        ...(title && { title }),
        ...(description && { description }),
        $defs: { ...rest }
      };
    }
  }

  // 递归处理对象，修复category引用和data_types引用
  function fixCategoryRefs(obj: any): any {
    if (typeof obj !== 'object' || obj === null) {
      return obj;
    }
    if (Array.isArray(obj)) {
      return obj.map(fixCategoryRefs);
    }
    const result: any = {};
    for (const [key, value] of Object.entries(obj)) {
      if (key === '$ref' && typeof value === 'string' && value.includes('_category.json#/$defs/')) {
        // 将 category.json#/$defs/Type 改为 category.json
        result[key] = value.replace(/#\/$defs\/\w+$/, '');
      } else if (key === '$ref' && typeof value === 'string' && value.includes('_category.json#/')) {
        // 将 category.json#/anypath 改为 category.json
        result[key] = value.replace(/#\/.*$/, '');
      } else if (key === '$ref' && typeof value === 'string' && value.includes('tidas_data_types.json#/$defs/')) {
        // 将 tidas_data_types.json#/$defs/TypeName 改为 tidas_data_types.json#/properties/TypeName
        result[key] = value.replace(/#\/$defs\//, '#/properties/');
      } else {
        result[key] = fixCategoryRefs(value);
      }
    }
    return result;
  }

  const fixed = fixCategoryRefs(schema);
  const tempPath = schemaPath.replace('.json', '.fixed.json');
  await fs.promises.writeFile(tempPath, JSON.stringify(fixed, null, 2));
  return tempPath;
}



async function generateTypes() {
  try {
    // 确保输出目录存在
    if (!fs.existsSync(OUTPUT_DIR)) {
      fs.mkdirSync(OUTPUT_DIR, { recursive: true });
    }

    // 获取所有 schema 文件
    const schemaFiles = fs.readdirSync(SCHEMA_DIR)
      .filter(file => file.endsWith('.json') && file.startsWith('tidas_'))

    const schemas: SchemaInfo[] = schemaFiles.map(file => {
      const name = file.replace('.json', '');
      const typeName = name
        .split('_')
        .map(part => part.charAt(0).toUpperCase() + part.slice(1))
        .join('');
      
      return {
        inputPath: path.join(SCHEMA_DIR, file),
        outputPath: path.join(OUTPUT_DIR, `${name}.ts`),
        name: typeName
      };
    });

    console.log(`Found ${schemas.length} schema files to process`);

    const successfulSchemas: SchemaInfo[] = [];

    // 生成每个类型
    for (const schema of schemas) {
      console.log(`Generating types for ${schema.name}...`);
      let usedSchemaPath = schema.inputPath;
      let tempFixedPath: string | null = null;
      try {
        // 预处理 schema，自动修正 category 文件
        tempFixedPath = await createFixedSchema(schema.inputPath);
        if (tempFixedPath !== schema.inputPath) {
          usedSchemaPath = tempFixedPath;
        }
        let tsContent = await compileFromFile(usedSchemaPath, {
          cwd: SCHEMA_DIR,
          declareExternallyReferenced: true,
          enableConstEnums: true,
          style: {
            semi: true,
            singleQuote: true,
          },
          unknownAny: false,
          // 处理无法解析的引用
          unreachableDefinitions: true,
          strictIndexSignatures: false,
          bannerComment: `/**
 * This file was automatically generated from ${path.basename(schema.inputPath)}
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSON Schema file,
 * and run "npm run generate-types" to regenerate this file.
 */`,
        });
        // 读取原始 schema 内容用于类型后处理
        let originalSchema: any = undefined;
        try {
          originalSchema = JSON.parse(fs.readFileSync(schema.inputPath, 'utf8'));
        } catch { /* ignore */ }
        tsContent = postProcessTypeScript(tsContent, originalSchema, schema.name);
        tsContent = postProcessDataTypeReferences(tsContent, originalSchema);
        // 写入文件
        fs.writeFileSync(schema.outputPath, tsContent);
        console.log(`✅ Generated ${schema.outputPath}`);
        successfulSchemas.push(schema);
      } catch (error) {
        console.error(`❌ Error generating types for ${schema.name}:`, error);
      } finally {
        // 删除临时 fixed 文件
        if (tempFixedPath && tempFixedPath !== schema.inputPath) {
          try { fs.unlinkSync(tempFixedPath); } catch { /* ignore */ }
        }
      }
    }

    // 生成索引文件 - 只包含成功生成的类型
    const exportStatements = successfulSchemas.map(schema => 
      `export * from './${path.basename(schema.outputPath, '.ts')}';`
    ).join('\n');

    const reExports: string[] = [];
    const unionTypes: string[] = [];

    // 定义类型映射
    const typeMapping: Record<string, string> = {
      'TidasContacts': 'ContactDataSet',
      'TidasFlows': 'FlowDataSet',
      'TidasProcesses': 'ProcessDataSet',
      'TidasUnitgroups': 'UnitGroupDataSet',
      'TidasSources': 'SourceDataSet',
      'TidasFlowproperties': 'FlowPropertyDataSet',
      'TidasLciamethods': 'LCIAMethodDataSet',
      'TidasLifecyclemodels': 'LifeCycleModelDataSet',
    };

    // 只为成功生成的类型创建重新导出
    successfulSchemas.forEach(schema => {
      const exportName = typeMapping[schema.name];
      if (exportName) {
        const fileName = path.basename(schema.outputPath, '.ts');
        reExports.push(`export { ${schema.name} as ${exportName} } from './${fileName}';`);
        unionTypes.push(exportName);
      }
    });

    const indexContent = `/**
 * Automatically generated index file for all Tidas types
 */

${exportStatements}

// Re-export commonly used types with simpler names
${reExports.join('\n')}

// Union type for all data sets
export type DataSet = 
${unionTypes.map(type => `  | ${type}`).join('\n')};
`;

    fs.writeFileSync(path.join(OUTPUT_DIR, 'index.ts'), indexContent);
    console.log('✅ Generated index file');

    console.log('\n✨ Type generation complete!');
  } catch (error) {
    console.error('Failed to generate types:', error);
    process.exit(1);
  }
}

// 运行生成器
if (require.main === module) {
  generateTypes();
}
