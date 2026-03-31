import { existsSync } from 'node:fs';
import { cp, mkdir, readdir, rm } from 'node:fs/promises';
import path from 'node:path';

export type RuntimeAssetDirectory = 'tidas' | 'eilcd';

export function resolveRuntimeAssetsDir(baseDir = __dirname) {
  const runtimeAssetsDir = path.resolve(baseDir, '../runtime-assets');
  if (!existsSync(runtimeAssetsDir)) {
    throw new Error(
      `Runtime assets directory not found: ${runtimeAssetsDir}. Build or sync the package assets first.`
    );
  }
  return runtimeAssetsDir;
}

export function resolveRuntimeAssetDir(
  assetName: RuntimeAssetDirectory,
  baseDir = __dirname
) {
  const assetDir = path.join(resolveRuntimeAssetsDir(baseDir), assetName);
  if (!existsSync(assetDir)) {
    throw new Error(`Runtime asset directory not found: ${assetDir}`);
  }
  return assetDir;
}

export async function copyRuntimeAssetDir(
  assetName: RuntimeAssetDirectory,
  outputDir: string,
  baseDir = __dirname
) {
  const sourceDir = resolveRuntimeAssetDir(assetName, baseDir);
  await mkdir(outputDir, { recursive: true });
  const entries = await readdir(sourceDir, { withFileTypes: true });

  for (const entry of entries) {
    const sourcePath = path.join(sourceDir, entry.name);
    const targetPath = path.join(outputDir, entry.name);
    await rm(targetPath, { recursive: true, force: true });
    await cp(sourcePath, targetPath, { recursive: true });
  }

  return outputDir;
}

export function copyTidasAssets(outputDir: string, baseDir = __dirname) {
  return copyRuntimeAssetDir('tidas', outputDir, baseDir);
}

export function copyEilcdAssets(outputDir: string, baseDir = __dirname) {
  return copyRuntimeAssetDir('eilcd', outputDir, baseDir);
}
