"""
TidasUnitgroups entity wrapper class for TIDAS SDK.
"""

import datetime
import uuid
from typing import Any, Dict, Optional

from ..core.base import TidasEntity
from ..core.wrappers.unitgroups_wrappers import UnitgroupsDataSetWrapper
from ..core.validation import ValidationConfig
from ..types.tidas_unitgroups import Model as UnitgroupsModel


class TidasUnitgroups(TidasEntity):
    """Wrapper class for Unitgroups entities with pythonic API.

    Represents a unitgroups in LCA.

    Example:
        >>> unitgroups = TidasUnitgroups()
        >>> unitgroups.unitgroups_data_set.unitgroups_information.data_set_information.name.set_text(
        ...     "Example Unitgroups", "en"
        ... )
        >>> unitgroups.validate()
    """

    def __init__(
        self,
        data: Optional[Dict[str, Any]] = None,
        validation_config: Optional[ValidationConfig] = None,
    ):
        """Initialize Unitgroups entity.

        Args:
            data: Unitgroups data as dictionary (TIDAS JSON format)
            validation_config: Validation configuration. If None, uses global default.
        """
        super().__init__(data, validation_config)
        self._pydantic_model = UnitgroupsModel

        # Initialize default structure if data is empty
        if not self._data:
            self._data = {
                "unitGroupDataSet": {
                    "unitgroupsInformation": {
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
    def unitgroups_data_set(self) -> UnitgroupsDataSetWrapper:
        """Access unitGroupDataSet field with IDE autocomplete and type hints.

        This property provides typed access to the dataset, enabling
        IDE autocomplete for all nested fields.

        Example:
            >>> unitgroups = TidasUnitgroups()
            >>> # IDE shows autocomplete as you type:
            >>> unitgroups.unitgroups_data_set.unitgroups_information.data_set_information.uuid = "..."
        """
        return self._get_typed_field("unitGroupDataSet", UnitgroupsDataSetWrapper)
