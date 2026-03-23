"""
Utilities for accessing packaged JSON Schema resources.
"""
from __future__ import annotations

import json
from importlib import resources
from typing import Any, cast

__all__ = ["load_schema", "load_schema_store", "schema_exists"]

SchemaType = dict[str, Any]
_SCHEMA_CACHE: dict[str, SchemaType] = {}
_SCHEMA_STORE_CACHE: dict[str, SchemaType] | None = None


def load_schema(name: str) -> SchemaType:
    """
    Load a JSON schema bundled with the SDK, caching it for repeated use.
    """
    if name in _SCHEMA_CACHE:
        return _SCHEMA_CACHE[name]

    schema_file = resources.files(__name__) / name
    if not schema_file.is_file():
        raise FileNotFoundError(f"Schema '{name}' is not packaged with the SDK.")

    with schema_file.open("r", encoding="utf-8") as handle:
        schema = cast(SchemaType, json.load(handle))

    _SCHEMA_CACHE[name] = schema
    return schema


def schema_exists(name: str) -> bool:
    """
    Check whether the given schema resource is bundled with the SDK.
    """
    schema_file = resources.files(__name__) / name
    return schema_file.is_file()


def load_schema_store() -> dict[str, SchemaType]:
    """
    Load all packaged schemas into a local reference store for relative $ref resolution.
    """
    global _SCHEMA_STORE_CACHE

    if _SCHEMA_STORE_CACHE is not None:
        return _SCHEMA_STORE_CACHE

    store: dict[str, SchemaType] = {}
    for schema_file in resources.files(__name__).iterdir():
        if not schema_file.is_file() or schema_file.name == "__init__.py":
            continue
        if not schema_file.name.endswith(".json"):
            continue

        schema = load_schema(schema_file.name)
        store[schema_file.name] = schema
        store[f"./{schema_file.name}"] = schema

        schema_id = schema.get("$id")
        if isinstance(schema_id, str):
            store[schema_id] = schema

    _SCHEMA_STORE_CACHE = store
    return store
