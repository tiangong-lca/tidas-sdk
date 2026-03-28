export const SUPPORTED_CATEGORIES = [
  'contacts',
  'flowproperties',
  'flows',
  'lciamethods',
  'lifecyclemodels',
  'processes',
  'sources',
  'unitgroups',
] as const;

export type SupportedCategory = (typeof SUPPORTED_CATEGORIES)[number];

export const CHINESE_CHARACTER_RE = /[\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]/;
