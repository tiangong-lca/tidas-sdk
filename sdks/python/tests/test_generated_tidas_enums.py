from pathlib import Path
import sys
from typing import Literal, get_args, get_origin

import pytest
from pydantic import ValidationError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from tidas_sdk.generated.tidas_flows import FlowDataSetModellingAndValidationLCIMethod
from tidas_sdk.generated.tidas_lciamethods import (
    CharacterisationFactorsFactorItem,
    CharacterisationFactorsFactorOption0,
    ItemCommonMethodItem,
    ItemCommonMethodOption0,
    LCIAMethodDataSetModellingAndValidationLCIAMethodNormalisationAndWeighting,
    LCIAMethodDataSetLCIAMethodInformationDataSetInformation,
    Option0CommonMethodItem,
    Option0CommonMethodOption0,
)


def literal_values(annotation) -> set[str]:
    values = set()

    def visit(node) -> None:
        if get_origin(node) is Literal:
            values.update(get_args(node))
            return
        for child in get_args(node):
            visit(child)

    visit(annotation)
    return values


def field_literal_values(model, field_name: str) -> set[str]:
    return literal_values(model.model_fields[field_name].annotation)


def test_lcia_area_of_protection_accepts_man_made_environment() -> None:
    values = field_literal_values(
        LCIAMethodDataSetLCIAMethodInformationDataSetInformation,
        "area_of_protection",
    )

    assert "Man-made environment" in values


def test_flow_type_accepts_other_flow() -> None:
    values = field_literal_values(
        FlowDataSetModellingAndValidationLCIMethod,
        "type_of_data_set",
    )

    assert "Other flow" in values


def test_lcia_uncertainty_distribution_uses_normal() -> None:
    # Both the single-object and array branches now use the ILCD-aligned field
    # name uncertainty_distribution_type (A5 unified the array branch).
    for model in (
        CharacterisationFactorsFactorOption0,
        CharacterisationFactorsFactorItem,
    ):
        values = field_literal_values(model, "uncertainty_distribution_type")
        assert "normal" in values
        assert "normalisation" not in values


def test_lcia_normalisation_boolean_field_keeps_schema_alias() -> None:
    field = LCIAMethodDataSetModellingAndValidationLCIAMethodNormalisationAndWeighting.model_fields[
        "normalisation"
    ]

    assert field.alias == "normalisation"


@pytest.mark.parametrize(
    "model",
    [
        Option0CommonMethodOption0,
        Option0CommonMethodItem,
        ItemCommonMethodOption0,
        ItemCommonMethodItem,
    ],
)
def test_review_method_uses_lcia_specific_values(model) -> None:
    # A4: LCIA-method review uses ILCD MethodOfReviewValues, not the process
    # review method list. "Compliance with legal limits" is process-only and
    # must NOT appear here.
    values = field_literal_values(model, "name")

    assert "Expert judgement" in values
    assert "Cross-check with other LCIA method(ology)" in values
    assert "Compliance with legal limits" not in values
    model.model_validate({"@name": "Expert judgement"})
    with pytest.raises(ValidationError):
        model.model_validate({"@name": "Compliance with legal limits"})
