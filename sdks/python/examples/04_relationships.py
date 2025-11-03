"""
Entity Relationships Example: Building Connected LCA Data Structures

This example demonstrates:
1. How TIDAS entities reference each other
2. Building a Flow → FlowProperty → UnitGroup relationship chain
3. Creating a complete, self-contained LCA dataset
4. Referential integrity considerations

In LCA (Life Cycle Assessment), entities form a network of relationships:
- Processes reference Flows (inputs/outputs)
- Flows reference FlowProperties (how to quantify them)
- FlowProperties reference UnitGroups (measurement units)
- Processes reference Contacts (who created the data)
- Processes reference Sources (scientific publications)
"""

import json
from pathlib import Path

from tidas_sdk import (
    ValidationConfig,
    create_contact,
    create_flow,
    create_flow_property,
    create_unit_group,
)

# Use weak validation for this example to allow incomplete data
config = ValidationConfig(mode="weak")

print("=" * 60)
print("BUILDING AN LCA ENTITY RELATIONSHIP GRAPH")
print("=" * 60)

# ============================================================
# Step 1: Create Base Entities (Unit Group)
# ============================================================

print("\n📦 Step 1: Create Unit Group (Base of the chain)")
print("-" * 60)

# Unit groups define measurement units (kg, MJ, m³, etc.)
# This is the foundation - other entities build on top

unit_group = create_unit_group(validation_config=config)

# Access the internal data structure
ug_info = unit_group._data["unitGroupDataSet"]["unitGroupInformation"]["dataSetInformation"]

# Set basic information
ug_info["common:UUID"] = unit_group._data["unitGroupDataSet"]["unitGroupInformation"]["dataSetInformation"].get("common:UUID", "550e8400-e29b-41d4-a716-446655440001")
ug_info["common:name"] = [
    {"@xml:lang": "en", "#text": "Mass units"},
    {"@xml:lang": "de", "#text": "Masseneinheiten"}
]

# Define units in the group
unit_group._data["unitGroupDataSet"]["units"] = {
    "unit": [
        {
            "@dataSetInternalID": "0",
            "name": "kg",
            "meanValue": 1.0,  # Reference unit
            "common:generalComment": [
                {"@xml:lang": "en", "#text": "kilogram - SI base unit for mass"}
            ]
        },
        {
            "@dataSetInternalID": "1",
            "name": "g",
            "meanValue": 0.001,  # Relative to kg
            "common:generalComment": [
                {"@xml:lang": "en", "#text": "gram"}
            ]
        },
        {
            "@dataSetInternalID": "2",
            "name": "t",
            "meanValue": 1000.0,  # Relative to kg
            "common:generalComment": [
                {"@xml:lang": "en", "#text": "metric ton"}
            ]
        }
    ]
}

unit_group_uuid = ug_info["common:UUID"]
print(f"✓ Created UnitGroup: 'Mass units'")
print(f"  UUID: {unit_group_uuid}")
print(f"  Units: kg (reference), g, t")

# ============================================================
# Step 2: Create Flow Property (References Unit Group)
# ============================================================

print("\n📦 Step 2: Create Flow Property (References Unit Group)")
print("-" * 60)

# Flow properties define what aspect of a flow to measure
# (mass, energy content, volume, etc.)

flow_property = create_flow_property(validation_config=config)

fp_info = flow_property._data["flowPropertyDataSet"]["flowPropertiesInformation"]["dataSetInformation"]

# Set basic information
fp_info["common:UUID"] = "550e8400-e29b-41d4-a716-446655440002"
fp_info["common:name"] = [
    {"@xml:lang": "en", "#text": "Mass"},
    {"@xml:lang": "de", "#text": "Masse"}
]

# Reference the unit group we created
# This establishes the relationship: FlowProperty → UnitGroup
flow_property._data["flowPropertyDataSet"]["flowPropertiesInformation"]["quantitativeReference"] = {
    "referenceToReferenceUnitGroup": {
        "@type": "unit group data set",
        "@refObjectId": unit_group_uuid,
        "@version": "00.00.000",
        "@uri": "",
        "common:shortDescription": [
            {"@xml:lang": "en", "#text": "Mass units"}
        ]
    }
}

