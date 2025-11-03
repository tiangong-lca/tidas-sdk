"""
Validation Modes Example: Understanding Strict, Weak, and Ignore Modes

This example demonstrates:
1. How each validation mode behaves
2. When to use each mode
3. Trade-offs between data quality and performance
4. Validation warning collection and analysis

The TIDAS SDK provides three validation modes to balance data quality with performance:
- STRICT: Enforce schema compliance (raise errors)
- WEAK: Collect violations as warnings (continue processing)
- IGNORE: Skip validation (maximum performance)
"""

from tidas_sdk import ValidationConfig, ValidationError, create_contact, set_global_validation_mode

# ============================================================
# Mode 1: STRICT Validation (Default)
# ============================================================

print("=" * 60)
print("MODE 1: STRICT VALIDATION (Default)")
print("=" * 60)

print("\nUse Case: Production data entry, API endpoints, critical workflows")
print("Behavior: Raises ValidationError immediately on any schema violation\n")

# Create contact with default strict mode
contact_strict = create_contact()

# Add some data (incomplete)
contact_strict._data["contactDataSet"]["contactInformation"]["dataSetInformation"]["common:name"] = [
    {"@xml:lang": "en", "#text": "Dr. Alice Chen"}
]
contact_strict._data["contactDataSet"]["contactInformation"]["dataSetInformation"]["email"] = "alice@example.com"

print("Attempting validation with incomplete data...")

try:
    contact_strict.validate()
    print("✓ Validation passed")
except ValidationError as e:
    print(f"✗ ValidationError raised (as expected):")
    print(f"  Field: {e.field_path}")
    print(f"  Issue: {e.expected}")
    print(f"  Type: {e.constraint_type}")
    print("\n  → Strict mode stops immediately at first error")
    print("  → Good for: preventing invalid data from entering system")
    print("  → Bad for: bulk imports where you want to see all errors")

# ============================================================
# Mode 2: WEAK Validation
# ============================================================

print("\n" + "=" * 60)
print("MODE 2: WEAK VALIDATION")
print("=" * 60)

print("\nUse Case: ETL pipelines, data migration, iterative data cleanup")
print("Behavior: Collects all violations as warnings, never raises errors\n")

# Create contact with weak validation
config_weak = ValidationConfig(mode="weak")
contact_weak = create_contact(validation_config=config_weak)

# Add the same incomplete data
contact_weak._data["contactDataSet"]["contactInformation"]["dataSetInformation"]["common:name"] = [
    {"@xml:lang": "en", "#text": "Dr. Bob Smith"}
]
contact_weak._data["contactDataSet"]["contactInformation"]["dataSetInformation"]["email"] = "bob@example.com"

# Add some invalid data too
contact_weak._data["contactDataSet"]["contactInformation"]["dataSetInformation"]["common:UUID"] = "invalid-uuid-format"

print("Attempting validation with incomplete AND invalid data...")

try:
    contact_weak.validate()
    print("✓ Validation completed (no exception raised)")

    # Collect warnings
    warnings = contact_weak.get_validation_warnings()
    print(f"\n  Found {len(warnings)} validation warnings:")

    for i, warning in enumerate(warnings[:5], 1):  # Show first 5
        print(f"\n  Warning #{i}:")
        print(f"    Field: {warning.field_path}")
        print(f"    Message: {warning.message}")
        print(f"    Expected: {warning.expected}")

    if len(warnings) > 5:
        print(f"\n  ... and {len(warnings) - 5} more warnings")

    print("\n  → Weak mode collects ALL errors in one pass")
    print("  → Good for: seeing all data quality issues at once")
    print("  → Bad for: when you must guarantee data quality")

except ValidationError:
    print("✗ Unexpected: Weak mode should not raise errors!")

# ============================================================
# Mode 3: IGNORE Validation
# ============================================================

print("\n" + "=" * 60)
print("MODE 3: IGNORE VALIDATION")
print("=" * 60)

print("\nUse Case: Bulk operations, trusted data sources, performance-critical paths")
print("Behavior: Skips all validation, maximum performance\n")

# Create contact with ignore mode
config_ignore = ValidationConfig(mode="ignore")
contact_ignore = create_contact(validation_config=config_ignore)

# Add completely invalid data (would normally fail)
contact_ignore._data["contactDataSet"]["contactInformation"]["dataSetInformation"]["common:name"] = "Not even an array!"
contact_ignore._data["contactDataSet"]["contactInformation"]["dataSetInformation"]["email"] = 12345  # Wrong type!
contact_ignore._data["invalid_field"] = "Should not exist"

print("Attempting validation with completely invalid data...")

contact_ignore.validate()
warnings = contact_ignore.get_validation_warnings()

print("✓ Validation completed (skipped)")
print(f"  Warnings collected: {len(warnings)}")
print("\n  → Ignore mode is a complete no-op")
print("  → Good for: maximum performance when data is trusted")
print("  → Bad for: any scenario requiring data quality assurance")

# ============================================================
# Comparison: Performance Impact
# ============================================================

print("\n" + "=" * 60)
print("PERFORMANCE COMPARISON")
print("=" * 60)

import time

# Sample data
sample_data = {
    "contactDataSet": {
        "contactInformation": {
            "dataSetInformation": {
                "common:name": [{"@xml:lang": "en", "#text": "Test Contact"}],
                "email": "test@example.com"
            }
        }
    }
}

