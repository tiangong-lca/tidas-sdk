import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFileSync } from 'node:fs';
import { describe, it } from 'node:test';
import path from 'node:path';
import {
  getAvailableTidasContractKinds,
  getTidasContractPack,
  getTidasMethodologyText,
  getTidasPublicRules,
  getTidasPublicRulesSchema,
  getTidasSchemaText,
  normalizeTidasContractKind,
} from './tidas-contract';

describe('TIDAS contract helpers', () => {
  it('normalizes singular, plural, and dashed kind aliases', () => {
    assert.strictEqual(normalizeTidasContractKind('processes'), 'process');
    assert.strictEqual(
      normalizeTidasContractKind('life-cycle-model'),
      'lifecyclemodel'
    );
    assert.ok(getAvailableTidasContractKinds().includes('flow'));
  });

  it('returns full schema text for process and flow contracts', () => {
    assert.ok('properties' in JSON.parse(getTidasSchemaText('process')));
    assert.ok('properties' in JSON.parse(getTidasSchemaText('flow')));
  });

  it('returns bundled methodology YAML text where available', () => {
    assert.ok(
      getTidasMethodologyText('process')?.includes(
        'Process Dataset Content Rules'
      )
    );
    assert.ok(
      getTidasMethodologyText('flow')?.includes('Flow Dataset Content Rules')
    );
    assert.strictEqual(getTidasMethodologyText('source'), null);
  });

  it('returns versioned public definitions without product execution policy', () => {
    assert.strictEqual(
      (
        getTidasPublicRulesSchema() as {
          properties?: { schema_version?: { const?: number } };
        }
      ).properties?.schema_version?.const,
      1
    );
    for (const kind of ['process', 'flow'] as const) {
      const selection = getTidasPublicRules(kind);
      assert.strictEqual(selection.status, 'covered');
      assert.strictEqual(selection.dataset_type, kind);
      assert.ok(selection.rules.length > 0);
      assert.strictEqual(
        selection.rules.every((rule) => rule.dataset_type === kind),
        true
      );
      for (const rule of selection.rules) {
        for (const productField of [
          'severity',
          'phase',
          'blocker',
          'waiver',
          'profile',
          'authorization',
        ]) {
          assert.strictEqual(productField in rule, false);
        }
      }
    }
  });

  it('distinguishes a valid uncovered kind from invalid input', () => {
    const uncovered = getTidasPublicRules('source');
    assert.deepStrictEqual(uncovered.rules, []);
    assert.strictEqual(uncovered.status, 'not-covered');
    assert.strictEqual(uncovered.dataset_type, 'source');
    assert.throws(
      () => getTidasPublicRules('unknown-kind'),
      /Unsupported TIDAS contract kind/
    );
  });

  it('binds the public index to the exact pinned reviewed candidate source', () => {
    const selection = getTidasPublicRules('flow');
    const indexPath = path.join(
      __dirname,
      'public-rules-assets',
      'public-rules.v1.json'
    );
    const digest = createHash('sha256')
      .update(readFileSync(indexPath))
      .digest('hex');
    assert.strictEqual(selection.source.index_sha256, digest);
    const packagePin = JSON.parse(
      readFileSync(
        path.join(__dirname, '../../../../scripts/ci/tidas-spec-pin.json'),
        'utf8'
      )
    );
    assert.strictEqual(selection.source.commit, packagePin.sourceCommit);
    assert.strictEqual(selection.source.rules_version, '2026.09.20');
    assert.strictEqual(selection.source.status, 'reviewed-candidate');
  });

  it('keeps the Process Version public definition aligned with the shipped schema', () => {
    const selection = getTidasPublicRules('process');
    if (selection.status !== 'covered') {
      throw new Error('Process public rules must be covered');
    }
    const versionRule = selection.rules.find(
      (rule) => rule.id === 'tidas.process.version.format'
    );
    assert.ok(versionRule);
    const dataTypes = JSON.parse(
      readFileSync(
        path.join(
          __dirname,
          '../runtime-assets/tidas/schemas/tidas_data_types.json'
        ),
        'utf8'
      )
    ) as { $defs: { Version: { pattern: string } } };
    const versionPattern = new RegExp(dataTypes.$defs.Version.pattern);
    for (const value of ['01.02', '01.02.003']) {
      assert.ok(versionPattern.test(value));
      assert.ok(
        versionRule.cases.positive.some((example) => example.includes(value))
      );
    }
    for (const value of ['1.1', '01.02.03']) {
      assert.strictEqual(versionPattern.test(value), false);
      assert.ok(
        versionRule.cases.negative.some((example) => example.includes(value))
      );
    }
  });

  it('keeps the SDK contract pack free of product runtime policy', () => {
    const modern = getTidasContractPack('process', {
      include: ['schema', 'public-rules'],
      includeAiContext: true,
    });
    assert.strictEqual(modern.publicRules?.status, 'covered');
    assert.ok(modern.manifest.publicRules);
    assert.strictEqual('runtimeRuleset' in modern, false);
    assert.strictEqual('ruleset' in modern.manifest, false);
    assert.strictEqual('runtime_ruleset' in (modern.aiContext ?? {}), false);
    assert.deepStrictEqual(modern.aiContext?.public_rules, modern.publicRules);
  });

  it('builds a reproducible AI context pack manifest', () => {
    const pack = getTidasContractPack('process', {
      profile: 'ai-import',
      includeAiContext: true,
    });

    assert.strictEqual(pack.manifest.kind, 'process');
    assert.strictEqual(pack.manifest.profile, 'ai-import');
    assert.match(pack.manifest.schema?.sha256 ?? '', /^[a-f0-9]{64}$/);
    assert.match(pack.manifest.methodology?.sha256 ?? '', /^[a-f0-9]{64}$/);
    assert.strictEqual('ruleset' in pack.manifest, false);
    assert.ok(pack.aiContext?.instructions.join(' ').includes('Foundry'));
  });
});