flow_property_uuid = fp_info["common:UUID"]
print(f"✓ Created FlowProperty: 'Mass'")
print(f"  UUID: {flow_property_uuid}")
print(f"  ➜ References UnitGroup: {unit_group_uuid}")

# ============================================================
# Step 3: Create Flow (References Flow Property)
# ============================================================

print("\n📦 Step 3: Create Flow (References Flow Property)")
print("-" * 60)

# Flows represent materials or energy in LCA
# (carbon dioxide, electricity, water, etc.)

flow = create_flow(validation_config=config)

flow_info = flow._data["flowDataSet"]["flowInformation"]["dataSetInformation"]

# Set basic information
flow_info["common:UUID"] = "550e8400-e29b-41d4-a716-446655440003"
flow_info["name"] = {
    "baseName": [
        {"@xml:lang": "en", "#text": "Carbon dioxide"},
        {"@xml:lang": "de", "#text": "Kohlendioxid"}
    ],
    "treatmentStandardsRoutes": [
        {"@xml:lang": "en", "#text": "Emission to air"}
    ]
}

# Reference the flow property
# This establishes the relationship: Flow → FlowProperty
flow._data["flowDataSet"]["flowProperties"] = {
    "flowProperty": [
        {
            "@dataSetInternalID": "0",
            "referenceToFlowPropertyDataSet": {
                "@type": "flow property data set",
                "@refObjectId": flow_property_uuid,
                "@version": "00.00.000",
                "@uri": "",
                "common:shortDescription": [
                    {"@xml:lang": "en", "#text": "Mass"}
                ]
            },
            "meanValue": 1.0  # This flow is quantified by mass
        }
    ]
}

flow_uuid = flow_info["common:UUID"]
print(f"✓ Created Flow: 'Carbon dioxide'")
print(f"  UUID: {flow_uuid}")
print(f"  ➜ References FlowProperty: {flow_property_uuid}")
print(f"    ➜ Which references UnitGroup: {unit_group_uuid}")

# ============================================================
# Step 4: Create Contact (Metadata Entity)
# ============================================================

print("\n📦 Step 4: Create Contact (For Process Attribution)")
print("-" * 60)

# Contacts represent people or organizations
# Processes reference contacts to indicate who created the data

contact = create_contact(validation_config=config)

contact_info = contact._data["contactDataSet"]["contactInformation"]["dataSetInformation"]

contact_info["common:UUID"] = "550e8400-e29b-41d4-a716-446655440004"
contact_info["common:name"] = [
    {"@xml:lang": "en", "#text": "Dr. Jane Smith - LCA Research Group"}
]
contact_info["email"] = "jane.smith@lca-research.org"
contact_info["WWWAddress"] = "https://lca-research.org"

contact_uuid = contact_info["common:UUID"]
print(f"✓ Created Contact: 'Dr. Jane Smith'")
print(f"  UUID: {contact_uuid}")

# ============================================================
# Relationship Summary
# ============================================================

print("\n" + "=" * 60)
print("RELATIONSHIP GRAPH")
print("=" * 60)

print("""
Created Entity Relationship Chain:

┌────────────────────────────────────────────────────────────┐
│                      UnitGroup                             │
│                    "Mass units"                            │
│                   (kg, g, t)                               │
└────────────────────────────────────────────────────────────┘
                        ▲
                        │ references
                        │
┌────────────────────────────────────────────────────────────┐
│                    FlowProperty                            │
│                       "Mass"                               │
│            (how to quantify flows)                         │
└────────────────────────────────────────────────────────────┘
                        ▲
                        │ references
                        │
┌────────────────────────────────────────────────────────────┐
│                       Flow                                 │
│                "Carbon dioxide"                            │
│            (environmental emission)                        │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│                     Contact                                │
│               "Dr. Jane Smith"                             │
│           (data author/owner)                              │
└────────────────────────────────────────────────────────────┘
""")