iterations = 1000

# Test ignore mode
start = time.perf_counter()
for _ in range(iterations):
    c = create_contact(sample_data, ValidationConfig(mode="ignore"))
    c.validate()
ignore_time = time.perf_counter() - start

# Test weak mode
start = time.perf_counter()
for _ in range(iterations):
    c = create_contact(sample_data, ValidationConfig(mode="weak"))
    c.validate()
weak_time = time.perf_counter() - start

# Test strict mode (will fail, so just measure one)
start = time.perf_counter()
c = create_contact(sample_data, ValidationConfig(mode="strict"))
try:
    c.validate()
except ValidationError:
    pass
strict_time = (time.perf_counter() - start) * iterations  # Extrapolate

print(f"\nValidating {iterations} entities:")
print(f"  Ignore mode: {ignore_time:.3f}s ({iterations/ignore_time:.0f} entities/s)")
print(f"  Weak mode:   {weak_time:.3f}s ({iterations/weak_time:.0f} entities/s)")
print(f"  Strict mode: {strict_time:.3f}s (estimated)")

print(f"\n  Speedup (ignore vs weak): {weak_time/ignore_time:.1f}x faster")

# ============================================================
# Mode Switching During Runtime
# ============================================================

print("\n" + "=" * 60)
print("RUNTIME MODE SWITCHING")
print("=" * 60)

# You can change validation mode for an entity after creation
contact_switch = create_contact()
contact_switch._data["contactDataSet"]["contactInformation"]["dataSetInformation"]["common:name"] = [
    {"@xml:lang": "en", "#text": "Mode Switcher"}
]

print("\n1. Start with strict mode (default):")
print(f"   Current mode: {contact_switch.get_validation_config().mode}")

print("\n2. Switch to weak mode for bulk processing:")
contact_switch.set_validation_mode("weak")
print(f"   Current mode: {contact_switch.get_validation_config().mode}")
contact_switch.validate()
print(f"   Warnings: {len(contact_switch.get_validation_warnings())}")

print("\n3. Switch to ignore mode for export:")
contact_switch.set_validation_mode("ignore")
print(f"   Current mode: {contact_switch.get_validation_config().mode}")
contact_switch.validate()
json_output = contact_switch.to_json_string()
print(f"   Exported: {len(json_output)} characters")

# ============================================================
# Global Mode Configuration
# ============================================================

print("\n" + "=" * 60)
print("GLOBAL MODE CONFIGURATION")
print("=" * 60)

print("\nSetting global validation mode affects all new entities:")

# Set global mode
set_global_validation_mode("weak")
print(f"\n1. Set global mode to: weak")

# Create new entities - they inherit global mode
contact1 = create_contact()
contact2 = create_contact()

print(f"   Entity 1 mode: {contact1.get_validation_config().mode}")
print(f"   Entity 2 mode: {contact2.get_validation_config().mode}")

# But you can still override per entity
contact3 = create_contact(validation_config=ValidationConfig(mode="strict"))
print(f"   Entity 3 mode (overridden): {contact3.get_validation_config().mode}")

# Reset global mode
set_global_validation_mode("strict")
print(f"\n2. Reset global mode to: strict")

# ============================================================
# Decision Guide
# ============================================================

print("\n" + "=" * 60)
print("VALIDATION MODE DECISION GUIDE")
print("=" * 60)

print("""
📋 When to use each mode:

┌─────────────────────────────────────────────────────────────┐
│ STRICT MODE (default)                                       │
├─────────────────────────────────────────────────────────────┤
│ ✓ Production data entry                                     │
│ ✓ API endpoints receiving external data                     │
│ ✓ Critical workflows requiring data quality                 │
│ ✓ When you want to fail fast on invalid data                │
│ ✗ Bulk imports (too slow, stops at first error)             │
│ ✗ Data exploration (too restrictive)                        │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ WEAK MODE                                                    │
├─────────────────────────────────────────────────────────────┤
│ ✓ ETL pipelines processing untrusted data                   │
│ ✓ Data migration from legacy systems                        │
│ ✓ Data quality analysis (find all issues at once)           │
│ ✓ Iterative data cleanup workflows                          │
│ ✗ Production systems (allows invalid data through)          │
│ ✗ Performance-critical paths (validation overhead)          │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ IGNORE MODE                                                  │
├─────────────────────────────────────────────────────────────┤
│ ✓ Bulk operations on trusted data                           │
│ ✓ Performance-critical code paths                           │
│ ✓ Data from validated sources (e.g., previous exports)      │
│ ✓ Initial import for speed (validate separately)            │
│ ✗ Any untrusted data source                                 │
│ ✗ When data quality is unknown                              │
└─────────────────────────────────────────────────────────────┘

🔄 Recommended Workflow for Large Datasets:

  1. IMPORT with ignore mode (fast)
     → Create all entities quickly

  2. VALIDATE with weak mode (comprehensive)
     → Collect all data quality issues
     → Analyze patterns, fix source data

  3. RE-IMPORT with strict mode (quality gate)
     → Ensure only valid data enters production
     → Fail fast on any remaining issues

  4. EXPORT with ignore mode (fast)
     → Export validated data efficiently
""")

print("\nFor more examples:")
print("  • See 01_basic_usage.py for basic validation")
print("  • See 02_batch_operations.py for performance optimization")
print("  • See 04_relationships.py for entity relationships")
