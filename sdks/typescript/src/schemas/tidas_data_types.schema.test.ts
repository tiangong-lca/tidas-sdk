import {
  AnnualSupplyOrProductionVolumeMultiLangSchema,
  AnnualSupplyOrProductionVolumeTextItemSchema,
  CommonOtherSchema,
} from './tidas_data_types.schema';

describe('CommonOtherSchema', () => {
  it('accepts namespace declarations plus non-common extension elements', () => {
    const result = CommonOtherSchema.safeParse({
      '@xmlns:ext': 'https://example.com/tidas/extensions',
      'ext:note': {
        '#text': 'Carbon dioxide',
        '@xml:lang': 'en',
      },
    });

    expect(result.success).toBe(true);
  });

  it('rejects legacy string common:other values', () => {
    const result = CommonOtherSchema.safeParse('Carbon dioxide');

    expect(result.success).toBe(false);
  });

  it('rejects namespace-only and common-prefixed entries', () => {
    expect(
      CommonOtherSchema.safeParse({
        '@xmlns:ext': 'https://example.com/tidas/extensions',
      }).success
    ).toBe(false);

    expect(
      CommonOtherSchema.safeParse({
        'common:note': 'Carbon dioxide',
      }).success
    ).toBe(false);
  });
});

describe('AnnualSupplyOrProductionVolumeMultiLangSchema', () => {
  it('accepts localized annual volume text with numeric prefix and suffix', () => {
    expect(
      AnnualSupplyOrProductionVolumeTextItemSchema.safeParse({
        '@xml:lang': 'en',
        '#text': '12.5 kg reference flow',
      }).success
    ).toBe(true);

    expect(
      AnnualSupplyOrProductionVolumeMultiLangSchema.safeParse([
        {
          '@xml:lang': 'en',
          '#text': '12.5 kg reference flow',
        },
      ]).success
    ).toBe(true);
  });

  it('rejects numeric text without suffix context', () => {
    expect(
      AnnualSupplyOrProductionVolumeTextItemSchema.safeParse({
        '@xml:lang': 'en',
        '#text': '12.5',
      }).success
    ).toBe(false);
  });
});