print("Key Relationships in TIDAS/ILCD:")
print("  • Flow → FlowProperty: How to quantify this flow")
print("  • FlowProperty → UnitGroup: What units to use")
print("  • Process → Flow: What materials/energy are exchanged")
print("  • Process → Contact: Who created this data")
print("  • Process → Source: Scientific reference")

# ============================================================
# Export Complete Dataset
# ============================================================

print("\n" + "=" * 60)
print("EXPORTING COMPLETE DATASET")
print("=" * 60)

output_dir = Path(__file__).parent / "output"
output_dir.mkdir(exist_ok=True)

# Export as a complete dataset with all related entities
complete_dataset = {
    "metadata": {
        "description": "Complete LCA entity relationship example",
        "created": "2025-11-03",
        "entities": 4
    },
    "unitGroups": [unit_group.to_json()],
    "flowProperties": [flow_property.to_json()],
    "flows": [flow.to_json()],
    "contacts": [contact.to_json()]
}

output_file = output_dir / "relationship_graph.json"
output_file.write_text(json.dumps(complete_dataset, indent=2))

print(f"\n✓ Exported complete dataset:")
print(f"  File: {output_file}")
print(f"  Size: {output_file.stat().st_size / 1024:.1f} KB")
print(f"  Entities:")
print(f"    • 1 UnitGroup")
print(f"    • 1 FlowProperty")
print(f"    • 1 Flow")
print(f"    • 1 Contact")

# ============================================================
# Referential Integrity Notes
# ============================================================

print("\n" + "=" * 60)
print("REFERENTIAL INTEGRITY CONSIDERATIONS")
print("=" * 60)

print("""
⚠️  Important Notes:

1. UUID MANAGEMENT:
   • Each entity must have a unique UUID
   • Referenced UUIDs must match exactly
   • SDK auto-generates UUIDs, but you can override

2. REFERENCE FORMAT:
   • References use @refObjectId for the UUID
   • Include @type to specify entity type
   • @version and @uri are optional but recommended

3. VALIDATION:
   • SDK does NOT enforce referential integrity
   • You can reference UUIDs that don't exist
   • External tools needed for full validation

4. EXPORT ORDER:
   • Export entities in dependency order for imports:
     1. UnitGroups (no dependencies)
     2. FlowProperties (depend on UnitGroups)
     3. Flows (depend on FlowProperties)
     4. Processes (depend on Flows, Contacts, Sources)

5. BEST PRACTICES:
   • Keep related entities together in files
   • Document relationships in metadata
   • Validate references before export
   • Use consistent UUID format (v4 recommended)
""")

# ============================================================
# Practical Example: Using Relationships
# ============================================================

print("\n" + "=" * 60)
print("PRACTICAL USAGE EXAMPLE")
print("=" * 60)

print("""
In a real LCA workflow, you would:

1. DEFINE BASE DATA (once per database):
   • Create standard unit groups (mass, energy, volume)
   • Create standard flow properties
   • Store their UUIDs for reuse

2. CREATE FLOWS (as needed):
   • Reference appropriate flow properties
   • Each flow can have multiple properties
   • Example: Natural gas has mass, energy, and volume

3. CREATE PROCESSES (the actual LCA data):
   • Reference flows for inputs/outputs
   • Reference contacts for data quality
   • Reference sources for scientific backing

4. BUILD COMPLETE SYSTEMS:
   • Link processes through flows
   • Example: Electricity→Steel→Car→Driving
   • Calculate impacts using LCIA methods

Example process exchange (pseudocode):
  process.exchanges.add({
    flow: CO2_flow_uuid,
    amount: 1.5,
    flowProperty: mass_property_uuid,
    unit: "kg"
  })
""")

print("\n✅ Example Complete!")
print("\nYou've learned:")
print("  • How to create entity relationships")
print("  • Reference format and structure")
print("  • Dependency ordering")
print("  • Export strategies")

print("\nNext Steps:")
print("  • Build more complex graphs with Processes")
print("  • Add Sources for scientific references")
print("  • Create LCIA Methods for impact assessment")
print("  • Export complete LCA databases")
