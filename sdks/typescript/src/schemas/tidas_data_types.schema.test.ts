import {
  AnnualSupplyOrProductionVolumeMultiLangSchema,
  AnnualSupplyOrProductionVolumeTextItemSchema,
  CASNumberSchema,
  CommonOtherSchema,
  TidasLanguageCodeSchema,
  LocalizedTextItemSchema,
} from './tidas_data_types.schema';
import { ValidationUtils } from '../core/config/ValidationConfig';

describe('CASNumberSchema', () => {
  it('accepts CAS numbers with a valid check digit', () => {
    expect(CASNumberSchema.safeParse('64-17-5').success).toBe(true);
    expect(CASNumberSchema.safeParse('007732-18-5').success).toBe(true);
  });

  it('rejects invalid format and invalid check digits', () => {
    expect(CASNumberSchema.safeParse('2023600').success).toBe(false);

    const result = CASNumberSchema.safeParse('64-17-6');

    expect(result.success).toBe(false);
    if (!result.success) {
      expect(
        ValidationUtils.normalizeIssues(result.error.issues)[0]?.code
      ).toBe('cas_number_checksum_error');
    }
  });
});

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

describe('LocalizedTextItemSchema', () => {
  it('accepts TIDAS language enumeration values', () => {
    expect(TidasLanguageCodeSchema.safeParse('en').success).toBe(true);
    expect(TidasLanguageCodeSchema.safeParse('de').success).toBe(true);
    expect(TidasLanguageCodeSchema.safeParse('zh').success).toBe(true);
    expect(
      LocalizedTextItemSchema.safeParse({
        '@xml:lang': 'de',
        '#text': 'Deutscher Titel',
      }).success
    ).toBe(true);
  });

  it('rejects language codes outside the TIDAS enumeration', () => {
    const result = LocalizedTextItemSchema.safeParse({
      '@xml:lang': 'en-US',
      '#text': 'English title',
    });

    expect(result.success).toBe(false);
    if (!result.success) {
      expect(
        ValidationUtils.normalizeIssues(result.error.issues)[0]?.code
      ).toBe('localized_text_language_not_in_tidas_enum');
    }
  });

  it('checks scripts only for exact zh and en language codes', () => {
    expect(
      LocalizedTextItemSchema.safeParse({
        '@xml:lang': 'zh',
        '#text': 'English only',
      }).success
    ).toBe(false);
    expect(
      LocalizedTextItemSchema.safeParse({
        '@xml:lang': 'en',
        '#text': '中文',
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
