"""
Multi-language text support for TIDAS entities.
"""

from typing import Any, Dict, List, Optional


class MultiLangText:
    """Wrapper for multi-language text fields in TIDAS format.

    TIDAS stores multi-language text as arrays of objects:
    [{"@xml:lang": "en", "#text": "value"}, ...]

    This class provides a pythonic API for setting and getting text.
    """

    def __init__(self, initial_data: Optional[List[Dict[str, Any]]] = None):
        """Initialize with optional language items.

        Args:
            initial_data: List of language items in TIDAS format
        """
        self._items: List[Dict[str, Any]] = initial_data if initial_data is not None else []

    def set_text(self, value: str, lang: str = "en") -> None:
        """Set text for a specific language.

        Updates existing entry or appends new one if language not found.

        Args:
            value: Text value to set
            lang: Language code (default: "en")
        """
        # Update existing item if language exists
        for item in self._items:
            if item.get("@xml:lang") == lang:
                item["#text"] = value
                return

        # Append new language item
        self._items.append({"@xml:lang": lang, "#text": value})

    def get_text(self, lang: Optional[str] = "en") -> Optional[str]:
        """Get text for a specific language.

        Args:
            lang: Language code to retrieve. If None, returns first available.

        Returns:
            Text for the specified language, or None if not found
        """
        if lang is None:
            # Return first available language
            return self._items[0]["#text"] if self._items else None

        # Search for specific language
        for item in self._items:
            if item.get("@xml:lang") == lang:
                return item.get("#text")

        return None

    @property
    def raw(self) -> List[Dict[str, Any]]:
        """Access raw array for advanced manipulation.

        Returns:
            List of language items in TIDAS format
        """
        return self._items

    def __repr__(self) -> str:
        """String representation showing available languages."""
        langs = [item.get("@xml:lang", "?") for item in self._items]
        return f"MultiLangText({langs})"
