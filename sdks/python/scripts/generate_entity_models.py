#!/usr/bin/env python3
"""
Generate entity model classes with default value initialization.

This script generates entity model classes that include initialize_defaults methods
similar to the TypeScript SDK implementation.
"""

import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from loguru import logger


class EntityModelGenerator:
    """Generate entity model classes with default value initialization."""

    def __init__(self, schema_dir: Optional[str] = None):
        """Initialize entity model generator.

        Args:
            schema_dir: Path to directory containing JSON schemas
        """
        if schema_dir is None:
            tidas_tools_path = os.environ.get("TIDAS_TOOLS_PATH")
            if tidas_tools_path:
                schema_dir = os.path.join(
                    tidas_tools_path, "src/tidas_tools/tidas/schemas"
                )
            else:
                repo_root = Path(__file__).parent.parent.parent.parent
                schema_dir = str(
                    repo_root
                    / "tidas-tools"
                    / "src"
                    / "tidas_tools"
                    / "tidas"
                    / "schemas"
                )

        self.schema_dir = Path(schema_dir)
        if not self.schema_dir.exists():
            raise FileNotFoundError(f"Schema directory not found: {self.schema_dir}")

        logger.info(f"Using schema directory: {self.schema_dir}")
        self.schemas: Dict[str, Dict[str, Any]] = {}

    def load_schema(self, schema_name: str) -> Dict[str, Any]:
        """Load a JSON schema file.

        Args:
            schema_name: Name of schema (e.g., 'tidas_processes')

        Returns:
            Parsed schema dictionary
        """
        schema_file = self.schema_dir / f"{schema_name}.json"
        with open(schema_file, "r", encoding="utf-8") as f:
            schema = json.load(f)
        self.schemas[schema_name] = schema
        return schema

    def get_entity_name(self, schema_name: str) -> str:
        """Convert schema name to entity class name.

        Args:
            schema_name: Schema name (e.g., 'tidas_processes')

        Returns:
            Entity class name (e.g., 'TidasProcess')
        """
        # Remove 'tidas_' prefix and convert to PascalCase
        name = schema_name.replace("tidas_", "")
        parts = name.split("_")
        return "Tidas" + "".join(word.capitalize() for word in parts)

    def get_dataset_name(self, schema_name: str) -> str:
        """Get the root dataset name for the entity.

        Args:
            schema_name: Schema name (e.g., 'tidas_processes')

        Returns:
            Dataset name (e.g., 'processDataSet')
        """
        schema = self.load_schema(schema_name)
        properties = schema.get("properties", {})
        if not properties:
            return f"{schema_name.replace('tidas_', '')}DataSet"

        # Return the first property name, which is typically the root dataset
        return list(properties.keys())[0]

    def get_namespace_attributes(self, schema_name: str) -> Dict[str, str]:
        """Get namespace attributes for the entity.

        Args:
            schema_name: Schema name (e.g., 'tidas_processes')

        Returns:
            Dictionary of namespace attributes
        """
        # Map entity types to their namespace attributes
        namespace_map = {
            "tidas_processes": {
                "@xmlns": "http://lca.jrc.it/ILCD/Process",
                "@xmlns:common": "http://lca.jrc.it/ILCD/Common",
                "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                "@version": "1.1",
                "@xsi:schemaLocation": "http://lca.jrc.it/ILCD/Process ../../schemas/ILCD_ProcessDataSet.xsd",
            },
            "tadas_contacts": {
                "@xmlns": "http://lca.jrc.it/ILCD/Contact",
                "@xmlns:common": "http://lca.jrc.it/ILCD/Common",
                "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                "@version": "1.1",
                "@xsi:schemaLocation": "http://lca.jrc.it/ILCD/Contact ../../schemas/ILCD_ContactDataSet.xsd",
            },
            "tadas_flows": {
                "@xmlns": "http://lca.jrc.it/ILCD/Flow",
                "@xmlns:common": "http://lca.jrc.it/ILCD/Common",
                "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                "@version": "1.1",
                "@xsi:schemaLocation": "http://lca.jrc.it/ILCD/Flow ../../schemas/ILCD_FlowDataSet.xsd",
            },
            "tadas_sources": {
                "@xmlns": "http://lca.jrc.it/ILCD/Source",
                "@xmlns:common": "http://lca.jrc.it/ILCD/Common",
                "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                "@version": "1.1",
                "@xsi:schemaLocation": "http://lca.jrc.it/ILCD/Source ../../schemas/ILCD_SourceDataSet.xsd",
            },
            "tadas_flowproperties": {
                "@xmlns": "http://lca.jrc.it/ILCD/FlowProperty",
                "@xmlns:common": "http://lca.jrc.it/ILCD/Common",
                "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                "@version": "1.1",
                "@xsi:schemaLocation": "http://lca.jrc.it/ILCD/FlowProperty ../../schemas/ILCD_FlowPropertyDataSet.xsd",
            },
            "tadas_unitgroups": {
                "@xmlns": "http://lca.jrc.it/ILCD/UnitGroup",
                "@xmlns:common": "http://lca.jrc.it/ILCD/Common",
                "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                "@version": "1.1",
                "@xsi:schemaLocation": "http://lca.jrc.it/ILCD/UnitGroup ../../schemas/ILCD_UnitGroupDataSet.xsd",
            },
            "tidas_lciamethods": {
                "@xmlns": "http://lca.jrc.it/ILCD/LCIAMethod",
                "@xmlns:common": "http://lca.jrc.it/ILCD/Common",
                "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                "@version": "1.1",
                "@xsi:schemaLocation": "http://lca.jrc.it/ILCD/LCIAMethod ../../schemas/ILCD_LCIAMethodDataSet.xsd",
            },
            "tidas_lifecyclemodels": {
                "@xmlns": "http://lca.jrc.it/ILCD/LifeCycleModel",
                "@xmlns:common": "http://lca.jrc.it/ILCD/Common",
                "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                "@version": "1.1",
                "@xsi:schemaLocation": "http://lca.jrc.it/ILCD/LifeCycleModel ../../schemas/ILCD_LifeCycleModelDataSet.xsd",
            },
        }

        return namespace_map.get(schema_name, {})

    def get_nested_structure_paths(self, schema_name: str) -> List[str]:
        """Get the nested structure paths for the entity.

        Args:
            schema_name: Schema name (e.g., 'tidas_processes')

        Returns:
            List of nested structure paths
        """
        # Map entity types to their nested structure paths
        structure_map = {
            "tidas_processes": [
                "processDataSet",
                "processDataSet.processInformation",
                "processDataSet.processInformation.dataSetInformation",
                "processDataSet.processInformation.dataSetInformation.classificationInformation",
                "processDataSet.processInformation.quantitativeReference",
                "processDataSet.processInformation.time",
                "processDataSet.processInformation.geography",
                "processDataSet.processInformation.technology",
                "processDataSet.modellingAndValidation",
                "processDataSet.modellingAndValidation.LCIMethodAndAllocation",
                "processDataSet.modellingAndValidation.dataSourcesTreatmentAndRepresentativeness",
                "processDataSet.modellingAndValidation.validation",
                "processDataSet.modellingAndValidation.complianceDeclarations",
                "processDataSet.administrativeInformation",
                "processDataSet.administrativeInformation.dataEntryBy",
                "processDataSet.administrativeInformation.publicationAndOwnership",
                "processDataSet.exchanges",
            ],
            "tadas_contacts": [
                "contactDataSet",
                "contactDataSet.contactInformation",
                "contactDataSet.contactInformation.dataSetInformation",
                "contactDataSet.contactInformation.dataSetInformation.classificationInformation",
                "contactDataSet.administrativeInformation",
                "contactDataSet.administrativeInformation.dataEntryBy",
                "contactDataSet.administrativeInformation.publicationAndOwnership",
            ],
            "tadas_flows": [
                "flowDataSet",
                "flowDataSet.flowInformation",
                "flowDataSet.flowInformation.dataSetInformation",
                "flowDataSet.flowInformation.dataSetInformation.classificationInformation",
                "flowDataSet.modellingAndValidation",
                "flowDataSet.administrativeInformation",
                "flowDataSet.administrativeInformation.dataEntryBy",
                "flowDataSet.administrativeInformation.publicationAndOwnership",
            ],
            "tadas_sources": [
                "sourceDataSet",
                "sourceDataSet.sourceInformation",
                "sourceDataSet.sourceInformation.dataSetInformation",
                "sourceDataSet.sourceInformation.dataSetInformation.classificationInformation",
                "sourceDataSet.administrativeInformation",
                "sourceDataSet.administrativeInformation.dataEntryBy",
                "sourceDataSet.administrativeInformation.publicationAndOwnership",
            ],
            "tadas_flowproperties": [
                "flowPropertyDataSet",
                "flowPropertyDataSet.flowPropertiesInformation",
                "flowPropertyDataSet.flowPropertiesInformation.dataSetInformation",
                "flowPropertyDataSet.flowPropertiesInformation.dataSetInformation.classificationInformation",
                "flowPropertyDataSet.modellingAndValidation",
                "flowPropertyDataSet.administrativeInformation",
                "flowPropertyDataSet.administrativeInformation.dataEntryBy",
                "flowPropertyDataSet.administrativeInformation.publicationAndOwnership",
            ],
            "tadas_unitgroups": [
                "unitGroupDataSet",
                "unitGroupDataSet.unitGroupInformation",
                "unitGroupDataSet.unitGroupInformation.dataSetInformation",
                "unitGroupDataSet.unitGroupInformation.dataSetInformation.classificationInformation",
                "unitGroupDataSet.modellingAndValidation",
                "unitGroupDataSet.administrativeInformation",
                "unitGroupDataSet.administrativeInformation.dataEntryBy",
                "unitGroupDataSet.administrativeInformation.publicationAndOwnership",
                "unitGroupDataSet.units",
            ],
            "tidas_lciamethods": [
                "LCIAMethodDataSet",
                "LCIAMethodDataSet.LCIAMethodInformation",
                "LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation",
                "LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.classificationInformation",
                "LCIAMethodDataSet.modellingAndValidation",
                "LCIAMethodDataSet.administrativeInformation",
                "LCIAMethodDataSet.administrativeInformation.dataEntryBy",
                "LCIAMethodDataSet.administrativeInformation.publicationAndOwnership",
                "LCIAMethodDataSet.characterisationFactors",
            ],
            "tidas_lifecyclemodels": [
                "lifeCycleModelDataSet",
                "lifeCycleModelDataSet.lifeCycleModelInformation",
                "lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation",
                "lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.classificationInformation",
                "lifeCycleModelDataSet.modellingAndValidation",
                "lifeCycleModelDataSet.administrativeInformation",
                "lifeCycleModelDataSet.administrativeInformation.dataEntryBy",
                "lifeCycleModelDataSet.administrativeInformation.publicationAndOwnership",
            ],
        }

        return structure_map.get(schema_name, [])

    def get_default_field_values(self, schema_name: str) -> Dict[str, Any]:
        """Get default field values for the entity.

        Args:
            schema_name: Schema name (e.g., 'tidas_processes')

        Returns:
            Dictionary of default field values
        """
        # Map entity types to their default field values
        defaults_map = {
            "tidas_processes": {
                "processDataSet.processInformation.dataSetInformation.common:UUID": "uuid.uuid4()",
                "processDataSet.administrativeInformation.dataEntryBy.common:timeStamp": "datetime.datetime.now().isoformat()",
            },
            "tadas_contacts": {
                "contactDataSet.contactInformation.dataSetInformation.common:UUID": "uuid.uuid4()",
                "contactDataSet.administrativeInformation.dataEntryBy.common:timeStamp": "datetime.datetime.now().isoformat()",
            },
            "tadas_flows": {
                "flowDataSet.flowInformation.dataSetInformation.common:UUID": "uuid.uuid4()",
                "flowDataSet.administrativeInformation.dataEntryBy.common:timeStamp": "datetime.datetime.now().isoformat()",
            },
            "tadas_sources": {
                "sourceDataSet.sourceInformation.dataSetInformation.common:UUID": "uuid.uuid4()",
                "sourceDataSet.administrativeInformation.dataEntryBy.common:timeStamp": "datetime.datetime.now().isoformat()",
            },
            "tadas_flowproperties": {
                "flowPropertyDataSet.flowPropertiesInformation.dataSetInformation.common:UUID": "uuid.uuid4()",
                "flowPropertyDataSet.administrativeInformation.dataEntryBy.common:timeStamp": "datetime.datetime.now().isoformat()",
            },
            "tadas_unitgroups": {
                "unitGroupDataSet.unitGroupInformation.dataSetInformation.common:UUID": "uuid.uuid4()",
                "unitGroupDataSet.administrativeInformation.dataEntryBy.common:timeStamp": "datetime.datetime.now().isoformat()",
            },
            "tadas_lciamethods": {
                "LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.common:UUID": "uuid.uuid4()",
                "LCIAMethodDataSet.administrativeInformation.dataEntryBy.common:timeStamp": "datetime.datetime.now().isoformat()",
            },
            "tadas_lifecyclemodels": {
                "lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:UUID": "uuid.uuid4()",
                "lifeCycleModelDataSet.administrativeInformation.dataEntryBy.common:timeStamp": "datetime.datetime.now().isoformat()",
            },
        }

        return defaults_map.get(schema_name, {})

    def generate_entity_model(self, schema_name: str) -> str:
        """Generate an entity model class with initialize_defaults method.

        Args:
            schema_name: Schema name (e.g., 'tidas_processes')

        Returns:
            Generated Python code
        """
        entity_name = self.get_entity_name(schema_name)
        dataset_name = self.get_dataset_name(schema_name)
        namespace_attrs = self.get_namespace_attributes(schema_name)
        nested_paths = self.get_nested_structure_paths(schema_name)
        default_values = self.get_default_field_values(schema_name)

        # Generate imports
        lines = [
            '"""',
            f"{entity_name} entity wrapper class for TIDAS SDK.",
            '"""',
            "",
            "import datetime",
            "import uuid",
            "from typing import Any, Dict, Optional",
            "",
            "from ..core.base import TidasEntity",
            f"from ..core.wrappers.{schema_name.replace('tidas_', '')}_wrappers import {entity_name.replace('Tidas', '')}DataSetWrapper",
            "from ..core.validation import ValidationConfig",
            f"from ..types.{schema_name} import Model as {entity_name.replace('Tidas', '')}Model",
            "",
            "",
            f"class {entity_name}(TidasEntity):",
            f'    """Wrapper class for {entity_name.replace("Tidas", "")} entities with pythonic API.',
            "",
            f"    Represents a {entity_name.replace('Tidas', '').lower()} in LCA.",
            "",
            "    Example:",
            f"        >>> {entity_name.lower().replace('tidas', '')} = {entity_name}()",
        ]

        # Add example based on entity type
        if schema_name == "tidas_processes":
            lines.extend(
                [
                    "        >>> process.process_data_set.process_information.data_set_information.name.base_name.set_text(",
                    '        ...     "Electricity production, photovoltaic", "en"',
                    "        ... )",
                ]
            )
        else:
            lines.extend(
                [
                    f"        >>> {entity_name.lower().replace('tidas', '')}.{entity_name.replace('Tidas', '').lower()}_data_set.{entity_name.replace('Tidas', '').lower()}_information.data_set_information.name.set_text(",
                    f'        ...     "Example {entity_name.replace("Tidas", "")}", "en"',
                    "        ... )",
                ]
            )

        lines.extend(
            [
                "        >>> {entity_lower}.validate()".format(
                    entity_lower=entity_name.lower().replace("tidas", "")
                ),
                '    """',
                "",
                "    def __init__(",
                "        self,",
                "        data: Optional[Dict[str, Any]] = None,",
                "        validation_config: Optional[ValidationConfig] = None,",
                "    ):",
                f"        \"\"\"Initialize {entity_name.replace('Tidas', '')} entity.",
                "",
                "        Args:",
                f"            data: {entity_name.replace('Tidas', '')} data as dictionary (TIDAS JSON format)",
                "            validation_config: Validation configuration. If None, uses global default.",
                '        """',
                "        super().__init__(data, validation_config)",
                f"        self._pydantic_model = {entity_name.replace('Tidas', '')}Model",
                "",
                "        # Initialize default structure if data is empty",
                "        if not self._data:",
                "            self._data = {",
                f'                "{dataset_name}": {{',
            ]
        )

        # Add basic structure based on entity type
        if schema_name == "tidas_processes":
            lines.extend(
                [
                    '                    "processInformation": {',
                    '                        "dataSetInformation": {}',
                    "                    },",
                    '                    "modellingAndValidation": {},',
                    '                    "administrativeInformation": {},',
                    '                    "exchanges": {}',
                    "                }",
                    "            }",
                ]
            )
        elif schema_name == "tadas_lciamethods":
            lines.extend(
                [
                    '                    "LCIAMethodInformation": {',
                    '                        "dataSetInformation": {}',
                    "                    },",
                    '                    "modellingAndValidation": {},',
                    '                    "administrativeInformation": {},',
                    '                    "characterisationFactors": {}',
                    "                }",
                    "            }",
                ]
            )
        elif schema_name == "tidas_lifecyclemodels":
            lines.extend(
                [
                    '                    "lifeCycleModelInformation": {',
                    '                        "dataSetInformation": {}',
                    "                    },",
                    '                    "modellingAndValidation": {},',
                    '                    "administrativeInformation": {}',
                    "                }",
                    "            }",
                ]
            )
        else:
            # Generic structure for other entities
            info_field = (
                schema_name.replace("tidas_", "").replace("_", "") + "Information"
            )
            lines.extend(
                [
                    f'                    "{info_field}": {{',
                    '                        "dataSetInformation": {}',
                    "                    },",
                    '                    "modellingAndValidation": {},',
                    '                    "administrativeInformation": {}',
                ]
            )

            # Add additional fields for specific entity types
            if schema_name == "tadas_unitgroups":
                lines.append('                    "units": {}')

            lines.extend(
                [
                    "                }",
                    "            }",
                ]
            )

        # Add initialize_defaults method
        lines.extend(
            [
                "",
                "    def initialize_defaults(self) -> None:",
                '        """Initialize default values and ensure required structure.',
                "",
                "        This method is called during initialization to set up",
                "        required namespace attributes and default field values.",
                '        """',
            ]
        )

        # Add namespace attributes
        for attr_name, attr_value in namespace_attrs.items():
            lines.extend(
                [
                    f'        self.set_nested_value("{dataset_name}.{attr_name}", "{attr_value}")',
                ]
            )

        # Add nested structure paths
        if nested_paths:
            lines.extend(
                [
                    "",
                    "        # Ensure required nested structure exists",
                    f"        self.ensure_nested_structure([",
                ]
            )

            for path in nested_paths:
                lines.append(f'            "{path}",')

            lines.extend(
                [
                    "        ])",
                ]
            )

        # Add default field values
        if default_values:
            lines.extend(
                [
                    "",
                    "        # Set required fields with default values if they don't exist",
                ]
            )

            for field_path, default_value in default_values.items():
                lines.extend(
                    [
                        f'        if not self.get_nested_value("{field_path}"):',
                        f'            self.set_nested_value("{field_path}", {default_value})',
                    ]
                )

        lines.extend(
            [
                "",
                f"    @property",
                f"    def {entity_name.replace('Tidas', '').lower()}_data_set(self) -> {entity_name.replace('Tidas', '')}DataSetWrapper:",
                f'        """Access {dataset_name} field with IDE autocomplete and type hints.',
                "",
                "        This property provides typed access to the dataset, enabling",
                "        IDE autocomplete for all nested fields.",
                "",
                "        Example:",
                f"            >>> {entity_name.lower().replace('tidas', '')} = {entity_name}()",
                "            >>> # IDE shows autocomplete as you type:",
            ]
        )

        # Add example based on entity type
        if schema_name == "tidas_processes":
            lines.extend(
                [
                    f'            >>> {entity_name.lower().replace("tidas", "")}.process_data_set.process_information.data_set_information.uuid = "..."',
                ]
            )
        else:
            lines.extend(
                [
                    f'            >>> {entity_name.lower().replace("tidas", "")}.{entity_name.replace("Tidas", "").lower()}_data_set.{entity_name.replace("Tidas", "").lower()}_information.data_set_information.uuid = "..."',
                ]
            )

        lines.extend(
            [
                '        """',
                f'        return self._get_typed_field("{dataset_name}", {entity_name.replace("Tidas", "")}DataSetWrapper)',
                "",
            ]
        )

        return "\n".join(lines)

    def generate_all_entity_models(self, output_dir: Path) -> None:
        """Generate entity model files for all entity types.

        Args:
            output_dir: Directory to write entity model files
        """
        output_dir.mkdir(parents=True, exist_ok=True)

        entities = [
            "contacts",
            "flows",
            "processes",
            "sources",
            "flowproperties",
            "unitgroups",
            "lciamethods",
            "lifecyclemodels",
        ]

        for entity in entities:
            schema_name = f"tidas_{entity}"
            logger.info(f"Generating entity model for {entity}...")
            try:
                code = self.generate_entity_model(schema_name)
                output_file = output_dir / f"{entity}.py"
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(code)
                logger.info(f"  ✓ Generated {output_file}")
            except Exception as e:
                logger.error(f"  ✗ Failed to generate {entity}: {e}")

        # Generate __init__.py
        init_file = output_dir / "__init__.py"
        with open(init_file, "w", encoding="utf-8") as f:
            f.write('"""Entity model classes for TIDAS SDK."""\n')
            f.write("from .contacts import TidasContacts\n")
            f.write("from .flows import TidasFlows\n")
            f.write("from .processes import TidasProcesses\n")
            f.write("from .sources import TidasSources\n")
            f.write("from .flowproperties import TidasFlowproperties\n")
            f.write("from .unitgroups import TidasUnitgroups\n")
            f.write("from .lciamethods import TidasLciamethods\n")
            f.write("from .lifecyclemodels import TidasLifecyclemodels\n")
            f.write("\n")
            f.write("__all__ = [\n")
            f.write("    'TidasContacts',\n")
            f.write("    'TidasFlows',\n")
            f.write("    'TidasProcesses',\n")
            f.write("    'TidasSources',\n")
            f.write("    'TidasFlowproperties',\n")
            f.write("    'TidasUnitgroups',\n")
            f.write("    'TidasLciamethods',\n")
            f.write("    'TidasLifecyclemodels',\n")
            f.write("]\n")
        logger.info(f"  ✓ Generated {init_file}")


def main() -> None:
    """Main entry point."""
    if len(sys.argv) > 1:
        output_dir = Path(sys.argv[1])
    else:
        # Default output directory
        script_dir = Path(__file__).parent
        output_dir = script_dir.parent / "src" / "tidas_sdk" / "models"

    logger.info("Starting entity model generation...")
    generator = EntityModelGenerator()
    generator.generate_all_entity_models(output_dir)
    logger.info("Entity model generation complete!")


if __name__ == "__main__":
    main()
