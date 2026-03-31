import { cp, mkdir, readdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { copyEilcdAssets, copyTidasAssets } from './runtime-assets';
import {
  datasetFromXml,
  datasetToXml,
  type XmlParseOptions,
  type XmlUnparseOptions,
} from '../xml';

export interface FormatConversionOptions {
  toXml?: boolean;
  parseOptions?: XmlParseOptions;
  unparseOptions?: XmlUnparseOptions;
}

export interface DirectoryConversionOptions extends FormatConversionOptions {
  includeAssets?: boolean;
  dataDirName?: string;
}

export interface DirectoryConversionResult {
  inputDir: string;
  outputDir: string;
  dataDir: string;
  toXml: boolean;
  convertedCount: number;
  copiedCount: number;
}

function normalizeJsonInput(input: string | Buffer | Record<string, unknown>) {
  if (typeof input === 'string') {
    return JSON.parse(input) as Record<string, unknown>;
  }

  if (Buffer.isBuffer(input)) {
    return JSON.parse(input.toString('utf8')) as Record<string, unknown>;
  }

  return input;
}

export function convertFormat(
  input: string | Buffer | Record<string, unknown>,
  options: FormatConversionOptions = {}
) {
  const { toXml = true, parseOptions, unparseOptions } = options;

  if (toXml) {
    return datasetToXml(normalizeJsonInput(input), unparseOptions);
  }

  if (typeof input !== 'string' && !Buffer.isBuffer(input)) {
    throw new TypeError('XML to JSON conversion expects a string or Buffer input.');
  }

  return datasetFromXml(input, parseOptions);
}

async function walkFiles(rootDir: string, currentDir = rootDir): Promise<string[]> {
  const entries = await readdir(currentDir, { withFileTypes: true });
  const files = await Promise.all(
    entries.map(async (entry) => {
      const entryPath = path.join(currentDir, entry.name);
      if (entry.isDirectory()) {
        return walkFiles(rootDir, entryPath);
      }
      return [entryPath];
    })
  );

  return files.flat();
}

function conversionTarget(
  sourceFile: string,
  inputDir: string,
  dataDir: string,
  targetExtension: string
) {
  const relativeFile = path.relative(inputDir, sourceFile);
  const relativeDir = path.dirname(relativeFile);
  const targetDir =
    relativeDir === '.' ? dataDir : path.join(dataDir, relativeDir);
  return path.join(
    targetDir,
    `${path.parse(sourceFile).name}${targetExtension}`
  );
}

async function copyAssetsForDirection(
  outputDir: string,
  toXml: boolean
): Promise<string> {
  return toXml ? copyEilcdAssets(outputDir) : copyTidasAssets(outputDir);
}

export async function convertDirectory(
  inputDir: string,
  outputDir: string,
  options: DirectoryConversionOptions = {}
): Promise<DirectoryConversionResult> {
  const {
    toXml = true,
    parseOptions,
    unparseOptions,
    includeAssets = true,
    dataDirName = 'data',
  } = options;
  const dataDir = path.join(outputDir, dataDirName);

  await mkdir(dataDir, { recursive: true });

  let convertedCount = 0;
  let copiedCount = 0;

  for (const sourceFile of await walkFiles(inputDir)) {
    const lowerName = sourceFile.toLowerCase();
    const shouldConvert = toXml
      ? lowerName.endsWith('.json')
      : lowerName.endsWith('.xml');
    const targetExtension = toXml ? '.xml' : '.json';
    const relativeFile = path.relative(inputDir, sourceFile);
    const targetFile = shouldConvert
      ? conversionTarget(sourceFile, inputDir, dataDir, targetExtension)
      : path.join(dataDir, relativeFile);

    await mkdir(path.dirname(targetFile), { recursive: true });

    if (!shouldConvert) {
      await cp(sourceFile, targetFile);
      copiedCount += 1;
      continue;
    }

    const raw = await readFile(sourceFile);
    const converted = convertFormat(raw, {
      toXml,
      parseOptions,
      unparseOptions,
    });

    if (typeof converted === 'string') {
      await writeFile(targetFile, converted, 'utf8');
    } else {
      await writeFile(
        targetFile,
        JSON.stringify(converted, null, 2),
        'utf8'
      );
    }

    convertedCount += 1;
  }

  if (includeAssets) {
    await copyAssetsForDirection(outputDir, toXml);
  }

  return {
    inputDir,
    outputDir,
    dataDir,
    toXml,
    convertedCount,
    copiedCount,
  };
}
