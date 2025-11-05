"""
Lciamethods classification categories.

Clean implementation using Literal types (matches TypeScript SDK pattern).
DO NOT auto-generate - regenerate using generate_category_types.py
"""

from typing import Literal, TypedDict


class LciamethodsCategoryData(TypedDict):
    """Lciamethods category metadata."""

    level: Literal['0', '1', '2']
    classId: str
    text: str


# Type-safe union of all lciamethods category IDs
Lciamethods = Literal[
    '1',  # Damage level LCIA methods
    '1.1',  # Total impact across areas of protection
    '1.2',  # Human health
    '1.2.1',  # Total human health, combined
    '1.2.2',  # Human health, toxicity
    '1.2.3',  # Human health, climate change
    '1.2.4',  # Human health, ionising radiation
    '1.2.5',  # Human health, ozone depletion
    '1.2.6',  # Human health, photooxidant creation
    '1.2.7',  # Human health, other
    '1.3',  # Natural environment
    '1.3.1',  # Total natural environment, combined
    '1.3.2',  # Natural environment, climate change
    '1.3.3',  # Natural environment, ozone depletion
    '1.3.4',  # Natural environment, land use
    '1.3.5',  # Natural environment, freshwater ecotoxicity
    '1.3.6',  # Natural environment, seawater ecotoxicity
    '1.3.7',  # Natural environment, terrestric ecotoxicity
    '1.3.8',  # Natural environment, acidification
    '1.3.9',  # Natural environment, eutrophication
    '1.3.10',  # Natural environment, photooxidant creation
    '1.3.11',  # Natural environment, ionising radiation
    '1.3.12',  # Natural environment, other
    '1.4',  # Man-made environment
    '1.4.1',  # Total man-made environment, combined
    '1.4.2',  # Man-made environment, acidification
    '1.4.3',  # Man-made environment, climate change
    '1.4.4',  # Man-made environment, eutrophication
    '1.4.5',  # Man-made environment, other
    '1.5',  # Resource availability
    '1.5.1',  # Total resource depletion, combined
    '1.5.2',  # Resource depletion, minerals and metals
    '1.5.3',  # Resource depletion, non-renewable energy resourcess
    '1.5.4',  # Resource depletion, land use
    '1.5.5',  # Resource depletion, renewable energy resources
    '1.5.6',  # Resource depletion, renewable non-energy resources
    '1.5.7',  # Resource depletion, other
    '2',  # Midpoint level LCIA methods
    '2.1',  # Combined methods
    '2.2',  # Climate change
    '2.3',  # Ozone depletion
    '2.4',  # Land use
    '2.5',  # Ecotoxicity
    '2.6',  # Acidification
    '2.7',  # Eutrophication
    '2.8',  # Photooxidant creation
    '2.9',  # Nuclear radiation
    '2.10',  # Human toxicity
    '2.11',  # Respiratory effects
    '2.12',  # Noise
    '2.13',  # Resource depletion
    '2.14',  # Other midpoint categories
]


# Type-safe union of all lciamethods category text values
TidasLciamethodsText = Literal[
    'Acidification',
    'Climate change',
    'Combined methods',
    'Damage level LCIA methods',
    'Ecotoxicity',
    'Eutrophication',
    'Human health',
    'Human health, climate change',
    'Human health, ionising radiation',
    'Human health, other',
    'Human health, ozone depletion',
    'Human health, photooxidant creation',
    'Human health, toxicity',
    'Human toxicity',
    'Land use',
    'Man-made environment',
    'Man-made environment, acidification',
    'Man-made environment, climate change',
    'Man-made environment, eutrophication',
    'Man-made environment, other',
    'Midpoint level LCIA methods',
    'Natural environment',
    'Natural environment, acidification',
    'Natural environment, climate change',
    'Natural environment, eutrophication',
    'Natural environment, freshwater ecotoxicity',
    'Natural environment, ionising radiation',
    'Natural environment, land use',
    'Natural environment, other',
    'Natural environment, ozone depletion',
    'Natural environment, photooxidant creation',
    'Natural environment, seawater ecotoxicity',
    'Natural environment, terrestric ecotoxicity',
    'Noise',
    'Nuclear radiation',
    'Other midpoint categories',
    'Ozone depletion',
    'Photooxidant creation',
    'Resource availability',
    'Resource depletion',
    'Resource depletion, land use',
    'Resource depletion, minerals and metals',
    'Resource depletion, non-renewable energy resourcess',
    'Resource depletion, other',
    'Resource depletion, renewable energy resources',
    'Resource depletion, renewable non-energy resources',
    'Respiratory effects',
    'Total human health, combined',
    'Total impact across areas of protection',
    'Total man-made environment, combined',
    'Total natural environment, combined',
    'Total resource depletion, combined',
]


