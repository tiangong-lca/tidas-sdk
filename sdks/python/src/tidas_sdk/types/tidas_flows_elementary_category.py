"""
FlowsElementary classification categories.

Clean implementation using Literal types (matches TypeScript SDK pattern).
DO NOT auto-generate - regenerate using generate_category_types.py
"""

from typing import Literal, TypedDict


class FlowsElementaryCategoryData(TypedDict):
    """FlowsElementary category metadata."""

    level: Literal['0', '1', '2']
    classId: str
    text: str


# Type-safe union of all flowselementary category IDs
FlowsElementary = Literal[
    '1',  # Emissions
    '1.1',  # Emissions to water
    '1.1.1',  # Emissions to fresh water
    '1.1.2',  # Emissions to sea water
    '1.1.3',  # Emissions to water, unspecified
    '1.1.4',  # Emissions to water, unspecified (long-term)
    '1.2',  # Emissions to soil
    '1.2.1',  # Emissions to agricultural soil
    '1.2.2',  # Emissions to non-agricultural soil
    '1.2.3',  # Emissions to soil, unspecified
    '1.2.4',  # Emissions to soil, unspecified (long-term)
    '1.3',  # Emissions to air
    '1.3.1',  # Emissions to urban air close to ground
    '1.3.2',  # Emissions to non-urban air or from high stacks
    '1.3.3',  # Emissions to lower stratosphere and upper troposphere
    '1.3.4',  # Emissions to air, unspecified
    '1.3.5',  # Emissions to air, unspecified (long-term)
    '2',  # Resources
    '2.1',  # Resources from ground
    '2.1.1',  # Non-renewable material resources from ground
    '2.1.2',  # Non-renewable element resources from ground
    '2.1.3',  # Non-renewable energy resources from ground
    '2.1.4',  # Renewable element resources from ground
    '2.1.5',  # Renewable energy resources from ground
    '2.1.6',  # Renewable material resources from ground
    '2.1.7',  # Renewable resources from ground, unspecified
    '2.1.8',  # Non-renewable resources from ground, unspecified
    '2.2',  # Resources from water
    '2.2.1',  # Non-renewable material resources from water
    '2.2.2',  # Non-renewable element resources from water
    '2.2.3',  # Non-renewable energy resources from water
    '2.2.4',  # Renewable element resources from water
    '2.2.5',  # Renewable energy resources from water
    '2.2.6',  # Renewable material resources from water
    '2.2.7',  # Renewable resources from water, unspecified
    '2.2.8',  # Non-renewable resources from water, unspecified
    '2.3',  # Resources from air
    '2.3.1',  # Non-renewable material resources from air
    '2.3.2',  # Non-renewable element resources from air
    '2.3.3',  # Non-renewable energy resources from air
    '2.3.4',  # Renewable element resources from air
    '2.3.5',  # Renewable energy resources from air
    '2.3.6',  # Renewable material resources from air
    '2.3.7',  # Renewable resources from air, unspecified
    '2.3.8',  # Non-renewable resources from air, unspecified
    '2.4',  # Resources from biosphere
    '2.4.1',  # Renewable element resources from biosphere
    '2.4.2',  # Renewable energy resources from biosphere
    '2.4.3',  # Renewable material resources from biosphere
    '2.4.4',  # Renewable genetic resources from biosphere
    '2.4.5',  # Renewable resources from biosphere, unspecified
    '3',  # Land use
    '3.1',  # Land occupation
    '3.2',  # Land transformation
    '4',  # Other elementary flows
]


