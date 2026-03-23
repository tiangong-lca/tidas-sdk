const formatUuid = (bytes: Uint8Array): string => {
  const normalized = bytes.slice();
  normalized[6] = (normalized[6] & 0x0f) | 0x40;
  normalized[8] = (normalized[8] & 0x3f) | 0x80;

  const hex = Array.from(normalized, (byte) =>
    byte.toString(16).padStart(2, '0')
  );

  return [
    hex.slice(0, 4).join(''),
    hex.slice(4, 6).join(''),
    hex.slice(6, 8).join(''),
    hex.slice(8, 10).join(''),
    hex.slice(10, 16).join(''),
  ].join('-');
};

const createFallbackBytes = (): Uint8Array => {
  const bytes = new Uint8Array(16);

  for (let index = 0; index < bytes.length; index += 1) {
    bytes[index] = Math.floor(Math.random() * 256);
  }

  return bytes;
};

export const randomUUID = (): string => {
  if (typeof globalThis.crypto?.randomUUID === 'function') {
    return globalThis.crypto.randomUUID();
  }

  if (typeof globalThis.crypto?.getRandomValues === 'function') {
    const bytes = new Uint8Array(16);
    globalThis.crypto.getRandomValues(bytes);
    return formatUuid(bytes);
  }

  return formatUuid(createFallbackBytes());
};
