"""
TidasLciamethods entity wrapper class for TIDAS SDK.
"""

import datetime
import uuid
from typing import Any, Dict, Optional

from ..core.base import TidasEntity
from ..core.wrappers.lciamethods_wrappers import LciamethodsDataSetWrapper
from ..core.validation import ValidationConfig
from ..types.tidas_lciamethods import Model as LciamethodsModel


class TidasLciamethods(TidasEntity):
    """Wrapper class for Lciamethods entities with pythonic API.

    Represents a lciamethods in LCA.

    Example:
        >>> lciamethods = TidasLciamethods()
        >>> lciamethods.lciamethods_data_set.lciamethods_information.data_set_information.name.set_text(
        ...     "Example Lciamethods", "en"
        ... )
        >>> lciamethods.validate()
    """

    def __init__(
        self,
        data: Optional[Dict[str, Any]] = None,
        validation_config: Optional[ValidationConfig] = None,
    ):
        """Initialize Lciamethods entity.

        Args:
            data: Lciamethods data as dictionary (TIDAS JSON format)
            validation_config: Validation configuration. If None, uses global default.
        """
        super().__init__(data, validation_config)
        self._pydantic_model = LciamethodsModel

        # Initialize default structure if data is empty
        if not self._data:
            self._data = {
                "LCIAMethodDataSet": {
                    "lciamethodsInformation": {
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
        self.set_nested_value("LCIAMethodDataSet.@xmlns", "http://lca.jrc.it/ILCD/LCIAMethod")
        self.set_nested_value("LCIAMethodDataSet.@xmlns:common", "http://lca.jrc.it/ILCD/Common")
        self.set_nested_value("LCIAMethodDataSet.@xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        self.set_nested_value("LCIAMethodDataSet.@version", "1.1")
        self.set_nested_value("LCIAMethodDataSet.@xsi:schemaLocation", "http://lca.jrc.it/ILCD/LCIAMethod ../../schemas/ILCD_LCIAMethodDataSet.xsd")

        # Ensure required nested structure exists
        self.ensure_nested_structure([
            "LCIAMethodDataSet",
            "LCIAMethodDataSet.LCIAMethodInformation",
            "LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation",
            "LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.classificationInformation",
            "LCIAMethodDataSet.modellingAndValidation",
            "LCIAMethodDataSet.administrativeInformation",
            "LCIAMethodDataSet.administrativeInformation.dataEntryBy",
            "LCIAMethodDataSet.administrativeInformation.publicationAndOwnership",
            "LCIAMethodDataSet.characterisationFactors",
        ])

    @property
    def lciamethods_data_set(self) -> LciamethodsDataSetWrapper:
        """Access LCIAMethodDataSet field with IDE autocomplete and type hints.

        This property provides typed access to the dataset, enabling
        IDE autocomplete for all nested fields.

        Example:
            >>> lciamethods = TidasLciamethods()
            >>> # IDE shows autocomplete as you type:
            >>> lciamethods.lciamethods_data_set.lciamethods_information.data_set_information.uuid = "..."
        """
        return self._get_typed_field("LCIAMethodDataSet", LciamethodsDataSetWrapper)
