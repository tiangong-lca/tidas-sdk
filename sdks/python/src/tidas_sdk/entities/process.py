"""
High level wrapper around the Process dataset.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from ..core.base import TidasEntity
from ..core.multilang import MultiLangList
from ..generated.tidas_processes import (
    AdministrativeInformation,
    DataEntryBy,
    DataSetInformation,
    Process,
    ProcessDataSet,
    ProcessInformation,
    PublicationAndOwnership,
)


class TidasProcess(TidasEntity[Process]):
    schema_name = "tidas_processes.json"

    def __init__(self, initial_data: dict[str, Any] | None = None, *, validate_on_init: bool = False) -> None:
        super().__init__(Process, initial_data, validate_on_init=validate_on_init)

    # ----------------------------------------------------------------------------------
    # Default bootstrapping
    # ----------------------------------------------------------------------------------

    def ensure_defaults(self) -> None:
        data_set = self.process_data_set
        if data_set is None:
            data_set = ProcessDataSet()
            self.process_data_set = data_set

        data_set.xmlns = data_set.xmlns or "http://lca.jrc.it/ILCD/Process"
        data_set.xmlns_common = data_set.xmlns_common or "http://lca.jrc.it/ILCD/Common"
        data_set.xmlns_xsi = data_set.xmlns_xsi or "http://www.w3.org/2001/XMLSchema-instance"
        data_set.version = data_set.version or "1.1"
        data_set.xsi_schema_location = (
            data_set.xsi_schema_location
            or "http://lca.jrc.it/ILCD/Process ../../schemas/ILCD_ProcessDataSet.xsd"
        )

        process_info = data_set.process_information or ProcessInformation()
        data_set.process_information = process_info

        data_info = process_info.data_set_information or DataSetInformation()
        process_info.data_set_information = data_info

        admin_info = data_set.administrative_information or AdministrativeInformation()
        data_set.administrative_information = admin_info

        data_entry = admin_info.data_entry_by or DataEntryBy()
        admin_info.data_entry_by = data_entry

        publication = admin_info.publication_and_ownership or PublicationAndOwnership()
        admin_info.publication_and_ownership = publication

        if not data_info.common_uuid:
            data_info.common_uuid = str(uuid4())

        if not data_entry.common_time_stamp:
            data_entry.common_time_stamp = datetime.now(tz=timezone.utc).isoformat()

        for field_name in (
            "common_name",
            "common_short_name",
            "common_synonyms",
            "common_general_comment",
        ):
            self._ensure_multilang(getattr(data_info, field_name), data_info, field_name)

    @staticmethod
    def _ensure_multilang(value: Any, container: DataSetInformation, field_name: str) -> None:
        if isinstance(value, MultiLangList):
            return
        if isinstance(value, list):
            setattr(container, field_name, MultiLangList(value))
            return
        if value is None:
            setattr(container, field_name, MultiLangList())
            return
        setattr(container, field_name, MultiLangList([value]))
