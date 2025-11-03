"""
Logging configuration for TIDAS SDK.
"""

import sys
from loguru import logger

# Configure loguru logger with default settings
logger.remove()  # Remove default handler

# Add stderr handler with structured format and WARNING level by default
logger.add(
    sys.stderr,
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
        "<level>{message}</level>"
    ),
    level="WARNING",
    colorize=True,
)


def configure_logger(level: str = "WARNING") -> None:
    """Configure the SDK logger with a specific level.

    Args:
        level: Log level - "DEBUG", "INFO", "WARNING", "ERROR", or "CRITICAL"
    """
    logger.remove()
    logger.add(
        sys.stderr,
        format=(
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
            "<level>{message}</level>"
        ),
        level=level,
        colorize=True,
    )


# Structured logging helpers for entity operations
def log_entity_created(entity_type: str, has_data: bool) -> None:
    """Log entity creation."""
    logger.debug(f"Created {entity_type} entity (with_data={has_data})")


def log_entity_validated(entity_type: str, mode: str, has_errors: bool) -> None:
    """Log entity validation."""
    if has_errors:
        logger.warning(
            f"Validation completed for {entity_type} in {mode} mode (errors found)"
        )
    else:
        logger.debug(
            f"Validation passed for {entity_type} in {mode} mode"
        )


def log_batch_operation(operation: str, entity_type: str, count: int) -> None:
    """Log batch operations."""
    logger.info(f"{operation} {count} {entity_type} entities")
