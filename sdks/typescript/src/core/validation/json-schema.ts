import { z } from 'zod';

type SchemaDependency =
  | {
      property: string;
      schema: z.ZodType;
    }
  | {
      property: string;
      required: readonly string[];
    };

type TupleOptions = {
  additionalItems?: boolean | z.ZodType;
  maxItems?: number;
  minItems?: number;
  uniqueItems?: boolean;
};

type OneOfDiscriminator = {
  property?: string;
  values: readonly unknown[];
};

function addIssues(
  ctx: z.RefinementCtx,
  result: z.ZodSafeParseResult<unknown>,
  prefix: PropertyKey[] = []
): void {
  if (result.success) {
    return;
  }

  for (const issue of result.error.issues) {
    ctx.addIssue({
      ...issue,
      path: [...prefix, ...issue.path],
    });
  }
}

function isRecord(value: unknown): value is Record<PropertyKey, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value);
}

function jsonValuesEqual(left: unknown, right: unknown): boolean {
  if (Object.is(left, right)) {
    return true;
  }
  if (Array.isArray(left) || Array.isArray(right)) {
    return (
      Array.isArray(left) &&
      Array.isArray(right) &&
      left.length === right.length &&
      left.every((entry, index) => jsonValuesEqual(entry, right[index]))
    );
  }
  if (!isRecord(left) || !isRecord(right)) {
    return false;
  }

  const leftKeys = Object.keys(left).sort();
  const rightKeys = Object.keys(right).sort();
  return (
    leftKeys.length === rightKeys.length &&
    leftKeys.every(
      (key, index) =>
        key === rightKeys[index] && jsonValuesEqual(left[key], right[key])
    )
  );
}

function addUniqueItemsIssue(values: readonly unknown[], ctx: z.RefinementCtx) {
  for (let right = 1; right < values.length; right += 1) {
    for (let left = 0; left < right; left += 1) {
      if (jsonValuesEqual(values[left], values[right])) {
        ctx.addIssue({
          code: 'custom',
          path: [right],
          message: 'Array items must be unique',
        });
        break;
      }
    }
  }
}

export function jsonSchemaOneOf<const TSchemas extends readonly z.ZodType[]>(
  schemas: TSchemas,
  discriminator?: OneOfDiscriminator
): z.ZodType<z.output<TSchemas[number]>, z.input<TSchemas[number]>> {
  const indexesByValue = new Map<unknown, number[]>();
  discriminator?.values.forEach((value, index) => {
    const indexes = indexesByValue.get(value) ?? [];
    indexes.push(index);
    indexesByValue.set(value, indexes);
  });

  const schema = z.unknown().superRefine((value, ctx) => {
    let candidateIndexes: readonly number[] | undefined;
    if (discriminator) {
      if (discriminator.property === undefined) {
        candidateIndexes = indexesByValue.get(value) ?? [];
      } else if (
        isRecord(value) &&
        Object.prototype.hasOwnProperty.call(value, discriminator.property)
      ) {
        candidateIndexes =
          indexesByValue.get(value[discriminator.property]) ?? [];
      }
    }
    const candidates = candidateIndexes ?? schemas.keys();
    let matches = 0;
    for (const index of candidates) {
      matches += Number(schemas[index].safeParse(value).success);
      if (matches > 1) {
        break;
      }
    }
    if (matches !== 1) {
      ctx.addIssue({
        code: 'custom',
        message: `Expected value to match exactly one schema; matched ${matches}`,
      });
    }
  });

  return schema as z.ZodType<
    z.output<TSchemas[number]>,
    z.input<TSchemas[number]>
  >;
}

export function jsonSchemaTuple(
  itemSchemas: readonly z.ZodType[],
  options: TupleOptions = {}
): z.ZodType<unknown[]> {
  return z.array(z.unknown()).superRefine((value, ctx) => {
    if (options.minItems !== undefined && value.length < options.minItems) {
      ctx.addIssue({
        code: 'too_small',
        origin: 'array',
        minimum: options.minItems,
        inclusive: true,
        message: `Too small: expected array to have >=${options.minItems} items`,
      });
    }
    if (options.maxItems !== undefined && value.length > options.maxItems) {
      ctx.addIssue({
        code: 'too_big',
        origin: 'array',
        maximum: options.maxItems,
        inclusive: true,
        message: `Too big: expected array to have <=${options.maxItems} items`,
      });
    }

    for (
      let index = 0;
      index < Math.min(value.length, itemSchemas.length);
      index += 1
    ) {
      addIssues(ctx, itemSchemas[index].safeParse(value[index]), [index]);
    }

    if (value.length > itemSchemas.length) {
      const additionalItems = options.additionalItems ?? true;
      if (additionalItems === false) {
        ctx.addIssue({
          code: 'custom',
          path: [itemSchemas.length],
          message: 'Array contains additional items',
        });
      } else if (additionalItems !== true) {
        for (let index = itemSchemas.length; index < value.length; index += 1) {
          addIssues(ctx, additionalItems.safeParse(value[index]), [index]);
        }
      }
    }

    if (options.uniqueItems) {
      addUniqueItemsIssue(value, ctx);
    }
  });
}

export function withJsonSchemaConditional<TSchema extends z.ZodType>(
  schema: TSchema,
  condition: z.ZodType,
  whenTrue?: z.ZodType,
  whenFalse?: z.ZodType
): TSchema {
  return schema.superRefine((value, ctx) => {
    const branch = condition.safeParse(value).success ? whenTrue : whenFalse;
    if (branch) {
      addIssues(ctx, branch.safeParse(value));
    }
  }) as TSchema;
}

export function withJsonSchemaDependencies<TSchema extends z.ZodType>(
  schema: TSchema,
  dependencies: readonly SchemaDependency[]
): TSchema {
  return schema.superRefine((value, ctx) => {
    if (!isRecord(value)) {
      return;
    }

    for (const dependency of dependencies) {
      if (!Object.prototype.hasOwnProperty.call(value, dependency.property)) {
        continue;
      }
      if ('schema' in dependency) {
        addIssues(ctx, dependency.schema.safeParse(value));
        continue;
      }
      for (const requiredProperty of dependency.required) {
        if (!Object.prototype.hasOwnProperty.call(value, requiredProperty)) {
          ctx.addIssue({
            code: 'custom',
            path: [requiredProperty],
            message: `Property is required when ${dependency.property} is present`,
          });
        }
      }
    }
  }) as TSchema;
}

export function withJsonSchemaUniqueItems<TSchema extends z.ZodType<unknown[]>>(
  schema: TSchema
): TSchema {
  return schema.superRefine(addUniqueItemsIssue) as TSchema;
}

/** Draft-07 `not: {required: [...]}` rejects coexisting aliases, including non-objects. */
export function jsonSchemaNotRequired(keys: readonly string[]) {
  return z.unknown().superRefine((value, context) => {
    const object = typeof value === 'object' && value !== null && !Array.isArray(value);
    if (!object || keys.every((key) => Object.prototype.hasOwnProperty.call(value, key))) {
      context.addIssue({ code: 'custom', message: 'Properties must not all be present', path: [keys[0] ?? ''] });
    }
  });
}
