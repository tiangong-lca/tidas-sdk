import path from 'node:path';

export type JsonSchema = boolean | JsonSchemaObject;

export interface JsonSchemaObject {
  $comment?: string;
  $defs?: Record<string, JsonSchema>;
  $ref?: string;
  additionalItems?: boolean | JsonSchema;
  additionalProperties?: boolean | JsonSchema;
  allOf?: JsonSchema[];
  anyOf?: JsonSchema[];
  const?: unknown;
  dependencies?: Record<string, JsonSchema | string[]>;
  description?: string;
  else?: JsonSchema;
  enum?: unknown[];
  exclusiveMaximum?: number;
  exclusiveMinimum?: number;
  format?: string;
  if?: JsonSchema;
  items?: JsonSchema | JsonSchema[];
  maxItems?: number;
  maxLength?: number;
  maximum?: number;
  minItems?: number;
  minLength?: number;
  minimum?: number;
  multipleOf?: number;
  not?: JsonSchema;
  oneOf?: JsonSchema[];
  pattern?: string;
  patternProperties?: Record<string, JsonSchema>;
  properties?: Record<string, JsonSchema>;
  propertyNames?: JsonSchema;
  required?: string[];
  then?: JsonSchema;
  type?:
    | 'array'
    | 'boolean'
    | 'integer'
    | 'null'
    | 'number'
    | 'object'
    | 'string'
    | Array<
        | 'array'
        | 'boolean'
        | 'integer'
        | 'null'
        | 'number'
        | 'object'
        | 'string'
      >;
  uniqueItems?: boolean;
}

interface RenderedModule {
  content: string;
  exportNames: string[];
}

interface ExternalImport {
  modulePath: string;
  names: Set<string>;
}

const SCHEMA_EXTENSION = '.json';

/**
 * Render TIDAS JSON Schema documents directly as deterministic Zod modules.
 *
 * This deliberately uses the JSON Schema AST rather than generated TypeScript
 * declarations. It therefore has no dependency on the TypeScript compiler API
 * or on source-code parsing heuristics.
 */
export class JsonSchemaToZod {
  private readonly imports = new Map<string, ExternalImport>();
  private readonly validationHelpers = new Set<string>();

  constructor(
    private readonly fileName: string,
    private readonly schema: JsonSchemaObject
  ) {}

