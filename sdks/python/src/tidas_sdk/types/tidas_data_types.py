"""
TIDAS base data types.

This file was manually created to provide clean, reusable type definitions.
DO NOT auto-generate this file - these are foundational types used across all schemas.
"""

from __future__ import annotations

from typing import Annotated, Union

from pydantic import AwareDatetime, BaseModel, Field, RootModel
from tidas_sdk.types.tidas_data_types import (
    CASNumber,
    FT,
    FTMultiLang,
    GIS,
    GlobalReferenceType,
    GlobalReferenceTypeOrArray,
    Int1,
    Int5,
    Int6,
    LevelType,
    MatR,
    MatV,
    MultiLangItem,
    MultiLangItemST,
    MultiLangItemString,
    Perc,
    Real,
    ST,
    STMultiLang,
    String,
    StringMultiLang,
    UUID,
    Year
)



# ========== String Types ==========


class MultiLangItem(BaseModel):
    """Single multi-language text item."""

    lang: str = Field(alias="@xml:lang")
    text: str = Field(alias="#text")


class MultiLangItemString(MultiLangItem):
    """Multi-language string item (max 500 chars)."""

    text: Annotated[str, Field(alias="#text", max_length=500)]


class MultiLangItemST(MultiLangItem):
    """Multi-language short text item (max 1000 chars)."""

    text: Annotated[str, Field(alias="#text", max_length=1000)]


# Multi-language type aliases
StringMultiLang = list[MultiLangItemString] | MultiLangItemString
"""Multi-language string with max 500 characters."""

STMultiLang = list[MultiLangItemST] | MultiLangItemST
"""Multi-language short text with max 1000 characters."""

FTMultiLang = list[MultiLangItem] | MultiLangItem
"""Multi-language free text with unlimited length."""


# ========== Integer Types ==========


class Int1(RootModel[str]):
    """1-digit integer number."""

    root: Annotated[str, Field(pattern=r"^[0-9]$")]


LevelType = Int1
"""1-digit integer, must be >= 0."""


# ========== Numeric Types ==========


class GlobalReferenceType(BaseModel):
    """Reference to another dataset or file."""

    type_: str = Field(alias="@type")
    ref_object_id: Annotated[
        str,
        Field(
            alias="@refObjectId",
            pattern=r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
        ),
    ]
    version: str = Field(alias="@version")
    uri: str = Field(alias="@uri")
    common_short_description: STMultiLang = Field(alias="common:shortDescription")


# Can also be an array of references
GlobalReferenceTypeOrArray = GlobalReferenceType | list[GlobalReferenceType]


# ========== Geographic Types ==========


dateTime = AwareDatetime
"""Date and time format according to ISO 8601."""


__all__ = [
    # String types
    "CASNumber",
    "FT",
    "ST",
    "String",
    # Multi-language types
    "MultiLangItem",
    "MultiLangItemString",
    "MultiLangItemST",
    "StringMultiLang",
    "STMultiLang",
    "FTMultiLang",
    # Integer types
    "Int1",
    "Int5",
    "Int6",
    "LevelType",
    # Numeric types
    "Perc",
    "Real",
    "MatR",
    "MatV",
    # Reference types
    "UUID",
    "GlobalReferenceType",
    "GlobalReferenceTypeOrArray",
    # Geographic types
    "GIS",
    # Date/Time types
    "Year",
    "dateTime",
]
