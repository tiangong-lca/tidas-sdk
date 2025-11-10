"""
Comprehensive test suite for TIDAS SDK Builder pattern classes.

Tests cover:
- Basic field assignment
- Nested builder chaining
- Array field handling
- Multi-language field helpers
- Build method validation
- Integration with Pydantic models
"""

import uuid
from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from tidas_sdk.builders.tidas_contacts_builders import (
    ContactDataSetBuilder,
    ContactInformationBuilder,
    DataSetInformationBuilder,
)
from tidas_sdk.types.tidas_contacts import ContactDataSet, DataSetInformation


class TestBasicBuilderUsage:
    """Test basic field assignment and simple builders."""

    def test_simple_field_assignment(self):
        """Test setting simple scalar fields."""
        builder = DataSetInformationBuilder()

        # Set fields directly
        builder.common_UUID = str(uuid.uuid4())
        builder.email = "test@example.com"
        builder.telephone = "+1-555-0123"

        # Build the model
        data_set_info = builder.build()

        # Verify
        assert data_set_info.email == "test@example.com"
        assert data_set_info.telephone == "+1-555-0123"
        assert isinstance(data_set_info, DataSetInformation)

    def test_optional_fields_are_none(self):
        """Test that unset optional fields remain None."""
        builder = DataSetInformationBuilder()
        builder.common_UUID = str(uuid.uuid4())
        builder.common_shortName = [{"@xml:lang": "en", "#text": "Test"}]
        builder.common_name = [{"@xml:lang": "en", "#text": "Test Name"}]

        data_set_info = builder.build()

        # Optional fields should be None if not set
        assert data_set_info.email is None
        assert data_set_info.telephone is None


class TestNestedBuilderChaining:
    """Test nested builder access and chaining."""

    def test_nested_builder_auto_initialization(self):
        """Test that nested builders are auto-initialized on access."""
        builder = ContactDataSetBuilder()

        # Access nested builder - should auto-initialize
        contact_info = builder.contactInformation
        assert contact_info is not None
        assert isinstance(contact_info, ContactInformationBuilder)

        # Access deeper nesting
        data_set_info = contact_info.dataSetInformation
        assert data_set_info is not None
        assert isinstance(data_set_info, DataSetInformationBuilder)

    def test_deep_nested_field_assignment(self):
        """Test setting fields through deep nesting."""
        builder = ContactDataSetBuilder()

        # Set deeply nested fields
        builder.contactInformation.dataSetInformation.email = "deep@example.com"
        builder.contactInformation.dataSetInformation.telephone = "+1-555-9999"

        # Build and verify
        contact_data_set = builder.build()
        assert contact_data_set.contactInformation.dataSetInformation.email == "deep@example.com"
        assert contact_data_set.contactInformation.dataSetInformation.telephone == "+1-555-9999"

    def test_nested_builder_persistence(self):
        """Test that accessing the same nested builder returns the same instance."""
        builder = ContactDataSetBuilder()

        # Access twice - should be same instance
        info1 = builder.contactInformation
        info2 = builder.contactInformation

        assert info1 is info2


