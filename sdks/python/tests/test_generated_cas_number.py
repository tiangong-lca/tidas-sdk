from __future__ import annotations

import pytest
from pydantic import TypeAdapter, ValidationError

from tidas_sdk.core.cas_number import is_valid_cas_number
from tidas_sdk.generated.tidas_data_types import CASNumber


def test_cas_number_accepts_valid_check_digit() -> None:
    adapter = TypeAdapter(CASNumber)

    assert is_valid_cas_number("64-17-5")
    assert is_valid_cas_number("007732-18-5")
    assert adapter.validate_python("64-17-5") == "64-17-5"
    assert adapter.validate_python("007732-18-5") == "007732-18-5"


def test_cas_number_rejects_invalid_format_and_check_digit() -> None:
    adapter = TypeAdapter(CASNumber)

    assert not is_valid_cas_number("2023600")
    assert not is_valid_cas_number("64-17-6")

    with pytest.raises(ValidationError):
        adapter.validate_python("2023600")

    with pytest.raises(ValidationError):
        adapter.validate_python("64-17-6")
