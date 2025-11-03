"""
LifeCycleModel entity wrapper class for TIDAS SDK.
"""

from typing import Any, Dict, Optional

from ..core.base import TidasEntity
from ..core.validation import ValidationConfig
from ..types.tidas_lifecyclemodels import Model as LifeCycleModelModel


class TidasLifeCycleModel(TidasEntity):
    """Wrapper class for LifeCycleModel entities with pythonic API.

    Represents a life cycle model or methodology.

    Example:
        >>> life_cycle_model = TidasLifeCycleModel()
        >>> life_cycle_model.life_cycle_model_data_set.life_cycle_model_information.data_set_information.name.set_text(
        ...     "Cradle-to-Gate", "en"
        ... )
        >>> life_cycle_model.validate()
    """

    def __init__(
        self,
        data: Optional[Dict[str, Any]] = None,
        validation_config: Optional[ValidationConfig] = None,
    ):
        """Initialize LifeCycleModel entity.

        Args:
            data: LifeCycleModel data as dictionary (TIDAS JSON format)
            validation_config: Validation configuration. If None, uses global default.
        """
        super().__init__(data, validation_config)
        self._pydantic_model = LifeCycleModelModel

        # Initialize default structure if data is empty
        if not self._data:
            self._data = {
                "lifeCycleModelDataSet": {
                    "lifeCycleModelInformation": {
                        "dataSetInformation": {}
                    },
                    "modellingAndValidation": {},
                    "administrativeInformation": {}
                }
            }
