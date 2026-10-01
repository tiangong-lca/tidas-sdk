import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { cpSync, mkdtempSync, readFileSync, writeFileSync } from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { describe, it } from 'node:test';
import { Validator } from 'jsonschema';

const packageRoot = path.resolve(import.meta.dirname, '..');
const repositoryRoot = path.resolve(packageRoot, '../..');
const sourceAssets = path.join(
  packageRoot,
  'src/contracts/public-rules-assets'
);
const sourcePin = path.join(
  repositoryRoot,
  'scripts/ci/tidas-public-rules-pin.json'
);
const syncScript = path.join(packageRoot, 'scripts/sync-public-rules.ts');

function fixture() {
  const root = mkdtempSync(path.join(os.tmpdir(), 'tidas-public-rules-'));
  const assets = path.join(root, 'assets');
  const pin = path.join(root, 'pin.json');
  cpSync(sourceAssets, assets, { recursive: true });
  cpSync(sourcePin, pin);
  return { assets, pin };
}

function verify({ assets, pin }) {
  return execFileSync(
    process.execPath,
    ['--import', 'tsx', syncScript, '--verify-bundled'],
    {
      cwd: packageRoot,
      encoding: 'utf8',
      env: {
        ...process.env,
        TIDAS_PUBLIC_RULES_OUTPUT_DIR: assets,
        TIDAS_PUBLIC_RULES_PIN_PATH: pin,
      },
      stdio: 'pipe',
    }
  );
}

describe('public-rules source verification', () => {
  it('uses the same qualified spec source as the package-input pin', () => {
    const publicPin = JSON.parse(readFileSync(sourcePin, 'utf8'));
    const packagePin = JSON.parse(
      readFileSync(
        path.join(repositoryRoot, 'scripts/ci/tidas-spec-pin.json'),
        'utf8'
      )
    );
    assert.strictEqual(
      publicPin.status,
      packagePin.sourceRef.startsWith('candidate/')
        ? 'reviewed-candidate'
        : 'released'
    );
    assert.strictEqual(publicPin.commit, packagePin.sourceCommit);
    assert.match(packagePin.version, /^\d+\.\d+\.\d+$/u);
    assert.ok(packagePin.sourceRef.startsWith('candidate/') || packagePin.sourceRef === `v${packagePin.version}`);
  });
  it('validates the bundled index against the bundled public schema', () => {
    const index = JSON.parse(
      readFileSync(path.join(sourceAssets, 'public-rules.v1.json'), 'utf8')
    );
    const schema = JSON.parse(
      readFileSync(
        path.join(sourceAssets, 'public-rules.v1.schema.json'),
        'utf8'
      )
    );
    const result = new Validator().validate(index, schema);
    assert.deepStrictEqual(result.errors, []);
  });

  it('accepts the exact index, schema, and source identity', () => {
    assert.match(verify(fixture()), /Verified bundled public rules/);
  });

  it('rejects a stale source identity even when rule bytes are unchanged', () => {
    const files = fixture();
    const identityPath = path.join(files.assets, 'public-rules.source.v1.json');
    const identity = JSON.parse(readFileSync(identityPath, 'utf8'));
    identity.commit = '0'.repeat(40);
    writeFileSync(identityPath, `${JSON.stringify(identity, null, 2)}\n`);
    assert.throws(() => verify(files), /identity mismatch for commit/);
  });

  it('rejects malformed or modified public rule bytes', () => {
    const files = fixture();
    const indexPath = path.join(files.assets, 'public-rules.v1.json');
    writeFileSync(indexPath, '{}\n');
    assert.throws(
      () => verify(files),
      /index does not match the pinned digest/
    );
  });
});
