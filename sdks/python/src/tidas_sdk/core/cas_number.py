"""
CAS Registry Number validation helpers.
"""
from __future__ import annotations

import re

CAS_NUMBER_PATTERN = re.compile(r"^[0-9]{2,7}-[0-9]{2}-[0-9]$")


def is_valid_cas_number(value: object) -> bool:
    if not isinstance(value, str) or not CAS_NUMBER_PATTERN.fullmatch(value):
        return False

    body, check_digit = value.rsplit("-", 1)
    digits = body.replace("-", "")
    checksum = sum(
        int(digit) * weight
        for weight, digit in enumerate(reversed(digits), start=1)
    )
    return checksum % 10 == int(check_digit)


def validate_cas_number_check_digit(value: str) -> str:
    if not CAS_NUMBER_PATTERN.fullmatch(value):
        return value

    if not is_valid_cas_number(value):
        raise ValueError("CASNumber check digit is invalid")

    return value
