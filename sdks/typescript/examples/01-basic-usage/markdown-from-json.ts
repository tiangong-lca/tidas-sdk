#!/usr/bin/env tsx

/**
 * Markdown export demo
 *
 * Reads sample JSON fixtures, builds Process/Flow/LifeCycleModel entities,
 * and prints the first line of their Markdown summaries.
 */

import { readFileSync } from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import {
  createFlowFromJSON,
  createLifeCycleModelFromJSON,
  createProcessFromJSON,
} from '@tiangong-lca/tidas-sdk/core';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

function loadFixture(filename: string) {
  const fullPath = path.resolve(__dirname, '../../../../test-data', filename);
  const raw = readFileSync(fullPath, 'utf-8');
  return JSON.parse(raw);
}

function renderMarkdown(entity: any, lang: string) {
  const fn = entity?.toMarkdown;
  if (typeof fn === 'function') {
    return fn.call(entity, lang) as string;
  }
  return 'toMarkdown is not available in this SDK build.';
}

function preview(label: string, markdown: string) {
  const firstLine = markdown.split('\n')[0];
  console.log(`✓ ${label} markdown: ${firstLine}`);
}

console.log('=== Markdown Export Demo ===\n');

const fixtures = {
  process: loadFixture('tidas-example-process.json'),
  flow: loadFixture('tidas-example-flow.json'),
  lifeCycleModel: loadFixture('tidas-example-model.json'),
};

const process = createProcessFromJSON(fixtures.process);
const processMd = renderMarkdown(process, 'en');
preview('Process', processMd);

const flow = createFlowFromJSON(fixtures.flow);
const flowMd = renderMarkdown(flow, 'en');
preview('Flow', flowMd);

const lcm = createLifeCycleModelFromJSON(fixtures.lifeCycleModel);
const lcmMd = renderMarkdown(lcm, 'en');
preview('Life Cycle Model', lcmMd);

console.log('\nFull process markdown preview:\n');
console.log(processMd);

console.log('\nFull flow markdown preview:\n');
console.log(flowMd);

console.log('\nFull life cycle model markdown preview:\n');
console.log(lcmMd);
