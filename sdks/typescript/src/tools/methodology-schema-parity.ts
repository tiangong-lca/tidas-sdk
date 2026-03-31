import { readFileSync } from 'node:fs';
import path from 'node:path';
import bundledMethodologies from '../data/bundled-methodologies.json';
import { resolveRuntimeAssetDir } from './runtime-assets';

export type MethodologySchemaParityStatus = 'ok' | 'warning' | 'error';

export interface MethodologySchemaParityFileReport {
  methodology_key: string;
  methodology_file: string;
  schema_file: string;
  status: MethodologySchemaParityStatus;
  errors: string[];
  warnings: string[];
}

export interface MethodologySchemaParitySummary {
  file_count: number;
  ok_count: number;
  warning_count: number;
  error_count: number;
}

export interface MethodologySchemaParityReport {
  ok: boolean;
  summary: MethodologySchemaParitySummary;
  files: MethodologySchemaParityFileReport[];
}

type JsonLikeRecord = Record<string, unknown>;

const IMPORTANT_SCHEMA_FIELDS = [
  'processDataSet',
  'processInformation',
  'modellingAndValidation',
  'administrativeInformation',
  'exchanges',
];

function isRecord(value: unknown): value is JsonLikeRecord {
  return Boolean(value) && typeof value === 'object' && !Array.isArray(value);
}

function replaceAllOccurrences(value: string, search: string, replacement: string) {
  return value.split(search).join(replacement);
}

function resolveSchemaFile(schemaFile: string, baseDir = __dirname) {
  return path.join(resolveRuntimeAssetDir('tidas', baseDir), 'schemas', schemaFile);
}

function loadSchema(schemaFile: string, baseDir = __dirname) {
  return JSON.parse(readFileSync(resolveSchemaFile(schemaFile, baseDir), 'utf8'));
}

export function extractMethodologyPaths(data: unknown, currentPath = ''): Set<string> {
  const paths = new Set<string>();

  if (!isRecord(data)) {
    return paths;
  }

  for (const [key, value] of Object.entries(data)) {
    if (key === '<rules>' || key === 'metadata' || key === 'global_rules') {
      continue;
    }

    const nextPath = currentPath ? `${currentPath}.${key}` : key;
    paths.add(nextPath);

    extractMethodologyPaths(value, nextPath).forEach((pathValue) =>
      paths.add(pathValue)
    );
  }

  return paths;
}

export function extractSchemaPaths(schema: unknown, currentPath = ''): Set<string> {
  const paths = new Set<string>();
  if (!isRecord(schema)) {
    return paths;
  }

  if (schema.type === 'array' && 'items' in schema) {
    const { items } = schema;
    if (Array.isArray(items)) {
      items.forEach((item) => {
        extractSchemaPaths(item, currentPath).forEach((pathValue) =>
          paths.add(pathValue)
        );
      });
    } else if (isRecord(items)) {
      if (items.type === 'object' || 'properties' in items) {
        extractSchemaPaths(items, currentPath).forEach((pathValue) =>
          paths.add(pathValue)
        );
      } else if (currentPath) {
        paths.add(currentPath);
      }
    }
  }

  const properties = schema.properties;
  if (isRecord(properties)) {
    for (const [propertyName, propertySchema] of Object.entries(properties)) {
      const cleanName = replaceAllOccurrences(
        replaceAllOccurrences(propertyName, 'common:', ''),
        '@',
        ''
      );
      const nextPath = currentPath ? `${currentPath}.${cleanName}` : cleanName;
      paths.add(nextPath);

      extractSchemaPaths(propertySchema, nextPath).forEach((pathValue) =>
        paths.add(pathValue)
      );
    }
  }

  return paths;
}

export function normalizeMethodologyPath(value: string) {
  let normalized = replaceAllOccurrences(
    replaceAllOccurrences(value, 'common:', ''),
    '@',
    ''
  );
  const replacements: Record<string, string> = {
    UUID: 'uuid',
    timeStamp: 'timestamp',
    dataSetVersion: 'datasetversion',
  };

  for (const [from, to] of Object.entries(replacements)) {
    normalized = replaceAllOccurrences(normalized, from, to);
  }

  return normalized.toLowerCase();
}

