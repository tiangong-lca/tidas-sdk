import type { Schema } from '../../utils/object-utils';
import { extractJson, getModel } from './ai';

describe('OpenAI-compatible copilot helpers', () => {
  const originalFetch = global.fetch;

  afterEach(() => {
    global.fetch = originalFetch;
    jest.restoreAllMocks();
  });

  it('extracts fenced and direct JSON without an external parser', () => {
    const schema: Schema = {
      type: 'object',
      properties: {
        name: { type: 'string' },
      },
    };

    expect(extractJson('{"name":"steel"}', schema)).toEqual({
      name: 'steel',
    });
    expect(extractJson('```json\n{"name":"steel"}\n```', schema)).toEqual({
      name: 'steel',
    });
  });

  it('posts to an OpenAI-compatible chat completions endpoint', async () => {
    const calls: Array<{ url: string; init: RequestInit }> = [];
    global.fetch = jest.fn(async (url, init) => {
      calls.push({ url: String(url), init: init as RequestInit });
      return new Response(
        JSON.stringify({
          choices: [
            {
              message: {
                content: '{"ok":true}',
              },
            },
          ],
        }),
        {
          status: 200,
          headers: { 'Content-Type': 'application/json' },
        }
      );
    }) as unknown as typeof fetch;

    const model = await getModel({
      apiKey: 'test-key',
      baseURL: 'https://example.test/v1',
      model: 'test-model',
    });
    const result = await model.invoke('hello');

    expect(calls).toHaveLength(1);
    expect(calls[0].url).toBe('https://example.test/v1/chat/completions');
    expect(calls[0].init.headers).toEqual({
      Authorization: 'Bearer test-key',
      'Content-Type': 'application/json',
    });
    expect(JSON.parse(calls[0].init.body as string)).toEqual({
      model: 'test-model',
      messages: [{ role: 'user', content: 'hello' }],
      temperature: 0,
    });
    expect(result.content).toBe('{"ok":true}');
  });
});
