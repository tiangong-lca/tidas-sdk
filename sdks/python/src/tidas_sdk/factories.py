"""
Factory functions for creating TIDAS entities.

This module provides convenient factory functions for creating all TIDAS entity types,
including single entity creation and batch operations. All factory functions support
automatic UUID generation and flexible validation configuration.
"""

import uuid
from typing import Any, Callable, Dict, List, Optional, TypeVar

from loguru import logger

from .core.validation import ValidationConfig
from .models import (
    TidasContact,
    TidasFlow,
    TidasFlowProperty,
    TidasLCIAMethod,
    TidasLifeCycleModel,
    TidasProcess,
    TidasSource,
    TidasUnitGroup,
)

# Type variable for generic entity types
TEntity = TypeVar("TEntity")


def _generate_uuid_if_needed(data: Dict[str, Any], uuid_path: List[str]) -> Dict[str, Any]:
    """Generate UUID for entity if not provided in data.

    Args:
        data: Entity data dictionary
        uuid_path: Path to UUID field as list of keys

    Returns:
        Modified data dictionary with UUID set
    """
    # Navigate to the parent of the UUID field
    current = data
    for key in uuid_path[:-1]:
        if key not in current:
            current[key] = {}
        current = current[key]

    # Check if UUID exists, if not generate one
    uuid_key = uuid_path[-1]
    if uuid_key not in current or not current[uuid_key]:
        current[uuid_key] = str(uuid.uuid4())
        logger.debug(f"Generated UUID: {current[uuid_key]}")

    return data


def _create_batch(
    factory_func: Callable[[Optional[Dict[str, Any]], Optional[ValidationConfig]], TEntity],
    data_list: List[Dict[str, Any]],
    validation_config: Optional[ValidationConfig] = None,
) -> List[TEntity]:
    """Generic batch creation helper.

    Args:
        factory_func: Single entity factory function
        data_list: List of entity data dictionaries
        validation_config: Optional validation configuration for all entities

    Returns:
        List of created entities
    """
    entities = []
    for data in data_list:
        entity = factory_func(data, validation_config)
        entities.append(entity)

    logger.info(f"Created batch of {len(entities)} entities")
    return entities


# Contact factory functions


def create_contact(
    data: Optional[Dict[str, Any]] = None,
    validation_config: Optional[ValidationConfig] = None,
) -> TidasContact:
    """Create a Contact entity.

    If data is provided without a UUID, a UUID will be automatically generated.

    Args:
        data: Contact data as dictionary (TIDAS JSON format). If None, creates empty contact.
        validation_config: Validation configuration. If None, uses global default.

    Returns:
        TidasContact instance

    Example:
        >>> contact = create_contact()
        >>> contact.contact_data_set.contact_information.data_set_information.name.set_text(
        ...     "Dr. Jane Smith", "en"
        ... )
        >>> contact.validate()
    """
    if data is None:
        data = {}

    # Auto-generate UUID if not provided
    uuid_path = ["contactDataSet", "contactInformation", "dataSetInformation", "common:UUID"]
    data = _generate_uuid_if_needed(data, uuid_path)

    return TidasContact(data=data, validation_config=validation_config)


def create_contacts_batch(
    data_list: List[Dict[str, Any]],
    validation_config: Optional[ValidationConfig] = None,
) -> List[TidasContact]:
    """Create multiple Contact entities in batch.

    UUIDs will be automatically generated for any contacts without UUIDs.

    Args:
        data_list: List of contact data dictionaries
        validation_config: Optional validation configuration for all contacts

    Returns:
        List of TidasContact instances

    Example:
        >>> contacts = create_contacts_batch([{}, {}])  # Create 2 empty contacts
        >>> len(contacts)
        2
    """
    return _create_batch(create_contact, data_list, validation_config)


# Flow factory functions


def create_flow(
    data: Optional[Dict[str, Any]] = None,
    validation_config: Optional[ValidationConfig] = None,
) -> TidasFlow:
    """Create a Flow entity.

    If data is provided without a UUID, a UUID will be automatically generated.

    Args:
        data: Flow data as dictionary (TIDAS JSON format). If None, creates empty flow.
        validation_config: Validation configuration. If None, uses global default.

    Returns:
        TidasFlow instance

    Example:
        >>> flow = create_flow()
        >>> flow.flow_data_set.flow_information.data_set_information.name.base_name.set_text(
        ...     "Carbon dioxide", "en"
        ... )
    """
    if data is None:
        data = {}

    # Auto-generate UUID if not provided
    uuid_path = ["flowDataSet", "flowInformation", "dataSetInformation", "common:UUID"]
    data = _generate_uuid_if_needed(data, uuid_path)

    return TidasFlow(data=data, validation_config=validation_config)


