"""
Schema parser for TIDAS JSON schemas.

Reads JSON schema files and extracts type definitions and constraints
for code generation.
"""

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from loguru import logger


class SchemaParser:
    """Parser for TIDAS JSON schemas."""

    def __init__(self, schema_dir: Optional[str] = None):
        """Initialize schema parser with schema directory.

        Args:
            schema_dir: Path to directory containing JSON schemas.
                       If None, uses TIDAS_TOOLS_PATH environment variable.

        Raises:
            FileNotFoundError: If schema directory not found
        """
        if schema_dir is None:
            # Try environment variable
            tidas_tools_path = os.environ.get("TIDAS_TOOLS_PATH")
            if tidas_tools_path:
                schema_dir = os.path.join(
                    tidas_tools_path, "src/tidas_tools/tidas/schemas"
                )
            else:
                # Try relative path from repository root
                repo_root = Path(__file__).parent.parent.parent.parent
                schema_dir = str(
                    repo_root / "tidas-tools" / "src" / "tidas_tools" / "tidas" / "schemas"
                )

        self.schema_dir = Path(schema_dir)
        if not self.schema_dir.exists():
            raise FileNotFoundError(
                f"TIDAS schema directory not found at {self.schema_dir}. "
                "Ensure tidas-tools is cloned alongside tidas-sdk or set TIDAS_TOOLS_PATH."
            )

        logger.info(f"Using schema directory: {self.schema_dir}")
        self.schemas: Dict[str, Dict[str, Any]] = {}
        self.dependencies: Dict[str, Set[str]] = {}

    def load_all_schemas(self) -> None:
        """Load all JSON schema files from the schema directory."""
        schema_files = list(self.schema_dir.glob("tidas_*.json"))
        logger.info(f"Found {len(schema_files)} schema files")

        for schema_file in schema_files:
            schema_name = schema_file.stem
            with open(schema_file, "r", encoding="utf-8") as f:
                self.schemas[schema_name] = json.load(f)
                logger.debug(f"Loaded schema: {schema_name}")

    def parse_schema(self, schema_name: str) -> Dict[str, Any]:
        """Parse a specific schema and extract type definitions.

        Args:
            schema_name: Name of schema to parse (without .json extension)

        Returns:
            Dictionary containing parsed schema information
        """
        if schema_name not in self.schemas:
            raise ValueError(f"Schema '{schema_name}' not loaded")

        schema = self.schemas[schema_name]
        return {
            "name": schema_name,
            "title": schema.get("title", schema_name),
            "description": schema.get("description", ""),
            "properties": schema.get("properties", {}),
            "required": schema.get("required", []),
            "definitions": schema.get("$defs", {}),
        }

    def identify_multilang_fields(
        self, properties: Dict[str, Any]
    ) -> List[str]:
        """Identify fields that contain multi-language text.

        Multi-language fields are arrays of objects with @xml:lang pattern.

        Args:
            properties: Schema properties dictionary

        Returns:
            List of field names that are multi-language
        """
        multilang_fields = []

        for field_name, field_schema in properties.items():
            if self._is_multilang_field(field_schema):
                multilang_fields.append(field_name)

        return multilang_fields

    def _is_multilang_field(self, field_schema: Dict[str, Any]) -> bool:
        """Check if a field schema represents multi-language text.

        Args:
            field_schema: Field schema definition

        Returns:
            True if field is multi-language
        """
        # Check if it's an array
        if field_schema.get("type") != "array":
            return False

        # Check items schema
        items = field_schema.get("items", {})
        if items.get("type") != "object":
            return False

        # Check for @xml:lang and #text properties
        item_props = items.get("properties", {})
        has_lang = "@xml:lang" in item_props
        has_text = "#text" in item_props

        return has_lang and has_text

    def build_dependency_graph(self) -> Dict[str, Set[str]]:
        """Build dependency graph for schemas based on $ref references.

        Returns:
            Dictionary mapping schema names to their dependencies
        """
        self.dependencies = {name: set() for name in self.schemas.keys()}

        for schema_name, schema in self.schemas.items():
            deps = self._extract_dependencies(schema)
            self.dependencies[schema_name] = deps

        return self.dependencies

    def _extract_dependencies(
        self, schema: Dict[str, Any], refs: Optional[Set[str]] = None
    ) -> Set[str]:
        """Recursively extract $ref dependencies from a schema.

        Args:
            schema: Schema dictionary to analyze
            refs: Accumulator for found references

        Returns:
            Set of schema names referenced
        """
        if refs is None:
            refs = set()

        if isinstance(schema, dict):
            # Check for $ref
            if "$ref" in schema:
                ref = schema["$ref"]
                # Extract schema name from reference
                # Refs look like: "tidas_contacts.json#/$defs/SomeType"
                if ".json" in ref:
                    schema_name = ref.split(".json")[0].split("/")[-1]
                    refs.add(schema_name)

            # Recurse into nested structures
            for value in schema.values():
                self._extract_dependencies(value, refs)

        elif isinstance(schema, list):
            for item in schema:
                self._extract_dependencies(item, refs)

        return refs

    def topological_sort(self) -> List[str]:
        """Sort schemas in dependency order using topological sort.

        Schemas with no dependencies come first, followed by schemas
        that depend on them.

        Returns:
            List of schema names in dependency order

        Raises:
            ValueError: If circular dependencies detected
        """
        if not self.dependencies:
            self.build_dependency_graph()

        # Kahn's algorithm for topological sorting
        # in-degree = number of dependencies (things this schema needs)
        in_degree = {name: len(deps) for name, deps in self.dependencies.items()}

        # Queue of nodes with no dependencies
        queue = [name for name, degree in in_degree.items() if degree == 0]
        result = []

        while queue:
            # Sort queue for deterministic output
            queue.sort()
            node = queue.pop(0)
            result.append(node)

            # Reduce in-degree for nodes that depend on this node
            for name, deps in self.dependencies.items():
                if node in deps:
                    in_degree[name] -= 1
                    if in_degree[name] == 0:
                        queue.append(name)

        # Check for cycles
        if len(result) != len(self.dependencies):
            raise ValueError("Circular dependencies detected in schemas")

        return result

    def get_schema_files(self) -> List[str]:
        """Get list of all schema file names.

        Returns:
            List of schema file names
        """
        return list(self.schemas.keys())

    def get_entity_schemas(self) -> List[str]:
        """Get list of main entity schemas (non-category).

        Returns:
            List of main entity schema names
        """
        return [
            name
            for name in self.schemas.keys()
            if "_category" not in name and name != "tidas_data_types"
        ]
