"""
XML serialization helpers.

The initial implementation keeps things intentionally simple and will be
replaced by a schema-aware variant once the generator can provide richer
metadata.
"""
from __future__ import annotations

from typing import Any, Mapping


def dataset_to_xml(dataset: Mapping[str, Any]) -> str:
    """
    Convert a dataset dictionary into a placeholder XML string.
    """
    # TODO: implement schema aware serialization.
    raise NotImplementedError(
        "XML serialization is not wired up yet. This stub exists as a reminder in the TODO list."
    )
