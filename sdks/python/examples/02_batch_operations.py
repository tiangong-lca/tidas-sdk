"""
Batch Operations Example: High-Performance Bulk Data Processing

This example demonstrates:
1. Creating 1000+ entities efficiently using batch functions
2. Performance optimization with validation modes
3. Bulk JSON export strategies
4. Collecting and analyzing validation warnings

Use Case: LCA researchers often need to process large datasets imported from
external sources (databases, Excel files, etc.). This example shows how to
efficiently clean and validate bulk data while maintaining performance.
"""

import json
import time
from pathlib import Path

from tidas_sdk import (
    ValidationConfig,
    create_contacts_batch,
    create_flows_batch,
)

# ============================================================
# Performance Pattern 1: Fast Creation with Validation Disabled
# ============================================================

print("=" * 60)
print("PATTERN 1: Fast Bulk Creation (Ignore Mode)")
print("=" * 60)

# When importing large datasets, you often want to create entities first
# and validate later. Use "ignore" mode for maximum performance.

# Prepare sample data (simulating data from an external source)
contact_data_list = [
    {
        "contactDataSet": {
            "contactInformation": {
                "dataSetInformation": {
                    "common:name": [{"@xml:lang": "en", "#text": f"Contact {i}"}],
                    "email": f"contact{i}@example.com",
                }
            }
        }
    }
    for i in range(1000)
]

# Create entities with validation disabled for speed
config_ignore = ValidationConfig(mode="ignore")

start_time = time.perf_counter()
contacts = create_contacts_batch(contact_data_list, validation_config=config_ignore)
duration = time.perf_counter() - start_time

print(f"\n✓ Created {len(contacts)} contacts in {duration:.3f} seconds")
print(f"  Performance: {len(contacts)/duration:.0f} entities/second")
print(f"  Average: {duration/len(contacts)*1000:.2f} ms per entity")

# Performance Target: Should complete in <1 second for 1000 entities
if duration < 1.0:
    print(f"  ✅ Performance target met (<1 second)")
else:
    print(f"  ⚠️  Performance target missed (took {duration:.2f}s)")

# ============================================================
# Performance Pattern 2: Validation After Creation (Weak Mode)
# ============================================================

print("\n" + "=" * 60)
print("PATTERN 2: Validation with Warning Collection (Weak Mode)")
print("=" * 60)

# After fast creation, validate entities in "weak" mode to collect issues
# without stopping the process. This allows you to identify all problems
# in one pass rather than fixing them one at a time.

# Recreate with weak validation to collect warnings
config_weak = ValidationConfig(mode="weak")
contacts_weak = create_contacts_batch(contact_data_list[:100], validation_config=config_weak)

print(f"\n✓ Created {len(contacts_weak)} contacts with weak validation")

# Validate all and collect warnings
all_warnings = []
for i, contact in enumerate(contacts_weak):
    contact.validate()
    warnings = contact.get_validation_warnings()
    if warnings:
        all_warnings.append((i, warnings))

print(f"  Found validation issues in {len(all_warnings)} contacts")

# Show sample warnings
if all_warnings:
    print("\n  Sample warnings (first 3):")
    for idx, (contact_idx, warnings) in enumerate(all_warnings[:3]):
        print(f"\n  Contact #{contact_idx}:")
        for warning in warnings[:2]:  # Show first 2 warnings per contact
            print(f"    - {warning.field_path[:50]}...")
            print(f"      {warning.message[:60]}...")

# ============================================================
# Performance Pattern 3: Selective Strict Validation
# ============================================================

print("\n" + "=" * 60)
print("PATTERN 3: Selective Strict Validation for Critical Data")
print("=" * 60)

# For production data entry, use strict validation on individual entities
# to catch errors immediately. Reserve batch operations for bulk imports.

print("\nCreating 10 entities with strict validation...")
config_strict = ValidationConfig(mode="strict")

strict_contacts = []
failed_count = 0

for i in range(10):
    try:
        contact = create_contacts_batch(
            [contact_data_list[i]],
            validation_config=config_strict
        )[0]
        contact.validate()
        strict_contacts.append(contact)
    except Exception as e:
        failed_count += 1
        if failed_count <= 3:  # Show first 3 errors
            print(f"  ⚠️  Contact {i} validation failed: {str(e)[:60]}...")

print(f"\n✓ Successfully validated: {len(strict_contacts)} contacts")
print(f"  Failed validation: {failed_count} contacts")

