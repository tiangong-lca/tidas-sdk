import { existsSync, readFileSync, readdirSync } from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import {
  type Options,
  type Schema,
  type ValidationError,
  Validator,
} from 'jsonschema';
import { resolveRuntimeAssetDir } from '../tools/runtime-assets';
import { SUPPORTED_CATEGORIES, type SupportedCategory } from './constants';
import {
  collectClassificationIssues,
  collectLocalizedTextIssues,
} from './validation-rules';
import {
  buildCategoryReport,
  buildPackageReport,
  type CategoryValidationReport,
  type PackageValidationReport,
  type ValidationIssue,
} from './report';

type JsonSchema = Schema & Record<string, unknown>;

type LoadedSchemaRegistry = {
  validator: Validator;
  rootSchemas: Map<SupportedCategory, JsonSchema>;
};

const SCHEMA_VALIDATION_OPTIONS: Readonly<Options> = {
  nestedErrors: false,
};

const schemaRegistryCache = new Map<string, LoadedSchemaRegistry>();

function isSupportedCategory(value: string): value is SupportedCategory {
  return SUPPORTED_CATEGORIES.includes(value as SupportedCategory);
}

function resolveSchemasDir(baseDir = __dirname) {
  return path.join(resolveRuntimeAssetDir('tidas', baseDir), 'schemas');
}

function parseSchemaFile(schemaPath: string) {
  return JSON.parse(readFileSync(schemaPath, 'utf8')) as JsonSchema;
}

function registerSchemaAliases(
  validator: Validator,
  schema: JsonSchema,
  schemaPath: string
) {
  const fileName = path.basename(schemaPath);
  const aliases = new Set<string>([
    fileName,
    `./${fileName}`,
    `/${fileName}`,
    pathToFileURL(schemaPath).href,
  ]);

  for (const id of [schema.$id, schema.id]) {
    if (typeof id === 'string' && id.length > 0) {
      aliases.add(id);
    }
  }

  aliases.forEach((alias) => {
    validator.addSchema(schema, alias);
  });
}

function loadSchemaRegistry(baseDir = __dirname): LoadedSchemaRegistry {
  const schemasDir = resolveSchemasDir(baseDir);
  const cachedRegistry = schemaRegistryCache.get(schemasDir);
  if (cachedRegistry) {
    return cachedRegistry;
  }

  const validator = new Validator();
  const rootSchemas = new Map<SupportedCategory, JsonSchema>();

  for (const fileName of readdirSync(schemasDir).sort()) {
    if (!fileName.endsWith('.json')) {
      continue;
    }

    const schemaPath = path.join(schemasDir, fileName);
    const schema = parseSchemaFile(schemaPath);
    registerSchemaAliases(validator, schema, schemaPath);

    const schemaName = fileName.replace(/^tidas_/, '').replace(/\.json$/, '');
    if (isSupportedCategory(schemaName)) {
      rootSchemas.set(schemaName, schema);
    }
  }

  const registry = {
    validator,
    rootSchemas,
  };
  schemaRegistryCache.set(schemasDir, registry);
  return registry;
}

function getCategorySchema(category: SupportedCategory, baseDir = __dirname) {
  const registry = loadSchemaRegistry(baseDir);
  const schema = registry.rootSchemas.get(category);

  if (!schema) {
    throw new Error(`Runtime schema not found for category '${category}'`);
  }

  return {
    schema,
    validator: registry.validator,
  };
}

function toLocation(pathParts: Array<string | number>) {
  return pathParts.length === 0 ? '<root>' : pathParts.join('/');
}

function normalizeSchemaMessage(error: ValidationError) {
  if (error.name === 'required' && typeof error.argument === 'string') {
    return `'${error.argument}' is a required property`;
  }

  return error.message;
}

function createSchemaIssue(
  category: string,
  filePath: string,
  error: ValidationError
): ValidationIssue {
  const location = toLocation(error.path ?? []);
  const context: Record<string, unknown> = {
    validator: error.name,
  };

  const normalizedArgument = normalizeErrorArgument(error.argument);
  if (normalizedArgument !== undefined) {
    context.argument = normalizedArgument;
  }

  return {
    issue_code: 'schema_error',
    severity: 'error',
    category,
    file_path: filePath,
    location,
    message: `Schema Error at ${location}: ${normalizeSchemaMessage(error)}`,
    context,
  };
}