class TestMultiLanguageHelpers:
    """Test multi-language field helper methods."""

    def test_set_multilang_text(self):
        """Test setting multi-language text using helper methods."""
        builder = DataSetInformationBuilder()

        # Set text in multiple languages
        builder.set_name("English Name", "en")
        builder.set_name("中文名称", "zh")
        builder.set_name("Nombre en Español", "es")

        # Build and verify
        info = builder.build()

        # Check that all languages are present
        assert len(info.common_name) == 3

        # Verify content
        names_by_lang = {item["@xml:lang"]: item["#text"] for item in info.common_name}
        assert names_by_lang["en"] == "English Name"
        assert names_by_lang["zh"] == "中文名称"
        assert names_by_lang["es"] == "Nombre en Español"

    def test_get_multilang_text(self):
        """Test getting multi-language text using helper methods."""
        builder = DataSetInformationBuilder()

        # Set text in multiple languages
        builder.set_name("English Name", "en")
        builder.set_name("French Name", "fr")

        # Get text for specific language
        assert builder.get_name("en") == "English Name"
        assert builder.get_name("fr") == "French Name"
        assert builder.get_name("de") is None  # Not set

    def test_update_existing_multilang_text(self):
        """Test updating existing multi-language text."""
        builder = DataSetInformationBuilder()

        # Set initial text
        builder.set_name("Initial Name", "en")
        assert builder.get_name("en") == "Initial Name"

        # Update the same language
        builder.set_name("Updated Name", "en")
        assert builder.get_name("en") == "Updated Name"

        # Verify only one entry for 'en'
        info = builder.build()
        en_names = [item for item in info.common_name if item["@xml:lang"] == "en"]
        assert len(en_names) == 1

    def test_direct_multilang_list_access(self):
        """Test direct manipulation of multi-lang field as list."""
        builder = DataSetInformationBuilder()

        # Set directly as list
        builder.common_name = [
            {"@xml:lang": "en", "#text": "Direct English"},
            {"@xml:lang": "de", "#text": "Direktes Deutsch"},
        ]

        # Verify
        assert builder.get_name("en") == "Direct English"
        assert builder.get_name("de") == "Direktes Deutsch"

    def test_multiple_multilang_fields(self):
        """Test setting multiple multi-lang fields."""
        builder = DataSetInformationBuilder()

        # Set name
        builder.set_name("Full Name", "en")
        builder.set_name("Nom Complet", "fr")

        # Set short name
        builder.set_shortName("Name", "en")
        builder.set_shortName("Nom", "fr")

        info = builder.build()

        # Verify both fields
        assert len(info.common_name) == 2
        assert len(info.common_shortName) == 2


class TestBuildMethod:
    """Test the build() method behavior."""

    def test_build_creates_valid_pydantic_model(self):
        """Test that build() creates a valid Pydantic model."""
        builder = DataSetInformationBuilder()
        builder.common_UUID = str(uuid.uuid4())
        builder.set_name("Test", "en")
        builder.set_shortName("T", "en")
        builder.email = "test@example.com"

        # Build
        info = builder.build()

        # Verify it's a Pydantic model
        assert isinstance(info, DataSetInformation)

        # Verify Pydantic validation works
        assert info.model_dump() is not None

    def test_build_with_nested_objects(self):
        """Test building with nested objects."""
        builder = ContactDataSetBuilder()

        # Set nested fields
        builder.contactInformation.dataSetInformation.common_UUID = str(uuid.uuid4())
        builder.contactInformation.dataSetInformation.set_name("Contact Name", "en")
        builder.contactInformation.dataSetInformation.set_shortName("CN", "en")
        builder.contactInformation.dataSetInformation.email = "contact@example.com"

        # Build
        contact_data = builder.build()

        # Verify structure
        assert isinstance(contact_data, ContactDataSet)
        assert contact_data.contactInformation is not None
        assert contact_data.contactInformation.dataSetInformation is not None
        assert contact_data.contactInformation.dataSetInformation.email == "contact@example.com"

    def test_build_multiple_times(self):
        """Test that build() can be called multiple times."""
        builder = DataSetInformationBuilder()
        builder.common_UUID = str(uuid.uuid4())
        builder.set_name("Name", "en")
        builder.set_shortName("N", "en")
        builder.email = "test@example.com"

        # Build twice
        info1 = builder.build()
        info2 = builder.build()

        # Should create separate instances
        assert info1 is not info2

        # But with same data
        assert info1.email == info2.email
        assert info1.common_UUID == info2.common_UUID


