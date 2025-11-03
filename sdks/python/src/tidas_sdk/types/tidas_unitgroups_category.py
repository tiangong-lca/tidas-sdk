"""
Unitgroups classification categories.

Clean implementation using Literal types (matches TypeScript SDK pattern).
DO NOT auto-generate - regenerate using generate_category_types.py
"""

from typing import Literal, TypedDict


class UnitgroupsCategoryData(TypedDict):
    """Unitgroups category metadata."""

    level: Literal['0']
    classId: str
    text: str


# Type-safe union of all unitgroups category IDs
Unitgroups = Literal[
    '1',  # Technical unit groups
    '2',  # Chemical composition unit groups
    '3',  # Economic unit groups
    '4',  # Other unit groups
]


# Type-safe union of all unitgroups category text values
TidasUnitgroupsText = Literal[
    'Chemical composition unit groups',
    'Economic unit groups',
    'Other unit groups',
    'Technical unit groups',
]


# Runtime metadata for lookups
UNITGROUPS_CATEGORIES: dict[str, UnitgroupsCategoryData] = {
    '1': {
        'level': '0',
        'classId': '1',
        'text': 'Technical unit groups',
    },
    '2': {
        'level': '0',
        'classId': '2',
        'text': 'Chemical composition unit groups',
    },
    '3': {
        'level': '0',
        'classId': '3',
        'text': 'Economic unit groups',
    },
    '4': {
        'level': '0',
        'classId': '4',
        'text': 'Other unit groups',
    },
}


__all__ = ['Unitgroups', 'TidasUnitgroupsText', 'UnitgroupsCategoryData', 'UNITGROUPS_CATEGORIES']