def create_flows_batch(
    data_list: List[Dict[str, Any]],
    validation_config: Optional[ValidationConfig] = None,
) -> List[TidasFlow]:
    """Create multiple Flow entities in batch.

    UUIDs will be automatically generated for any flows without UUIDs.

    Args:
        data_list: List of flow data dictionaries
        validation_config: Optional validation configuration for all flows

    Returns:
        List of TidasFlow instances
    """
    return _create_batch(create_flow, data_list, validation_config)


# Process factory functions


def create_process(
    data: Optional[Dict[str, Any]] = None,
    validation_config: Optional[ValidationConfig] = None,
) -> TidasProcess:
    """Create a Process entity.

    If data is provided without a UUID, a UUID will be automatically generated.

    Args:
        data: Process data as dictionary (TIDAS JSON format). If None, creates empty process.
        validation_config: Validation configuration. If None, uses global default.

    Returns:
        TidasProcess instance

    Example:
        >>> process = create_process()
        >>> process.process_data_set.process_information.data_set_information.name.base_name.set_text(
        ...     "Electricity production", "en"
        ... )
    """
    if data is None:
        data = {}

    # Auto-generate UUID if not provided
    uuid_path = ["processDataSet", "processInformation", "dataSetInformation", "common:UUID"]
    data = _generate_uuid_if_needed(data, uuid_path)

    return TidasProcess(data=data, validation_config=validation_config)


def create_processes_batch(
    data_list: List[Dict[str, Any]],
    validation_config: Optional[ValidationConfig] = None,
) -> List[TidasProcess]:
    """Create multiple Process entities in batch.

    UUIDs will be automatically generated for any processes without UUIDs.

    Args:
        data_list: List of process data dictionaries
        validation_config: Optional validation configuration for all processes

    Returns:
        List of TidasProcess instances
    """
    return _create_batch(create_process, data_list, validation_config)


# Source factory functions


def create_source(
    data: Optional[Dict[str, Any]] = None,
    validation_config: Optional[ValidationConfig] = None,
) -> TidasSource:
    """Create a Source entity.

    If data is provided without a UUID, a UUID will be automatically generated.

    Args:
        data: Source data as dictionary (TIDAS JSON format). If None, creates empty source.
        validation_config: Validation configuration. If None, uses global default.

    Returns:
        TidasSource instance

    Example:
        >>> source = create_source()
        >>> source.source_data_set.source_information.data_set_information.short_name.set_text(
        ...     "Smith et al. 2024", "en"
        ... )
    """
    if data is None:
        data = {}

    # Auto-generate UUID if not provided
    uuid_path = ["sourceDataSet", "sourceInformation", "dataSetInformation", "common:UUID"]
    data = _generate_uuid_if_needed(data, uuid_path)

    return TidasSource(data=data, validation_config=validation_config)


def create_sources_batch(
    data_list: List[Dict[str, Any]],
    validation_config: Optional[ValidationConfig] = None,
) -> List[TidasSource]:
    """Create multiple Source entities in batch.

    UUIDs will be automatically generated for any sources without UUIDs.

    Args:
        data_list: List of source data dictionaries
        validation_config: Optional validation configuration for all sources

    Returns:
        List of TidasSource instances
    """
    return _create_batch(create_source, data_list, validation_config)


# FlowProperty factory functions


def create_flow_property(
    data: Optional[Dict[str, Any]] = None,
    validation_config: Optional[ValidationConfig] = None,
) -> TidasFlowProperty:
    """Create a FlowProperty entity.

    If data is provided without a UUID, a UUID will be automatically generated.

    Args:
        data: FlowProperty data as dictionary (TIDAS JSON format). If None, creates empty flow property.
        validation_config: Validation configuration. If None, uses global default.

    Returns:
        TidasFlowProperty instance

    Example:
        >>> flow_property = create_flow_property()
        >>> flow_property.flow_property_data_set.flow_properties_information.data_set_information.name.set_text(
        ...     "Mass", "en"
        ... )
    """
    if data is None:
        data = {}

    # Auto-generate UUID if not provided
    uuid_path = [
        "flowPropertyDataSet",
        "flowPropertiesInformation",
        "dataSetInformation",
        "common:UUID",
    ]
    data = _generate_uuid_if_needed(data, uuid_path)

    return TidasFlowProperty(data=data, validation_config=validation_config)


def create_flow_properties_batch(
    data_list: List[Dict[str, Any]],
    validation_config: Optional[ValidationConfig] = None,
) -> List[TidasFlowProperty]:
    """Create multiple FlowProperty entities in batch.

    UUIDs will be automatically generated for any flow properties without UUIDs.

    Args:
        data_list: List of flow property data dictionaries
        validation_config: Optional validation configuration for all flow properties

    Returns:
        List of TidasFlowProperty instances
    """
    return _create_batch(create_flow_property, data_list, validation_config)


# UnitGroup factory functions


