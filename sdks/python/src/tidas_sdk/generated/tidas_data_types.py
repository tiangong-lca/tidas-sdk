"""
Auto generated file. DO NOT EDIT.
Source: tidas_data_types.json
"""
from __future__ import annotations

from pydantic import Field
from tidas_sdk.core.base import TidasBaseModel
from tidas_sdk.core.multilang import MultiLangList

from datetime import datetime

class Globalreferencetype(TidasBaseModel):
    """Represents a reference to another dataset or file. Either refObjectId and version, or uri, or both have to be specified."""
    pass

class DataTypes(TidasBaseModel):
    pass
