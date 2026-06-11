from pathlib import Path
import sys
from typing import get_args, get_origin

import pytest
from pydantic import ValidationError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from tidas_sdk.generated.tidas_data_types import (
    AnnualSupplyOrProductionVolumeMultiLang,
    AnnualSupplyOrProductionVolumeTextItem,
    FTMultiLang,
    Languages,
    LocalizedText1000Item,
    LocalizedText500Item,
    LocalizedTextItem,
    STMultiLang,
    StringMultiLang,
)
from tidas_sdk.core.multilang import MultiLangList


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


def test_localized_text_item_enforces_ilcd_language_enum() -> None:
    language_values = set(get_args(Languages))

    assert {"en", "de", "zh"}.issubset(language_values)
    assert "en-US" not in language_values

    LocalizedTextItem.model_validate({"@xml:lang": "de", "#text": "Deutscher Titel"})

    with pytest.raises(ValidationError):
        LocalizedTextItem.model_validate({"@xml:lang": "en-US", "#text": "English"})


def test_localized_text_specializations_preserve_max_length() -> None:
    LocalizedText500Item.model_validate({"@xml:lang": "fr", "#text": "a" * 500})
    LocalizedText1000Item.model_validate({"@xml:lang": "fr", "#text": "a" * 1000})

    with pytest.raises(ValidationError):
        LocalizedText500Item.model_validate({"@xml:lang": "fr", "#text": "a" * 501})

    with pytest.raises(ValidationError):
        LocalizedText1000Item.model_validate({"@xml:lang": "fr", "#text": "a" * 1001})


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


def test_annual_supply_volume_alias_preserves_patterned_item_type() -> None:
    annual_array_type, annual_item_type = get_args(
        AnnualSupplyOrProductionVolumeMultiLang
    )

    assert get_origin(annual_array_type) is list
    assert get_args(annual_array_type) == (AnnualSupplyOrProductionVolumeTextItem,)
    assert annual_item_type is AnnualSupplyOrProductionVolumeTextItem

    AnnualSupplyOrProductionVolumeTextItem.model_validate(
        {"@xml:lang": "en", "#text": "12.5 kg reference flow"}
    )

    with pytest.raises(ValidationError):
        AnnualSupplyOrProductionVolumeTextItem.model_validate(
            {"@xml:lang": "en", "#text": "12.5"}
        )


def test_localized_text_item_rejects_en_text_with_chinese_characters() -> None:
    with pytest.raises(ValidationError):
        LocalizedTextItem.model_validate(
            {"@xml:lang": "en", "#text": "天工LCA数据团队"}
        )


def test_localized_text_item_rejects_zh_text_without_chinese_characters() -> None:
    with pytest.raises(ValidationError):
        LocalizedTextItem.model_validate(
            {"@xml:lang": "zh", "#text": "Tiangong LCA Data Team"}
        )


def test_multilang_list_rejects_non_ilcd_language_code() -> None:
    values = MultiLangList()

    with pytest.raises(ValueError):
        values.set_text("English title", "en-US")
