"""
Process entity wrapper class for TIDAS SDK.
"""

from typing import Any, Dict, Optional

from ..core.base import TidasEntity
from ..core.validation import ValidationConfig
from ..types.tidas_processes import Model as ProcessModel


class TidasProcess(TidasEntity):
    """Wrapper class for Process entities with pythonic API.

    Represents a process (unit process or system) in LCA.

    Example:
        >>> process = TidasProcess()
        >>> process.process_data_set.process_information.data_set_information.name.base_name.set_text(
        ...     "Electricity production, photovoltaic", "en"
        ... )
        >>> process.validate()
    """

    def __init__(
        self,
        data: Optional[Dict[str, Any]] = None,
        validation_config: Optional[ValidationConfig] = None,
    ):
        """Initialize Process entity.

        Args:
            data: Process data as dictionary (TIDAS JSON format)
            validation_config: Validation configuration. If None, uses global default.
        """
        super().__init__(data, validation_config)
        self._pydantic_model = ProcessModel

        # Initialize default structure if data is empty
        if not self._data:
            self._data = {
                "processDataSet": {
                    "processInformation": {
                        "dataSetInformation": {}
                    },
                    "modellingAndValidation": {},
                    "administrativeInformation": {},
                    "exchanges": {}
                }
            }