# Runtime metadata for lookups
FLOWS_ELEMENTARY_CATEGORIES: dict[str, FlowsElementaryCategoryData] = {
    '1': {
        'level': '0',
        'classId': '1',
        'text': 'Emissions',
    },
    '1.1': {
        'level': '1',
        'classId': '1.1',
        'text': 'Emissions to water',
    },
    '1.1.1': {
        'level': '2',
        'classId': '1.1.1',
        'text': 'Emissions to fresh water',
    },
    '1.1.2': {
        'level': '2',
        'classId': '1.1.2',
        'text': 'Emissions to sea water',
    },
    '1.1.3': {
        'level': '2',
        'classId': '1.1.3',
        'text': 'Emissions to water, unspecified',
    },
    '1.1.4': {
        'level': '2',
        'classId': '1.1.4',
        'text': 'Emissions to water, unspecified (long-term)',
    },
    '1.2': {
        'level': '1',
        'classId': '1.2',
        'text': 'Emissions to soil',
    },
    '1.2.1': {
        'level': '2',
        'classId': '1.2.1',
        'text': 'Emissions to agricultural soil',
    },
    '1.2.2': {
        'level': '2',
        'classId': '1.2.2',
        'text': 'Emissions to non-agricultural soil',
    },
    '1.2.3': {
        'level': '2',
        'classId': '1.2.3',
        'text': 'Emissions to soil, unspecified',
    },
    '1.2.4': {
        'level': '2',
        'classId': '1.2.4',
        'text': 'Emissions to soil, unspecified (long-term)',
    },
    '1.3': {
        'level': '1',
        'classId': '1.3',
        'text': 'Emissions to air',
    },
    '1.3.1': {
        'level': '2',
        'classId': '1.3.1',
        'text': 'Emissions to urban air close to ground',
    },
    '1.3.2': {
        'level': '2',
        'classId': '1.3.2',
        'text': 'Emissions to non-urban air or from high stacks',
    },
    '1.3.3': {
        'level': '2',
        'classId': '1.3.3',
        'text': 'Emissions to lower stratosphere and upper troposphere',
    },
    '1.3.4': {
        'level': '2',
        'classId': '1.3.4',
        'text': 'Emissions to air, unspecified',
    },
    '1.3.5': {
        'level': '2',
        'classId': '1.3.5',
        'text': 'Emissions to air, unspecified (long-term)',
    },
    '2': {
        'level': '0',
        'classId': '2',
        'text': 'Resources',
    },
    '2.1': {
        'level': '1',
        'classId': '2.1',
        'text': 'Resources from ground',
    },
    '2.1.1': {
        'level': '2',
        'classId': '2.1.1',
        'text': 'Non-renewable material resources from ground',
    },
    '2.1.2': {
        'level': '2',
        'classId': '2.1.2',
        'text': 'Non-renewable element resources from ground',
    },
    '2.1.3': {
        'level': '2',
        'classId': '2.1.3',
        'text': 'Non-renewable energy resources from ground',
    },
    '2.1.4': {
        'level': '2',
        'classId': '2.1.4',
        'text': 'Renewable element resources from ground',
    },
    '2.1.5': {
        'level': '2',
        'classId': '2.1.5',
        'text': 'Renewable energy resources from ground',
    },
    '2.1.6': {
        'level': '2',
        'classId': '2.1.6',
        'text': 'Renewable material resources from ground',
    },
    '2.1.7': {
        'level': '2',
        'classId': '2.1.7',
        'text': 'Renewable resources from ground, unspecified',
    },
    '2.1.8': {
        'level': '2',
        'classId': '2.1.8',
        'text': 'Non-renewable resources from ground, unspecified',
    },
    '2.2': {
        'level': '1',
        'classId': '2.2',
        'text': 'Resources from water',
    },
    '2.2.1': {
        'level': '2',
        'classId': '2.2.1',
        'text': 'Non-renewable material resources from water',
    },
    '2.2.2': {
        'level': '2',
        'classId': '2.2.2',
        'text': 'Non-renewable element resources from water',
    },
    '2.2.3': {
        'level': '2',
        'classId': '2.2.3',
        'text': 'Non-renewable energy resources from water',
    },
    '2.2.4': {
        'level': '2',
        'classId': '2.2.4',
        'text': 'Renewable element resources from water',
    },
    '2.2.5': {
        'level': '2',
        'classId': '2.2.5',
        'text': 'Renewable energy resources from water',
    },
    '2.2.6': {
        'level': '2',
        'classId': '2.2.6',
        'text': 'Renewable material resources from water',
    },
    '2.2.7': {
        'level': '2',
        'classId': '2.2.7',
        'text': 'Renewable resources from water, unspecified',
    },
    '2.2.8': {
        'level': '2',
        'classId': '2.2.8',
        'text': 'Non-renewable resources from water, unspecified',
    },
    '2.3': {
        'level': '1',
        'classId': '2.3',
        'text': 'Resources from air',
    },
    '2.3.1': {
        'level': '2',
        'classId': '2.3.1',
        'text': 'Non-renewable material resources from air',
    },
    '2.3.2': {
        'level': '2',
        'classId': '2.3.2',
        'text': 'Non-renewable element resources from air',
    },
    '2.3.3': {
        'level': '2',
        'classId': '2.3.3',
        'text': 'Non-renewable energy resources from air',
    },
    '2.3.4': {
        'level': '2',
        'classId': '2.3.4',
        'text': 'Renewable element resources from air',
    },
    '2.3.5': {
        'level': '2',
        'classId': '2.3.5',
        'text': 'Renewable energy resources from air',
    },
    '2.3.6': {
        'level': '2',
        'classId': '2.3.6',
        'text': 'Renewable material resources from air',
    },
    '2.3.7': {
        'level': '2',
        'classId': '2.3.7',
        'text': 'Renewable resources from air, unspecified',
    },
    '2.3.8': {
        'level': '2',
        'classId': '2.3.8',
        'text': 'Non-renewable resources from air, unspecified',
    },
    '2.4': {
        'level': '1',
        'classId': '2.4',
        'text': 'Resources from biosphere',
    },
    '2.4.1': {
        'level': '2',
        'classId': '2.4.1',
        'text': 'Renewable element resources from biosphere',
    },
    '2.4.2': {
        'level': '2',
        'classId': '2.4.2',
        'text': 'Renewable energy resources from biosphere',
    },
    '2.4.3': {
        'level': '2',
        'classId': '2.4.3',
        'text': 'Renewable material resources from biosphere',
    },
    '2.4.4': {
        'level': '2',
        'classId': '2.4.4',
        'text': 'Renewable genetic resources from biosphere',
    },
    '2.4.5': {
        'level': '2',
        'classId': '2.4.5',
        'text': 'Renewable resources from biosphere, unspecified',
    },
    '3': {
        'level': '0',
        'classId': '3',
        'text': 'Land use',
    },
    '3.1': {
        'level': '1',
        'classId': '3.1',
        'text': 'Land occupation',
    },
    '3.2': {
        'level': '1',
        'classId': '3.2',
        'text': 'Land transformation',
    },
    '4': {
        'level': '0',
        'classId': '4',
        'text': 'Other elementary flows',
    },
}


__all__ = ['FlowsElementary', 'FlowsElementaryCategoryData', 'FLOWS_ELEMENTARY_CATEGORIES']
