"""
TIDAS Python SDK

Python SDK for TIDAS/ILCD Life Cycle Assessment (LCA) data format.
"""

__version__ = "0.1.0"

# Core validation imports
from .core.validation import (
    ValidationConfig,
    ValidationWarning,
    get_global_validation_mode,
    set_global_validation_mode,
)

# Exception imports
from .core.exceptions import (
    ConfigurationError,
    SchemaGenerationError,
    TidasException,
    ValidationError,
)

# Entity model imports
from .models import (
    TidasContacts,
    TidasFlows,
    TidasFlowproperties,
    TidasLciamethods,
    TidasLifecyclemodels,
    TidasProcesses,
    TidasSources,
    TidasUnitgroups,
)

# Factory function imports
from .factories import (
    create_contact,
    create_contacts_batch,
    create_flow,
    create_flow_property,
    create_flow_properties_batch,
    create_flows_batch,
    create_lcia_method,
    create_lcia_methods_batch,
    create_life_cycle_model,
    create_life_cycle_models_batch,
    create_process,
    create_processes_batch,
    create_source,
    create_sources_batch,
    create_unit_group,
    create_unit_groups_batch,
)

__all__ = [
    # Version
    "__version__",
    # Validation
    "ValidationConfig",
    "ValidationWarning",
    "get_global_validation_mode",
    "set_global_validation_mode",
    # Exceptions
    "TidasException",
    "ValidationError",
    "SchemaGenerationError",
    "ConfigurationError",
    # Entity models
    "TidasContact",
    "TidasFlow",
    "TidasFlowProperty",
    "TidasLCIAMethod",
    "TidasLifeCycleModel",
    "TidasProcess",
    "TidasSource",
    "TidasUnitGroup",
    # Factory functions
    "create_contact",
    "create_contacts_batch",
    "create_flow",
    "create_flows_batch",
    "create_process",
    "create_processes_batch",
    "create_source",
    "create_sources_batch",
    "create_flow_property",
    "create_flow_properties_batch",
    "create_unit_group",
    "create_unit_groups_batch",
    "create_lcia_method",
    "create_lcia_methods_batch",
    "create_life_cycle_model",
    "create_life_cycle_models_batch",
]
