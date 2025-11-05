"""
TidasFlows entity wrapper class for TIDAS SDK.
"""

import datetime
import uuid
from typing import Any, Dict, Optional

from ..core.base import TidasEntity
from ..core.wrappers.flows_wrappers import FlowsDataSetWrapper
from ..core.validation import ValidationConfig
from ..types.tidas_flows import Model as FlowsModel


class TidasFlows(TidasEntity):
    """Wrapper class for Flows entities with pythonic API.

    Represents a flows in LCA.

    Example:
        >>> flows = TidasFlows()
        >>> flows.flows_data_set.flows_information.data_set_information.name.set_text(
        ...     "Example Flows", "en"
        ... )
        >>> flows.validate()
    """

    def __init__(
        self,
        data: Optional[Dict[str, Any]] = None,
        validation_config: Optional[ValidationConfig] = None,
    ):
        """Initialize Flows entity.

        Args:
            data: Flows data as dictionary (TIDAS JSON format)
            validation_config: Validation configuration. If None, uses global default.
        """
        super().__init__(data, validation_config)
        self._pydantic_model = FlowsModel

        # Initialize default structure if data is empty
        if not self._data:
            self._data = {
                "flowDataSet": {
                    "flowsInformation": {
                        "dataSetInformation": {}
                    },
                    "modellingAndValidation": {},
                    "administrativeInformation": {}
                }
            }

    def initialize_defaults(self) -> None:
        """Initialize default values and ensure required structure.

        This method is called during initialization to set up
        required namespace attributes and default field values.
        """

    @property
    def flows_data_set(self) -> FlowsDataSetWrapper:
        """Access flowDataSet field with IDE autocomplete and type hints.

        This property provides typed access to the dataset, enabling
        IDE autocomplete for all nested fields.

        Example:
            >>> flows = TidasFlows()
            >>> # IDE shows autocomplete as you type:
            >>> flows.flows_data_set.flows_information.data_set_information.uuid = "..."
        """
        return self._get_typed_field("flowDataSet", FlowsDataSetWrapper)
