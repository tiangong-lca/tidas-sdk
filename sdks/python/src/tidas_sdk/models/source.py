"""
Source entity wrapper class for TIDAS SDK.
"""

from typing import Any, Dict, Optional

from ..core.base import TidasEntity
from ..core.wrappers.sources_wrappers import SourcesDataSetWrapper
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

    @property
    def source_data_set(self) -> SourcesDataSetWrapper:
        """Access sourceDataSet field with IDE autocomplete and type hints.

        This property provides typed access to the source dataset, enabling
        IDE autocomplete for all nested fields.

        Example:
            >>> source = TidasSource()
            >>> # IDE shows autocomplete as you type:
            >>> source.source_data_set.source_information.data_set_information.uuid = "..."
            >>> source.source_data_set.source_information.data_set_information.short_name.set_text(
            ...     "IPCC 2021", "en"
            ... )

        Returns:
            Auto-generated typed wrapper for the sourceDataSet field
        """
        return self._get_typed_field("sourceDataSet", SourcesDataSetWrapper)
