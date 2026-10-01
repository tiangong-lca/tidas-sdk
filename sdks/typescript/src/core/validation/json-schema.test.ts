import assert from 'node:assert/strict';
import { describe, it } from 'node:test';
import { z } from 'zod';
import {
  jsonSchemaOneOf,
  jsonSchemaNotRequired,
  jsonSchemaTuple,
  withJsonSchemaConditional,
  withJsonSchemaDependencies,
  withJsonSchemaUniqueItems,
} from './json-schema';

describe('JSON Schema runtime validation helpers', () => {
  it('requires exactly one oneOf match', () => {
    const exact = jsonSchemaOneOf([
      z.object({ left: z.literal(true) }),
      z.object({ right: z.literal(true) }),
    ]);

    assert.strictEqual(exact.safeParse({}).success, false);
    assert.strictEqual(exact.safeParse({ left: true }).success, true);
    assert.strictEqual(
      exact.safeParse({ left: true, right: true }).success,
      false
    );
  });

  it('uses a discriminator without changing zero, one, or ambiguous matches', () => {
    const exact = jsonSchemaOneOf(
      [
        z.object({ kind: z.literal('left').optional() }),
        z.object({ kind: z.literal('right').optional() }),
      ],
      { property: 'kind', values: ['left', 'right'] }
    );

    assert.strictEqual(exact.safeParse({ kind: 'missing' }).success, false);
    assert.strictEqual(exact.safeParse({ kind: 'left' }).success, true);
    assert.strictEqual(exact.safeParse({}).success, false);
  });

  it('supports partial tuples and validates additionalItems policy', () => {
    const closed = jsonSchemaTuple([z.literal('first'), z.number().int()], {
      additionalItems: false,
    });
    assert.strictEqual(closed.safeParse([]).success, true);
    assert.strictEqual(closed.safeParse(['first']).success, true);
    assert.strictEqual(closed.safeParse(['first', 2]).success, true);
    assert.strictEqual(closed.safeParse(['first', 2, 'extra']).success, false);

    const typedRest = jsonSchemaTuple([z.literal('first')], {
      additionalItems: z.string(),
    });
    assert.strictEqual(typedRest.safeParse(['first', 'second']).success, true);
    assert.strictEqual(typedRest.safeParse(['first', 2]).success, false);
  });

  it('compares uniqueItems using deep JSON equality independent of key order', () => {
    const unique = withJsonSchemaUniqueItems(z.array(z.unknown()));
    const result = unique.safeParse([
      { alpha: 1, beta: [2] },
      { beta: [2], alpha: 1 },
    ]);

    assert.strictEqual(result.success, false);
    if (!result.success) {
      assert.deepStrictEqual(result.error.issues[0]?.path, [1]);
    }
  });

  it('forwards conditional and dependency issues with stable property paths', () => {
    const base = z.object({
      state: z.string().optional(),
      evidence: z.string().optional(),
    });
    const conditional = withJsonSchemaConditional(
      base,
      z.object({ state: z.literal('reviewed') }),
      z.object({ evidence: z.string() })
    );
    const conditionalResult = conditional.safeParse({ state: 'reviewed' });
    assert.strictEqual(conditionalResult.success, false);
    if (!conditionalResult.success) {
      assert.deepStrictEqual(conditionalResult.error.issues[0]?.path, [
        'evidence',
      ]);
    }

    const dependent = withJsonSchemaDependencies(base, [
      {
        property: 'state',
        schema: z.object({ evidence: z.string() }),
      },
    ]);
    const dependencyResult = dependent.safeParse({ state: 'reviewed' });
    assert.strictEqual(dependencyResult.success, false);
    if (!dependencyResult.success) {
      assert.deepStrictEqual(dependencyResult.error.issues[0]?.path, [
        'evidence',
      ]);
    }
  });
});

it('negated required rejects coexisting aliases without stripping valid data', () => {
  const schema = jsonSchemaNotRequired(['canonical', 'legacy']);
  for (const value of [{}, { canonical: 0 }, { legacy: '0' }]) {
    assert.deepEqual(schema.parse(value), value);
  }
  for (const value of [null, [], 1, 'value', { canonical: 0, legacy: 0 }]) {
    assert.equal(schema.safeParse(value).success, false);
  }
  assert.equal(jsonSchemaNotRequired([]).safeParse({}).success, false);
});
