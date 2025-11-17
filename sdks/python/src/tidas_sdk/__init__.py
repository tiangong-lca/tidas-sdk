"""
TIDAS Python SDK public interface.

The package exposes high-level factory helpers (e.g. ``create_process``)
as well as entity classes that wrap generated models. The actual factories
and entities will be populated as the SDK generation workflow is completed.
"""

from .core.factory import (  # noqa: F401
    create_contact,
    create_flow,
    create_flow_property,
    create_lcia_method,
    create_life_cycle_model,
    create_process,
    create_process_from_json,
    create_processes_batch,
    create_source,
    create_unit_group,
)

from .core.factory import (  # noqa: F401
    TidasContact,
    TidasFlow,
    TidasFlowProperty,
    TidasLCIAMethod,
    TidasLifeCycleModel,
    TidasProcess,
    TidasSource,
    TidasUnitGroup,
)

__all__ = [
    "create_contact",
    "create_flow",
    "create_flow_property",
    "create_lcia_method",
    "create_life_cycle_model",
    "create_process",
    "create_process_from_json",
    "create_processes_batch",
    "create_source",
    "create_unit_group",
    "TidasContact",
    "TidasFlow",
    "TidasFlowProperty",
    "TidasLCIAMethod",
    "TidasLifeCycleModel",
    "TidasProcess",
    "TidasSource",
    "TidasUnitGroup",
]
