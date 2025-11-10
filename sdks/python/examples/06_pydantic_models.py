#!/usr/bin/env python3
"""
Example demonstrating the use of Pydantic models for TIDAS entities.

This example shows how to use the new create_process_model function
to create Process entities as Pydantic models with built-in validation.
"""

import json
from pathlib import Path

from tidas_sdk.factories import (
    create_process,
    create_process_model,
    create_processes_batch,
    create_process_model_batch,
)
from tidas_sdk.models import TidasProcesses
from tidas_sdk.types.tidas_processes import Model as ProcessesModel


def main():
    """Demonstrate both wrapper and Pydantic model approaches."""

    print("=== TIDAS Python SDK: Pydantic Models Example ===\n")

    # Example 1: Create a process using the wrapper class (original approach)
    print("1. Creating a process using TidasProcesses wrapper class:")
    process_model = create_process()
    process_model.initialize_defaults()
    process_model = process_model.to_pydantic()
    process_model.processDataSet.processInformation.dataSetInformation.name.baseName.set_text(
        "Electricity production, photovoltaic", "en"
    )
    process_model.processDataSet.administrativeInformation.dataEntryBy.common_timeStamp = (
        "2024-01-01T00:00:00Z"
    )
    print(process_model.model_dump_json())


if __name__ == "__main__":
    main()
