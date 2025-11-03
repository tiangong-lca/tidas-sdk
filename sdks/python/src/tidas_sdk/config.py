"""
Global configuration module for TIDAS SDK.
"""

from .core.validation import (
    ValidationConfig,
    get_global_validation_mode,
    set_global_validation_mode,
)

__all__ = [
    "ValidationConfig",
    "get_global_validation_mode",
    "set_global_validation_mode",
]