  renderModule(): RenderedModule {
    validateSchemaTree(this.schema, '#', this.fileName);
    const bodies: string[] = [];
    const exportNames: string[] = [];

    for (const [definitionName, definition] of sortDefinitions(
      this.schema.$defs ?? {},
      this.fileName
    )) {
      const exportName = schemaName(definitionName);
      bodies.push(
        `export const ${exportName}${this.exportTypeAnnotation()} = ${this.renderSchema(
          definition,
          `#/$defs/${definitionName}`
        )};`
      );
      exportNames.push(exportName);
    }

    if (hasRootSchema(this.schema)) {
      const exportName = schemaName(fileBaseName(this.fileName));
      bodies.push(
        `export const ${exportName}${this.exportTypeAnnotation()} = ${this.renderSchema(
          withoutDefinitions(this.schema),
          '#'
        )};`
      );
      exportNames.push(exportName);
    }

    if (bodies.length === 0) {
      throw new Error(
        `${this.fileName}: schema has neither $defs nor a renderable root`
      );
    }

    const importBlocks = ["import { z } from 'zod';"];
    if (this.validationHelpers.size > 0) {
      importBlocks.push(
        `import { ${[...this.validationHelpers]
          .sort()
          .join(', ')} } from './../core/validation/json-schema';`
      );
    }
    for (const { modulePath, names } of [...this.imports.values()].sort(
      (left, right) => left.modulePath.localeCompare(right.modulePath)
    )) {
      importBlocks.push(
        `import { ${[...names].sort().join(', ')} } from '${modulePath}';`
      );
    }

    return {
      content: `// Generated directly from TIDAS JSON Schema: ${
        this.fileName
      }\n${importBlocks.join('\n')}\n\n${bodies.join('\n\n')}\n`,
      exportNames,
    };
  }

  private renderSchema(schema: JsonSchema, location: string): string {
    if (schema === true) {
      return 'z.unknown()';
    }
    if (schema === false) {
      return 'z.never()';
    }

    const fragments: string[] = [];
    if (Object.prototype.hasOwnProperty.call(schema, 'const')) {
      fragments.push(`z.literal(${renderLiteral(schema.const)})`);
    }

    if (schema.enum) {
      fragments.push(
        schema.enum.length === 0
          ? 'z.never()'
          : renderUnion(
              schema.enum.map((value) => `z.literal(${renderLiteral(value)})`)
            )
      );
    }

    if (schema.$ref) {
      fragments.push(this.renderReference(schema.$ref, location));
    }

    const base =
      schema.$ref && !hasIndependentRefSiblingConstraints(schema)
        ? null
        : this.renderBaseSchema(schema, location);
    if (base) {
      fragments.push(base);
    }

    if (schema.anyOf) {
      if (schema.anyOf.length === 0) {
        fragments.push('z.never()');
      } else {
        fragments.push(
          renderUnion(
            schema.anyOf.map((entry, index) =>
              this.renderSchema(entry, `${location}/anyOf/${index}`)
            )
          )
        );
      }
    }

    if (schema.oneOf) {
      this.validationHelpers.add('jsonSchemaOneOf');
      const discriminator = findOneOfDiscriminator(schema.oneOf);
      const eraseBranchTypes = this.exportsOpaqueCategorySchemas();
      fragments.push(
        `jsonSchemaOneOf([${schema.oneOf
          .map(
            (entry, index) =>
              eraseBranchTypes
                ? `(${this.renderSchema(
                    entry,
                    `${location}/oneOf/${index}`
                  )}) as z.ZodType`
                : this.renderSchema(entry, `${location}/oneOf/${index}`)
          )
          .join(', ')}]${eraseBranchTypes ? ' as z.ZodType[]' : ''}${
          discriminator ? `, ${JSON.stringify(discriminator)}` : ''
        })`
      );
    }

    if (isNegatedRequired(schema.not)) {
      this.validationHelpers.add('jsonSchemaNotRequired');
      fragments.push(`jsonSchemaNotRequired(${JSON.stringify(schema.not.required)})`);
    }

    const conditionals: Array<{
      schema: JsonSchemaObject;
      location: string;
    }> = [];

    if (schema.allOf) {
      for (const [index, entry] of schema.allOf.entries()) {
        const entryLocation = `${location}/allOf/${index}`;
        if (
          isConditionalSchema(entry) &&
          isDomainOverlayConditional(this.fileName, entryLocation)
        ) {
          continue;
        }
        if (isConditionalSchema(entry)) {
          conditionals.push({ schema: entry, location: entryLocation });
          continue;
        }
        fragments.push(this.renderSchema(entry, entryLocation));
      }
    }

    if (schema.if !== undefined) {
      if (!isDomainOverlayConditional(this.fileName, location)) {
        conditionals.push({ schema, location });
      }
    }

    const meaningfulFragments = deduplicate(fragments);
    if (meaningfulFragments.length === 0 && conditionals.length === 0) {
      if (isExplicitEmptySchema(schema)) {
        return 'z.unknown()';
      }
      throw new Error(
        `${this.fileName}${location}: unsupported JSON Schema shape (${Object.keys(
          schema
        ).join(', ')})`
      );
    }

    let rendered =
      meaningfulFragments.length > 0
        ? renderIntersection(meaningfulFragments)
        : 'z.unknown()';
    for (const conditional of conditionals) {
      rendered = this.renderConditional(
        rendered,
        conditional.schema,
        conditional.location
      );
    }
    return rendered;
  }

  private exportsOpaqueCategorySchemas(): boolean {
    return this.fileName.endsWith('_category.json');
  }

  private exportTypeAnnotation(): string {
    return this.exportsOpaqueCategorySchemas() ? ': z.ZodType<any>' : '';
  }

  private renderConditional(
    base: string,
    schema: JsonSchemaObject,
    location: string
  ): string {
    if (schema.if === undefined) {
      return base;
    }
    this.validationHelpers.add('withJsonSchemaConditional');
    const condition = this.renderSchema(schema.if, `${location}/if`);
    const whenTrue = schema.then !== undefined
      ? this.renderSchema(schema.then, `${location}/then`)
      : 'undefined';
    const whenFalse = schema.else !== undefined
      ? this.renderSchema(schema.else, `${location}/else`)
      : 'undefined';
    return `withJsonSchemaConditional(${base}, ${condition}, ${whenTrue}, ${whenFalse})`;
  }

  private renderReference(reference: string, location: string): string {
    if (reference.startsWith('#/$defs/')) {
      const definitionName = decodeReferenceSegment(
        reference.slice('#/$defs/'.length)
      );
      if (!definitionName || definitionName.includes('/')) {
        throw new Error(
          `${this.fileName}${location}: unsupported local reference ${reference}`
        );
      }
      return schemaName(definitionName);
    }

    const [rawTarget, fragment] = reference.split('#', 2);
    if (!rawTarget) {
      throw new Error(
        `${this.fileName}${location}: unsupported reference ${reference}`
      );
    }

    const targetFile = path.posix.basename(rawTarget);
    if (!targetFile.endsWith(SCHEMA_EXTENSION)) {
      throw new Error(
        `${this.fileName}${location}: referenced document is not JSON Schema: ${reference}`
      );
    }

    let importedName: string;
    if (fragment) {
      const prefix = '/$defs/';
      if (!fragment.startsWith(prefix)) {
        throw new Error(
          `${this.fileName}${location}: unsupported external fragment ${reference}`
        );
      }
      importedName = schemaName(
        decodeReferenceSegment(fragment.slice(prefix.length))
      );
    } else {
      importedName = schemaName(fileBaseName(targetFile));
    }

    const targetBase = targetFile.slice(0, -SCHEMA_EXTENSION.length);
    const modulePath = `./${targetBase}.schema`;
    const externalImport = this.imports.get(modulePath) ?? {
      modulePath,
      names: new Set<string>(),
    };
    externalImport.names.add(importedName);
    this.imports.set(modulePath, externalImport);

    return importedName;
  }

  private renderBaseSchema(
    schema: JsonSchemaObject,
    location: string
  ): string | null {
    if (Array.isArray(schema.type)) {
      return renderUnion(
        schema.type
          .map((type) =>
            this.renderBaseSchema(
              { ...schema, type },
              `${location}/type/${type}`
            )
          )
          .filter((value): value is string => value !== null)
      );
    }

    const inferredType = schema.type ?? inferTypeFromKeywords(schema);

    switch (inferredType) {
      case 'array':
        return this.renderArray(schema, location);
      case 'boolean':
        return 'z.boolean()';
      case 'integer':
        return applyNumericConstraints('z.number().int()', schema);
      case 'number':
        return applyNumericConstraints('z.number()', schema);
      case 'null':
        return 'z.null()';
      case 'object':
        return this.renderObject(schema, location);
      case 'string':
        return applyStringConstraints(
          'z.string()',
          schema,
          this.fileName,
          location
        );
      case null:
        return null;
      default:
        throw new Error(
          `${this.fileName}${location}: unsupported JSON Schema type ${String(
            inferredType
          )}`
        );
    }
  }

  private renderArray(schema: JsonSchemaObject, location: string): string {
    if (!schema.items) {
      throw new Error(`${this.fileName}${location}: array has no items schema`);
    }

    let rendered: string;
    if (Array.isArray(schema.items)) {
      const itemSchemas = schema.items.map((item, index) =>
        this.renderSchema(item, `${location}/items/${index}`)
      );
      this.validationHelpers.add('jsonSchemaTuple');
      const options: string[] = [];
      if (schema.additionalItems !== undefined) {
        options.push(
          `additionalItems: ${
            typeof schema.additionalItems === 'boolean'
              ? String(schema.additionalItems)
              : this.renderSchema(
                  schema.additionalItems,
                  `${location}/additionalItems`
                )
          }`
        );
      }
      if (schema.minItems !== undefined) {
        options.push(`minItems: ${schema.minItems}`);
      }
      if (schema.maxItems !== undefined) {
        options.push(`maxItems: ${schema.maxItems}`);
      }
      if (schema.uniqueItems) {
        options.push('uniqueItems: true');
      }
      rendered = `jsonSchemaTuple([${itemSchemas.join(', ')}], { ${options.join(
        ', '
      )} })`;
    } else {
      rendered = `z.array(${this.renderSchema(
        schema.items,
        `${location}/items`
      )})`;
      if (schema.minItems !== undefined) {
        rendered += `.min(${schema.minItems})`;
      }
      if (schema.maxItems !== undefined) {
        rendered += `.max(${schema.maxItems})`;
      }
      if (schema.uniqueItems) {
        this.validationHelpers.add('withJsonSchemaUniqueItems');
        rendered = `withJsonSchemaUniqueItems(${rendered})`;
      }
    }

    return rendered;
  }

  private renderObject(schema: JsonSchemaObject, location: string): string {
    if (isCommonOtherOverlay(this.fileName, location)) {
      return 'z.object({}).strict()';
    }
    const properties = schema.properties ?? {};
    const required = new Set(schema.required ?? []);
    const propertyNames = new Set([...Object.keys(properties), ...required]);

    if (propertyNames.size === 0) {
      if (
        schema.additionalProperties &&
        typeof schema.additionalProperties === 'object'
      ) {
        return `z.record(z.string(), ${this.renderSchema(
          schema.additionalProperties,
          `${location}/additionalProperties`
        )})`;
      }
      if (schema.additionalProperties === true) {
        return 'z.record(z.string(), z.unknown())';
      }
      return schema.additionalProperties === false
        ? 'z.object({}).strict()'
        : 'z.object({})';
    }

    const renderedProperties = [...propertyNames].map((propertyName) => {
      const propertySchema = properties[propertyName];
      const rendered = propertySchema
        ? this.renderSchema(
            propertySchema,
            `${location}/properties/${escapeReferenceSegment(propertyName)}`
          )
        : 'z.unknown()';
      return `${renderPropertyName(propertyName)}: ${
        required.has(propertyName) ? rendered : `${rendered}.optional()`
      }`;
    });

    let rendered = `z.object({${renderedProperties.join(', ')}})`;
    if (schema.additionalProperties === false) {
      rendered += '.strict()';
    } else if (
      schema.additionalProperties &&
      typeof schema.additionalProperties === 'object'
    ) {
      rendered += `.catchall(${this.renderSchema(
        schema.additionalProperties,
        `${location}/additionalProperties`
      )})`;
    }

    if (schema.dependencies) {
      this.validationHelpers.add('withJsonSchemaDependencies');
      const dependencies = Object.entries(schema.dependencies).map(
        ([property, dependency]) =>
          Array.isArray(dependency)
            ? `{ property: ${JSON.stringify(property)}, required: ${JSON.stringify(
                dependency
              )} }`
            : `{ property: ${JSON.stringify(
                property
              )}, schema: ${this.renderSchema(
                dependency,
                `${location}/dependencies/${escapeReferenceSegment(property)}`
              )} }`
      );
      rendered = `withJsonSchemaDependencies(${rendered}, [${dependencies.join(
        ', '
      )}])`;
    }

    return rendered;
  }
}

function hasRootSchema(schema: JsonSchemaObject): boolean {
  return Object.keys(schema).some(
    (key) => key !== '$schema' && key !== '$defs' && key !== 'description' && key !== '$comment'
  );
}

function withoutDefinitions(schema: JsonSchemaObject): JsonSchemaObject {
  const {
    $defs: _definitions,
    $schema: _dialect,
    ...root
  } = schema as JsonSchemaObject & { $schema?: string };
  return root;
}

function isConditionalSchema(
  schema: JsonSchema
): schema is JsonSchemaObject & { if: JsonSchema } {
  return (
    typeof schema === 'object' &&
    schema !== null &&
    Object.prototype.hasOwnProperty.call(schema, 'if')
  );
}

function isExplicitEmptySchema(schema: JsonSchemaObject): boolean {
  const ignoredKeys = new Set(['description', '$comment', 'else', 'if', 'then']);
  return Object.keys(schema).every((key) => ignoredKeys.has(key));
}

function renderUnion(schemas: string[]): string {
  const uniqueSchemas = deduplicate(schemas);
  if (uniqueSchemas.length === 0) {
    return 'z.never()';
  }
  if (uniqueSchemas.length === 1) {
    return uniqueSchemas[0];
  }
  return `z.union([${uniqueSchemas.join(', ')}])`;
}

function renderIntersection(schemas: string[]): string {
  if (schemas.length === 1) {
    return schemas[0];
  }
  return schemas
    .slice(1)
    .reduce(
      (combined, schema) => `z.intersection(${combined}, ${schema})`,
      schemas[0]
    );
}

function applyStringConstraints(
  base: string,
  schema: JsonSchemaObject,
  fileName: string,
  location: string
): string {
  let rendered = base;
  switch (schema.format) {
    case undefined:
    case 'cas-number':
      break;
    case 'date-time':
      rendered = 'z.iso.datetime({ offset: true })';
      break;
    case 'email':
      rendered = 'z.email()';
      break;
    case 'uri':
      rendered = 'z.url()';
      break;
    default:
      throw new Error(
        `${fileName}${location}: unsupported JSON Schema format ${schema.format}`
      );
  }
  if (schema.minLength !== undefined) {
    rendered += `.min(${schema.minLength})`;
  }
  if (schema.maxLength !== undefined) {
    rendered += `.max(${schema.maxLength})`;
  }
  if (schema.pattern !== undefined) {
    rendered += `.regex(${renderRegExp(schema.pattern)})`;
  }
  return rendered;
}

function inferTypeFromKeywords(
  schema: JsonSchemaObject
): 'array' | 'number' | 'object' | 'string' | null {
  if (
    schema.properties ||
    schema.required ||
    schema.patternProperties ||
    schema.additionalProperties !== undefined ||
    schema.dependencies
  ) {
    return 'object';
  }
  if (
    schema.items ||
    schema.minItems !== undefined ||
    schema.maxItems !== undefined ||
    schema.uniqueItems !== undefined ||
    schema.additionalItems !== undefined
  ) {
    return 'array';
  }
  if (
    schema.minLength !== undefined ||
    schema.maxLength !== undefined ||
    schema.pattern !== undefined ||
    schema.format !== undefined
  ) {
    return 'string';
  }
  if (
    schema.minimum !== undefined ||
    schema.maximum !== undefined ||
    schema.exclusiveMinimum !== undefined ||
    schema.exclusiveMaximum !== undefined ||
    schema.multipleOf !== undefined
  ) {
    return 'number';
  }
  return null;
}

function applyNumericConstraints(
  base: string,
  schema: JsonSchemaObject
): string {
  let rendered = base;
  if (schema.minimum !== undefined) {
    rendered += `.min(${schema.minimum})`;
  }
  if (schema.maximum !== undefined) {
    rendered += `.max(${schema.maximum})`;
  }
  if (schema.exclusiveMinimum !== undefined) {
    rendered += `.gt(${schema.exclusiveMinimum})`;
  }
  if (schema.exclusiveMaximum !== undefined) {
    rendered += `.lt(${schema.exclusiveMaximum})`;
  }
  if (schema.multipleOf !== undefined) {
    rendered += `.multipleOf(${schema.multipleOf})`;
  }
  return rendered;
}

function renderRegExp(pattern: string): string {
  return `/${pattern.replaceAll('/', '\\/')}/`;
}

function renderLiteral(value: unknown): string {
  if (
    value === null ||
    typeof value === 'string' ||
    typeof value === 'number' ||
    typeof value === 'boolean'
  ) {
    return JSON.stringify(value);
  }
  throw new Error(`Unsupported JSON Schema literal: ${JSON.stringify(value)}`);
}

function fileBaseName(fileName: string): string {
  const withoutExtension = fileName.endsWith(SCHEMA_EXTENSION)
    ? fileName.slice(0, -SCHEMA_EXTENSION.length)
    : fileName;
  return withoutExtension
    .replace(/^tidas_/, '')
    .split('_')
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join('');
}

function schemaName(name: string): string {
  return `${name}Schema`;
}

function decodeReferenceSegment(value: string): string {
  return decodeURIComponent(value).replaceAll('~1', '/').replaceAll('~0', '~');
}

function escapeReferenceSegment(value: string): string {
  return value.replaceAll('~', '~0').replaceAll('/', '~1');
}

function renderPropertyName(name: string): string {
  return /^[A-Za-z_$][A-Za-z0-9_$]*$/.test(name) ? name : JSON.stringify(name);
}

function deduplicate(values: string[]): string[] {
  return [...new Set(values)];
}

function findOneOfDiscriminator(
  branches: JsonSchema[]
): { property?: string; values: unknown[] } | null {
  if (branches.length === 0) {
    return null;
  }

  if (
    branches.every(
      (branch) =>
        typeof branch === 'object' &&
        Object.prototype.hasOwnProperty.call(branch, 'const') &&
        isPrimitiveLiteral(branch.const)
    )
  ) {
    return {
      values: branches.map((branch) =>
        typeof branch === 'object' ? branch.const : undefined
      ),
    };
  }

  const objects = branches.filter(
    (branch): branch is JsonSchemaObject =>
      typeof branch === 'object' && branch !== null
  );
  if (objects.length !== branches.length) {
    return null;
  }

  const candidates = Object.keys(objects[0].properties ?? {}).filter(
    (property) =>
      objects.every((branch) => {
        const propertySchema = branch.properties?.[property];
        return (
          typeof propertySchema === 'object' &&
          propertySchema !== null &&
          Object.prototype.hasOwnProperty.call(propertySchema, 'const') &&
          isPrimitiveLiteral(propertySchema.const)
        );
      })
  );
  if (candidates.length === 0) {
    return null;
  }

  const property = candidates.sort((left, right) => {
    const distinct = (name: string) =>
      new Set(
        objects.map((branch) => {
          const propertySchema = branch.properties?.[name];
          return typeof propertySchema === 'object' && propertySchema !== null
            ? propertySchema.const
            : undefined;
        })
      ).size;
    return distinct(right) - distinct(left) || left.localeCompare(right);
  })[0];

  return {
    property,
    values: objects.map((branch) => {
      const propertySchema = branch.properties?.[property];
      return typeof propertySchema === 'object' && propertySchema !== null
        ? propertySchema.const
        : undefined;
    }),
  };
}

function isPrimitiveLiteral(value: unknown): boolean {
  return (
    value === null ||
    typeof value === 'string' ||
    typeof value === 'number' ||
    typeof value === 'boolean'
  );
}

function hasIndependentRefSiblingConstraints(
  schema: JsonSchemaObject
): boolean {
  return Boolean(
    schema.properties ||
    schema.required ||
    schema.patternProperties ||
    schema.items ||
    schema.anyOf ||
    schema.oneOf ||
    schema.allOf ||
    schema.minItems !== undefined ||
    schema.maxItems !== undefined ||
    schema.minLength !== undefined ||
    schema.maxLength !== undefined ||
    schema.pattern !== undefined ||
    schema.minimum !== undefined ||
    schema.maximum !== undefined ||
    schema.exclusiveMinimum !== undefined ||
    schema.exclusiveMaximum !== undefined ||
    schema.multipleOf !== undefined ||
    schema.format === 'date-time' ||
    schema.format === 'email' ||
    schema.format === 'uri' ||
    schema.uniqueItems !== undefined ||
    schema.additionalItems !== undefined ||
    schema.additionalProperties !== undefined ||
    schema.dependencies !== undefined
  );
}

const SUPPORTED_SCHEMA_KEYWORDS = new Set([
  '$comment',
  '$defs',
  '$ref',
  '$schema',
  'additionalItems',
  'additionalProperties',
  'allOf',
  'anyOf',
  'const',
  'dependencies',
  'description',
  'else',
  'enum',
  'exclusiveMaximum',
  'exclusiveMinimum',
  'format',
  'if',
  'items',
  'maxItems',
  'maxLength',
  'maximum',
  'minItems',
  'minLength',
  'minimum',
  'multipleOf',
  'not',
  'oneOf',
  'pattern',
  'patternProperties',
  'properties',
  'propertyNames',
  'required',
  'then',
  'type',
  'uniqueItems',
]);

function validateSchemaTree(
  schema: JsonSchema,
  location: string,
  fileName: string
): void {
  if (typeof schema === 'boolean') {
    return;
  }

  for (const keyword of Object.keys(schema)) {
    if (!SUPPORTED_SCHEMA_KEYWORDS.has(keyword)) {
      throw new Error(
        `${fileName}${location}: unsupported JSON Schema keyword ${keyword}`
      );
    }
  }

  if (schema.$comment !== undefined && typeof schema.$comment !== 'string') {
    throw new Error(`${fileName}${location}: $comment must be a string`);
  }

  if (schema.format) {
    const supported = ['date-time', 'email', 'uri'].includes(schema.format);
    if (!supported && !isCASNumberOverlay(fileName, location, schema.format)) {
      throw new Error(
        `${fileName}${location}: unsupported JSON Schema format ${schema.format}`
      );
    }
  }

  if (schema.patternProperties && !isCommonOtherOverlay(fileName, location)) {
    throw new Error(
      `${fileName}${location}: patternProperties is only supported by the CommonOther domain overlay`
    );
  }
  if (schema.not && !isNegatedRequired(schema.not) && !isAllowedNotOverlay(fileName, location)) {
    throw new Error(
      `${fileName}${location}: not requires a required-only constraint or the CommonOther/LocalizedText domain overlay`
    );
  }
  if (
    schema.propertyNames &&
    !(
      fileName === 'tidas_data_types.json' &&
      location === '#/$defs/CommonOther/not'
    )
  ) {
    throw new Error(
      `${fileName}${location}: propertyNames is only supported by the CommonOther domain overlay`
    );
  }

  for (const [name, definition] of Object.entries(schema.$defs ?? {})) {
    validateSchemaTree(
      definition,
      `${location}/$defs/${escapeReferenceSegment(name)}`,
      fileName
    );
  }
  for (const [name, property] of Object.entries(schema.properties ?? {})) {
    validateSchemaTree(
      property,
      `${location}/properties/${escapeReferenceSegment(name)}`,
      fileName
    );
  }
  for (const [pattern, property] of Object.entries(
    schema.patternProperties ?? {}
  )) {
    validateSchemaTree(
      property,
      `${location}/patternProperties/${escapeReferenceSegment(pattern)}`,
      fileName
    );
  }
  for (const [property, dependency] of Object.entries(
    schema.dependencies ?? {}
  )) {
    if (Array.isArray(dependency)) {
      if (!dependency.every((entry) => typeof entry === 'string')) {
        throw new Error(
          `${fileName}${location}/dependencies/${escapeReferenceSegment(
            property
          )}: property dependency must contain only property names`
        );
      }
    } else {
      validateSchemaTree(
        dependency,
        `${location}/dependencies/${escapeReferenceSegment(property)}`,
        fileName
      );
    }
  }

  const arrays: Array<[string, JsonSchema[] | undefined]> = [
    ['allOf', schema.allOf],
    ['anyOf', schema.anyOf],
    ['oneOf', schema.oneOf],
  ];
  for (const [keyword, entries] of arrays) {
    entries?.forEach((entry, index) =>
      validateSchemaTree(entry, `${location}/${keyword}/${index}`, fileName)
    );
  }

  if (Array.isArray(schema.items)) {
    schema.items.forEach((entry, index) =>
      validateSchemaTree(entry, `${location}/items/${index}`, fileName)
    );
  } else if (schema.items) {
    validateSchemaTree(schema.items, `${location}/items`, fileName);
  }

  const children: Array<[string, JsonSchema | undefined]> = [
    [
      'additionalItems',
      typeof schema.additionalItems === 'object'
        ? schema.additionalItems
        : undefined,
    ],
    [
      'additionalProperties',
      typeof schema.additionalProperties === 'object'
        ? schema.additionalProperties
        : undefined,
    ],
    ['else', schema.else],
    ['if', schema.if],
    ['not', schema.not],
    ['propertyNames', schema.propertyNames],
    ['then', schema.then],
  ];
  for (const [keyword, child] of children) {
    if (child !== undefined) {
      validateSchemaTree(child, `${location}/${keyword}`, fileName);
    }
  }
}

function isCommonOtherOverlay(fileName: string, location: string): boolean {
  return (
    fileName === 'tidas_data_types.json' && location === '#/$defs/CommonOther'
  );
}

function isAllowedNotOverlay(fileName: string, location: string): boolean {
  return (
    fileName === 'tidas_data_types.json' &&
    (location === '#/$defs/CommonOther' ||
      location === '#/$defs/LocalizedTextItem/allOf/1/then/properties/#text')
  );
}

function isCASNumberOverlay(
  fileName: string,
  location: string,
  format: string
): boolean {
  return (
    format === 'cas-number' &&
    fileName === 'tidas_data_types.json' &&
    location === '#/$defs/CASNumber'
  );
}

function isDomainOverlayConditional(
  fileName: string,
  location: string
): boolean {
  return (
    (fileName === 'tidas_data_types.json' &&
      (location === '#/$defs/LocalizedTextItem/allOf/0' ||
        location === '#/$defs/LocalizedTextItem/allOf/1')) ||
    (fileName === 'tidas_flows.json' &&
      location === '#/properties/flowDataSet/allOf/0')
  );
}

function sortDefinitions(
  definitions: Record<string, JsonSchema>,
  fileName: string
): Array<[string, JsonSchema]> {
  const originalOrder = Object.keys(definitions);
  const visited = new Set<string>();
  const visiting = new Set<string>();
  const result: Array<[string, JsonSchema]> = [];

  const visit = (name: string): void => {
    if (visited.has(name)) {
      return;
    }
    if (visiting.has(name)) {
      throw new Error(
        `${fileName}: circular local $defs reference involving ${name}`
      );
    }

    const definition = definitions[name];
    if (!definition) {
      throw new Error(`${fileName}: missing local $defs target ${name}`);
    }

    visiting.add(name);
    for (const dependency of collectLocalDefinitionReferences(definition)) {
      if (dependency === name) {
        continue;
      }
      if (!Object.prototype.hasOwnProperty.call(definitions, dependency)) {
        throw new Error(
          `${fileName}: missing local $defs target ${dependency}`
        );
      }
      visit(dependency);
    }
    visiting.delete(name);
    visited.add(name);
    result.push([name, definition]);
  };

  for (const name of originalOrder) {
    visit(name);
  }
  return result;
}

function collectLocalDefinitionReferences(schema: JsonSchema): Set<string> {
  const references = new Set<string>();

  const visit = (value: unknown): void => {
    if (Array.isArray(value)) {
      for (const entry of value) {
        visit(entry);
      }
      return;
    }
    if (!value || typeof value !== 'object') {
      return;
    }

    const object = value as Record<string, unknown>;
    if (
      Object.prototype.hasOwnProperty.call(object, 'const') ||
      Object.prototype.hasOwnProperty.call(object, 'enum')
    ) {
      return;
    }
    const reference = object.$ref;
    if (typeof reference === 'string' && reference.startsWith('#/$defs/')) {
      references.add(
        decodeReferenceSegment(reference.slice('#/$defs/'.length))
      );
    }
    for (const [key, entry] of Object.entries(object)) {
      if (key !== '$ref' && key !== 'description') {
        visit(entry);
      }
    }
  };

  visit(schema);
  return references;
}

function isNegatedRequired(schema: JsonSchema | undefined): schema is JsonSchemaObject & { required: string[] } {
  return typeof schema === 'object' && schema !== null &&
    Object.keys(schema).every((key) => key === 'required' || key === '$comment') &&
    Array.isArray(schema.required) && schema.required.every((key) => typeof key === 'string');
}
