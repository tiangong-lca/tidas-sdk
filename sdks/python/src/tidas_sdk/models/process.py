"""
Process entity wrapper class for TIDAS SDK.
"""

from typing import Any, Dict, Optional

from ..core.base import TidasEntity
from ..core.wrappers.processes_wrappers import ProcessesDataSetWrapper
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

    @property
    def process_data_set(self) -> ProcessesDataSetWrapper:
        """Access processDataSet field with IDE autocomplete and type hints.

        This property provides typed access to the process dataset, enabling
        IDE autocomplete for all nested fields.

        Example:
            >>> process = TidasProcess()
            >>> # IDE shows autocomplete as you type:
            >>> process.process_data_set.process_information.data_set_information.uuid = "..."
            >>> process.process_data_set.process_information.data_set_information.name.base_name.set_text(
            ...     "Electricity production, photovoltaic", "en"
            ... )

        Returns:
            Auto-generated typed wrapper for the processDataSet field
        """
        return self._get_typed_field("processDataSet", ProcessesDataSetWrapper)
