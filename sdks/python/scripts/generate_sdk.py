#!/usr/bin/env python3
"""
Fine-grained JSON Schema -> Pydantic generator.

Compared to off-the-shelf tools this script gives us the levers required for:
    * consistent naming/alias handling across the SDK
    * automatic MultiLangList wiring
    * incremental evolution as the schema surface grows
"""
from __future__ import annotations

import argparse
import json
import keyword
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

# Ensure the SDK sources are importable when running the script directly.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = PROJECT_ROOT / "sdks/python/src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


@dataclass
class GeneratorConfig:
    schemas_dir: Path
    output_dir: Path


@dataclass
class FieldDef:
    name: str
    alias: str
    type_hint: str
    required: bool
    default: str | None = None
    default_factory: str | None = None
    description: str | None = None
    constraints: dict[str, str] = field(default_factory=dict)


@dataclass
class ModelDef:
    name: str
    description: str | None
    fields: list[FieldDef] = field(default_factory=list)
    base_class: str | None = None


@dataclass
class ModuleArtifact:
    models: list[ModelDef]
    typing_imports: set[str]
    needs_multilang: bool
    warnings: list[str]
    standard_imports: set[str]


@dataclass
class ScalarInfo:
    hint: str
    needs_multilang: bool = False
    typing_imports: set[str] = field(default_factory=set)


class SchemaGenerator:
    def __init__(self, config: GeneratorConfig) -> None:
        self.config = config
        self.generated_index: list[tuple[str, list[str]]] = []
        self.schema_cache_dir = self.config.output_dir.parent / "schemas"
        self.global_scalars: dict[str, ScalarInfo] = {}

    def run(self) -> None:
        self.config.output_dir.mkdir(parents=True, exist_ok=True)
        self.schema_cache_dir.mkdir(parents=True, exist_ok=True)
        schema_paths = sorted(
            self._iter_schema_files(),
            key=lambda path: (path.stem != "tidas_data_types", path.name),
        )
        for schema_path in schema_paths:
            module_name = schema_path.stem
            artifact = self._build_artifact(schema_path, module_name)
            output = self._render_module(schema_path.name, artifact)
            target_path = self.config.output_dir / f"{module_name}.py"
            target_path.write_text(output, encoding="utf-8")
            self.generated_index.append(
                (module_name, [model.name for model in artifact.models])
            )
            print(f"✓ Generated {target_path.relative_to(self.config.output_dir.parent)}")
            for warning in artifact.warnings:
                print(f"  ⚠ {warning}")
            self._copy_schema(schema_path)

        self._write_package_init()

    def _iter_schema_files(self) -> Iterable[Path]:
        return self.config.schemas_dir.glob("*.json")

    def _build_artifact(self, schema_path: Path, module_name: str) -> ModuleArtifact:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        converter = SchemaConverter(
            schema,
            module_name,
            global_scalars=self.global_scalars,
        )
        return converter.convert()

    def _render_module(self, source_name: str, artifact: ModuleArtifact) -> str:
        lines = [
            '"""',
            "Auto generated file. DO NOT EDIT.",
            f"Source: {source_name}",
            '"""',
            "from __future__ import annotations",
            "",
        ]

        if artifact.typing_imports:
            imports = ", ".join(sorted(artifact.typing_imports))
            lines.append(f"from typing import {imports}")
            lines.append("")

        lines.append("from pydantic import Field")
        lines.append("from tidas_sdk.core.base import TidasBaseModel")
        if artifact.needs_multilang:
            lines.append("from tidas_sdk.core.multilang import MultiLangList")
        lines.append("")
        for import_line in sorted(artifact.standard_imports):
            lines.append(import_line)
        if artifact.standard_imports:
            lines.append("")

        for model in artifact.models:
            lines.extend(self._render_model(model))
            lines.append("")

        return "\n".join(lines)

    @staticmethod
    def _render_model(model: ModelDef) -> list[str]:
        base = model.base_class or "TidasBaseModel"
        lines: list[str] = [f"class {model.name}({base}):"]
        if model.description:
            safe_desc = sanitize_docstring(model.description)
            lines.append(f'    """{safe_desc}"""')

        if not model.fields:
            lines.append("    pass")
            return lines

        for field_def in model.fields:
            annotation = field_def.type_hint
            if (
                not field_def.required
                and field_def.default_factory is None
                and field_def.default in (None, "None")
                and "None" not in annotation
            ):
                annotation = f"{annotation} | None"

            field_args: list[str] = []
            if field_def.default_factory:
                field_args.append(f"default_factory={field_def.default_factory}")
            else:
                default_expr = field_def.default or "..."
                field_args.append(f"default={default_expr}")

            field_args.append(f"alias='{field_def.alias}'")
            if field_def.description:
                field_args.append(f"description={repr(field_def.description)}")
            for key, value in field_def.constraints.items():
                field_args.append(f"{key}={value}")

            field_line = (
                f"    {field_def.name}: {annotation} = Field({', '.join(field_args)})"
            )
            lines.append(field_line)

        return lines

    def _write_package_init(self) -> None:
        if not self.generated_index:
            return

        lines = [
            '"""Exports for auto-generated models."""',
            "from __future__ import annotations",
            "",
        ]
        exported_names: list[str] = []
        for module, names in self.generated_index:
            for name in names:
                lines.append(f"from .{module} import {name}")
            exported_names.extend(names)

        lines.append("")
        lines.append("__all__ = [")
        for name in exported_names:
            lines.append(f"    '{name}',")
        lines.append("]\n")

        target = self.config.output_dir / "__init__.py"
        target.write_text("\n".join(lines), encoding="utf-8")

    def _copy_schema(self, schema_path: Path) -> None:
        destination = self.schema_cache_dir / schema_path.name
        try:
            shutil.copy2(schema_path, destination)
        except FileNotFoundError:
            # schema may not exist if submodule not initialized
            pass