def create_unit_group(
    data: Optional[Dict[str, Any]] = None,
    validation_config: Optional[ValidationConfig] = None,
) -> TidasUnitGroup:
    """Create a UnitGroup entity.

    If data is provided without a UUID, a UUID will be automatically generated.

    Args:
        data: UnitGroup data as dictionary (TIDAS JSON format). If None, creates empty unit group.
        validation_config: Validation configuration. If None, uses global default.

    Returns:
        TidasUnitGroup instance

    Example:
        >>> unit_group = create_unit_group()
        >>> unit_group.unit_group_data_set.unit_group_information.data_set_information.name.set_text(
        ...     "Mass units", "en"
        ... )
    """
    if data is None:
        data = {}

    # Auto-generate UUID if not provided
    uuid_path = [
        "unitGroupDataSet",
        "unitGroupInformation",
        "dataSetInformation",
        "common:UUID",
    ]
    data = _generate_uuid_if_needed(data, uuid_path)

    return TidasUnitGroup(data=data, validation_config=validation_config)


def create_unit_groups_batch(
    data_list: List[Dict[str, Any]],
    validation_config: Optional[ValidationConfig] = None,
) -> List[TidasUnitGroup]:
    """Create multiple UnitGroup entities in batch.

    UUIDs will be automatically generated for any unit groups without UUIDs.

    Args:
        data_list: List of unit group data dictionaries
        validation_config: Optional validation configuration for all unit groups

    Returns:
        List of TidasUnitGroup instances
    """
    return _create_batch(create_unit_group, data_list, validation_config)


# LCIAMethod factory functions


def create_lcia_method(
    data: Optional[Dict[str, Any]] = None,
    validation_config: Optional[ValidationConfig] = None,
) -> TidasLCIAMethod:
    """Create an LCIAMethod entity.

    If data is provided without a UUID, a UUID will be automatically generated.

    Args:
        data: LCIAMethod data as dictionary (TIDAS JSON format). If None, creates empty LCIA method.
        validation_config: Validation configuration. If None, uses global default.

    Returns:
        TidasLCIAMethod instance

    Example:
        >>> lcia_method = create_lcia_method()
        >>> lcia_method.lcia_method_data_set.lcia_method_information.data_set_information.name.set_text(
        ...     "ReCiPe 2016", "en"
        ... )
    """
    if data is None:
        data = {}

    # Auto-generate UUID if not provided
    uuid_path = [
        "lciaMethodDataSet",
        "lciaMethodInformation",
        "dataSetInformation",
        "common:UUID",
    ]
    data = _generate_uuid_if_needed(data, uuid_path)

    return TidasLCIAMethod(data=data, validation_config=validation_config)


def create_lcia_methods_batch(
    data_list: List[Dict[str, Any]],
    validation_config: Optional[ValidationConfig] = None,
) -> List[TidasLCIAMethod]:
    """Create multiple LCIAMethod entities in batch.

    UUIDs will be automatically generated for any LCIA methods without UUIDs.

    Args:
        data_list: List of LCIA method data dictionaries
        validation_config: Optional validation configuration for all LCIA methods

    Returns:
        List of TidasLCIAMethod instances
    """
    return _create_batch(create_lcia_method, data_list, validation_config)


# LifeCycleModel factory functions


def create_life_cycle_model(
    data: Optional[Dict[str, Any]] = None,
    validation_config: Optional[ValidationConfig] = None,
) -> TidasLifeCycleModel:
    """Create a LifeCycleModel entity.

    If data is provided without a UUID, a UUID will be automatically generated.

    Args:
        data: LifeCycleModel data as dictionary (TIDAS JSON format). If None, creates empty life cycle model.
        validation_config: Validation configuration. If None, uses global default.

    Returns:
        TidasLifeCycleModel instance

    Example:
        >>> model = create_life_cycle_model()
        >>> model.life_cycle_model_data_set.life_cycle_model_information.data_set_information.name.set_text(
        ...     "Cradle to Gate", "en"
        ... )
    """
    if data is None:
        data = {}

    # Auto-generate UUID if not provided
    uuid_path = [
        "lifeCycleModelDataSet",
        "lifeCycleModelInformation",
        "dataSetInformation",
        "common:UUID",
    ]
    data = _generate_uuid_if_needed(data, uuid_path)

    return TidasLifeCycleModel(data=data, validation_config=validation_config)


def create_life_cycle_models_batch(
    data_list: List[Dict[str, Any]],
    validation_config: Optional[ValidationConfig] = None,
) -> List[TidasLifeCycleModel]:
    """Create multiple LifeCycleModel entities in batch.

    UUIDs will be automatically generated for any life cycle models without UUIDs.

    Args:
        data_list: List of life cycle model data dictionaries
        validation_config: Optional validation configuration for all life cycle models

    Returns:
        List of TidasLifeCycleModel instances
    """
    return _create_batch(create_life_cycle_model, data_list, validation_config)


# Export list
__all__ = [
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
