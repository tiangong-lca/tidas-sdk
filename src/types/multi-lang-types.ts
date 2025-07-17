export interface MultiLangArrayLike extends Array<{ '@xml:lang': string; '#text': string }> {
  setText?(value: string, lang?: string): void;
  getText?(lang?: string): string | undefined;
}

export class MultiLangArray extends Array<{ '@xml:lang': string; '#text': string }> implements MultiLangArrayLike {
  setText(value: string, lang: string = 'en') {
    const existing = this.find(item => item['@xml:lang'] === lang);
    if (existing) {
      existing['#text'] = value;
    } else {
      this.push({ '@xml:lang': lang, '#text': value });
    }
  }
  getText(lang: string = 'en'): string | undefined {
    if (lang) {
      const found = this.find(item => item['@xml:lang'] === lang);
      return found ? found['#text'] : undefined;
    }
    return this.length > 0 ? this[0]['#text'] : undefined;
  }
}

export class MultiLangItemClass {
  '@xml:lang': string;
  '#text': string;
  constructor(lang: string, text: string) {
    this['@xml:lang'] = lang;
    this['#text'] = text;
  }
  setText(value: string, lang: string = 'en') {
    this['@xml:lang'] = lang;
    this['#text'] = value;
  }
  getText(lang: string = 'en'): string | undefined {
    if (!lang || this['@xml:lang'] === lang) {
      return this['#text'];
    }
    return undefined;
  }
}

export type MultiLangItem = MultiLangItemClass;