function isJsonPrimitive(value: unknown) {
  return (
    value === null ||
    typeof value === 'string' ||
    typeof value === 'number' ||
    typeof value === 'boolean'
  );
}

function normalizeErrorArgument(argument: unknown) {
  if (argument === undefined) {
    return undefined;
  }

  if (isJsonPrimitive(argument)) {
    return argument;
  }

  if (Array.isArray(argument)) {
    return argument.every((item) => isJsonPrimitive(item)) ? argument : undefined;
  }

  if (
    argument &&
    typeof argument === 'object' &&
    'id' in argument &&
    'length' in argument
  ) {
    const errorDetail = argument as {
      id?: unknown;
      length?: unknown;
    };
    return {
      id: errorDetail.id,
      length: errorDetail.length,
    };
  }

  return undefined;
}

function createValidationErrorIssue(
  category: string,
  filePath: string,
  error: unknown
): ValidationIssue {
  return {
    issue_code: 'validation_error',
    severity: 'error',
    category,
    file_path: filePath,
    location: '<root>',
    message: `Validation error: ${
      error instanceof Error ? error.message : String(error)
    }`,
    context: {},
  };
}

function createInvalidJsonIssue(
  category: string,
  filePath: string,
  error: unknown
): ValidationIssue {
  return {
    issue_code: 'invalid_json',
    severity: 'error',
    category,
    file_path: filePath,
    location: '<root>',
    message: `Invalid JSON: ${
      error instanceof Error ? error.name : 'Error'
    }: ${error instanceof Error ? error.message : String(error)}`,
    context: {},
  };
}

function dedupeIssues(issues: ValidationIssue[]) {
  const seen = new Set<string>();
  const deduped: ValidationIssue[] = [];

  for (const issue of issues) {
    const key = `${issue.issue_code}|${issue.file_path}|${issue.location}|${issue.message}`;
    if (seen.has(key)) {
      continue;
    }

    seen.add(key);
    deduped.push(issue);
  }

  return deduped;
}

function collectSchemaIssues(
  validator: Validator,
  schema: JsonSchema,
  jsonItem: unknown,
  category: SupportedCategory,
  filePath: string
) {
  try {
    return validator
      .validate(jsonItem, schema, SCHEMA_VALIDATION_OPTIONS)
      .errors.map((error) => createSchemaIssue(category, filePath, error));
  } catch (error) {
    return [createValidationErrorIssue(category, filePath, error)];
  }
}

export function categoryValidate(
  jsonFilePath: string,
  category: SupportedCategory,
  emitLogs = true
): CategoryValidationReport {
  const issues: ValidationIssue[] = [];
  const { schema, validator } = getCategorySchema(category);

  for (const fileName of readdirSync(jsonFilePath).sort()) {
    if (!fileName.endsWith('.json')) {
      continue;
    }

    const fullPath = path.join(jsonFilePath, fileName);
    let jsonItem: unknown;

    try {
      jsonItem = JSON.parse(readFileSync(fullPath, 'utf8'));
    } catch (error) {
      issues.push(createInvalidJsonIssue(category, fullPath, error));
      continue;
    }

    const itemIssues = dedupeIssues([
      ...collectSchemaIssues(validator, schema, jsonItem, category, fullPath),
      ...collectLocalizedTextIssues(jsonItem, category, fullPath),
      ...collectClassificationIssues(jsonItem, category, fullPath),
    ]);

    issues.push(...itemIssues);

    if (!emitLogs) {
      continue;
    }

    if (itemIssues.length === 0) {
      console.info(`INFO: ${fullPath} PASSED.`);
      continue;
    }

    itemIssues.forEach((issue) => {
      console.error(`ERROR: ${fullPath} ${issue.message}`);
    });
  }

  return buildCategoryReport(category, issues);
}

export function validatePackageDir(
  inputDir: string,
  emitLogs = false
): PackageValidationReport {
  const { rootSchemas } = loadSchemaRegistry();
  const categoryReports = SUPPORTED_CATEGORIES.flatMap((category) => {
    const categoryDir = path.join(inputDir, category);
    if (!existsSync(categoryDir) || !rootSchemas.has(category)) {
      return [];
    }

    return [categoryValidate(categoryDir, category, emitLogs)];
  });

  return buildPackageReport(inputDir, categoryReports);
}
