"""
Fallback placeholder for the Process dataset model.

This file will eventually be overwritten by the auto generator. It enables the
early development of entity helpers without depending on the generation
pipeline being ready.
"""
from __future__ import annotations

from typing import Any

from pydantic import Field

from ..core.base import TidasBaseModel


class Process(TidasBaseModel):
    """
    Minimal structure that mimics the ILCD Process dataset root.
    """

    process_data_set: dict[str, Any] | None = Field(
        default_factory=dict,
        validation_alias="processDataSet",
        serialization_alias="processDataSet",
        alias="processDataSet",
    )
