"""
Exception classes for TIDAS SDK.
"""

from typing import Any, Optional


class TidasException(Exception):
    """Base exception for all TIDAS SDK errors."""

    pass


class ValidationError(TidasException):
    """Raised when entity data violates schema constraints (strict mode)."""

    def __init__(
        self,
        field_path: str,
        expected: str,
        actual: Any,
        constraint_type: str = "validation",
    ):
        self.field_path = field_path
        self.expected = expected
        self.actual = actual
        self.constraint_type = constraint_type

        message = f"Field '{field_path}' {expected}, got {actual!r}"
        super().__init__(message)

    @classmethod
    def from_pydantic(cls, pydantic_error: Any) -> "ValidationError":
        """Convert Pydantic validation error to TIDAS ValidationError.

        Args:
            pydantic_error: Pydantic ValidationError instance

        Returns:
            ValidationError instance with first error from pydantic error
        """
        # Take first error for simplicity
        error = pydantic_error.errors()[0]
        return cls(
            field_path=".".join(str(p) for p in error["loc"]),
            expected=error["msg"],
            actual=error.get("input"),
            constraint_type=error["type"],
        )


class SchemaGenerationError(TidasException):
    """Raised when code generation from schemas fails."""

    def __init__(self, schema_file: str, reason: str):
        self.schema_file = schema_file
        self.reason = reason
        super().__init__(f"Failed to generate code from {schema_file}: {reason}")


class ConfigurationError(TidasException):
    """Raised when SDK configuration is invalid."""

    pass
