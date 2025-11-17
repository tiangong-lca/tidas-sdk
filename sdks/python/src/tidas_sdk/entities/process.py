"""
High level wrapper around the Process dataset.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from ..core.base import TidasEntity
from ..core.multilang import MultiLangList
from ..generated.tidas_processes import Process


class TidasProcess(TidasEntity[Process]):
    schema_name = "tidas_processes.json"

    def __init__(self, initial_data: dict[str, Any] | None = None, *, validate_on_init: bool = False) -> None:
        super().__init__(Process, initial_data, validate_on_init=validate_on_init)

    # ----------------------------------------------------------------------------------
    # Default bootstrapping
    # ----------------------------------------------------------------------------------

    def ensure_defaults(self) -> None:
        if self.process_data_set is None:
            self.process_data_set = {}
        data_set = self.process_data_set

        # Namespaces
        for key, value in (
            ("@xmlns", "http://lca.jrc.it/ILCD/Process"),
            ("@xmlns:common", "http://lca.jrc.it/ILCD/Common"),
            ("@xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance"),
            ("@version", "1.1"),
            (
                "@xsi:schemaLocation",
                "http://lca.jrc.it/ILCD/Process ../../schemas/ILCD_ProcessDataSet.xsd",
            ),
        ):
            data_set.setdefault(key, value)

        process_info = data_set.setdefault("processInformation", {})
        data_info = process_info.setdefault("dataSetInformation", {})
        admin_info = data_set.setdefault("administrativeInformation", {})
        data_entry = admin_info.setdefault("dataEntryBy", {})

        data_info.setdefault("common:UUID", str(uuid4()))
        timestamp_field = "common:timeStamp"
        data_entry.setdefault(timestamp_field, datetime.now(tz=timezone.utc).isoformat())

        # Multi-lang defaults
        self._ensure_multilang(data_info, "common:name")
        self._ensure_multilang(data_info, "common:shortName")
        self._ensure_multilang(data_info, "common:synonyms")
        self._ensure_multilang(data_info, "common:generalComment")

    # ----------------------------------------------------------------------------------
    # Helpers
    # ----------------------------------------------------------------------------------

    @staticmethod
    def _ensure_multilang(node: dict[str, Any], key: str) -> None:
        current = node.get(key)
        if isinstance(current, MultiLangList):
            return
        node[key] = MultiLangList(current or [])
