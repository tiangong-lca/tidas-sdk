export class MultiLangArray extends Array<{
  '@xml:lang': string;
  '#text': string;
}> {
  setText(value: string, lang: string = 'en') {
    const existing = this.find((item) => item['@xml:lang'] === lang);
    if (existing) {
      existing['#text'] = value;
    } else {
      this.push({ '@xml:lang': lang, '#text': value });
    }
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
}

export type MultiLangItem = MultiLangItemClass;
