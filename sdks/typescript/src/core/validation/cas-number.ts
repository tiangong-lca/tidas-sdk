export const CAS_NUMBER_PATTERN = /^[0-9]{2,7}-[0-9]{2}-[0-9]$/;
export const CAS_NUMBER_CHECKSUM_ERROR_CODE = 'cas_number_checksum_error';

export function isValidCASNumber(value: unknown): value is string {
  if (typeof value !== 'string' || !CAS_NUMBER_PATTERN.test(value)) {
    return false;
  }

  const [bodyPart, middlePart, checkDigitPart] = value.split('-');
  const digits = `${bodyPart}${middlePart}`;
  const checksum = [...digits]
    .reverse()
    .reduce((sum, digit, index) => sum + Number(digit) * (index + 1), 0);

  return checksum % 10 === Number(checkDigitPart);
}