# ============================================================
# Performance Pattern 4: Bulk JSON Export
# ============================================================

print("\n" + "=" * 60)
print("PATTERN 4: Efficient Bulk JSON Export")
print("=" * 60)

# When exporting large datasets, use batch operations to minimize overhead

output_dir = Path(__file__).parent / "output"
output_dir.mkdir(exist_ok=True)

# Export all contacts to a single JSON array file
start_time = time.perf_counter()
all_contact_data = [contact.to_json() for contact in contacts[:100]]
export_duration = time.perf_counter() - start_time

output_file = output_dir / "contacts_batch.json"
output_file.write_text(json.dumps(all_contact_data, indent=2))

print(f"\n✓ Exported {len(all_contact_data)} contacts in {export_duration:.3f} seconds")
print(f"  File: {output_file}")
print(f"  Size: {output_file.stat().st_size / 1024:.1f} KB")
print(f"  Performance: {len(all_contact_data)/export_duration:.0f} entities/second")

# ============================================================
# Performance Pattern 5: Mixed Entity Types
# ============================================================

print("\n" + "=" * 60)
print("PATTERN 5: Processing Multiple Entity Types")
print("=" * 60)

# Real LCA workflows often involve multiple entity types (flows, processes, etc.)
# Process them in batch for efficiency.

# Create flows
flow_data_list = [
    {
        "flowDataSet": {
            "flowInformation": {
                "dataSetInformation": {
                    "name": {
                        "baseName": [{"@xml:lang": "en", "#text": f"Flow {i}"}]
                    }
                }
            }
        }
    }
    for i in range(500)
]

start_time = time.perf_counter()
flows = create_flows_batch(flow_data_list, validation_config=config_ignore)
flow_duration = time.perf_counter() - start_time

print(f"\n✓ Created {len(flows)} flows in {flow_duration:.3f} seconds")
print(f"  Performance: {len(flows)/flow_duration:.0f} flows/second")

# Combined export
combined_data = {
    "contacts": [c.to_json() for c in contacts[:50]],
    "flows": [f.to_json() for f in flows[:50]]
}

combined_file = output_dir / "mixed_entities_batch.json"
combined_file.write_text(json.dumps(combined_data, indent=2))

print(f"\n✓ Exported mixed dataset:")
print(f"  Contacts: {len(combined_data['contacts'])}")
print(f"  Flows: {len(combined_data['flows'])}")
print(f"  File: {combined_file}")
print(f"  Size: {combined_file.stat().st_size / 1024:.1f} KB")

# ============================================================
# Summary and Best Practices
# ============================================================

print("\n" + "=" * 60)
print("BATCH OPERATIONS COMPLETE")
print("=" * 60)

print("\n📊 Performance Summary:")
print(f"  • 1000 contacts created in {duration:.3f}s ({len(contacts)/duration:.0f} entities/s)")
print(f"  • 500 flows created in {flow_duration:.3f}s ({len(flows)/flow_duration:.0f} entities/s)")
print(f"  • Validation warnings collected from 100 entities")
print(f"  • Batch export completed successfully")

print("\n💡 Best Practices for Batch Operations:")
print("\n  1. IMPORT PHASE (Use 'ignore' mode):")
print("     - Create all entities quickly without validation")
print("     - Target: >1000 entities/second")
print("     - Use: create_*_batch() functions")

print("\n  2. VALIDATION PHASE (Use 'weak' mode):")
print("     - Validate all entities, collect all warnings")
print("     - Identify patterns in data quality issues")
print("     - Fix issues in source data, then re-import")

print("\n  3. CLEANUP PHASE (Use 'strict' mode):")
print("     - After fixing source data, re-import with strict validation")
print("     - Ensures only valid data enters production")

print("\n  4. EXPORT PHASE:")
print("     - Use list comprehension for bulk to_json()")
print("     - Write to single file for related entities")
print("     - Consider chunking for very large datasets (>10,000 entities)")

print("\n  5. MEMORY MANAGEMENT:")
print("     - For datasets >100,000 entities, process in chunks")
print("     - Release memory between chunks")
print("     - Consider streaming JSON output")

print("\n📁 Output Files:")
print(f"  • {output_file.name} ({len(all_contact_data)} contacts)")
print(f"  • {combined_file.name} (mixed entities)")

print("\nNext Steps:")
print("  • See 03_validation_modes.py for detailed validation strategies")
print("  • See 04_relationships.py for entity relationships")
