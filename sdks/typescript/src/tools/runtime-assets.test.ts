import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {
  copyEilcdAssets,
  copyTidasAssets,
  resolveRuntimeAssetDir,
  resolveRuntimeAssetsDir,
} from './runtime-assets';

function makeTempDir(prefix: string) {
  return fs.mkdtempSync(path.join(os.tmpdir(), prefix));
}

describe('runtime asset helpers', () => {
  it('resolves the packaged runtime asset directories', () => {
    const runtimeAssetsDir = resolveRuntimeAssetsDir();
    const eilcdDir = resolveRuntimeAssetDir('eilcd');
    const tidasDir = resolveRuntimeAssetDir('tidas');

    expect(fs.existsSync(runtimeAssetsDir)).toBe(true);
    expect(fs.existsSync(path.join(eilcdDir, 'schemas'))).toBe(true);
    expect(fs.existsSync(path.join(tidasDir, 'schemas'))).toBe(true);
  });

  it('copies eilcd asset contents into the output root', async () => {
    const outputDir = makeTempDir('tidas-sdk-eilcd-assets-');

    await copyEilcdAssets(outputDir);

    expect(fs.existsSync(path.join(outputDir, 'schemas'))).toBe(true);
    expect(fs.existsSync(path.join(outputDir, 'stylesheets'))).toBe(true);
    expect(fs.existsSync(path.join(outputDir, 'eilcd'))).toBe(false);
  });

  it('copies tidas asset contents into the output root', async () => {
    const outputDir = makeTempDir('tidas-sdk-tidas-assets-');

    await copyTidasAssets(outputDir);

    expect(fs.existsSync(path.join(outputDir, 'schemas'))).toBe(true);
    expect(fs.existsSync(path.join(outputDir, 'methodologies'))).toBe(true);
    expect(fs.existsSync(path.join(outputDir, 'tidas'))).toBe(false);
  });
});
