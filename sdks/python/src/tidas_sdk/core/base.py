"""
Base entity class for all TIDAS entities.
"""

import copy
import json
from abc import ABC
from typing import Any, Dict, List, Optional, Type, TypeVar, cast

from loguru import logger
from pydantic import BaseModel, ValidationError as PydanticValidationError

from .exceptions import ValidationError
from .validation import ValidationConfig, ValidationWarning, get_default_validation_config

T = TypeVar('T')


class TidasEntity(ABC):
    """Abstract base class providing common functionality for all TIDAS entities.

    All TIDAS entity types (Contact, Flow, Process, etc.) inherit from this class.
    Provides validation, JSON export, cloning, and field access methods.
    """

    def __init__(
        self,
        data: Optional[Dict[str, Any]] = None,
        validation_config: Optional[ValidationConfig] = None,
    ):
        """Initialize entity with optional data and validation config.

        Args:
            data: Entity data as dictionary (TIDAS JSON format)
            validation_config: Validation configuration. If None, uses global default.
        """
        self._data: Dict[str, Any] = data if data is not None else {}
        self._validation_config = (
            validation_config
            if validation_config is not None
            else get_default_validation_config()
        )
        self._validation_warnings: List[ValidationWarning] = []
        self._wrappers_cache: Dict[str, Any] = {}

        # Subclasses must set this to their Pydantic model class
        self._pydantic_model: Optional[Type[BaseModel]] = None

    def validate(self) -> None:
        """Validate entity data according to current mode.

        Behavior depends on validation mode:
        - strict: Raises ValidationError on any violation
        - weak: Collects violations as warnings (accessible via get_validation_warnings)
        - ignore: Skips validation (no-op)

        Raises:
            ValidationError: If validation fails in strict mode
        """
        if self._validation_config.mode == "ignore":
            return

        if self._pydantic_model is None:
            logger.warning("No Pydantic model set for validation")
            return

        try:
            # Use Pydantic validation
            self._pydantic_model.model_validate(self._data)
            logger.debug(f"Validation passed for {self.__class__.__name__}")

        except PydanticValidationError as e:
            if self._validation_config.mode == "strict":
                # Convert to our exception type and raise
                raise ValidationError.from_pydantic(e)

            # weak mode - collect as warnings
            self._validation_warnings.clear()
            for error in e.errors():
                warning = ValidationWarning(
                    field_path=".".join(str(p) for p in error["loc"]),
                    message=error["msg"],
                    expected=error["type"],
                    actual=error.get("input"),
                )
                self._validation_warnings.append(warning)
                if self._validation_config.include_warnings:
                    logger.warning(
                        f"Validation warning: {warning.field_path} - {warning.message}"
                    )

    def get_validation_warnings(self) -> List[ValidationWarning]:
        """Return list of validation warnings from weak mode.

        Returns:
            Copy of validation warnings list
        """
        return self._validation_warnings.copy()

    def set_validation_mode(self, mode: str) -> None:
        """Change validation mode for this entity.

        Args:
            mode: New validation mode ("strict", "weak", or "ignore")
        """
        self._validation_config.mode = mode  # type: ignore

    def get_validation_config(self) -> ValidationConfig:
        """Return current validation configuration.

        Returns:
            Current validation configuration
        """
        return self._validation_config

    def to_json(self) -> Dict[str, Any]:
        """Export entity as dictionary matching TIDAS JSON structure.

        Returns:
            Entity data as dictionary
        """
        return copy.deepcopy(self._data)

    def to_json_string(self, indent: Optional[int] = None) -> str:
        """Export entity as formatted JSON string.

        Args:
            indent: Number of spaces for indentation. None for compact output.

        Returns:
            Entity data as JSON string
        """
        return json.dumps(self._data, indent=indent, ensure_ascii=False)

    def clone(self) -> "TidasEntity":
        """Create a deep copy of this entity.

        Returns:
            New entity instance with copied data
        """
        cloned_data = copy.deepcopy(self._data)
        cloned_config = ValidationConfig(
            mode=self._validation_config.mode,
            include_warnings=self._validation_config.include_warnings,
        )
        return self.__class__(data=cloned_data, validation_config=cloned_config)

    def get_value(self, path: str) -> Any:
        """Get nested value using dot notation.

        Example:
            entity.get_value("contactDataSet.contactInformation.dataSetInformation.name")

        Args:
            path: Dot-separated path to field

        Returns:
            Value at the specified path, or None if not found
        """
        keys = path.split(".")
        value: Any = self._data

        for key in keys:
            if isinstance(value, dict):
                value = value.get(key)
                if value is None:
                    return None
            else:
                return None

        return value

    def _get_typed_field(
        self,
        field_name: str,
        wrapper_type: Type[T],
        *,
        cache: bool = True
    ) -> T:
        """Get a typed wrapper for a field.

        This method enables IDE autocomplete and type checking by returning
        typed wrapper objects instead of raw dictionaries.

        Args:
            field_name: Name of the field in the entity data
            wrapper_type: Wrapper class to instantiate
            cache: Whether to cache the wrapper instance (default: True)

        Returns:
            Typed wrapper instance for the field
        """
        cache_key = f"{field_name}_{wrapper_type.__name__}"

        if cache and cache_key in self._wrappers_cache:
            return cast(T, self._wrappers_cache[cache_key])

        # Ensure field exists in data
        self._ensure_field_exists(field_name)

        # Create wrapper instance - wrapper_type is a callable that returns T
        wrapper = cast(T, wrapper_type(self, self._data[field_name]))  # type: ignore[call-arg,redundant-cast]

        if cache:
            self._wrappers_cache[cache_key] = wrapper

        return wrapper

    def _ensure_field_exists(self, field_name: str) -> None:
        """Ensure a field exists in the entity data.

        Creates the field with an empty dict if it doesn't exist.

        Args:
            field_name: Name of the field to ensure exists
        """
        if field_name not in self._data:
            self._data[field_name] = {}
