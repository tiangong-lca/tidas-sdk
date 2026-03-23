from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

from tidas_sdk import create_flow


FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"


def _load_payload() -> dict[str, object]:
    return json.loads((FIXTURES_DIR / "flow-validation-parity.json").read_text(encoding="utf-8"))


def _payload_with_required_name_fields() -> dict[str, object]:
    payload = deepcopy(_load_payload())
    name = payload["flowDataSet"]["flowInformation"]["dataSetInformation"]["name"]
    name["treatmentStandardsRoutes"] = [{"@xml:lang": "en", "#text": "tar, syngas, char"}]
    name["mixAndLocationTypes"] = [{"@xml:lang": "en", "#text": "at plant"}]
    return payload


def test_flow_pydantic_validation_rejects_missing_required_name_fields() -> None:
    entity = create_flow(_load_payload())

    assert entity.validate(mode="pydantic") is False

    error = entity.last_validation_error()
    assert error is not None

    rendered = str(error)
    assert "treatmentStandardsRoutes" in rendered or "treatment_standards_routes" in rendered
    assert "mixAndLocationTypes" in rendered or "mix_and_location_types" in rendered


def test_flow_pydantic_validation_rejects_invalid_localized_text() -> None:
    entity = create_flow(_payload_with_required_name_fields())

    assert entity.validate(mode="pydantic") is False

    error = entity.last_validation_error()
    assert error is not None
    assert "must not contain Chinese characters" in str(error)


def test_flow_jsonschema_validation_returns_validation_errors_not_execution_errors() -> None:
    entity = create_flow(_load_payload())

    assert entity.validate(mode="jsonschema") is False

    errors = entity.jsonschema_errors()
    assert errors
    assert all("Schema validation failed to execute" not in message for message in errors)
