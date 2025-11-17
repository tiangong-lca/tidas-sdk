"""
Factory helpers for constructing TIDAS entities.
"""
from __future__ import annotations

from typing import Any, Mapping

from ..entities.process import TidasProcess

__all__ = [
    "create_process",
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
    validate_on_init: bool = False,
) -> TidasProcess:
    """
    Create a Process entity from a partial JSON payload.
    """
    return TidasProcess(dict(data) if data is not None else None, validate_on_init=validate_on_init)


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
