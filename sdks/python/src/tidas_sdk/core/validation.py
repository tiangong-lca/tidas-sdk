"""
Validation configuration and data structures for TIDAS SDK.
"""

from dataclasses import dataclass
from typing import Any, Literal

ValidationMode = Literal["strict", "weak", "ignore"]

# Global validation mode
_GLOBAL_VALIDATION_MODE: ValidationMode = "strict"


@dataclass
class ValidationConfig:
    """Configuration for entity validation behavior.

    Attributes:
        mode: Validation mode - "strict" (raise errors), "weak" (collect warnings),
              or "ignore" (skip validation)
        include_warnings: Whether to collect warnings in weak mode
    """

    mode: ValidationMode = "strict"
    include_warnings: bool = True


@dataclass
class ValidationWarning:
    """Represents a validation issue in weak mode (non-exception).

    Attributes:
        field_path: Dot-notation path to field
        message: Human-readable error message
        expected: Expected type or constraint
        actual: Actual value that failed validation
        severity: Warning severity level
    """

    field_path: str
    message: str
    expected: str
    actual: Any
    severity: Literal["warning", "error"] = "warning"

    def __str__(self) -> str:
        """String representation showing severity, path and message."""
        return f"[{self.severity.upper()}] {self.field_path}: {self.message}"


def set_global_validation_mode(mode: ValidationMode) -> None:
    """Set the global validation mode for all new entities.

    Args:
        mode: Validation mode to set globally
    """
    global _GLOBAL_VALIDATION_MODE
    _GLOBAL_VALIDATION_MODE = mode


def get_global_validation_mode() -> ValidationMode:
    """Get the current global validation mode.

    Returns:
        Current global validation mode
    """
    return _GLOBAL_VALIDATION_MODE


def get_default_validation_config() -> ValidationConfig:
    """Get a validation config using the global mode.

    Returns:
        ValidationConfig with current global mode
    """
    return ValidationConfig(mode=_GLOBAL_VALIDATION_MODE)
