import { existsSync } from 'node:fs';
import { cp, rm } from 'node:fs/promises';
import path from 'node:path';

const SOURCE_DIR = path.join(__dirname, '../src/runtime-assets');
const OUTPUT_DIR = path.join(__dirname, '../dist/runtime-assets');

async function main() {
  if (!existsSync(SOURCE_DIR)) {
    throw new Error(
      'Runtime assets are missing under src/runtime-assets. Run npm run sync-runtime-assets first.'
    );
  }

  await rm(OUTPUT_DIR, { recursive: true, force: true });
  await cp(SOURCE_DIR, OUTPUT_DIR, { recursive: true });
  console.log(`Copied runtime assets to ${OUTPUT_DIR}`);
}

if (require.main === module) {
  main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
  });
}
