import { existsSync, readFileSync, readdirSync } from 'node:fs';
import path from 'node:path';
import type { ZodIssue } from 'zod';
import {
  ContactSchema,
  FlowPropertySchema,
  FlowSchema,
  LCIAMethodSchema,
  LifeCycleModelSchema,
  ProcessSchema,
  SourceSchema,
  UnitGroupSchema,
} from '../schemas';
import { SUPPORTED_CATEGORIES, type SupportedCategory } from './constants';
import {
  collectClassificationIssues,
  collectFlowSchemaGapIssues,
  collectLocalizedTextIssues,
} from './validation-rules';
import {
  buildCategoryReport,
  buildPackageReport,
  type CategoryValidationReport,
  type PackageValidationReport,
  type ValidationIssue,
} from './report';

type SchemaValidator = {
  safeParse(
    data: unknown
  ):
    | { success: true; data: unknown }
    | { success: false; error: { issues: ZodIssue[] } };
};

type NormalizedPath = Array<string | number>;

type NormalizedIssue = {
  code: ZodIssue['code'] | 'missing_union_value';
  path: NormalizedPath;
  message: string;
  format?: string;
  expected?: string;
  values?: unknown[];
};

const CATEGORY_SCHEMAS: Record<SupportedCategory, SchemaValidator> = {
  contacts: ContactSchema,
  flowproperties: FlowPropertySchema,
  flows: FlowSchema,
  lciamethods: LCIAMethodSchema,
  lifecyclemodels: LifeCycleModelSchema,
  processes: ProcessSchema,
  sources: SourceSchema,
  unitgroups: UnitGroupSchema,
};

function toLocation(pathParts: Array<string | number>) {
  return pathParts.length === 0 ? '<root>' : pathParts.join('/');
}

function normalizePath(
  pathParts: ReadonlyArray<PropertyKey> | undefined
): NormalizedPath {
  return (pathParts ?? []).filter(
    (part): part is string | number =>
      typeof part === 'string' || typeof part === 'number'
  );
}

function getValueAtPath(root: unknown, pathParts: Array<string | number>) {
  let current = root;
  for (const part of pathParts) {
    if (current === null || current === undefined) {
      return undefined;
    }
    if (typeof part === 'number') {
      if (!Array.isArray(current)) {
        return undefined;
      }
      current = current[part];
      continue;
    }
    if (typeof current !== 'object') {
      return undefined;
    }
    current = (current as Record<string, unknown>)[part];
  }
  return current;
}

function isJsonSchemaDateTimeLike(value: unknown) {
  return (
    typeof value === 'string' &&
    /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$/.test(
      value
    )
  );
}

function normalizeUnionIssue(
  issue: ZodIssue & { errors?: ZodIssue[][] },
  prefix: Array<string | number>
): NormalizedIssue[] {
  const currentPath = [...prefix, ...normalizePath(issue.path)];
  const childIssues = (issue.errors ?? []).flatMap((branch) =>
    branch.flatMap((child) => normalizeZodIssue(child, currentPath))
  );
  const deeperChildren = childIssues.filter(
    (child) => child.path.length > currentPath.length
  );

  if (deeperChildren.length > 0) {
    return deeperChildren;
  }

  const onlyGenericUnionMisses =
    childIssues.length > 0 &&
    childIssues.every(
      (child) =>
        child.code === 'invalid_type' &&
        (child as { expected?: string }).expected !== undefined &&
        ['array', 'object'].includes(
          String((child as { expected?: string }).expected)
        )
    );

  if (onlyGenericUnionMisses) {
    return [
      {
        code: 'missing_union_value',
        path: currentPath,
        message: 'Missing union value',
      },
    ];
  }

  return childIssues;
}

function normalizeZodIssue(
  issue: ZodIssue,
  prefix: Array<string | number> = []
): NormalizedIssue[] {
  const unionIssue = issue as ZodIssue & { errors?: ZodIssue[][] };
  if (unionIssue.code === 'invalid_union' && Array.isArray(unionIssue.errors)) {
    return normalizeUnionIssue(unionIssue, prefix);
  }

  return [
    {
      code: issue.code,
      path: [...prefix, ...normalizePath(issue.path)],
      message: issue.message,
      format: 'format' in issue ? issue.format : undefined,
      expected: 'expected' in issue ? String(issue.expected) : undefined,
      values: 'values' in issue ? issue.values : undefined,
    },
  ];
}

