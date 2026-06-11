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
    uncertainty_distribution_values = field_literal_values(
        CharacterisationFactorsFactorOption0,
        "uncertainty_distribution_type",
    )
    uncertainty_type_values = field_literal_values(
        CharacterisationFactorsFactorItem,
        "uncertainty_type",
    )

    assert "normal" in uncertainty_distribution_values
    assert "normalisation" not in uncertainty_distribution_values
    assert "normal" in uncertainty_type_values
    assert "normalisation" not in uncertainty_type_values


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
def test_review_method_accepts_exact_compliance_with_legal_limits(model) -> None:
    values = field_literal_values(model, "name")

    assert "Compliance with legal limits" in values
    assert all(
        not value.startswith("Compliance with legal limitsRegulated")
        for value in values
    )
    model.model_validate({"@name": "Compliance with legal limits"})
    with pytest.raises(ValidationError):
        model.model_validate(
            {"@name": "Compliance with legal limitsRegulated limits given"}
        )
