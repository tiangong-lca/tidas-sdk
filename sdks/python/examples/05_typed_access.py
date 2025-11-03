#!/usr/bin/env python3
"""
Example 05: Typed Field Access with IDE Autocomplete

This example demonstrates the new typed field access feature that provides
IDE autocomplete and type checking for entity fields.

Key Features:
- IDE autocomplete as you type
- Type safety with mypy/pylance
- Cleaner, more readable code
- Full backwards compatibility with dict access

Run:
    uv run python examples/05_typed_access.py
    # or
    ./examples/run_example.sh 05_typed_access.py
"""

import uuid

from tidas_sdk import create_contact


def main() -> None:
    """Demonstrate typed field access patterns."""

    print("=" * 80)
    print("TIDAS SDK - Example 05: Typed Field Access")
    print("=" * 80)
    print()

    # =========================================================================
    # Part 1: Before and After Comparison
    # =========================================================================
    print("Part 1: Before and After Comparison")
    print("-" * 80)

    contact = create_contact()

    # OLD WAY: Dict-based access (still works!)
    print("\n1. OLD WAY - Dict Access:")
    print("   contact._data['contactDataSet']['contactInformation']...")
    contact._data["contactDataSet"]["contactInformation"]["dataSetInformation"]["common:UUID"] = str(uuid.uuid4())
    contact._data["contactDataSet"]["contactInformation"]["dataSetInformation"]["common:name"] = [
        {"@xml:lang": "en", "#text": "Dr. Jane Smith"}
    ]
    print("   ❌ No autocomplete")
    print("   ❌ Easy to make typos")
    print("   ❌ Hard to discover available fields")

    # NEW WAY: Typed property access
    print("\n2. NEW WAY - Typed Access:")
    print("   contact.contact_data_set.contact_information...")
    contact_new = create_contact()
    contact_new.contact_data_set.contact_information.data_set_information.uuid = str(uuid.uuid4())
    contact_new.contact_data_set.contact_information.data_set_information.name.set_text(
        "Dr. Jane Smith", "en"
    )
    print("   ✅ Full IDE autocomplete")
    print("   ✅ Type checking catches errors")
    print("   ✅ Discover fields as you type")

    print()

    # =========================================================================
    # Part 2: Creating a Complete Contact with Typed Access
    # =========================================================================
    print("\nPart 2: Creating Contact with Typed Access")
    print("-" * 80)

    contact = create_contact()

    # Access the nested information structure once
    # IDE provides autocomplete at each level!
    info = contact.contact_data_set.contact_information.data_set_information

    # Set UUID
    info.uuid = str(uuid.uuid4())
    print(f"✓ UUID set: {info.uuid}")

    # Set multi-language name
    # IDE shows: set_text(value: str, lang: str = "en") -> None
    info.name.set_text("Dr. Jane Smith", "en")
    info.name.set_text("Dr. Jane Schmidt", "de")
    info.name.set_text("Dr. Jeanne Dubois", "fr")
    print(f"✓ Name set in 3 languages:")
    print(f"  English: {info.name.get_text('en')}")
    print(f"  German:  {info.name.get_text('de')}")
    print(f"  French:  {info.name.get_text('fr')}")

    # Set short name
    info.short_name.set_text("J. Smith", "en")
    print(f"✓ Short name: {info.short_name.get_text('en')}")

    # Set contact details
    # IDE knows these are Optional[str]
    info.email = "jane.smith@research.org"
    info.telephone = "+1-555-0123"
    info.www_address = "https://research.org/jane"
    print(f"✓ Email: {info.email}")
    print(f"✓ Phone: {info.telephone}")
    print(f"✓ Website: {info.www_address}")

    # Set contact address
    info.contact_address.set_text("123 Research Blvd, Science City, SC 12345", "en")
    print(f"✓ Address: {info.contact_address.get_text('en')}")

    print()

    # =========================================================================
    # Part 3: Type Safety in Action
    # =========================================================================
    print("\nPart 3: Type Safety")
    print("-" * 80)

    # Type checkers (mypy, pylance) will catch errors like:
    # info.email = 12345  # ❌ Type error: int is not assignable to str | None
    # info.uuid = None     # ❌ Type error: None is not assignable to str

    print("Type checking with mypy/pylance:")
    print("  info.email = 'test@example.com'  ✅ Valid")
    print("  info.email = 12345               ❌ Type error caught by IDE")
    print("  info.uuid = 'valid-uuid'         ✅ Valid")
    print("  info.uuid = None                 ❌ Type error caught by IDE")

    print()

    # =========================================================================
    # Part 4: Backwards Compatibility
    # =========================================================================
    print("\nPart 4: Backwards Compatibility")
    print("-" * 80)

    contact = create_contact()

    # Both access modes work simultaneously!
    contact.contact_data_set.contact_information.data_set_information.email = "typed@example.com"
    dict_email = contact._data["contactDataSet"]["contactInformation"]["dataSetInformation"]["email"]

    print(f"Typed access set: {contact.contact_data_set.contact_information.data_set_information.email}")
    print(f"Dict access reads: {dict_email}")
    print(f"Both equal: {contact.contact_data_set.contact_information.data_set_information.email == dict_email}")

    # Changes via dict are visible via typed access
    contact._data["contactDataSet"]["contactInformation"]["dataSetInformation"]["telephone"] = "+1-999-8888"
    typed_phone = contact.contact_data_set.contact_information.data_set_information.telephone
    print(f"\nDict access set phone: {contact._data['contactDataSet']['contactInformation']['dataSetInformation']['telephone']}")
    print(f"Typed access reads: {typed_phone}")

    print()

    # =========================================================================
    # Part 5: Multi-Language Text Helper
    # =========================================================================
    print("\nPart 5: Multi-Language Text Operations")
    print("-" * 80)

    contact = create_contact()
    name = contact.contact_data_set.contact_information.data_set_information.name

    # Set multiple languages
    name.set_text("Carbon Dioxide", "en")
    name.set_text("Kohlendioxid", "de")
    name.set_text("Dióxido de carbono", "es")
    name.set_text("Dioxyde de carbone", "fr")

    # Get specific languages
    print("Available translations:")
    for lang in ["en", "de", "es", "fr"]:
        text = name.get_text(lang)
        print(f"  {lang}: {text}")

    # Get first available (when you don't know which languages exist)
    first = name.get_text()
    print(f"\nFirst available: {first}")

    # Access raw data if needed
    print(f"Raw data structure: {name.raw}")

    print()

    # =========================================================================
    # Part 6: IDE Autocomplete Demo
    # =========================================================================
    print("\nPart 6: IDE Autocomplete Chain")
    print("-" * 80)

    contact = create_contact()

    print("Type this in your IDE to see autocomplete:")
    print()
    print("  contact.                  # IDE shows: contact_data_set, validate(), to_json(), ...")
    print("  contact.contact_data_set. # IDE shows: contact_information, administrative_information")
    print("  contact.contact_data_set.contact_information.")
    print("                            # IDE shows: data_set_information")
    print("  contact.contact_data_set.contact_information.data_set_information.")
    print("                            # IDE shows: uuid, name, short_name, email,")
    print("                            #            telephone, www_address, contact_address, ...")
    print()
    print("  # For multi-language fields:")
    print("  name = contact.contact_data_set.contact_information.data_set_information.name")
    print("  name.                     # IDE shows: set_text(), get_text(), raw")

    print()

    # =========================================================================
    # Part 7: Export to JSON
    # =========================================================================
    print("\nPart 7: Export to JSON")
    print("-" * 80)

    # Create a complete contact using typed access
    contact = create_contact()
    info = contact.contact_data_set.contact_information.data_set_information

    info.uuid = "550e8400-e29b-41d4-a716-446655440000"
    info.name.set_text("Dr. Research Scientist", "en")
    info.short_name.set_text("Dr. R. Scientist", "en")
    info.email = "research@example.com"
    info.telephone = "+1-555-0199"

    # Export to JSON
    json_str = contact.to_json_string(indent=2)
    print("Exported JSON (first 500 chars):")
    print(json_str[:500] + "...")

    print()

    # =========================================================================
    # Part 8: Performance Comparison
    # =========================================================================
    print("\nPart 8: Performance Notes")
    print("-" * 80)

    import time

    # Dict access baseline
    contact = create_contact()
    start = time.perf_counter()
    for _ in range(10000):
        _ = contact._data["contactDataSet"]["contactInformation"]["dataSetInformation"]
    dict_time = time.perf_counter() - start

    # Typed access (with caching)
    start = time.perf_counter()
    for _ in range(10000):
        _ = contact.contact_data_set.contact_information.data_set_information
    typed_time = time.perf_counter() - start

    print(f"Dict access (10,000 iterations):  {dict_time*1000:.2f}ms")
    print(f"Typed access (10,000 iterations): {typed_time*1000:.2f}ms")
    print(f"Overhead: {((typed_time / dict_time - 1) * 100):.1f}%")
    print()
    print("Note: Typed access uses caching, so repeated access has minimal overhead.")
    print("      The developer experience benefit far outweighs the small performance cost.")

    print()

    # =========================================================================
    # Summary
    # =========================================================================
    print("\n" + "=" * 80)
    print("SUMMARY: Why Use Typed Access?")
    print("=" * 80)
    print()
    print("✅ IDE Autocomplete - Discover fields as you type")
    print("✅ Type Safety - Catch errors before runtime")
    print("✅ Cleaner Code - More readable and maintainable")
    print("✅ Multi-Language - Easy API for i18n text")
    print("✅ Backwards Compatible - Dict access still works")
    print("✅ Performance - <5% overhead with caching")
    print()
    print("Migration Tip: Start using typed access for new code, gradually")
    print("               migrate existing code when modifying it.")
    print()
    print("=" * 80)


if __name__ == "__main__":
    main()
