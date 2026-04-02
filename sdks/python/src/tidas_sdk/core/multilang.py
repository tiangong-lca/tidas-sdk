"""
Utilities for handling ILCD multi-language text arrays.
"""
from __future__ import annotations

import re
from typing import Any, Iterable, MutableSequence, TypedDict


MultiLangItem = TypedDict(
    "MultiLangItem",
    {"@xml:lang": str, "#text": str},
    total=False,
)

CHINESE_CHARACTER_PATTERN = re.compile(r"[\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]")


class MultiLangList(list[MultiLangItem]):
    """
    List wrapper that exposes convenient helpers for language specific entries.
    """

    def __init__(self, values: Iterable[MultiLangItem] | None = None) -> None:
        super().__init__()
        if not values:
            return
        for value in values:
            lang = value.get("@xml:lang")
            text = value.get("#text")
            if lang and text is not None:
                self.append({"@xml:lang": lang, "#text": text})

    def set_text(self, text: str, lang: str = "en") -> None:
        """
        Upsert the text for a specific locale.
        """
        validate_multilang_item({"@xml:lang": lang, "#text": text})
        for entry in self:
            if entry.get("@xml:lang") == lang:
                entry["#text"] = text
                return
        self.append({"@xml:lang": lang, "#text": text})

    def get_text(self, lang: str | None = "en") -> str | None:
        """
        Fetch the best matching text for the requested language.
        """
        if lang:
            for entry in self:
                if entry.get("@xml:lang") == lang:
                    return entry.get("#text")
        return self[0].get("#text") if self else None

    def to_plain_list(self) -> list[MultiLangItem]:
        """
        Produce a JSON serializable representation.
        """
        return [{"@xml:lang": item.get("@xml:lang", ""), "#text": item.get("#text", "")} for item in self]


def _is_multilang_item(value: Any) -> bool:
    return (
        isinstance(value, dict)
        and "@xml:lang" in value
        and "#text" in value
        and isinstance(value.get("@xml:lang"), str)
        and (value.get("#text") is None or isinstance(value.get("#text"), str))
    )


def _is_multilang_list(value: Any) -> bool:
    if not isinstance(value, MutableSequence):
        return False
    if not value:
        return False
    return all(_is_multilang_item(entry) for entry in value)


def validate_multilang_item(value: MultiLangItem) -> None:
    lang = value.get("@xml:lang")
    text = value.get("#text")

    if not isinstance(lang, str) or not isinstance(text, str):
        return

    if re.match(r"^[zZ][hH](?:-|$)", lang) and not CHINESE_CHARACTER_PATTERN.search(text):
        raise ValueError(
            "@xml:lang values starting with 'zh' must include at least one Chinese character"
        )

    if re.match(r"^[eE][nN](?:-|$)", lang) and CHINESE_CHARACTER_PATTERN.search(text):
        raise ValueError(
            "@xml:lang values starting with 'en' must not contain Chinese characters"
        )


def validate_multilang_entries(values: Iterable[MultiLangItem]) -> None:
    for value in values:
        validate_multilang_item(value)


def wrap_multilang(value: Any) -> Any:
    """
    Convert dictionaries/lists from JSON payloads into their pythonic wrappers.
    """
    if _is_multilang_list(value):
        return MultiLangList(value)
    if _is_multilang_item(value):
        return MultiLangList([value])
    return value


def deep_wrap_multilang(payload: Any) -> Any:
    """
    Recursively walk payloads (dict/list) and wrap multi-language nodes.
    """
    if isinstance(payload, dict):
        return wrap_multilang({k: deep_wrap_multilang(v) for k, v in payload.items()})
    if isinstance(payload, list):
        wrapped_items = [deep_wrap_multilang(item) for item in payload]
        flattened_items: list[MultiLangItem] = []
        for item in wrapped_items:
            if isinstance(item, MultiLangList):
                flattened_items.extend(item.to_plain_list())
                continue
            if _is_multilang_item(item):
                flattened_items.append(item)
                continue
            return wrapped_items
        return MultiLangList(flattened_items) if flattened_items else wrapped_items
    return payload
