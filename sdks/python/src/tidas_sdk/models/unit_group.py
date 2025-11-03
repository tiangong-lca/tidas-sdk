"""
UnitGroup entity wrapper class for TIDAS SDK.
"""

from typing import Any, Dict, Optional

from ..core.base import TidasEntity
from ..core.wrappers.unitgroups_wrappers import UnitgroupsDataSetWrapper
from ..core.validation import ValidationConfig
from ..types.tidas_unitgroups import Model as UnitGroupModel


class TidasUnitGroup(TidasEntity):
    """Wrapper class for UnitGroup entities with pythonic API.

    Represents a group of measurement units.

    Example:
        >>> unit_group = TidasUnitGroup()
        >>> unit_group.unit_group_data_set.unit_group_information.data_set_information.name.set_text(
        ...     "Mass units", "en"
        ... )
        >>> unit_group.validate()
    """

    def __init__(
        self,
        data: Optional[Dict[str, Any]] = None,
        validation_config: Optional[ValidationConfig] = None,
    ):
        """Initialize UnitGroup entity.

        Args:
            data: UnitGroup data as dictionary (TIDAS JSON format)
            validation_config: Validation configuration. If None, uses global default.
        """
        super().__init__(data, validation_config)
        self._pydantic_model = UnitGroupModel

        # Initialize default structure if data is empty
        if not self._data:
            self._data = {
                "unitGroupDataSet": {
                    "unitGroupInformation": {
                        "dataSetInformation": {}
                    },
                    "modellingAndValidation": {},
                    "administrativeInformation": {},
                    "units": {}
                }
            }

    @property
    def unit_group_data_set(self) -> UnitgroupsDataSetWrapper:
        """Access unitGroupDataSet field with IDE autocomplete and type hints.

        This property provides typed access to the unit group dataset, enabling
        IDE autocomplete for all nested fields.

        Example:
            >>> unit_group = TidasUnitGroup()
            >>> # IDE shows autocomplete as you type:
            >>> unit_group.unit_group_data_set.unit_group_information.data_set_information.uuid = "..."
            >>> unit_group.unit_group_data_set.unit_group_information.data_set_information.name.set_text(
            ...     "Mass units", "en"
            ... )

        Returns:
            Auto-generated typed wrapper for the unitGroupDataSet field
        """
        return self._get_typed_field("unitGroupDataSet", UnitgroupsDataSetWrapper)
