import { ProcessesSchema } from './tidas_processes.schema';

function exchangeLocationSchema() {
  return (ProcessesSchema as any).shape.processDataSet.shape.exchanges.shape
    .exchange.element.shape.location;
}

describe('process exchange location schema', () => {
  it('accepts location category codes and legacy non-empty strings', () => {
    const schema = exchangeLocationSchema();

    expect(schema.safeParse('CN').success).toBe(true);
    expect(schema.safeParse('GLO').success).toBe(true);
    expect(schema.safeParse('Legacy plant area').success).toBe(true);
  });

  it('rejects empty strings and localized text shapes', () => {
    const schema = exchangeLocationSchema();

    expect(schema.safeParse('').success).toBe(false);
    expect(schema.safeParse({ '@xml:lang': 'en', '#text': 'CN' }).success).toBe(
      false
    );
    expect(
      schema.safeParse([{ '@xml:lang': 'en', '#text': 'CN' }]).success
    ).toBe(false);
  });
});