class SchemaConverter:
    """
    Convert a single JSON schema document into a ModuleArtifact.
    """

    def __init__(
        self,
        schema: dict[str, Any],
        module_name: str,
        *,
        global_scalars: dict[str, ScalarInfo] | None = None,
    ) -> None:
        self.schema = schema
        self.module_name = module_name
        self.models: dict[str, ModelDef] = {}
        self.model_order: list[str] = []
        self.ref_map: dict[str, str] = {}
        self.typing_imports: set[str] = set()
        self.needs_multilang = False
        self.warnings: list[str] = []
        self.standard_imports: set[str] = set()
        self.scalar_aliases: dict[str, ScalarInfo] = {}
        self.used_class_names: set[str] = set()
        self.global_scalars = global_scalars if global_scalars is not None else {}

    def convert(self) -> ModuleArtifact:
        self._register_definitions()
        root_name = self._unique_class_name(
            self._derive_class_name(self.schema, self.module_name)
        )
        self.ref_map["#"] = root_name
        self._ensure_model(root_name, self.schema)
        ordered_models = [self.models[name] for name in self.model_order]
        return ModuleArtifact(
            models=ordered_models,
            typing_imports=self.typing_imports,
            needs_multilang=self.needs_multilang,
            warnings=self.warnings,
            standard_imports=self.standard_imports,
        )

    def _register_definitions(self) -> None:
        for def_name, def_schema in self.schema.get("$defs", {}).items():
            class_name = to_pascal_case(def_name)
            pointer = f"#/$defs/{def_name}"
            scalar = self._infer_scalar(def_schema)
            if scalar:
                self._register_scalar(def_name, pointer, scalar)
                continue
            class_name = self._unique_class_name(class_name)
            self.ref_map[pointer] = class_name
            self._ensure_model(class_name, def_schema)

    def _ensure_model(self, class_name: str, schema: dict[str, Any]) -> ModelDef:
        if class_name in self.models:
            return self.models[class_name]

        model = self._build_model(class_name, schema)
        self.models[class_name] = model
        self.model_order.append(class_name)
        return model

    def _build_model(self, class_name: str, schema: dict[str, Any]) -> ModelDef:
        normalized = self._normalize_object_schema(schema)
        properties = normalized["properties"]
        required = normalized["required"]
        description = normalized["description"]
        base_class = normalized["base_class"]

        fields: list[FieldDef] = []
        for prop_name, prop_schema in properties.items():
            is_required = prop_name in required
            field = self._build_field(class_name, prop_name, prop_schema, is_required)
            fields.append(field)

        return ModelDef(
            name=class_name,
            description=description,
            fields=fields,
            base_class=base_class,
        )

    def _build_field(
        self,
        parent_class: str,
        prop_name: str,
        prop_schema: dict[str, Any],
        is_required: bool,
    ) -> FieldDef:
        field_name = to_snake_case(prop_name)
        if keyword.iskeyword(field_name):
            field_name += "_"

        alias = prop_name
        description = prop_schema.get("description")

        if self._is_multilang(prop_schema):
            self.needs_multilang = True
            type_hint = "MultiLangList"
            default_factory = "MultiLangList"
            is_required = False
            default_value = None
        else:
            type_hint = self._determine_type(parent_class, prop_name, prop_schema)
            default_factory = self._default_factory(prop_schema)
            default_value = self._default_value(prop_schema, is_required, default_factory)

        constraints = self._collect_constraints(prop_schema)

        return FieldDef(
            name=field_name,
            alias=alias,
            type_hint=type_hint,
            required=is_required,
            default_factory=default_factory,
            default=default_value,
            description=description,
            constraints=constraints,
        )

    def _default_factory(self, schema: dict[str, Any]) -> str | None:
        type_name = schema.get("type")
        if self._is_multilang(schema):
            return "MultiLangList"
        if type_name == "array":
            return "list"
        if type_name == "object" and schema.get("properties"):
            return None  # prefer nested model default None unless schema supplies default
        if isinstance(schema.get("default"), (list, dict)):
            self.warnings.append(
                f"{self.module_name}: skipped mutable default for {schema.get('title', 'field')}"
            )
        return None

    def _default_value(
        self,
        schema: dict[str, Any],
        is_required: bool,
        default_factory: str | None,
    ) -> str | None:
        if default_factory:
            return None
        if "default" in schema and not isinstance(schema["default"], (dict, list)):
            return repr(schema["default"])
        return "..." if is_required else "None"

    def _determine_type(
        self,
        parent_class: str,
        prop_name: str,
        schema: dict[str, Any],
    ) -> str:
        if isinstance(schema, list):
            option_types = {
                self._determine_type(parent_class, f"{prop_name}Option{i}", option)
                for i, option in enumerate(schema)
                if isinstance(option, (dict, list))
            }
            if option_types:
                return " | ".join(sorted(option_types))
            self.typing_imports.add("Any")
            return "Any"

        if not isinstance(schema, dict):
            self.typing_imports.add("Any")
            return "Any"

        fmt = schema.get("format")
        if fmt == "date-time":
            self.standard_imports.add("from datetime import datetime")
            return "datetime"
        if fmt == "date":
            self.standard_imports.add("from datetime import date")
            return "date"
        if fmt == "time":
            self.standard_imports.add("from datetime import time")
            return "time"
        if fmt == "uuid":
            self.standard_imports.add("from uuid import UUID")
            return "UUID"

        if "$ref" in schema:
            return self._resolve_ref(schema["$ref"])

        if "const" in schema:
            value = schema["const"]
            self.typing_imports.add("Literal")
            return f"Literal[{repr(value)}]"

        for key in ("oneOf", "anyOf"):
            if key in schema:
                options = schema[key]
                types = {
                    self._determine_type(parent_class, f"{prop_name}Option{i}", option)
                    for i, option in enumerate(options)
                }
                return " | ".join(sorted(types))

        if "enum" in schema:
            self.typing_imports.add("Literal")
            literals = ", ".join(repr(value) for value in schema["enum"])
            return f"Literal[{literals}]"

        if "allOf" in schema:
            inline_schema: dict[str, Any] | None = None
            ref_types: list[str] = []
            for entry in schema["allOf"]:
                if isinstance(entry, dict):
                    if "$ref" in entry:
                        ref_types.append(self._resolve_ref(entry["$ref"]))
                    elif entry.get("type") == "object":
                        inline_schema = inline_schema or {}
                        inline_schema = self._merge_inline_schema(inline_schema, entry)
                    else:
                        # treat as constraint-only fragment, ignore
                        continue
            if inline_schema:
                if ref_types:
                    inline_schema = {**inline_schema, "$ref": ref_types[0]}
                return self._inline_model(parent_class, prop_name, inline_schema)
            if ref_types:
                return ref_types[0]
            # Fall back to schema without allOf (constraints only)
            reduced_schema = {k: v for k, v in schema.items() if k != "allOf"}
            if reduced_schema:
                return self._determine_type(parent_class, prop_name, reduced_schema)
            self.warnings.append(
                f"{self.module_name}: unsupported allOf on {prop_name}, using Any"
            )
            self.typing_imports.add("Any")
            return "Any"

        type_name = schema.get("type")
        if isinstance(type_name, list):
            non_null = [t for t in type_name if t != "null"]
            if not non_null:
                self.typing_imports.add("Any")
                return "Any"
            schema = {**schema, "type": non_null[0]}
            return f"{self._determine_type(parent_class, prop_name, schema)} | None"

        if type_name == "array":
            item_schema = schema.get("items", {})
            item_type = self._determine_type(parent_class, f"{prop_name}Item", item_schema)
            return f"list[{item_type}]"

        if type_name == "object":
            if schema.get("properties"):
                return self._inline_model(parent_class, prop_name, schema)
            additional = schema.get("additionalProperties")
            if isinstance(additional, dict):
                value_type = self._determine_type(
                    parent_class, f"{prop_name}Value", additional
                )
                return f"dict[str, {value_type}]"
            self.typing_imports.add("Any")
            return "dict[str, Any]"

        return self._map_primitive(type_name)

    def _inline_model(
        self,
        parent_class: str,
        prop_name: str,
        schema: dict[str, Any],
        qualifier: str | None = None,
    ) -> str:
        class_name = self._compose_class_name(parent_class, prop_name, qualifier)
        self._ensure_model(class_name, schema)
        return class_name

    def _map_primitive(self, type_name: str | None) -> str:
        mapping = {
            "string": "str",
            "number": "float",
            "integer": "int",
            "boolean": "bool",
        }
        if type_name in mapping:
            return mapping[type_name]
        self.typing_imports.add("Any")
        return "Any"

    def _resolve_ref(self, ref: str) -> str:
        scalar = self._lookup_scalar(ref)
        if scalar:
            if scalar.needs_multilang:
                self.needs_multilang = True
            for imp in scalar.typing_imports:
                if imp.startswith("from ") or imp.startswith("import "):
                    self.standard_imports.add(imp)
                else:
                    self.typing_imports.add(imp)
            return scalar.hint

        if ref not in self.ref_map:
            target = ref.split("/")[-1]
            class_name = self._unique_class_name(to_pascal_case(target))
            self.ref_map[ref] = class_name
        return self.ref_map[ref]

    @staticmethod
    def _derive_class_name(schema: dict[str, Any], module_name: str) -> str:
        if "title" in schema:
            return to_pascal_case(schema["title"])
        stem = module_name
        if stem.startswith("tidas_"):
            stem = stem.removeprefix("tidas_")
        return to_pascal_case(stem)

    @staticmethod
    def _is_multilang(schema: dict[str, Any]) -> bool:
        if isinstance(schema, list):
            return any(
                SchemaConverter._is_multilang(item)
                for item in schema
                if isinstance(item, dict)
            )

        if schema.get("$ref", "").endswith("MultiLang"):
            return True

        title = schema.get("title", "")
        if isinstance(title, str) and title.endswith("MultiLang"):
            return True

        if schema.get("type") == "array":
            items = schema.get("items", {})
            # items can be a schema or a list of schemas (tuples, anyOf style)
            if isinstance(items, list):
                return any(
                    SchemaConverter._is_multilang(item)
                    for item in items
                    if isinstance(item, dict)
                )
            return SchemaConverter._is_multilang_object(items)

        if schema.get("type") == "object":
            return SchemaConverter._is_multilang_object(schema)

        return False

    @staticmethod
    def _is_multilang_object(schema: dict[str, Any]) -> bool:
        if isinstance(schema, list):
            return any(
                SchemaConverter._is_multilang_object(item)
                for item in schema
                if isinstance(item, dict)
            )
        if not isinstance(schema, dict):
            return False
        properties = schema.get("properties", {})
        return "@xml:lang" in properties and "#text" in properties

    def _normalize_object_schema(self, schema: Any) -> dict[str, Any]:
        """
        Merge object schemas by resolving allOf constructs and capture base classes.
        """
        properties: dict[str, Any] = {}
        required: set[str] = set()
        description: str | None = None
        base_class: str | None = None

        if not isinstance(schema, dict):
            return {
                "properties": properties,
                "required": required,
                "description": description,
                "base_class": base_class,
            }

        if isinstance(schema.get("description"), str):
            description = schema["description"]

        if "$ref" in schema:
            scalar = self._lookup_scalar(schema["$ref"])
            if scalar is None:
                candidate = self._resolve_ref(schema["$ref"])
                if candidate and candidate[0].isupper() and candidate.isidentifier():
                    base_class = candidate

        all_of = schema.get("allOf")
        if isinstance(all_of, list):
            for part in all_of:
                normalized = self._normalize_object_schema(part)
                properties.update(normalized["properties"])
                required |= normalized["required"]
                if not description:
                    description = normalized["description"]
                if normalized["base_class"] and not base_class:
                    base_class = normalized["base_class"]

        if "properties" in schema and isinstance(schema["properties"], dict):
            properties.update(schema["properties"])

        required |= set(schema.get("required", []))

        return {
            "properties": properties,
            "required": required,
            "description": description,
            "base_class": base_class,
        }

    def _collect_constraints(self, schema: dict[str, Any]) -> dict[str, str]:
        constraints: dict[str, str] = {}
        if not isinstance(schema, dict):
            return constraints

        if "minimum" in schema:
            constraints["ge"] = repr(schema["minimum"])
        if "maximum" in schema:
            constraints["le"] = repr(schema["maximum"])
        if "exclusiveMinimum" in schema:
            constraints["gt"] = repr(schema["exclusiveMinimum"])
        if "exclusiveMaximum" in schema:
            constraints["lt"] = repr(schema["exclusiveMaximum"])
        if "minLength" in schema:
            constraints["min_length"] = repr(schema["minLength"])
        if "maxLength" in schema:
            constraints["max_length"] = repr(schema["maxLength"])
        if "pattern" in schema:
            pattern = schema["pattern"]
            if isinstance(pattern, str):
                constraints["pattern"] = repr(pattern)
        if "minItems" in schema:
            constraints["min_items"] = repr(schema["minItems"])
        if "maxItems" in schema:
            constraints["max_items"] = repr(schema["maxItems"])
        if "multipleOf" in schema:
            constraints["multiple_of"] = repr(schema["multipleOf"])

        return constraints

    def _register_scalar(self, name: str, pointer: str, scalar: ScalarInfo) -> None:
        self.scalar_aliases[pointer] = scalar
        self.scalar_aliases[name] = scalar
        self.global_scalars[name] = scalar
        self.global_scalars[pointer] = scalar
        if scalar.needs_multilang:
            self.needs_multilang = True
        for imp in scalar.typing_imports:
            if imp.startswith("from ") or imp.startswith("import "):
                self.standard_imports.add(imp)
            else:
                self.typing_imports.add(imp)

    def _lookup_scalar(self, ref: str) -> ScalarInfo | None:
        if ref in self.scalar_aliases:
            return self.scalar_aliases[ref]
        target = ref.split("/")[-1]
        if target in self.scalar_aliases:
            return self.scalar_aliases[target]
        if ref in self.global_scalars:
            return self.global_scalars[ref]
        if target in self.global_scalars:
            return self.global_scalars[target]
        return None

    def _infer_scalar(self, schema: Any) -> ScalarInfo | None:
        if not isinstance(schema, dict):
            return None
        if self._is_multilang(schema):
            return ScalarInfo("MultiLangList", needs_multilang=True)
        if "$ref" in schema:
            ref_scalar = self._lookup_scalar(schema["$ref"])
            if ref_scalar:
                return ref_scalar

        if "anyOf" in schema and isinstance(schema["anyOf"], list):
            options = [
                self._infer_scalar(option) for option in schema["anyOf"] if isinstance(option, (dict, list))
            ]
            options = [opt for opt in options if opt is not None]
            if options and all(opt.hint == options[0].hint for opt in options):
                combined_imports: set[str] = set()
                for opt in options:
                    combined_imports.update(opt.typing_imports)
                return ScalarInfo(
                    hint=options[0].hint,
                    needs_multilang=any(opt.needs_multilang for opt in options),
                    typing_imports=combined_imports,
                )
            return None

        schema_type = schema.get("type")
        if schema_type == "string":
            fmt = schema.get("format")
            if fmt == "date-time":
                return ScalarInfo("datetime", typing_imports={"from datetime import datetime"})
            if fmt == "date":
                return ScalarInfo("date", typing_imports={"from datetime import date"})
            if fmt == "time":
                return ScalarInfo("time", typing_imports={"from datetime import time"})
            return ScalarInfo("str")
        if schema_type == "integer":
            return ScalarInfo("int")
        if schema_type == "number":
            return ScalarInfo("float")
        if schema_type == "boolean":
            return ScalarInfo("bool")

        if "enum" in schema and isinstance(schema["enum"], list):
            literals = ", ".join(repr(value) for value in schema["enum"])
            return ScalarInfo(f"Literal[{literals}]", typing_imports={"Literal"})

        return None

    def _compose_class_name(
        self,
        parent: str,
        suffix: str,
        qualifier: str | None = None,
    ) -> str:
        suffix_token = to_pascal_case(suffix)
        tokens = self._split_pascal(parent)
        base_tokens = tokens[-2:] if len(tokens) >= 2 else tokens
        parts = base_tokens + [suffix_token]
        if qualifier:
            parts.append(to_pascal_case(qualifier))
        candidate = "".join(parts) or suffix_token or "GeneratedModel"
        return self._unique_class_name(candidate)

    def _unique_class_name(self, candidate: str) -> str:
        if not candidate:
            candidate = "GeneratedModel"
        candidate = candidate[0].upper() + candidate[1:]
        if len(candidate) > 64:
            tail = self._split_pascal(candidate)[-3:]
            if tail:
                candidate = "".join(tail)
            else:
                candidate = candidate[-64:]
        base = candidate
        counter = 1
        while base in self.used_class_names:
            counter += 1
            base = f"{candidate}{counter}"
        self.used_class_names.add(base)
        return base

    @staticmethod
    def _split_pascal(value: str) -> list[str]:
        step = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
        step = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", step)
        return [part for part in step.replace("__", "_").split("_") if part]

    @staticmethod
    def _merge_inline_schema(base: dict[str, Any], new: dict[str, Any]) -> dict[str, Any]:
        merged = {**base}
        if "properties" in new:
            merged.setdefault("properties", {})
            merged["properties"].update(new["properties"])
        if "required" in new:
            merged.setdefault("required", [])
            merged["required"] = list({*merged["required"], *new["required"]})
        for key in ("description", "title"):
            if key in new and key not in merged:
                merged[key] = new[key]
        return merged


