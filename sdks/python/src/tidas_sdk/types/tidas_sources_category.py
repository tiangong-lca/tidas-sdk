"""
Sources classification categories.

Clean implementation using Literal types (matches TypeScript SDK pattern).
DO NOT auto-generate - regenerate using generate_category_types.py
"""

from typing import Literal, TypedDict


class SourcesCategoryData(TypedDict):
    """Sources category metadata."""

    level: Literal['0']
    classId: str
    text: str


# Type-safe union of all sources category IDs
Sources = Literal[
    '0',  # Images
    '1',  # Data set formats
    '2',  # Databases
    '3',  # Compliance systems
    '4',  # Statistical classifications
    '5',  # Publications and communications
    '6',  # Other source types
]


# Type-safe union of all sources category text values
TidasSourcesText = Literal[
    'Compliance systems',
    'Data set formats',
    'Databases',
    'Images',
    'Other source types',
    'Publications and communications',
    'Statistical classifications',
]


# Runtime metadata for lookups
SOURCES_CATEGORIES: dict[str, SourcesCategoryData] = {
    '0': {
        'level': '0',
        'classId': '0',
        'text': 'Images',
    },
    '1': {
        'level': '0',
        'classId': '1',
        'text': 'Data set formats',
    },
    '2': {
        'level': '0',
        'classId': '2',
        'text': 'Databases',
    },
    '3': {
        'level': '0',
        'classId': '3',
        'text': 'Compliance systems',
    },
    '4': {
        'level': '0',
        'classId': '4',
        'text': 'Statistical classifications',
    },
    '5': {
        'level': '0',
        'classId': '5',
        'text': 'Publications and communications',
    },
    '6': {
        'level': '0',
        'classId': '6',
        'text': 'Other source types',
    },
}


__all__ = ['Sources', 'TidasSourcesText', 'SourcesCategoryData', 'SOURCES_CATEGORIES']
