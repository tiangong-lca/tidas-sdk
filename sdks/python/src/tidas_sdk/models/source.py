"""
Source entity wrapper class for TIDAS SDK.
"""

from typing import Any, Dict, Optional

from ..core.base import TidasEntity
from ..core.validation import ValidationConfig
from ..types.tidas_sources import Model as SourceModel


class TidasSource(TidasEntity):
    """Wrapper class for Source entities with pythonic API.

    Represents a literature source or publication.

    Example:
        >>> source = TidasSource()
        >>> source.source_data_set.source_information.data_set_information.short_name.set_text(
        ...     "IPCC 2021", "en"
        ... )
        >>> source.validate()
    """

    def __init__(
        self,
        data: Optional[Dict[str, Any]] = None,
        validation_config: Optional[ValidationConfig] = None,
    ):
        """Initialize Source entity.

        Args:
            data: Source data as dictionary (TIDAS JSON format)
            validation_config: Validation configuration. If None, uses global default.
        """
        super().__init__(data, validation_config)
        self._pydantic_model = SourceModel

        # Initialize default structure if data is empty
        if not self._data:
            self._data = {
                "sourceDataSet": {
                    "sourceInformation": {
                        "dataSetInformation": {}
                    },
                    "administrativeInformation": {}
                }
            }
