from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from tidas_sdk import create_contact
from tidas_sdk.core.multilang import MultiLangList, deep_wrap_multilang


def _localized_text(text: str) -> dict[str, str]:
    return {"@xml:lang": "en", "#text": text}


def _reference_payload(*, type_name: str, ref_object_id: str, short_description: str) -> dict[str, object]:
    return {
        "@type": type_name,
        "@refObjectId": ref_object_id,
        "@version": "01.00.000",
        "@uri": f"https://example.com/{ref_object_id}",
        "common:shortDescription": _localized_text(short_description),
    }


def _contact_payload() -> dict[str, object]:
    return {
        "contactDataSet": {
            "@xmlns": "http://lca.jrc.it/ILCD/Contact",
            "@xmlns:common": "http://lca.jrc.it/ILCD/Common",
            "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
            "@version": "1.1",
            "@xsi:schemaLocation": "http://lca.jrc.it/ILCD/Contact ../../schemas/ILCD_ContactDataSet.xsd",
            "contactInformation": {
                "dataSetInformation": {
                    "common:UUID": "08b5c3f5-e917-4fec-a883-28cb7bc2e604",
                    "common:shortName": _localized_text("ZMJ"),
                    "common:name": [_localized_text("Zhong Miaojiu")],
                    "classificationInformation": {
                        "common:classification": {
                            "common:class": {
                                "@level": "0",
                                "@classId": "contact",
                                "#text": "Contact",
                            }
                        }
                    },
                }
            },
            "administrativeInformation": {
                "dataEntryBy": {
                    "common:timeStamp": "2026-04-02T00:00:00",
                    "common:referenceToDataSetFormat": _reference_payload(
                        type_name="source data set",
                        ref_object_id="00000000-0000-0000-0000-000000000001",
                        short_description="ILCD format reference",
                    ),
                },
                "publicationAndOwnership": {
                    "common:dataSetVersion": "01.01.000",
                    "common:referenceToOwnershipOfDataSet": _reference_payload(
                        type_name="contact data set",
                        ref_object_id="00000000-0000-0000-0000-000000000002",
                        short_description="Owner contact reference",
                    ),
                },
            },
        }
    }


def test_deep_wrap_multilang_wraps_nested_single_item_dicts() -> None:
    payload = {
        "contactDataSet": {
            "contactInformation": {
                "dataSetInformation": {
                    "common:shortName": _localized_text("ZMJ"),
                }
            }
        }
    }

    wrapped = deep_wrap_multilang(payload)
    short_name = wrapped["contactDataSet"]["contactInformation"]["dataSetInformation"]["common:shortName"]

    assert isinstance(short_name, MultiLangList)
    assert short_name.get_text() == "ZMJ"


def test_contact_pydantic_validation_accepts_single_object_multilang_fields() -> None:
    entity = create_contact(_contact_payload())

    assert entity.validate(mode="pydantic") is True

    short_name = entity.contact_data_set.contact_information.data_set_information.common_short_name
    assert isinstance(short_name, MultiLangList)
    assert short_name.get_text() == "ZMJ"


def test_contact_pydantic_validation_still_rejects_empty_reference_objects() -> None:
    payload = deepcopy(_contact_payload())
    data_set_information = payload["contactDataSet"]["contactInformation"]["dataSetInformation"]
    publication_and_ownership = payload["contactDataSet"]["administrativeInformation"]["publicationAndOwnership"]

    data_set_information["referenceToContact"] = {}
    data_set_information["referenceToLogo"] = {}
    publication_and_ownership["common:referenceToPrecedingDataSetVersion"] = {}

    entity = create_contact(payload)

    assert entity.validate(mode="pydantic") is False

    error = entity.last_validation_error()
    assert error is not None

    rendered = str(error)
    assert "referenceToContact" in rendered or "reference_to_contact" in rendered
    assert "referenceToLogo" in rendered or "reference_to_logo" in rendered
    assert (
        "referenceToPrecedingDataSetVersion" in rendered
        or "common_reference_to_preceding_data_set_version" in rendered
    )
    assert "common:shortName" not in rendered
    assert "common_short_name" not in rendered
