import assert from 'node:assert/strict';
import test from 'node:test';
import { JsonSchemaToTypeScript, createTidasConfig } from '../scripts/json-schema-to-typescript.ts';

test('array element unions bind as a whole instead of applying [] only to the last enum value', () => {
  const converter = new JsonSchemaToTypeScript(createTidasConfig());
  const output = converter.convertSchemaToTypeScript({
    type: 'object', properties: { approaches: { type: 'array', items: { enum: ['Allocation - mass', 'Other'] } } },
  });
  assert.match(output, /approaches\?: \("Allocation - mass" \| "Other"\)\[\]/);
});