function shouldIgnoreIssue(issue: NormalizedIssue, jsonItem: unknown) {
  if (issue.code === 'invalid_format' && issue.format === 'datetime') {
    return isJsonSchemaDateTimeLike(getValueAtPath(jsonItem, issue.path));
  }
  return false;
}

function createSchemaIssue(
  category: string,
  filePath: string,
  issue: NormalizedIssue
): ValidationIssue {
  const rawLocation = issue.path;
  const valueAtPath =
    rawLocation.length > 0 ? rawLocation[rawLocation.length - 1] : '';

  if (
    issue.code === 'missing_union_value' &&
    typeof valueAtPath === 'string' &&
    rawLocation.length > 0
  ) {
    const parentLocation = toLocation(rawLocation.slice(0, -1));
    return {
      issue_code: 'schema_error',
      severity: 'error',
      category,
      file_path: filePath,
      location: parentLocation,
      message: `Schema Error at ${parentLocation}: '${valueAtPath}' is a required property`,
      context: {
        validator: 'required',
      },
    };
  }

  if (
    issue.code === 'invalid_value' &&
    typeof valueAtPath === 'string' &&
    rawLocation.length > 0
  ) {
    const parentLocation = toLocation(rawLocation.slice(0, -1));
    return {
      issue_code: 'schema_error',
      severity: 'error',
      category,
      file_path: filePath,
      location: parentLocation,
      message: `Schema Error at ${parentLocation}: '${valueAtPath}' is a required property`,
      context: {
        validator: 'required',
      },
    };
  }

  const location = toLocation(rawLocation);
  return {
    issue_code: 'schema_error',
    severity: 'error',
    category,
    file_path: filePath,
    location,
    message: `Schema Error at ${location}: ${issue.message}`,
    context: {
      validator:
        issue.code === 'invalid_type'
          ? 'type'
          : issue.code === 'invalid_format'
            ? 'format'
            : issue.code,
    },
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
  schema: SchemaValidator,
  jsonItem: unknown,
  category: SupportedCategory,
  filePath: string
) {
  const result = schema.safeParse(jsonItem);
  if (result.success) {
    return [];
  }

  return result.error.issues
    .flatMap((issue) => normalizeZodIssue(issue))
    .filter((issue) => !shouldIgnoreIssue(issue, jsonItem))
    .map((issue) => createSchemaIssue(category, filePath, issue));
}

export function categoryValidate(
  jsonFilePath: string,
  category: SupportedCategory,
  emitLogs = true
): CategoryValidationReport {
  const issues: ValidationIssue[] = [];
  const schema = CATEGORY_SCHEMAS[category];

  for (const fileName of readdirSync(jsonFilePath).sort()) {
    if (!fileName.endsWith('.json')) {
      continue;
    }

    const fullPath = path.join(jsonFilePath, fileName);
    let jsonItem: unknown;

    try {
      jsonItem = JSON.parse(readFileSync(fullPath, 'utf8'));
    } catch (error) {
      issues.push({
        issue_code: 'invalid_json',
        severity: 'error',
        category,
        file_path: fullPath,
        location: '<root>',
        message: `Invalid JSON: ${error instanceof Error ? error.name : 'Error'}: ${
          error instanceof Error ? error.message : String(error)
        }`,
        context: {},
      });
      continue;
    }

    const itemIssues = dedupeIssues([
      ...collectSchemaIssues(schema, jsonItem, category, fullPath),
      ...collectLocalizedTextIssues(jsonItem, category, fullPath),
      ...collectFlowSchemaGapIssues(jsonItem, category, fullPath),
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
  const categoryReports = SUPPORTED_CATEGORIES.flatMap((category) => {
    const categoryDir = path.join(inputDir, category);
    if (!existsSync(categoryDir)) {
      return [];
    }

    return [categoryValidate(categoryDir, category, emitLogs)];
  });

  return buildPackageReport(inputDir, categoryReports);
}
