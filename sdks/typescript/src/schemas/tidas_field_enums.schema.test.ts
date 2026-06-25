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

function reviewScopeSchema() {
  return lciaDataSetShape().modellingAndValidation.shape.validation.shape.review
    .shape['common:scope'];
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

    expect(schema.safeParse('Man-made environment').success).toBe(true);
  });

  it('accepts the TIDAS flow type values', () => {
    const schema = flowTypeOfDataSetSchema();

    expect(schema.safeParse('Other flow').success).toBe(true);
  });

  it('uses normal as the TIDAS uncertainty distribution enum value', () => {
    const factorSchema = characterisationFactorSchema();
    const factorObjectSchema = factorSchema.options[0];
    const factorArrayItemSchema = factorSchema.options[1].element;

    expect(
      factorObjectSchema.shape.uncertaintyDistributionType.safeParse('normal')
        .success
    ).toBe(true);
    expect(
      factorObjectSchema.shape.uncertaintyDistributionType.safeParse(
        'normalisation'
      ).success
    ).toBe(false);
    expect(
      factorArrayItemSchema.shape.uncertaintyDistributionType.safeParse('normal')
        .success
    ).toBe(true);
    expect(
      factorArrayItemSchema.shape.uncertaintyDistributionType.safeParse(
        'normalisation'
      ).success
    ).toBe(false);
  });

  it('uses the LCIA-specific review method enum values', () => {
    const scopeSchema = unwrapOptionalSchema(reviewScopeSchema());
    const scopeObjectSchema = scopeSchema.options[0];
    const scopeArrayItemSchema = scopeSchema.options[1].element;
    const methodObjectSchema =
      scopeObjectSchema.shape['common:method'].options[0];
    const methodArrayItemSchema =
      scopeArrayItemSchema.shape['common:method'].options[1].element;

    // A4: LCIA-method review uses ILCD MethodOfReviewValues, not the process
    // review method list ("Compliance with legal limits" is process-only).
    expect(
      methodObjectSchema.shape['@name'].safeParse('Expert judgement').success
    ).toBe(true);
    expect(
      methodArrayItemSchema.shape['@name'].safeParse('Expert judgement').success
    ).toBe(true);
    expect(
      methodObjectSchema.shape['@name'].safeParse(
        'Compliance with legal limits'
      ).success
    ).toBe(false);
  });
});
