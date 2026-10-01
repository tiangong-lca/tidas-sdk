import assert from 'node:assert/strict';
import { describe, it } from 'node:test';
import { FlowsSchema } from './tidas_flows.schema';
import { LciamethodsSchema } from './tidas_lciamethods.schema';

function lciaDataSetShape() {
  return (LciamethodsSchema as any).shape.LCIAMethodDataSet.shape;
}

function areaOfProtectionSchema() {
  return lciaDataSetShape().LCIAMethodInformation.shape.dataSetInformation.shape
    .areaOfProtection;
}

function characterisationFactorSchema() {
  return lciaDataSetShape().characterisationFactors.shape.factor;
}

function objectSchema(schema: any): any {
  if (schema.shape) return schema;
  if (schema.unwrap) return objectSchema(schema.unwrap());
  if (schema._def.left) return objectSchema(schema._def.left);
  if (schema.options) return objectSchema(schema.options[0]);
  throw new Error('Expected an object branch');
}

function reviewScopeSchema() {
  return objectSchema(lciaDataSetShape().modellingAndValidation.shape.validation.shape.review).shape.scope;
}

function unwrapOptionalSchema(schema: any) {
  return schema.unwrap?.() ?? schema._def.innerType;
}

function flowTypeOfDataSetSchema() {
  return (FlowsSchema as any).shape.flowDataSet.shape.modellingAndValidation
    .shape.LCIMethod.shape.typeOfDataSet;
}

describe('TIDAS field enum schemas', () => {
  it('accepts the TIDAS LCIA area of protection values', () => {
    const schema = areaOfProtectionSchema();

    assert.strictEqual(schema.safeParse('Man-made environment').success, true);
  });

  it('accepts the TIDAS flow type values', () => {
    const schema = flowTypeOfDataSetSchema();

    assert.strictEqual(schema.safeParse('Other flow').success, true);
  });

  it('uses normal as the TIDAS uncertainty distribution enum value', () => {
    const factorSchema = characterisationFactorSchema();
    const factorObjectSchema = objectSchema(factorSchema.options[0]);
    const factorArrayItemSchema = objectSchema(factorSchema.options[1].element);

    assert.strictEqual(
      factorObjectSchema.shape.uncertaintyDistributionType.safeParse('normal')
        .success,
      true
    );
    assert.strictEqual(
      factorObjectSchema.shape.uncertaintyDistributionType.safeParse(
        'normalisation'
      ).success,
      false
    );
    assert.strictEqual(
      factorArrayItemSchema.shape.uncertaintyDistributionType.safeParse(
        'normal'
      ).success,
      true
    );
    assert.strictEqual(
      factorArrayItemSchema.shape.uncertaintyDistributionType.safeParse(
        'normalisation'
      ).success,
      false
    );
  });

  it('uses the LCIA-specific review method enum values', () => {
    const scopeSchema = unwrapOptionalSchema(reviewScopeSchema());
    const scopeObjectSchema = objectSchema(scopeSchema.options[0]);
    const scopeArrayItemSchema = objectSchema(scopeSchema.options[1].element);
    const methodObjectSchema =
      objectSchema(scopeObjectSchema.shape.method);
    const methodArrayItemSchema =
      objectSchema(scopeArrayItemSchema.shape.method);

    // A4: LCIA-method review uses ILCD MethodOfReviewValues, not the process
    // review method list ("Compliance with legal limits" is process-only).
    assert.strictEqual(
      methodObjectSchema.shape['@name'].safeParse('Expert judgement').success,
      true
    );
    assert.strictEqual(
      methodArrayItemSchema.shape['@name'].safeParse('Expert judgement')
        .success,
      true
    );
    assert.strictEqual(
      methodObjectSchema.shape['@name'].safeParse(
        'Compliance with legal limits'
      ).success,
      false
    );
  });

  it('requires the remaining LCIA review evidence unless the method is Not reviewed', () => {
    const reviewSchema =
      lciaDataSetShape().modellingAndValidation.shape.validation.shape.review;

    assert.strictEqual(
      reviewSchema.safeParse({ '@type': 'Not reviewed' }).success,
      true
    );

    const result = reviewSchema.safeParse({
      '@type': 'Independent external review',
    });
    assert.strictEqual(result.success, false);
    if (!result.success) {
      assert.deepStrictEqual(
        result.error.issues.map((issue: any) => issue.path.join('.')).sort(),
        [
          '',
          'common:referenceToNameOfReviewerAndInstitution',
          'common:reviewDetails',
        ]
      );
    }
  });
});
