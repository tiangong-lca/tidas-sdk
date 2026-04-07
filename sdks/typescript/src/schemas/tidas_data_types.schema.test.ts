import {
  LocalizedText500ItemSchema,
  LocalizedTextItemSchema,
  RequiredFTMultiLangSchema,
  RequiredSTMultiLangSchema,
  RequiredStringMultiLangSchema,
  STMultiLangSchema,
  StringMultiLangSchema,
} from './tidas_data_types.schema';

describe('localized text schemas', () => {
  it('requires both @xml:lang and #text', () => {
    expect(
      LocalizedTextItemSchema.safeParse({
        '@xml:lang': 'en',
      }).success
    ).toBe(false);

    expect(
      LocalizedTextItemSchema.safeParse({
        '#text': 'English title',
      }).success
    ).toBe(false);
  });

  it('enforces localized language checks for zh and en values', () => {
    expect(
      StringMultiLangSchema.safeParse({
        '@xml:lang': 'zh-CN',
        '#text': 'english only',
      }).success
    ).toBe(false);

    expect(
      StringMultiLangSchema.safeParse({
        '@xml:lang': 'en',
        '#text': 'English 中文',
      }).success
    ).toBe(false);

    expect(
      StringMultiLangSchema.safeParse([
        {
          '@xml:lang': 'zh',
          '#text': '中文名称',
        },
        {
          '@xml:lang': 'en-US',
          '#text': 'English title',
        },
        {
          '@xml:lang': 'fr',
          '#text': 'Bonjour 中文',
        },
      ]).success
    ).toBe(true);
  });

  it('keeps optional localized arrays compatible with empty defaults', () => {
    expect(StringMultiLangSchema.safeParse([]).success).toBe(true);
    expect(STMultiLangSchema.safeParse([]).success).toBe(true);
  });

  it('rejects empty arrays for required localized text variants', () => {
    expect(RequiredStringMultiLangSchema.safeParse([]).success).toBe(false);
    expect(RequiredSTMultiLangSchema.safeParse([]).success).toBe(false);
    expect(RequiredFTMultiLangSchema.safeParse([]).success).toBe(false);
  });

  it('preserves max length limits for localized text variants', () => {
    expect(
      LocalizedText500ItemSchema.safeParse({
        '@xml:lang': 'fr',
        '#text': 'a'.repeat(500),
      }).success
    ).toBe(true);

    expect(
      LocalizedText500ItemSchema.safeParse({
        '@xml:lang': 'fr',
        '#text': 'a'.repeat(501),
      }).success
    ).toBe(false);

    expect(
      STMultiLangSchema.safeParse({
        '@xml:lang': 'en',
        '#text': 'a'.repeat(1001),
      }).success
    ).toBe(false);
  });
});
