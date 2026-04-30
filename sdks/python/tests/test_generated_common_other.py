from __future__ import annotations

import pytest
from pydantic import ValidationError

from tidas_sdk.generated.tidas_flows import FlowDataSetFlowInformationQuantitativeReference


def _name_payload(common_other: object) -> dict[str, object]:
    return {
        "referenceToReferenceFlowProperty": "0",
        "common:other": common_other,
    }


def test_common_other_accepts_extension_object() -> None:
    model = FlowDataSetFlowInformationQuantitativeReference.model_validate(
        _name_payload(
            {
                "@xmlns:ext": "https://example.com/tidas/extensions",
                "ext:note": {"#text": "Carbon dioxide", "@xml:lang": "en"},
            }
        )
    )

    assert model.common_other == {
        "@xmlns:ext": "https://example.com/tidas/extensions",
        "ext:note": {"#text": "Carbon dioxide", "@xml:lang": "en"},
    }


def test_common_other_rejects_legacy_string() -> None:
    with pytest.raises(ValidationError):
        FlowDataSetFlowInformationQuantitativeReference.model_validate(
            _name_payload("Carbon dioxide")
        )


def test_common_other_rejects_namespace_only_and_common_entries() -> None:
    with pytest.raises(ValidationError):
        FlowDataSetFlowInformationQuantitativeReference.model_validate(
            _name_payload({"@xmlns:ext": "https://example.com/tidas/extensions"})
        )

    with pytest.raises(ValidationError):
        FlowDataSetFlowInformationQuantitativeReference.model_validate(
            _name_payload({"common:note": "Carbon dioxide"})
        )
