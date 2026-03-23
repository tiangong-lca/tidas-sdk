"""
Auto generated file. DO NOT EDIT.
Source: tidas_data_types.json
"""
from __future__ import annotations

import re

from typing import Annotated

from pydantic import Field, model_validator
from tidas_sdk.core.base import TidasBaseModel
from tidas_sdk.core.multilang import MultiLangList

from datetime import datetime

CHINESE_CHARACTER_PATTERN = re.compile(r'[\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]')

# CAS Number, leading zeros are requried.
CASNumber = Annotated[str, Field(pattern='^[0-9]{2,7}-[0-9]{2}-[0-9]$')]
# Free text with an unlimited length.
FT = str
# 1-digit integer number
Int1 = Annotated[str, Field(pattern='^[0-9]$')]
# 5-digit integer number
Int5 = Annotated[str, Field(pattern='^(0|[1-9]\\d{0,4})$')]
# 6-digit integer number
Int6 = Annotated[str, Field(pattern='^(0|[1-9]\\d{0,5})$')]
# 1-digit integer number, must be equal to or greater than 0
LevelType = Int1
# percentage amount
Perc = Annotated[str, Field(pattern='^(100(\\.0{1,3})?|([0-9]|[1-9][0-9])(\\.\\d{1,3})?)$')]
# Mathematical rule
MatR = str
# Mathematical variable or parameter
MatV = str
# 38-digit real number
Real = Annotated[str, Field(pattern='[+-]?(\\d+(\\.\\d*)?|\\.\\d+)([Ee][+-]?\\d+)?$')]
# Short text with a maximum length of 1000 characters
ST = Annotated[str, Field(max_length=1000)]
# String with a maximum length of 500 characters. Must have a minimum length of 1.
String = Annotated[str, Field(min_length=1, max_length=500)]
# Global geographical reference in Latitude and LongitudeExamples: "+42.42;-180", "0;0", "13.22 ; -3"
GIS = Annotated[str, Field(pattern='^\\s*[+-]?((90(\\.0+)?)|([0-8]?\\d(\\.\\d+)?))\\s*;\\s*[+-]?((180(\\.0+)?)|((1[0-7]\\d|[0-9]?\\d)(\\.\\d+)?))\\s*$')]
# Unique Universal Identifier, 16-byte hex number
UUID = Annotated[str, Field(pattern='^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')]
# 4-digit year
Year = Annotated[int, Field(ge=1000, le=9999)]
# Date and time format acc. to ISO 8601
DateTime = datetime

class LocalizedTextItem(TidasBaseModel):
    """Language-tagged text with optional script checks for selected languages."""
    xml_lang: str = Field(default=..., alias='@xml:lang')
    text: str = Field(default=..., alias='#text')

    @model_validator(mode='after')
    def _validate_language_script(self) -> 'LocalizedTextItem':
        if re.match(r'^[zZ][hH](?:-|$)', self.xml_lang) and not CHINESE_CHARACTER_PATTERN.search(self.text):
            raise ValueError("@xml:lang values starting with 'zh' must include at least one Chinese character")
        if re.match(r'^[eE][nN](?:-|$)', self.xml_lang) and CHINESE_CHARACTER_PATTERN.search(self.text):
            raise ValueError("@xml:lang values starting with 'en' must not contain Chinese characters")
        return self

class LocalizedText500Item(LocalizedTextItem):
    """Language-tagged text with a maximum length of 500 characters."""
    xml_lang: str = Field(default=..., alias='@xml:lang')
    text: str = Field(default=..., alias='#text', max_length=500)

    @model_validator(mode='after')
    def _validate_language_script(self) -> 'LocalizedText500Item':
        if re.match(r'^[zZ][hH](?:-|$)', self.xml_lang) and not CHINESE_CHARACTER_PATTERN.search(self.text):
            raise ValueError("@xml:lang values starting with 'zh' must include at least one Chinese character")
        if re.match(r'^[eE][nN](?:-|$)', self.xml_lang) and CHINESE_CHARACTER_PATTERN.search(self.text):
            raise ValueError("@xml:lang values starting with 'en' must not contain Chinese characters")
        return self

class LocalizedText1000Item(LocalizedTextItem):
    """Language-tagged text with a maximum length of 1000 characters."""
    xml_lang: str = Field(default=..., alias='@xml:lang')
    text: str = Field(default=..., alias='#text', max_length=1000)

    @model_validator(mode='after')
    def _validate_language_script(self) -> 'LocalizedText1000Item':
        if re.match(r'^[zZ][hH](?:-|$)', self.xml_lang) and not CHINESE_CHARACTER_PATTERN.search(self.text):
            raise ValueError("@xml:lang values starting with 'zh' must include at least one Chinese character")
        if re.match(r'^[eE][nN](?:-|$)', self.xml_lang) and CHINESE_CHARACTER_PATTERN.search(self.text):
            raise ValueError("@xml:lang values starting with 'en' must not contain Chinese characters")
        return self

class GlobalReferenceTypeVariant0(TidasBaseModel):
    type: str = Field(default=..., alias='@type')
    ref_object_id: str = Field(default=..., alias='@refObjectId', pattern='^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')
    version: str = Field(default=..., alias='@version')
    uri: str = Field(default=..., alias='@uri')
    common_short_description: MultiLangList = Field(default=..., alias='common:shortDescription')

class GlobalReferenceTypeVariant1Item(TidasBaseModel):
    type: str = Field(default=..., alias='@type')
    ref_object_id: str = Field(default=..., alias='@refObjectId', pattern='^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')
    version: str = Field(default=..., alias='@version')
    uri: str = Field(default=..., alias='@uri')
    common_short_description: MultiLangList = Field(default=..., alias='common:shortDescription')

class DataTypes(TidasBaseModel):
    pass

# Multi-language string with a maximum length of 500 characters
StringMultiLang = list[LocalizedText500Item] | LocalizedText500Item
# Multi-lang short text with a maximum length of 1000 characters.
STMultiLang = list[LocalizedText1000Item] | LocalizedText1000Item
# Multi-lang free text with an unlimited length.
FTMultiLang = list[LocalizedTextItem] | LocalizedTextItem
# Represents a reference to another dataset or file. In TIDAS, references must include type, refObjectId, version, uri, and shortDescription.
GlobalReferenceType = GlobalReferenceTypeVariant0 | list[GlobalReferenceTypeVariant1Item]
