"""
TidasFlowproperties entity wrapper class for TIDAS SDK.
"""

import datetime
import uuid
from typing import Any, Dict, Optional

from ..core.base import TidasEntity
from ..core.wrappers.flowproperties_wrappers import FlowpropertiesDataSetWrapper
from ..core.validation import ValidationConfig
from ..types.tidas_flowproperties import Model as FlowpropertiesModel


class TidasFlowproperties(TidasEntity):
    """Wrapper class for Flowproperties entities with pythonic API.

    Represents a flowproperties in LCA.

    Example:
        >>> flowproperties = TidasFlowproperties()
        >>> flowproperties.flowproperties_data_set.flowproperties_information.data_set_information.name.set_text(
        ...     "Example Flowproperties", "en"
        ... )
        >>> flowproperties.validate()
    """

    def __init__(
        self,
        data: Optional[Dict[str, Any]] = None,
        validation_config: Optional[ValidationConfig] = None,
    ):
        """Initialize Flowproperties entity.

        Args:
            data: Flowproperties data as dictionary (TIDAS JSON format)
            validation_config: Validation configuration. If None, uses global default.
        """
        super().__init__(data, validation_config)
        self._pydantic_model = FlowpropertiesModel

        # Initialize default structure if data is empty
        if not self._data:
            self._data = {
                "flowPropertyDataSet": {
                    "flowpropertiesInformation": {
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
    def flowproperties_data_set(self) -> FlowpropertiesDataSetWrapper:
        """Access flowPropertyDataSet field with IDE autocomplete and type hints.

        This property provides typed access to the dataset, enabling
        IDE autocomplete for all nested fields.

        Example:
            >>> flowproperties = TidasFlowproperties()
            >>> # IDE shows autocomplete as you type:
            >>> flowproperties.flowproperties_data_set.flowproperties_information.data_set_information.uuid = "..."
        """
        return self._get_typed_field("flowPropertyDataSet", FlowpropertiesDataSetWrapper)
