"""
Flow entity wrapper class for TIDAS SDK.
"""

from typing import Any, Dict, Optional

from ..core.base import TidasEntity
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