class TestValidation:
    """Test validation behavior of builders."""

    def test_validation_disabled_by_default(self):
        """Test that validation is disabled during construction."""
        builder = DataSetInformationBuilder()

        # Should not raise even with invalid UUID format
        builder.common_UUID = "not-a-valid-uuid"
        # No exception should be raised here

    def test_validation_on_build(self):
        """Test that validation happens during build()."""
        builder = DataSetInformationBuilder()
        builder.common_UUID = "invalid-uuid"
        builder.set_name("Name", "en")
        builder.set_shortName("N", "en")

        # Should raise validation error on build
        with pytest.raises(ValidationError):
            builder.build()

    def test_required_fields_validation(self):
        """Test that required fields are validated on build()."""
        builder = DataSetInformationBuilder()
        # Missing required fields

        # Should fail validation
        with pytest.raises(ValidationError) as exc_info:
            builder.build()

        # Check that it's complaining about required fields
        assert "common_UUID" in str(exc_info.value) or "UUID" in str(exc_info.value)


class TestComplexScenarios:
    """Test complex real-world scenarios."""

    def test_build_complete_contact(self):
        """Test building a complete contact entity."""
        builder = ContactDataSetBuilder()

        # Set namespace attributes
        builder.field_xmlns = "http://lca.jrc.it/ILCD/Contact"
        builder.field_version = "1.1"

        # Set contact information
        contact_uuid = str(uuid.uuid4())
        builder.contactInformation.dataSetInformation.common_UUID = contact_uuid
        builder.contactInformation.dataSetInformation.set_name("Dr. Jane Smith", "en")
        builder.contactInformation.dataSetInformation.set_shortName("J. Smith", "en")
        builder.contactInformation.dataSetInformation.email = "jane.smith@example.com"
        builder.contactInformation.dataSetInformation.telephone = "+1-555-0100"
        builder.contactInformation.dataSetInformation.WWWAddress = "https://example.com/jane"

        # Build
        contact = builder.build()

        # Comprehensive verification
        assert contact.contactInformation.dataSetInformation.common_UUID == contact_uuid
        assert contact.contactInformation.dataSetInformation.email == "jane.smith@example.com"

        # Verify multi-lang fields
        name_text = next(
            item["#text"]
            for item in contact.contactInformation.dataSetInformation.common_name
            if item["@xml:lang"] == "en"
        )
        assert name_text == "Dr. Jane Smith"

    def test_incremental_construction(self):
        """Test building an entity incrementally over multiple steps."""
        builder = ContactDataSetBuilder()

        # Step 1: Basic info
        builder.contactInformation.dataSetInformation.common_UUID = str(uuid.uuid4())
        builder.contactInformation.dataSetInformation.set_name("Contact", "en")
        builder.contactInformation.dataSetInformation.set_shortName("C", "en")

        # Step 2: Add contact details (later)
        builder.contactInformation.dataSetInformation.email = "contact@example.com"

        # Step 3: Add multilingual support (even later)
        builder.contactInformation.dataSetInformation.set_name("Kontakt", "de")
        builder.contactInformation.dataSetInformation.set_shortName("K", "de")

        # Build when ready
        contact = builder.build()

        # Verify all steps are included
        assert contact.contactInformation.dataSetInformation.email == "contact@example.com"
        assert len(contact.contactInformation.dataSetInformation.common_name) == 2


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_empty_builder_raises_validation_error(self):
        """Test that building an empty builder raises validation error."""
        builder = DataSetInformationBuilder()

        with pytest.raises(ValidationError):
            builder.build()

    def test_none_values_excluded_from_build(self):
        """Test that None values are excluded from built model."""
        builder = DataSetInformationBuilder()
        builder.common_UUID = str(uuid.uuid4())
        builder.set_name("Name", "en")
        builder.set_shortName("N", "en")
        builder.email = None  # Explicitly set to None

        info = builder.build()

        # None values should be excluded
        assert info.email is None

    def test_multilang_field_empty_list_handling(self):
        """Test handling of empty multi-lang field lists."""
        builder = DataSetInformationBuilder()
        builder.common_UUID = str(uuid.uuid4())
        builder.common_name = []  # Empty list
        builder.common_shortName = [{"@xml:lang": "en", "#text": "Short"}]

        # Should handle empty list gracefully
        with pytest.raises(ValidationError):
            # Empty required field should fail validation
            builder.build()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
