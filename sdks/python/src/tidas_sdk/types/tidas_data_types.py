"""
TIDAS base data types.

This file was manually created to provide clean, reusable type definitions.
DO NOT auto-generate this file - these are foundational types used across all schemas.
"""

from __future__ import annotations

from typing import Annotated, Union

from pydantic import AwareDatetime, BaseModel, Field, RootModel


# ========== String Types ==========


class String(RootModel[str]):
    """String with max 500 characters, min 1 character."""

    root: Annotated[str, Field(min_length=1, max_length=500)]


class ST(RootModel[str]):
    """Short text with a maximum length of 1000 characters."""

    root: Annotated[str, Field(max_length=1000)]


class FT(RootModel[str]):
    """Free text with an unlimited length."""

    root: str


class CASNumber(RootModel[str]):
    """CAS Number, leading zeros are required."""

    root: Annotated[str, Field(pattern=r"^[0-9]{2,7}-[0-9]{2}-[0-9]$")]


# ========== Multi-Language Types ==========


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


class Int5(RootModel[str]):
    """5-digit integer number."""

    root: Annotated[str, Field(pattern=r"^(0|[1-9]\d{0,4})$")]


class Int6(RootModel[str]):
    """6-digit integer number."""

    root: Annotated[str, Field(pattern=r"^(0|[1-9]\d{0,5})$")]


LevelType = Int1
"""1-digit integer, must be >= 0."""


# ========== Numeric Types ==========


class Perc(RootModel[str]):
    """Percentage amount."""

    root: Annotated[
        str, Field(pattern=r"^(100(\.0{1,3})?|([0-9]|[1-9][0-9])(\.\d{1,3})?)$")
    ]


class Real(RootModel[str]):
    """38-digit real number."""

    root: Annotated[str, Field(pattern=r"[+-]?(\d+(\.\d*)?|\.\d+)([Ee][+-]?\d+)?$")]


class MatR(RootModel[str]):
    """Mathematical rule."""

    root: str


class MatV(RootModel[str]):
    """Mathematical variable or parameter."""

    root: str


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


class GIS(RootModel[str]):
    """Global geographical reference in Latitude and Longitude.

    Examples: "+42.42;-180", "0;0", "13.22 ; -3"
    """

    root: Annotated[
        str,
        Field(
            pattern=r"^\s*[+-]?((90(\.0+)?)|([0-8]?\d(\.\d+)?))\s*;\s*[+-]?((180(\.0+)?)|((1[0-7]\d|[0-9]?\d)(\.\d+)?))\s*$"
        ),
    ]


# ========== Date/Time Types ==========


class Year(RootModel[int]):
    """4-digit year."""

    root: Annotated[int, Field(ge=1000, le=9999)]


class UUID(RootModel[str]):
    """Unique Universal Identifier, 16-byte hex number."""

    root: Annotated[
        str,
        Field(
            pattern=r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
        ),
    ]


# DateTime is handled by pydantic's built-in AwareDatetime type
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
