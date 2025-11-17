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


@dataclass
class ModelDef:
    name: str
    description: str | None
    fields: list[FieldDef] = field(default_factory=list)


@dataclass
class ModuleArtifact:
    models: list[ModelDef]
    typing_imports: set[str]
    needs_multilang: bool
    warnings: list[str]


class SchemaGenerator:
    def __init__(self, config: GeneratorConfig) -> None:
        self.config = config
        self.generated_index: list[tuple[str, list[str]]] = []

    def run(self) -> None:
        self.config.output_dir.mkdir(parents=True, exist_ok=True)
        for schema_path in sorted(self._iter_schema_files()):
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

        self._write_package_init()

    def _iter_schema_files(self) -> Iterable[Path]:
        return self.config.schemas_dir.glob("*.json")

    def _build_artifact(self, schema_path: Path, module_name: str) -> ModuleArtifact:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        converter = SchemaConverter(schema, module_name)
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

        for model in artifact.models:
            lines.extend(self._render_model(model))
            lines.append("")

        return "\n".join(lines)

    @staticmethod
    def _render_model(model: ModelDef) -> list[str]:
        lines: list[str] = [f"class {model.name}(TidasBaseModel):"]
        if model.description:
            lines.append(f'    """{model.description}"""')

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


class SchemaConverter:
    """
    Convert a single JSON schema document into a ModuleArtifact.
    """

    def __init__(self, schema: dict[str, Any], module_name: str) -> None:
        self.schema = schema
        self.module_name = module_name
        self.models: dict[str, ModelDef] = {}
        self.model_order: list[str] = []
        self.ref_map: dict[str, str] = {}
        self.typing_imports: set[str] = set()
        self.needs_multilang = False
        self.warnings: list[str] = []

    def convert(self) -> ModuleArtifact:
        self._register_definitions()
        root_name = self._derive_class_name(self.schema, self.module_name)
        self.ref_map["#"] = root_name
        self._ensure_model(root_name, self.schema)
        ordered_models = [self.models[name] for name in self.model_order]
        return ModuleArtifact(
            models=ordered_models,
            typing_imports=self.typing_imports,
            needs_multilang=self.needs_multilang,
            warnings=self.warnings,
        )

    def _register_definitions(self) -> None:
        for def_name, def_schema in self.schema.get("$defs", {}).items():
            class_name = to_pascal_case(def_name)
            pointer = f"#/$defs/{def_name}"
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
        required = set(schema.get("required", []))
        properties: dict[str, Any] = schema.get("properties", {})
        fields: list[FieldDef] = []
        for prop_name, prop_schema in properties.items():
            field = self._build_field(class_name, prop_name, prop_schema, prop_name in required)
            fields.append(field)
        description = schema.get("description")
        return ModelDef(name=class_name, description=description, fields=fields)

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

        return FieldDef(
            name=field_name,
            alias=alias,
            type_hint=type_hint,
            required=is_required,
            default_factory=default_factory,
            default=default_value,
            description=description,
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
            # Best effort: prefer referenced type, otherwise fall back to inline object.
            for entry in schema["allOf"]:
                if "$ref" in entry:
                    return self._resolve_ref(entry["$ref"])
                if entry.get("type") == "object":
                    return self._inline_model(parent_class, prop_name, entry)
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
    ) -> str:
        class_name = f"{parent_class}{to_pascal_case(prop_name)}"
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
        if ref not in self.ref_map:
            target = ref.split("/")[-1]
            class_name = to_pascal_case(target)
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
        if schema.get("$ref", "").endswith("MultiLang"):
            return True

        title = schema.get("title", "")
        if isinstance(title, str) and title.endswith("MultiLang"):
            return True

        if schema.get("type") == "array":
            items = schema.get("items", {})
            return SchemaConverter._is_multilang_object(items)

        if schema.get("type") == "object":
            return SchemaConverter._is_multilang_object(schema)

        return False

    @staticmethod
    def _is_multilang_object(schema: dict[str, Any]) -> bool:
        properties = schema.get("properties", {})
        return "@xml:lang" in properties and "#text" in properties


def to_pascal_case(value: str) -> str:
    parts = [segment for segment in value.replace("-", "_").split("_") if segment]
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
        else:
            result.append(char)
    snake = "".join(result)
    while "__" in snake:
        snake = snake.replace("__", "_")
    snake = snake.strip("_")
    return snake or "field"


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