# Runtime metadata for lookups
LCIAMETHODS_CATEGORIES: dict[str, LciamethodsCategoryData] = {
    '1': {
        'level': '0',
        'classId': '1',
        'text': 'Damage level LCIA methods',
    },
    '1.1': {
        'level': '1',
        'classId': '1.1',
        'text': 'Total impact across areas of protection',
    },
    '1.2': {
        'level': '1',
        'classId': '1.2',
        'text': 'Human health',
    },
    '1.2.1': {
        'level': '2',
        'classId': '1.2.1',
        'text': 'Total human health, combined',
    },
    '1.2.2': {
        'level': '2',
        'classId': '1.2.2',
        'text': 'Human health, toxicity',
    },
    '1.2.3': {
        'level': '2',
        'classId': '1.2.3',
        'text': 'Human health, climate change',
    },
    '1.2.4': {
        'level': '2',
        'classId': '1.2.4',
        'text': 'Human health, ionising radiation',
    },
    '1.2.5': {
        'level': '2',
        'classId': '1.2.5',
        'text': 'Human health, ozone depletion',
    },
    '1.2.6': {
        'level': '2',
        'classId': '1.2.6',
        'text': 'Human health, photooxidant creation',
    },
    '1.2.7': {
        'level': '2',
        'classId': '1.2.7',
        'text': 'Human health, other',
    },
    '1.3': {
        'level': '1',
        'classId': '1.3',
        'text': 'Natural environment',
    },
    '1.3.1': {
        'level': '2',
        'classId': '1.3.1',
        'text': 'Total natural environment, combined',
    },
    '1.3.2': {
        'level': '2',
        'classId': '1.3.2',
        'text': 'Natural environment, climate change',
    },
    '1.3.3': {
        'level': '2',
        'classId': '1.3.3',
        'text': 'Natural environment, ozone depletion',
    },
    '1.3.4': {
        'level': '2',
        'classId': '1.3.4',
        'text': 'Natural environment, land use',
    },
    '1.3.5': {
        'level': '2',
        'classId': '1.3.5',
        'text': 'Natural environment, freshwater ecotoxicity',
    },
    '1.3.6': {
        'level': '2',
        'classId': '1.3.6',
        'text': 'Natural environment, seawater ecotoxicity',
    },
    '1.3.7': {
        'level': '2',
        'classId': '1.3.7',
        'text': 'Natural environment, terrestric ecotoxicity',
    },
    '1.3.8': {
        'level': '2',
        'classId': '1.3.8',
        'text': 'Natural environment, acidification',
    },
    '1.3.9': {
        'level': '2',
        'classId': '1.3.9',
        'text': 'Natural environment, eutrophication',
    },
    '1.3.10': {
        'level': '2',
        'classId': '1.3.10',
        'text': 'Natural environment, photooxidant creation',
    },
    '1.3.11': {
        'level': '2',
        'classId': '1.3.11',
        'text': 'Natural environment, ionising radiation',
    },
    '1.3.12': {
        'level': '2',
        'classId': '1.3.12',
        'text': 'Natural environment, other',
    },
    '1.4': {
        'level': '1',
        'classId': '1.4',
        'text': 'Man-made environment',
    },
    '1.4.1': {
        'level': '2',
        'classId': '1.4.1',
        'text': 'Total man-made environment, combined',
    },
    '1.4.2': {
        'level': '2',
        'classId': '1.4.2',
        'text': 'Man-made environment, acidification',
    },
    '1.4.3': {
        'level': '2',
        'classId': '1.4.3',
        'text': 'Man-made environment, climate change',
    },
    '1.4.4': {
        'level': '2',
        'classId': '1.4.4',
        'text': 'Man-made environment, eutrophication',
    },
    '1.4.5': {
        'level': '2',
        'classId': '1.4.5',
        'text': 'Man-made environment, other',
    },
    '1.5': {
        'level': '1',
        'classId': '1.5',
        'text': 'Resource availability',
    },
    '1.5.1': {
        'level': '2',
        'classId': '1.5.1',
        'text': 'Total resource depletion, combined',
    },
    '1.5.2': {
        'level': '2',
        'classId': '1.5.2',
        'text': 'Resource depletion, minerals and metals',
    },
    '1.5.3': {
        'level': '2',
        'classId': '1.5.3',
        'text': 'Resource depletion, non-renewable energy resourcess',
    },
    '1.5.4': {
        'level': '2',
        'classId': '1.5.4',
        'text': 'Resource depletion, land use',
    },
    '1.5.5': {
        'level': '2',
        'classId': '1.5.5',
        'text': 'Resource depletion, renewable energy resources',
    },
    '1.5.6': {
        'level': '2',
        'classId': '1.5.6',
        'text': 'Resource depletion, renewable non-energy resources',
    },
    '1.5.7': {
        'level': '2',
        'classId': '1.5.7',
        'text': 'Resource depletion, other',
    },
    '2': {
        'level': '0',
        'classId': '2',
        'text': 'Midpoint level LCIA methods',
    },
    '2.1': {
        'level': '1',
        'classId': '2.1',
        'text': 'Combined methods',
    },
    '2.2': {
        'level': '1',
        'classId': '2.2',
        'text': 'Climate change',
    },
    '2.3': {
        'level': '1',
        'classId': '2.3',
        'text': 'Ozone depletion',
    },
    '2.4': {
        'level': '1',
        'classId': '2.4',
        'text': 'Land use',
    },
    '2.5': {
        'level': '1',
        'classId': '2.5',
        'text': 'Ecotoxicity',
    },
    '2.6': {
        'level': '1',
        'classId': '2.6',
        'text': 'Acidification',
    },
    '2.7': {
        'level': '1',
        'classId': '2.7',
        'text': 'Eutrophication',
    },
    '2.8': {
        'level': '1',
        'classId': '2.8',
        'text': 'Photooxidant creation',
    },
    '2.9': {
        'level': '1',
        'classId': '2.9',
        'text': 'Nuclear radiation',
    },
    '2.10': {
        'level': '1',
        'classId': '2.10',
        'text': 'Human toxicity',
    },
    '2.11': {
        'level': '1',
        'classId': '2.11',
        'text': 'Respiratory effects',
    },
    '2.12': {
        'level': '1',
        'classId': '2.12',
        'text': 'Noise',
    },
    '2.13': {
        'level': '1',
        'classId': '2.13',
        'text': 'Resource depletion',
    },
    '2.14': {
        'level': '1',
        'classId': '2.14',
        'text': 'Other midpoint categories',
    },
}


__all__ = ['Lciamethods', 'TidasLciamethodsText', 'LciamethodsCategoryData', 'LCIAMETHODS_CATEGORIES']
