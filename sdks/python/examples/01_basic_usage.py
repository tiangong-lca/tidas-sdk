"""
Basic Usage Example: Creating and Validating a TIDAS Contact Entity

This example demonstrates:
1. Creating a Contact entity with the factory function
2. Setting multi-language text fields
3. Validating the entity in strict mode
4. Exporting to JSON format

TIDAS (Tiangong LCA Data Access System) is a data format for Life Cycle Assessment (LCA)
based on the ILCD (International Life Cycle Data) standard. A Contact entity represents
a person or organization involved in LCA data creation or management.
"""

import json
from pathlib import Path

from tidas_sdk import ValidationError, create_contact

# ============================================================
# Step 1: Create a Contact Entity
# ============================================================

# The create_contact() factory function creates a new Contact entity with a
# pre-generated UUID and minimal structure. You can also pass existing data
# as a dictionary to initialize from JSON.
contact = create_contact()

print("✓ Created empty Contact entity")

# Access the internal data structure
# Note: In production code, you would access this through the to_json() method
# or work with the data dictionary before creating the entity
data = contact.to_json()
print(f"  UUID: {data['contactDataSet']['contactInformation']['dataSetInformation']['common:UUID']}")

# ============================================================
# Step 2: Set Basic Information
# ============================================================

# Access the nested structure using dictionary-style access on the internal data
# In TIDAS/ILCD format, data is deeply nested following the XML schema
# For modification, we access the internal _data attribute (note: this is implementation detail)
contact_info = contact._data["contactDataSet"]["contactInformation"]["dataSetInformation"]

# Set the full name - note the 'common:' prefix which indicates it's from the
# common namespace in ILCD
contact_info["common:name"] = [
    {"@xml:lang": "en", "#text": "Dr. Jane Smith"}
]

# Set a short name for abbreviated references
contact_info["common:shortName"] = [
    {"@xml:lang": "en", "#text": "J. Smith"}
]

# Set contact details
contact_info["email"] = "jane.smith@example.com"
contact_info["WWWAddress"] = "https://example.com/staff/jane-smith"

print("\n✓ Set contact information:")
print(f"  Name: {contact_info['common:name'][0]['#text']}")
print(f"  Email: {contact_info['email']}")

# ============================================================
# Step 3: Add Multi-Language Support
# ============================================================

# TIDAS supports multi-language text fields for internationalization
# Each language has its own entry with an @xml:lang attribute

# Add French translation
contact_info["common:name"].append(
    {"@xml:lang": "fr", "#text": "Dr. Jane Smith"}
)

# Add German translation
contact_info["common:name"].append(
    {"@xml:lang": "de", "#text": "Dr. Jane Schmidt"}
)

print("\n✓ Added multi-language support:")
for name_entry in contact_info["common:name"]:
    print(f"  [{name_entry['@xml:lang']}] {name_entry['#text']}")

# ============================================================
# Step 4: Validation (will fail on incomplete data)
# ============================================================

# The SDK supports three validation modes:
# - strict (default): Raises ValidationError on any schema violation
# - weak: Collects violations as warnings without raising
# - ignore: Skips validation entirely for performance

print("\n📋 Attempting strict validation...")

try:
    contact.validate()
    print("✓ Validation passed!")

except ValidationError as e:
    # Expected to fail because we haven't set all required fields
    print(f"⚠ Validation failed (expected for incomplete data):")
    print(f"  Field: {e.field_path}")
    print(f"  Issue: {e.expected}")
    print("\nThis is normal - the Contact needs additional required fields")
    print("such as @xmlns namespace declarations and classification information.")

# ============================================================
# Step 5: Export to JSON
# ============================================================

# Even without full validation, you can export the data structure
# This is useful during data entry and iterative data quality improvement

# Export as formatted JSON string
json_string = contact.to_json_string(indent=2)

print("\n✓ Exported to JSON format:")
print(f"  Length: {len(json_string)} characters")
print("\nFirst 20 lines of JSON:")
print("---")
for i, line in enumerate(json_string.split("\n")[:20], 1):
    print(f"{i:3d}  {line}")
print("  ...")

# ============================================================
# Step 6: Save to File
# ============================================================

# Save the JSON to a file
output_dir = Path(__file__).parent / "output"
output_dir.mkdir(exist_ok=True)

output_file = output_dir / "contact.json"
output_file.write_text(json_string)

print(f"\n✓ Saved to file: {output_file}")
print(f"  Size: {output_file.stat().st_size} bytes")

# ============================================================
# Step 7: Load from File (Round-Trip)
# ============================================================

# Demonstrate loading the data back from JSON
loaded_data = json.loads(output_file.read_text())
loaded_contact = create_contact(loaded_data)

print("\n✓ Loaded contact from JSON file")
loaded_data_check = loaded_contact.to_json()
print(f"  Name: {loaded_data_check['contactDataSet']['contactInformation']['dataSetInformation']['common:name'][0]['#text']}")
print(f"  Email: {loaded_data_check['contactDataSet']['contactInformation']['dataSetInformation']['email']}")

# Verify round-trip preserves data
assert loaded_contact.to_json() == contact.to_json(), "Round-trip data mismatch!"
print("✓ Round-trip verification passed")

# ============================================================
# Summary
# ============================================================

print("\n" + "=" * 60)
print("EXAMPLE COMPLETE")
print("=" * 60)
print("\nKey Takeaways:")
print("1. Use create_contact() to create Contact entities")
print("2. Access nested fields using dictionary-style syntax")
print("3. Multi-language fields use @xml:lang and #text")
print("4. Validation enforces TIDAS/ILCD schema constraints")
print("5. Export to JSON with to_json_string()")
print("6. JSON round-trip preserves all data")
print("\nNext Steps:")
print("- See 02_batch_operations.py for bulk processing")
print("- See 03_validation_modes.py for validation strategies")
print("- See 04_relationships.py for entity relationships")
