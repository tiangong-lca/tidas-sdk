import { MultiLangArray, MultiLangItemClass } from '../types/multi-lang-types';

type MultiLangLike =
  | MultiLangArray
  | MultiLangItemClass
  | { '@xml:lang'?: string; '#text'?: string }
  | Array<{ '@xml:lang'?: string; '#text'?: string }>;

function isMultiLangLike(value: any): value is MultiLangLike {
  if (!value) return false;
  if (value instanceof MultiLangArray || value instanceof MultiLangItemClass) return true;
  if (Array.isArray(value) && value.length && typeof value[0] === 'object') {
    return '#text' in value[0];
  }
  return typeof value === 'object' && '#text' in value;
}

export function ensureArray<T>(value: T | T[] | undefined | null): T[] {
  if (value === undefined || value === null) return [];
  return Array.isArray(value) ? value : [value];
}

export function collectTexts(value: any, lang = 'en'): string[] {
  if (!value) return [];
  if (typeof value === 'string') return [value];

  if (isMultiLangLike(value)) {
    const entries = Array.isArray(value) ? value : [value];
    const langMatches: string[] = [];
    const fallback: string[] = [];
    for (const entry of entries) {
      const text = (entry as any)['#text'];
      const entryLang = (entry as any)['@xml:lang'];
      if (!text) continue;
      if (lang && entryLang === lang) langMatches.push(String(text));
      else fallback.push(String(text));
    }
    return langMatches.length ? langMatches : fallback;
  }

  if (Array.isArray(value)) {
    return value.map(v => String(v));
  }
  if (typeof value === 'object' && '#text' in value) {
    return [String((value as any)['#text'])];
  }
  return [];
}

export function pickText(value: any, lang = 'en'): string | undefined {
  const texts = collectTexts(value, lang);
  return texts.length ? texts[0] : undefined;
}

export function joinTexts(value: any, lang = 'en', sep = '\n\n'): string | undefined {
  const texts = collectTexts(value, lang).map(item => item.trim()).filter(Boolean);
  return texts.length ? texts.join(sep) : undefined;
}

export function formatNumber(value: any): string {
  if (value === undefined || value === null) return '';
  if (typeof value === 'number') return Number.isFinite(value) ? value.toString() : String(value);
  const parsed = Number(value);
  return Number.isFinite(parsed) ? parsed.toString() : String(value);
}

export function pickShortDescription(ref: any, lang = 'en'): string | undefined {
  if (!ref) return undefined;
  if (Array.isArray(ref)) {
    for (const entry of ref) {
      const text = pickShortDescription(entry, lang);
      if (text) return text;
    }
    return undefined;
  }
  if (typeof ref === 'object') {
    if ('common:shortDescription' in ref) {
      return pickText((ref as any)['common:shortDescription'], lang);
    }
    if ('#text' in ref) return pickText(ref, lang);
  }
  return undefined;
}