def to_pascal_case(value: str) -> str:
    sanitized = (
        value.replace("-", "_")
        .replace(":", "_")
        .replace(".", "_")
        .replace("/", "_")
        .replace("@", "_")
        .replace("#", "_")
        .replace(" ", "_")
    )
    parts = [segment for segment in sanitized.split("_") if segment]
    return "".join(segment.capitalize() for segment in parts) or "GeneratedModel"


def to_snake_case(value: str) -> str:
    result: list[str] = []
    for char in value:
        if char.isupper():
            if result:
                result.append("_")
            result.append(char.lower())
        elif char in " -:./":
            result.append("_")
        elif char in "@#":
            continue
        else:
            result.append(char)
    snake = "".join(result)
    while "__" in snake:
        snake = snake.replace("__", "_")
    snake = snake.strip("_")
    return snake or "field"


def sanitize_docstring(text: str) -> str:
    escaped = text.replace("\\", "\\\\").replace('"', '\\"')
    return escaped


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate Python SDK models from JSON Schema files."
    )
    parser.add_argument(
        "--schemas",
        type=Path,
        default=Path("../../tidas-tools/src/tidas_tools/tidas/schemas"),
        help="Directory containing *.json schema files.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("../src/tidas_sdk/generated"),
        help="Output directory for generated modules.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = GeneratorConfig(
        schemas_dir=args.schemas.resolve(),
        output_dir=args.output.resolve(),
    )
    generator = SchemaGenerator(config)
    generator.run()


if __name__ == "__main__":
    main()
