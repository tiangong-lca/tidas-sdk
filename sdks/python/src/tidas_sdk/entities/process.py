"""
High level wrapper around the Process dataset.
"""
from __future__ import annotations

from typing import Any
from uuid import uuid4

from ..core.base import TidasEntity
from ..generated.tidas_processes import (
    ProcessDataSetAdministrativeInformationDataEntryBy,
    ProcessDataSetAdministrativeInformationPublicationAndOwnership,
    ProcessDataSetProcessInformationDataSetInformation,
    Processes,
    ProcessesProcessDataSet,
    ProcessesProcessDataSetAdministrativeInformation,
    ProcessesProcessDataSetProcessInformation,
)
from .utils import default_timestamp, ensure_model, ensure_multilang


class TidasProcess(TidasEntity[Processes]):
    schema_name = "tidas_processes.json"

    def __init__(
        self,
        initial_data: dict[str, Any] | Processes | None = None,
        *,
        validate_on_init: bool = False,
    ) -> None:
        super().__init__(Processes, initial_data, validate_on_init=validate_on_init)

    def ensure_defaults(self) -> None:
        dataset = ensure_model(self, "process_data_set", ProcessesProcessDataSet)
        dataset.xmlns = dataset.xmlns or "http://lca.jrc.it/ILCD/Process"
        dataset.xmlns_common = dataset.xmlns_common or "http://lca.jrc.it/ILCD/Common"
        dataset.xmlns_xsi = dataset.xmlns_xsi or "http://www.w3.org/2001/XMLSchema-instance"
        dataset.version = dataset.version or "1.1"
        dataset.locations = dataset.locations or "../ILCDLocations.xml"
        dataset.xsi_schema_location = (
            dataset.xsi_schema_location
            or "http://lca.jrc.it/ILCD/Process ../../schemas/ILCD_ProcessDataSet.xsd"
        )

        process_info = ensure_model(
            dataset,
            "process_information",
            ProcessesProcessDataSetProcessInformation,
        )
        data_info = ensure_model(
            process_info,
            "data_set_information",
            ProcessDataSetProcessInformationDataSetInformation,
        )
        if not data_info.common_uuid:
            data_info.common_uuid = str(uuid4())
        for field_name in (
            "common_name",
            "common_short_name",
            "common_synonyms",
            "common_general_comment",
        ):
            ensure_multilang(data_info, field_name)

        admin = ensure_model(
            dataset,
            "administrative_information",
            ProcessesProcessDataSetAdministrativeInformation,
        )
        data_entry = ensure_model(
            admin,
            "data_entry_by",
            ProcessDataSetAdministrativeInformationDataEntryBy,
        )
        if not data_entry.common_time_stamp:
            data_entry.common_time_stamp = default_timestamp()
        ensure_model(
            admin,
            "publication_and_ownership",
            ProcessDataSetAdministrativeInformationPublicationAndOwnership,
        )
