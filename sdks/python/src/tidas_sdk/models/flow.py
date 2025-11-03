"""
Flow entity wrapper class for TIDAS SDK.
"""

from typing import Any, Dict, Optional

from ..core.base import TidasEntity
from ..core.wrappers.flows_wrappers import FlowsDataSetWrapper
from ..core.validation import ValidationConfig
from ..types.tidas_flows import Model as FlowModel


class TidasFlow(TidasEntity):
    """Wrapper class for Flow entities with pythonic API.

    Represents a material or energy flow in LCA.

    Example:
        >>> flow = TidasFlow()
        >>> flow.flow_data_set.flow_information.data_set_information.name.base_name.set_text(
        ...     "Carbon dioxide", "en"
        ... )
        >>> flow.validate()
    """

    def __init__(
        self,
        data: Optional[Dict[str, Any]] = None,
        validation_config: Optional[ValidationConfig] = None,
    ):
        """Initialize Flow entity.

        Args:
            data: Flow data as dictionary (TIDAS JSON format)
            validation_config: Validation configuration. If None, uses global default.
        """
        super().__init__(data, validation_config)
        self._pydantic_model = FlowModel

        # Initialize default structure if data is empty
        if not self._data:
            self._data = {
                "flowDataSet": {
                    "flowInformation": {
                        "dataSetInformation": {}
                    },
                    "modellingAndValidation": {},
                    "administrativeInformation": {}
                }
            }

    @property
    def flow_data_set(self) -> FlowsDataSetWrapper:
        """Access flowDataSet field with IDE autocomplete and type hints.

        This property provides typed access to the flow dataset, enabling
        IDE autocomplete for all nested fields.

        Example:
            >>> flow = TidasFlow()
            >>> # IDE shows autocomplete as you type:
            >>> flow.flow_data_set.flow_information.data_set_information.uuid = "..."
            >>> flow.flow_data_set.flow_information.data_set_information.name.base_name.set_text(
            ...     "Carbon dioxide", "en"
            ... )

        Returns:
            Auto-generated typed wrapper for the flowDataSet field
        """
        return self._get_typed_field("flowDataSet", FlowsDataSetWrapper)
