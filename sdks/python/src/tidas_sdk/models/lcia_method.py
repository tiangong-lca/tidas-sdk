"""
LCIAMethod entity wrapper class for TIDAS SDK.
"""

from typing import Any, Dict, Optional

from ..core.base import TidasEntity
from ..core.wrappers.lciamethods_wrappers import LciamethodsDataSetWrapper
from ..core.validation import ValidationConfig
from ..types.tidas_lciamethods import Model as LCIAMethodModel


class TidasLCIAMethod(TidasEntity):
    """Wrapper class for LCIAMethod entities with pythonic API.

    Represents an LCIA (Life Cycle Impact Assessment) method.

    Example:
        >>> lcia_method = TidasLCIAMethod()
        >>> lcia_method.lcia_method_data_set.lcia_method_information.data_set_information.name.set_text(
        ...     "ReCiPe 2016", "en"
        ... )
        >>> lcia_method.validate()
    """

    def __init__(
        self,
        data: Optional[Dict[str, Any]] = None,
        validation_config: Optional[ValidationConfig] = None,
    ):
        """Initialize LCIAMethod entity.

        Args:
            data: LCIAMethod data as dictionary (TIDAS JSON format)
            validation_config: Validation configuration. If None, uses global default.
        """
        super().__init__(data, validation_config)
        self._pydantic_model = LCIAMethodModel

        # Initialize default structure if data is empty
        if not self._data:
            self._data = {
                "LCIAMethodDataSet": {
                    "LCIAMethodInformation": {
                        "dataSetInformation": {}
                    },
                    "modellingAndValidation": {},
                    "administrativeInformation": {},
                    "characterisationFactors": {}
                }
            }

    @property
    def lcia_method_data_set(self) -> LciamethodsDataSetWrapper:
        """Access LCIAMethodDataSet field with IDE autocomplete and type hints.

        This property provides typed access to the LCIA method dataset, enabling
        IDE autocomplete for all nested fields.

        Example:
            >>> lcia_method = TidasLCIAMethod()
            >>> # IDE shows autocomplete as you type:
            >>> lcia_method.lcia_method_data_set.lcia_method_information.data_set_information.uuid = "..."
            >>> lcia_method.lcia_method_data_set.lcia_method_information.data_set_information.name.set_text(
            ...     "ReCiPe 2016", "en"
            ... )

        Returns:
            Auto-generated typed wrapper for the LCIAMethodDataSet field
        """
        return self._get_typed_field("LCIAMethodDataSet", LciamethodsDataSetWrapper)
