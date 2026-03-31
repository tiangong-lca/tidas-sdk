import { existsSync } from 'node:fs';
import { cp, mkdir, rm } from 'node:fs/promises';
import path from 'node:path';
import {
  resolveTidasToolsPackageDir,
  requireTidasToolsPackageDir,
} from './resolve-tidas-tools-path.js';

const OUTPUT_DIR = path.join(__dirname, '../src/runtime-assets');
const ASSET_NAMES = ['tidas', 'eilcd'] as const;

async function copyAssetDir(
  sourceRoot: string,
  outputRoot: string,
  assetName: (typeof ASSET_NAMES)[number]
) {
  const sourceDir = path.join(sourceRoot, assetName);
  const targetDir = path.join(outputRoot, assetName);

  await rm(targetDir, { recursive: true, force: true });
  await cp(sourceDir, targetDir, { recursive: true });
}

async function main() {
  const packageDir = resolveTidasToolsPackageDir();

  if (!packageDir) {
    if (existsSync(path.join(OUTPUT_DIR, 'tidas')) && existsSync(path.join(OUTPUT_DIR, 'eilcd'))) {
      console.warn(
        'No tidas-tools checkout found. Keeping existing runtime assets under src/runtime-assets.'
      );
      return;
    }

    requireTidasToolsPackageDir(
      'Runtime asset sync requires access to the upstream tidas-tools repository. Set TIDAS_TOOLS_PATH, place a sibling ../tidas-tools checkout next to this repo, or run ../../scripts/ci/generate-typescript-sdk.sh.'
    );
    return;
  }

  await mkdir(OUTPUT_DIR, { recursive: true });

  for (const assetName of ASSET_NAMES) {
    await copyAssetDir(packageDir, OUTPUT_DIR, assetName);
    console.log(`Synced runtime assets: ${assetName}`);
  }
}

if (require.main === module) {
  main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
  });
}
