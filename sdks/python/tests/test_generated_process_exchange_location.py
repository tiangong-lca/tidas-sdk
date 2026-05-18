from __future__ import annotations

import pytest
from pydantic import ValidationError

from tidas_sdk.core.multilang import MultiLangList
from tidas_sdk.generated.tidas_processes import ExchangesExchangeItem


def _exchange_payload(location: object) -> dict[str, object]:
    return {
        "@dataSetInternalID": "1",
        "referenceToFlowDataSet": {
            "@type": "flow data set",
            "@refObjectId": "12345678-1234-1234-1234-123456789abc",
            "@version": "00.00.000",
            "@uri": "",
            "common:shortDescription": MultiLangList(
                [{"@xml:lang": "en", "#text": "Reference flow"}]
            ),
        },
        "location": location,
        "exchangeDirection": "Input",
        "meanAmount": "1.0",
        "resultingAmount": "1.0",
        "dataDerivationTypeStatus": "Measured",
    }


def test_exchange_location_accepts_location_code_and_legacy_string() -> None:
    assert (
        ExchangesExchangeItem.model_validate(_exchange_payload("CN")).location == "CN"
    )
    assert (
        ExchangesExchangeItem.model_validate(_exchange_payload("GLO")).location == "GLO"
    )
    assert (
        ExchangesExchangeItem.model_validate(
            _exchange_payload("Legacy plant area")
        ).location
        == "Legacy plant area"
    )


def test_exchange_location_rejects_empty_and_multilang_shapes() -> None:
    with pytest.raises(ValidationError):
        ExchangesExchangeItem.model_validate(_exchange_payload(""))

    with pytest.raises(ValidationError):
        ExchangesExchangeItem.model_validate(
            _exchange_payload({"@xml:lang": "en", "#text": "CN"})
        )

    with pytest.raises(ValidationError):
        ExchangesExchangeItem.model_validate(
            _exchange_payload([{"@xml:lang": "en", "#text": "CN"}])
        )
