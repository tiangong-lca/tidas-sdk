from pathlib import Path
import sys
from typing import get_args, get_origin

import pytest
from pydantic import ValidationError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from tidas_sdk.generated.tidas_data_types import (
    FTMultiLang,
    LocalizedText1000Item,
    LocalizedText500Item,
    LocalizedTextItem,
    STMultiLang,
    StringMultiLang,
)


def test_localized_text_item_requires_schema_fields() -> None:
    item = LocalizedTextItem.model_validate(
        {"@xml:lang": "en", "#text": "English title"}
    )

    assert item.xml_lang == "en"
    assert item.text == "English title"

    with pytest.raises(ValidationError):
        LocalizedTextItem.model_validate({"#text": "English title"})

    with pytest.raises(ValidationError):
        LocalizedTextItem.model_validate({"@xml:lang": "en"})


def test_localized_text_specializations_preserve_max_length() -> None:
    LocalizedText500Item.model_validate(
        {"@xml:lang": "fr", "#text": "a" * 500}
    )
    LocalizedText1000Item.model_validate(
        {"@xml:lang": "fr", "#text": "a" * 1000}
    )

    with pytest.raises(ValidationError):
        LocalizedText500Item.model_validate(
            {"@xml:lang": "fr", "#text": "a" * 501}
        )

    with pytest.raises(ValidationError):
        LocalizedText1000Item.model_validate(
            {"@xml:lang": "fr", "#text": "a" * 1001}
        )


def test_multilang_aliases_reference_localized_text_models() -> None:
    string_array_type, string_item_type = get_args(StringMultiLang)
    st_array_type, st_item_type = get_args(STMultiLang)
    ft_array_type, ft_item_type = get_args(FTMultiLang)

    assert get_origin(string_array_type) is list
    assert get_args(string_array_type) == (LocalizedText500Item,)
    assert string_item_type is LocalizedText500Item

    assert get_origin(st_array_type) is list
    assert get_args(st_array_type) == (LocalizedText1000Item,)
    assert st_item_type is LocalizedText1000Item

    assert get_origin(ft_array_type) is list
    assert get_args(ft_array_type) == (LocalizedTextItem,)
    assert ft_item_type is LocalizedTextItem
