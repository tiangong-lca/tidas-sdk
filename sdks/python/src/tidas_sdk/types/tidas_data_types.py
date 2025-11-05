"""
TIDAS base data types.

This file was manually created to provide clean, reusable type definitions.
DO NOT auto-generate this file - these are foundational types used across all schemas.
"""

from __future__ import annotations

from typing import Annotated, Union

from pydantic import AwareDatetime, BaseModel, Field, RootModel



# ========== String Types ==========

CASNumber = Annotated[str, Field(pattern=r"^[0-9]{2,7}-[0-9]{2}-[0-9]$")]
"""CAS Number, leading zeros are required."""

FT = str
"""Free text with an unlimited length."""

ST = Annotated[str, Field(max_length=1000)]
"""Short text with a maximum length of 1000 characters."""

String = Annotated[str, Field(min_length=1, max_length=500)]
"""String with a maximum length of 500 characters. Must have a minimum length of 1."""


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


class Int1(RootModel):
    """1-digit integer number."""

    root: str = Field(pattern=r"^[0-9]$")


class Int5(RootModel):
    """5-digit integer number."""

    root: str = Field(pattern=r"^(0|[1-9]\d{0,4})$")


class Int6(RootModel):
    """6-digit integer number."""

    root: str = Field(pattern=r"^(0|[1-9]\d{0,5})$")


LevelType = Int1
"""1-digit integer, must be >= 0."""


# ========== Numeric Types ==========

Perc = Annotated[str, Field(pattern=r"^0\.\d+$")]
"""Percentage amount."""

Real = Annotated[str, Field(pattern=r"[+-]?(\d+(\.\d*)?|\.\d+)([Ee][+-]?\d+)?$")]
"""38-digit real number."""

MatR = str
"""Mathematical rule."""

MatV = str
"""Mathematical variable or parameter."""


# ========== Reference Types ==========


class GlobalReferenceType(BaseModel):
    """Reference to another dataset or file."""

    type_: str = Field(alias="@type")
    ref_object_id: str = Field(
        alias="@refObjectId",
        pattern=r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
    )
    version: str = Field(alias="@version")
    uri: str = Field(alias="@uri")
    common_short_description: 'STMultiLang' = Field(alias="common:shortDescription")


# Can also be an array of references
GlobalReferenceTypeOrArray = GlobalReferenceType | list[GlobalReferenceType]

UUID = Annotated[str, Field(pattern=r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")]
"""Unique Universal Identifier, 16-byte hex number."""


# ========== Geographic Types ==========

GIS = Annotated[str, Field(pattern=r"^\s*[+-]?((90(\.0+)?)|([0-8]?\d(\.\d+)?))\s*;\s*[+-]?((180(\.0+)?)|((1[0-7]\d|[0-9]?\d)(\.\d+)?))\s*$")]
"""Global geographical reference in Latitude and Longitude. Examples: "+42.42;-180", "0;0", "13.22 ; -3"."""


# ========== Date/Time Types ==========

class Year(RootModel):
    """4-digit year."""

    root: int = Field(ge=1000, le=9999)


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

# Rebuild models to resolve forward references
GlobalReferenceType.model_rebuild()
