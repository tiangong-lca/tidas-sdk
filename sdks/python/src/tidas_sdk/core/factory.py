"""
Factory helpers for constructing TIDAS entities.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable, Mapping

from .base import ValidationMode
from ..entities.process import TidasProcess

__all__ = [
    "create_process",
    "create_process_from_json",
    "create_processes_batch",
    "create_flow",
    "create_contact",
    "create_source",
    "create_flow_property",
    "create_unit_group",
    "create_lcia_method",
    "create_life_cycle_model",
    "TidasProcess",
    "TidasFlow",
    "TidasContact",
    "TidasSource",
    "TidasFlowProperty",
    "TidasUnitGroup",
    "TidasLCIAMethod",
    "TidasLifeCycleModel",
]


def create_process(
    data: Mapping[str, Any] | None = None,
    *,
    validate: bool = False,
    validation_mode: ValidationMode = "pydantic",
) -> TidasProcess:
    """
    Create a Process entity from a partial JSON payload.
    """
    entity = TidasProcess(
        dict(data) if data is not None else None,
        validate_on_init=validate and validation_mode == "pydantic",
    )
    if validate:
        entity.validate(mode=validation_mode)
    return entity


def create_process_from_json(
    json_data: str | bytes | Path,
    *,
    validate: bool = False,
    validation_mode: ValidationMode = "pydantic",
) -> TidasProcess:
    """
    Create a Process entity from JSON string/bytes/path input.
    """
    payload = _parse_json_payload(json_data)
    return create_process(payload, validate=validate, validation_mode=validation_mode)


def create_processes_batch(
    data_array: Iterable[Mapping[str, Any]],
    *,
    validate: bool = False,
    validation_mode: ValidationMode = "pydantic",
) -> list[TidasProcess]:
    """
    Batch create Process entities.
    """
    return [
        create_process(data, validate=validate, validation_mode=validation_mode)
        for data in data_array
    ]


# Placeholder factories for the remaining entity types. These will be fleshed out as the
# generator starts producing the corresponding models.
def _unimplemented(name: str):
    def _raise(*_: Any, **__: Any) -> None:
        raise NotImplementedError(
            f"{name} entity is not available yet. Run the generator once it is implemented."
        )

    return _raise


create_flow = _unimplemented("Flow")
create_contact = _unimplemented("Contact")
create_source = _unimplemented("Source")
create_flow_property = _unimplemented("FlowProperty")
create_unit_group = _unimplemented("UnitGroup")
create_lcia_method = _unimplemented("LCIAMethod")
create_life_cycle_model = _unimplemented("LifeCycleModel")


# Entity placeholders keep the public API stable while we build out their concrete implementations.
class _PlaceholderEntity:  # pragma: no cover - thin shim
    def __init__(self, *_: Any, **__: Any) -> None:
        raise NotImplementedError(
            "Full entity support is not ready yet. This placeholder prevents import errors."
        )


TidasFlow = _PlaceholderEntity
TidasContact = _PlaceholderEntity
TidasSource = _PlaceholderEntity
TidasFlowProperty = _PlaceholderEntity
TidasUnitGroup = _PlaceholderEntity
TidasLCIAMethod = _PlaceholderEntity
TidasLifeCycleModel = _PlaceholderEntity


def _parse_json_payload(json_data: str | bytes | Path) -> Mapping[str, Any]:
    if isinstance(json_data, Path):
        content = json_data.read_text(encoding="utf-8")
    elif isinstance(json_data, bytes):
        content = json_data.decode("utf-8")
    else:
        content = json_data
    return json.loads(content)
