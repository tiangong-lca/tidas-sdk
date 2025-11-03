"""
Flowproperties classification categories.

Clean implementation using Literal types (matches TypeScript SDK pattern).
DO NOT auto-generate - regenerate using generate_category_types.py
"""

from typing import Literal, TypedDict


class FlowpropertiesCategoryData(TypedDict):
    """Flowproperties category metadata."""

    level: Literal['0']
    classId: str
    text: str


# Type-safe union of all flowproperties category IDs
Flowproperties = Literal[
    '1',  # Technical flow properties
    '2',  # Chemical composition of flows
    '3',  # Economic flow properties
    '4',  # Other flow properties
]


# Type-safe union of all flowproperties category text values
TidasFlowpropertiesText = Literal[
    'Chemical composition of flows',
    'Economic flow properties',
    'Other flow properties',
    'Technical flow properties',
]


# Runtime metadata for lookups
FLOWPROPERTIES_CATEGORIES: dict[str, FlowpropertiesCategoryData] = {
    '1': {
        'level': '0',
        'classId': '1',
        'text': 'Technical flow properties',
    },
    '2': {
        'level': '0',
        'classId': '2',
        'text': 'Chemical composition of flows',
    },
    '3': {
        'level': '0',
        'classId': '3',
        'text': 'Economic flow properties',
    },
    '4': {
        'level': '0',
        'classId': '4',
        'text': 'Other flow properties',
    },
}


__all__ = ['Flowproperties', 'TidasFlowpropertiesText', 'FlowpropertiesCategoryData', 'FLOWPROPERTIES_CATEGORIES']