export function compareMethodologyWithSchema(
  methodology: unknown,
  schema: unknown
) {
  const errors: string[] = [];
  const warnings: string[] = [];

  try {
    const methodologyPaths = extractMethodologyPaths(methodology);
    const schemaPaths = extractSchemaPaths(schema);

    const normalizedMethodologyPaths = new Map<string, string>();
    methodologyPaths.forEach((pathValue) => {
      normalizedMethodologyPaths.set(
        normalizeMethodologyPath(pathValue),
        pathValue
      );
    });

    const normalizedSchemaPaths = new Map<string, string>();
    schemaPaths.forEach((pathValue) => {
      normalizedSchemaPaths.set(normalizeMethodologyPath(pathValue), pathValue);
    });

    for (const [normalizedPath, originalPath] of normalizedMethodologyPaths) {
      if (normalizedSchemaPaths.has(normalizedPath)) {
        continue;
      }

      warnings.push(
        `Field '${originalPath}' in YAML methodology not found in schema`
      );
    }

    for (const [normalizedPath, originalPath] of normalizedSchemaPaths) {
      if (normalizedMethodologyPaths.has(normalizedPath)) {
        continue;
      }

      if (!IMPORTANT_SCHEMA_FIELDS.some((field) => originalPath.includes(field))) {
        continue;
      }

      const topLevel = originalPath.split('.', 1)[0] ?? '';
      if (!IMPORTANT_SCHEMA_FIELDS.includes(topLevel)) {
        continue;
      }

      warnings.push(
        `Schema field '${originalPath}' not covered in YAML methodology`
      );
    }
  } catch (error) {
    errors.push(
      `Error processing methodology/schema comparison: ${
        error instanceof Error ? error.message : String(error)
      }`
    );
  }

  return {
    errors,
    warnings,
  };
}

export function validateBundledMethodologies(baseDir = __dirname) {
  const files: MethodologySchemaParityFileReport[] = [];
  const methodologies = bundledMethodologies.methodologies ?? {};

  for (const methodologyKey of Object.keys(methodologies).sort()) {
    const methodologyFile = `tidas_${methodologyKey}.yaml`;
    const schemaFile = `tidas_${methodologyKey}.json`;
    const methodology = methodologies[methodologyKey as keyof typeof methodologies];

    try {
      const schema = loadSchema(schemaFile, baseDir);
      const { errors, warnings } = compareMethodologyWithSchema(
        methodology,
        schema
      );
      files.push({
        methodology_key: methodologyKey,
        methodology_file: methodologyFile,
        schema_file: schemaFile,
        status: errors.length > 0 ? 'error' : warnings.length > 0 ? 'warning' : 'ok',
        errors,
        warnings,
      });
    } catch (error) {
      files.push({
        methodology_key: methodologyKey,
        methodology_file: methodologyFile,
        schema_file: schemaFile,
        status: 'error',
        errors: [
          `No corresponding schema file found or could not be loaded: ${schemaFile} (${
            error instanceof Error ? error.message : String(error)
          })`,
        ],
        warnings: [],
      });
    }
  }

  const summary = files.reduce<MethodologySchemaParitySummary>(
    (accumulator, fileReport) => {
      accumulator.file_count += 1;
      if (fileReport.status === 'ok') {
        accumulator.ok_count += 1;
      } else if (fileReport.status === 'warning') {
        accumulator.warning_count += 1;
      } else {
        accumulator.error_count += 1;
      }
      return accumulator;
    },
    {
      file_count: 0,
      ok_count: 0,
      warning_count: 0,
      error_count: 0,
    }
  );

  return {
    ok: summary.error_count === 0,
    summary,
    files,
  } satisfies MethodologySchemaParityReport;
}

export const validateMethodologySchemaParity = validateBundledMethodologies;
