"""
Contacts classification categories.

Clean implementation using Literal types (matches TypeScript SDK pattern).
DO NOT auto-generate - regenerate using generate_category_types.py
"""

from typing import Literal, TypedDict


class ContactsCategoryData(TypedDict):
    """Contacts category metadata."""

    level: Literal['0', '1']
    classId: str
    text: str


# Type-safe union of all contacts category IDs
Contacts = Literal[
    '1',  # Group of organisations, project
    '2',  # Organisations
    '2.1',  # Private companies
    '2.2',  # Governmental organisations
    '2.3',  # Non-governmental organisations
    '2.4',  # Other organisations
    '3',  # Working groups within organisation
    '4',  # Persons
    '5',  # Other
]


# Runtime metadata for lookups
CONTACTS_CATEGORIES: dict[str, ContactsCategoryData] = {
    '1': {
        'level': '0',
        'classId': '1',
        'text': 'Group of organisations, project',
    },
    '2': {
        'level': '0',
        'classId': '2',
        'text': 'Organisations',
    },
    '2.1': {
        'level': '1',
        'classId': '2.1',
        'text': 'Private companies',
    },
    '2.2': {
        'level': '1',
        'classId': '2.2',
        'text': 'Governmental organisations',
    },
    '2.3': {
        'level': '1',
        'classId': '2.3',
        'text': 'Non-governmental organisations',
    },
    '2.4': {
        'level': '1',
        'classId': '2.4',
        'text': 'Other organisations',
    },
    '3': {
        'level': '0',
        'classId': '3',
        'text': 'Working groups within organisation',
    },
    '4': {
        'level': '0',
        'classId': '4',
        'text': 'Persons',
    },
    '5': {
        'level': '0',
        'classId': '5',
        'text': 'Other',
    },
}


__all__ = ['Contacts', 'ContactsCategoryData', 'CONTACTS_CATEGORIES']
