"""
Typed field access wrappers for TIDAS entities.

This module provides wrapper classes that enable IDE autocomplete and type checking
for nested entity fields, while maintaining backwards compatibility with dict-based access.
"""

from typing import Any, Dict, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from tidas_sdk.core.base import TidasEntity


class MultiLangText:
    """Wrapper for multi-language text fields.

    Provides type-safe methods for getting and setting text in multiple languages.
    The underlying data structure is a list of dicts with @xml:lang and #text keys.

    Example:
        >>> name = MultiLangText([{"@xml:lang": "en", "#text": "Carbon Dioxide"}])
        >>> name.set_text("Kohlendioxid", "de")
        >>> name.get_text("de")
        'Kohlendioxid'
    """

    __slots__ = ('_data',)

    def __init__(self, data: List[Dict[str, str]]) -> None:
        """Initialize multi-language text wrapper.

        Args:
            data: List of language entries, each with @xml:lang and #text keys
        """
        self._data = data

    def set_text(self, value: str, lang: str = "en") -> None:
        """Set text for a specific language.

        If an entry for the language already exists, it will be updated.
        Otherwise, a new entry is added.

        Args:
            value: The text content to set
            lang: Language code (e.g., "en", "de", "fr"). Defaults to "en"
        """
        for entry in self._data:
            if entry.get("@xml:lang") == lang:
                entry["#text"] = value
                return
        self._data.append({"@xml:lang": lang, "#text": value})

    def get_text(self, lang: Optional[str] = None) -> Optional[str]:
        """Get text for a specific language.

        Args:
            lang: Language code to retrieve. If None, returns the first available text.

        Returns:
            The text content for the specified language, or None if not found
        """
        if lang is None:
            return self._data[0]["#text"] if self._data else None
        for entry in self._data:
            if entry.get("@xml:lang") == lang:
                return entry.get("#text")
        return None

    @property
    def raw(self) -> List[Dict[str, str]]:
        """Access the raw multi-language array.

        Returns:
            List of dicts with @xml:lang and #text keys
        """
        return self._data

    def __repr__(self) -> str:
        """Return string representation showing available languages."""
        langs = [entry.get("@xml:lang", "?") for entry in self._data]
        return f"MultiLangText(languages={langs})"


class BaseWrapper:
    """Base class for all entity field wrappers.

    Provides common functionality for accessing nested fields with type safety.
    All wrappers use __slots__ for memory efficiency.
    """

    __slots__ = ('_entity', '_data')

    def __init__(self, entity: 'TidasEntity', data: Dict[str, Any]) -> None:
        """Initialize wrapper.

        Args:
            entity: Parent TidasEntity instance (for validation context)
            data: Dictionary containing the field data
        """
        self._entity = entity
        self._data = data

    def _ensure_field(self, field_name: str) -> None:
        """Ensure a field exists in the data dict.

        Creates the field with an empty dict if it doesn't exist.

        Args:
            field_name: Name of the field to ensure exists
        """
        if field_name not in self._data:
            self._data[field_name] = {}

    def _get_multi_lang(self, field_name: str) -> MultiLangText:
        """Get a multi-language text field wrapper.

        Args:
            field_name: Name of the field containing multi-lang data

        Returns:
            MultiLangText wrapper for the field
        """
        if field_name not in self._data:
            self._data[field_name] = []
        return MultiLangText(self._data[field_name])


# Contact entity wrappers

class DataSetInformationWrapper(BaseWrapper):
    """Wrapper for Contact's dataSetInformation field."""

    __slots__ = ()

    @property
    def uuid(self) -> Optional[str]:
        """UUID of the contact dataset."""
        return self._data.get("common:UUID")

    @uuid.setter
    def uuid(self, value: str) -> None:
        """Set UUID of the contact dataset."""
        self._data["common:UUID"] = value

    @property
    def short_name(self) -> MultiLangText:
        """Short name of the contact (max 40 chars per language)."""
        return self._get_multi_lang("common:shortName")

    @property
    def name(self) -> MultiLangText:
        """Full name of the contact."""
        return self._get_multi_lang("common:name")

    @property
    def email(self) -> Optional[str]:
        """Email address of the contact."""
        return self._data.get("email")

    @email.setter
    def email(self, value: Optional[str]) -> None:
        """Set email address of the contact."""
        if value is None:
            self._data.pop("email", None)
        else:
            self._data["email"] = value

    @property
    def telephone(self) -> Optional[str]:
        """Telephone number of the contact."""
        return self._data.get("telephone")

    @telephone.setter
    def telephone(self, value: Optional[str]) -> None:
        """Set telephone number of the contact."""
        if value is None:
            self._data.pop("telephone", None)
        else:
            self._data["telephone"] = value

    @property
    def telefax(self) -> Optional[str]:
        """Fax number of the contact."""
        return self._data.get("telefax")

    @telefax.setter
    def telefax(self, value: Optional[str]) -> None:
        """Set fax number of the contact."""
        if value is None:
            self._data.pop("telefax", None)
        else:
            self._data["telefax"] = value

    @property
    def www_address(self) -> Optional[str]:
        """Website URL of the contact."""
        return self._data.get("WWWAddress")

    @www_address.setter
    def www_address(self, value: Optional[str]) -> None:
        """Set website URL of the contact."""
        if value is None:
            self._data.pop("WWWAddress", None)
        else:
            self._data["WWWAddress"] = value

    @property
    def contact_address(self) -> MultiLangText:
        """Physical address of the contact."""
        return self._get_multi_lang("contactAddress")


class ContactInformationWrapper(BaseWrapper):
    """Wrapper for Contact's contactInformation field."""

    __slots__ = ()

    @property
    def data_set_information(self) -> DataSetInformationWrapper:
        """Access dataSetInformation field with type hints."""
        self._ensure_field("dataSetInformation")
        return DataSetInformationWrapper(self._entity, self._data["dataSetInformation"])


class ContactDataSetWrapper(BaseWrapper):
    """Wrapper for Contact's contactDataSet root field."""

    __slots__ = ()

    @property
    def contact_information(self) -> ContactInformationWrapper:
        """Access contactInformation field with type hints."""
        self._ensure_field("contactInformation")
        return ContactInformationWrapper(self._entity, self._data["contactInformation"])
