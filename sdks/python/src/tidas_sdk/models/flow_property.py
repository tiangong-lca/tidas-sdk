"""
FlowProperty entity wrapper class for TIDAS SDK.
"""

from typing import Any, Dict, Optional

from ..core.base import TidasEntity
from ..core.wrappers.flowproperties_wrappers import FlowpropertiesDataSetWrapper
from ..core.validation import ValidationConfig
from ..types.tidas_flowproperties import Model as FlowPropertyModel


class TidasFlowProperty(TidasEntity):
    """Wrapper class for FlowProperty entities with pythonic API.

    Represents a quantifiable property of flows (mass, energy, volume).

    Example:
        >>> flow_property = TidasFlowProperty()
        >>> flow_property.flow_property_data_set.flow_properties_information.data_set_information.name.set_text(
        ...     "Mass", "en"
        ... )
        >>> flow_property.validate()
    """

    def __init__(
        self,
        data: Optional[Dict[str, Any]] = None,
        validation_config: Optional[ValidationConfig] = None,
    ):
        """Initialize FlowProperty entity.

        Args:
            data: FlowProperty data as dictionary (TIDAS JSON format)
            validation_config: Validation configuration. If None, uses global default.
        """
        super().__init__(data, validation_config)
        self._pydantic_model = FlowPropertyModel

        # Initialize default structure if data is empty
        if not self._data:
            self._data = {
                "flowPropertyDataSet": {
                    "flowPropertiesInformation": {
                        "dataSetInformation": {}
                    },
                    "modellingAndValidation": {},
                    "administrativeInformation": {}
                }
            }

    @property
    def flow_property_data_set(self) -> FlowpropertiesDataSetWrapper:
        """Access flowPropertyDataSet field with IDE autocomplete and type hints.

        This property provides typed access to the flow property dataset, enabling
        IDE autocomplete for all nested fields.

        Example:
            >>> flow_property = TidasFlowProperty()
            >>> # IDE shows autocomplete as you type:
            >>> flow_property.flow_property_data_set.flow_properties_information.data_set_information.uuid = "..."
            >>> flow_property.flow_property_data_set.flow_properties_information.data_set_information.name.set_text(
            ...     "Mass", "en"
            ... )

        Returns:
            Auto-generated typed wrapper for the flowPropertyDataSet field
        """
        return self._get_typed_field("flowPropertyDataSet", FlowpropertiesDataSetWrapper)
