"""
TidasProcesses entity wrapper class for TIDAS SDK.
"""

import datetime
import uuid
from typing import Any, Dict, Optional

from ..core.base import TidasEntity
from ..core.wrappers.processes_wrappers import ProcessesDataSetWrapper
from ..core.validation import ValidationConfig
from ..types.tidas_processes import Model as ProcessesModel


class TidasProcesses(TidasEntity):
    """Wrapper class for Processes entities with pythonic API.

    Represents a processes in LCA.

    Example:
        >>> processes = TidasProcesses()
        >>> process.process_data_set.process_information.data_set_information.name.base_name.set_text(
        ...     "Electricity production, photovoltaic", "en"
        ... )
        >>> processes.validate()
    """

    def __init__(
        self,
        data: Optional[Dict[str, Any]] = None,
        validation_config: Optional[ValidationConfig] = None,
    ):
        """Initialize Processes entity.

        Args:
            data: Processes data as dictionary (TIDAS JSON format)
            validation_config: Validation configuration. If None, uses global default.
        """
        super().__init__(data, validation_config)
        self._pydantic_model = ProcessesModel

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

    def initialize_defaults(self) -> None:
        """Initialize default values and ensure required structure.

        This method is called during initialization to set up
        required namespace attributes and default field values.
        """
        # IMPORTANT: Ensure nested structure FIRST, then set xmlns fields
        # (ensure_nested_structure overwrites existing values with empty dicts)
        self.ensure_nested_structure([
            "processDataSet",
            "processDataSet.processInformation",
            "processDataSet.processInformation.dataSetInformation",
            "processDataSet.processInformation.dataSetInformation.classificationInformation",
            "processDataSet.processInformation.quantitativeReference",
            "processDataSet.processInformation.time",
            "processDataSet.processInformation.geography",
            "processDataSet.processInformation.technology",
            "processDataSet.modellingAndValidation",
            "processDataSet.modellingAndValidation.LCIMethodAndAllocation",
            "processDataSet.modellingAndValidation.dataSourcesTreatmentAndRepresentativeness",
            "processDataSet.modellingAndValidation.validation",
            "processDataSet.modellingAndValidation.complianceDeclarations",
            "processDataSet.administrativeInformation",
            "processDataSet.administrativeInformation.dataEntryBy",
            "processDataSet.administrativeInformation.publicationAndOwnership",
            "processDataSet.exchanges",
        ])

        # Set XML namespace attributes
        self.set_nested_value("processDataSet.@xmlns", "http://lca.jrc.it/ILCD/Process")
        self.set_nested_value("processDataSet.@xmlns:common", "http://lca.jrc.it/ILCD/Common")
        self.set_nested_value("processDataSet.@xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        self.set_nested_value("processDataSet.@version", "1.1")
        self.set_nested_value("processDataSet.@xsi:schemaLocation", "http://lca.jrc.it/ILCD/Process ../../schemas/ILCD_ProcessDataSet.xsd")

        # Set required fields with default values if they don't exist
        if not self.get_nested_value("processDataSet.processInformation.dataSetInformation.common:UUID"):
            self.set_nested_value("processDataSet.processInformation.dataSetInformation.common:UUID", str(uuid.uuid4()))
        if not self.get_nested_value("processDataSet.administrativeInformation.dataEntryBy.common:timeStamp"):
            self.set_nested_value("processDataSet.administrativeInformation.dataEntryBy.common:timeStamp", datetime.datetime.now().isoformat())

    @property
    def processes_data_set(self) -> ProcessesDataSetWrapper:
        """Access processDataSet field with IDE autocomplete and type hints.

        This property provides typed access to the dataset, enabling
        IDE autocomplete for all nested fields.

        Example:
            >>> processes = TidasProcesses()
            >>> # IDE shows autocomplete as you type:
            >>> processes.process_data_set.process_information.data_set_information.uuid = "..."
        """
        return self._get_typed_field("processDataSet", ProcessesDataSetWrapper)
