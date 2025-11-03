#!/usr/bin/env python3
"""
Post-process auto-generated Pydantic type files to:
1. Remove duplicate type definitions
2. Replace type references with base types from tidas_data_types.py
3. Add imports from tidas_data_types.py
4. Remove redundant type aliases

This script follows the pattern used in TypeScript SDK's post-processing approach.
"""

import re
import sys
from pathlib import Path
from typing import Set, Dict, List


class TypeFilePostProcessor:
    """Post-process generated Pydantic type files."""

    # Type mappings: numbered variants -> base type
    TYPE_REPLACEMENTS = {
        # MultiLang types - map to base types
        r'\bStringMultiLang\d+\b': 'StringMultiLang',
        r'\bStringMultiLang\d+Item\b': 'StringMultiLang',
        r'\bSTMultiLang\d+\b': 'STMultiLang',
        r'\bSTMultiLang\d+Item\b': 'STMultiLang',
        r'\bFTMultiLang\d+\b': 'FTMultiLang',
        r'\bFTMultiLang\d+Item\b': 'FTMultiLang',
        # GlobalReferenceType variants
        r'\bGlobalReferenceType\d+\b': 'GlobalReferenceType',
        r'\bGlobalReferenceTypeItem\b': 'GlobalReferenceType',
    }

    # Base types that should be imported from tidas_data_types
    BASE_TYPES = {
        'CASNumber', 'FT', 'ST', 'String',
        'MultiLangItem', 'MultiLangItemString', 'MultiLangItemST',
        'StringMultiLang', 'STMultiLang', 'FTMultiLang',
        'Int1', 'Int5', 'Int6', 'LevelType',
        'Perc', 'Real', 'MatR', 'MatV',
        'UUID', 'GlobalReferenceType', 'GlobalReferenceTypeOrArray',
        'GIS', 'Year', 'DateTime',
    }

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.content = file_path.read_text(encoding='utf-8')
        self.lines = self.content.split('\n')
        self.used_base_types: Set[str] = set()
        self.removed_classes: Set[str] = set()
        self.removed_aliases: int = 0
        self.replacements_made: Dict[str, int] = {}

    def replace_type_references(self) -> str:
        """Replace numbered type variants with base types."""
        content = self.content

        for pattern, replacement in self.TYPE_REPLACEMENTS.items():
            # Count replacements
            matches = re.findall(pattern, content)
            if matches:
                unique_matches = set(matches)
                for match in unique_matches:
                    count = content.count(match)
                    if match != replacement:  # Don't count if already the base type
                        self.replacements_made[f"{match} → {replacement}"] = count

                # Perform replacement
                content = re.sub(pattern, replacement, content)
                # Track that we're using this base type
                self.used_base_types.add(replacement)

        return content

    def detect_used_base_types(self, content: str) -> None:
        """Detect which base types from tidas_data_types.py are used."""
        for base_type in self.BASE_TYPES:
            # Check if type is referenced in content
            if re.search(rf'\b{base_type}\b', content):
                self.used_base_types.add(base_type)

    def is_duplicate_class(self, line: str) -> tuple[bool, str | None]:
        """Check if line starts a duplicate class definition that should be removed."""
        # Patterns for classes that will be replaced by base types
        duplicate_patterns = [
            # MultiLang variants
            r'^class (StringMultiLang\d+)(Item)?\(',
            r'^class (STMultiLang\d+)(Item)?\(',
            r'^class (FTMultiLang\d+)(Item)?\(',
            # GlobalReferenceType variants
            r'^class (GlobalReferenceType\d+)\(',
            r'^class (GlobalReferenceTypeItem)\(',
            # Simple types that are in BASE_TYPES
            r'^class (CASNumber)\(RootModel',
            r'^class (FT)\(RootModel',
            r'^class (ST)\(RootModel',
            r'^class (String)\(RootModel',
            r'^class (Int\d+)\(RootModel',
            r'^class (LevelType)\(RootModel',
            r'^class (Perc)\(RootModel',
            r'^class (MatR)\(RootModel',
            r'^class (MatV)\(RootModel',
            r'^class (Real)\(RootModel',
            r'^class (GIS)\(RootModel',
            r'^class (Year)\(RootModel',
            r'^class (DateTime)\(RootModel',
        ]

        for pattern in duplicate_patterns:
            match = re.match(pattern, line)
            if match:
                class_name = match.group(1)
                if match.lastindex >= 2 and match.group(2):
                    class_name += match.group(2)
                return True, class_name

        return False, None

    def remove_duplicate_classes(self, lines: List[str]) -> List[str]:
        """Remove duplicate class definitions."""
        new_lines = []
        skip_lines = False
        current_class = None

        i = 0
        while i < len(self.lines):
            line = self.lines[i]

            # Check if this starts a duplicate class
            is_dup, class_name = self.is_duplicate_class(line)

            if is_dup:
                current_class = class_name
                self.removed_classes.add(class_name)
                skip_lines = True
                i += 1
                continue

            # If skipping, check if we've reached end of class
            if skip_lines:
                stripped = line.lstrip()
                # End when we hit a new top-level definition or empty line followed by definition
                if not line.strip():
                    # Check next line
                    if i + 1 < len(self.lines):
                        next_line = self.lines[i + 1]
                        if (next_line and not next_line.startswith(' ') and
                            (next_line.startswith('class ') or
                             next_line.startswith('def ') or
                             next_line.startswith('from ') or
                             next_line.startswith('import ') or
                             re.match(r'^\w+\s*=', next_line))):
                            skip_lines = False
                            current_class = None
                elif stripped and not line.startswith(' '):
                    # New top-level definition
                    if (stripped.startswith('class ') or
                        stripped.startswith('def ') or
                        stripped.startswith('from ') or
                        stripped.startswith('import ') or
                        re.match(r'^\w+\s*=', stripped)):
                        skip_lines = False
                        current_class = None
                        new_lines.append(line)
                        i += 1
                        continue

                i += 1
                continue

            new_lines.append(line)
            i += 1

        return new_lines

    def remove_redundant_aliases(self, lines: List[str]) -> List[str]:
        """Remove redundant numbered aliases."""
        new_lines = []
        for line in lines:
            stripped = line.strip()
            match = re.match(r'^(\w+)\s*=\s*(\w+)$', stripped)

            if match:
                alias, original = match.groups()
                # Remove if both have same base name
                alias_base = re.sub(r'\d+$', '', alias)
                original_base = re.sub(r'\d+$', '', original)

                if alias_base == original_base:
                    self.removed_aliases += 1
                    continue

            new_lines.append(line)

        return new_lines

    def add_imports(self, lines: List[str]) -> List[str]:
        """Add imports from tidas_data_types.py."""
        if not self.used_base_types:
            return lines

        # Find insertion point
        insert_idx = 0
        for i, line in enumerate(lines):
            if line.startswith('from __future__'):
                insert_idx = i + 1
                break

        # Create import statement
        sorted_types = sorted(self.used_base_types)
        import_lines = ['from .tidas_data_types import (']
        for type_name in sorted_types:
            import_lines.append(f'    {type_name},')
        import_lines.append(')')
        import_lines.append('')

        # Insert imports
        return lines[:insert_idx] + import_lines + lines[insert_idx:]

    def process(self) -> str:
        """Run all post-processing steps."""
        # Step 1: Replace type references
        content = self.replace_type_references()

        # Step 2: Detect used base types
        self.detect_used_base_types(content)

        # Step 3: Work with updated content
        lines = content.split('\n')
        self.lines = lines  # Update for class removal

        # Step 4: Remove duplicate class definitions
        lines = self.remove_duplicate_classes(lines)

        # Step 5: Remove redundant aliases
        lines = self.remove_redundant_aliases(lines)

        # Step 6: Add imports
        lines = self.add_imports(lines)

        return '\n'.join(lines)

    def save(self, output_path: Path = None) -> None:
        """Save processed content."""
        if output_path is None:
            output_path = self.file_path

        processed = self.process()
        output_path.write_text(processed, encoding='utf-8')

        print(f"✓ Processed {self.file_path.name}")
        if self.replacements_made:
            total_replacements = sum(self.replacements_made.values())
            print(f"  - Made {total_replacements} type reference replacements")
            # Show a few examples
            examples = list(self.replacements_made.items())[:3]
            for repl, count in examples:
                print(f"    • {repl} ({count}x)")
        if self.removed_classes:
            print(f"  - Removed {len(self.removed_classes)} duplicate class definitions")
        if self.removed_aliases > 0:
            print(f"  - Removed {self.removed_aliases} redundant aliases")
        if self.used_base_types:
            print(f"  - Added imports for {len(self.used_base_types)} base types")


def main():
    """Process all entity files."""
    script_dir = Path(__file__).parent
    types_dir = script_dir.parent / 'src' / 'tidas_sdk' / 'types'

    entity_files = [
        'tidas_contacts.py',
        'tidas_flows.py',
        'tidas_processes.py',
        'tidas_sources.py',
        'tidas_flowproperties.py',
        'tidas_unitgroups.py',
        'tidas_lciamethods.py',
        'tidas_lifecyclemodels.py',
    ]

    print("=" * 60)
    print("POST-PROCESSING GENERATED TYPE FILES")
    print("=" * 60)
    print()

    success_count = 0
    error_count = 0

    for filename in entity_files:
        file_path = types_dir / filename
        if file_path.exists():
            try:
                processor = TypeFilePostProcessor(file_path)
                processor.save()
                success_count += 1
                print()
            except Exception as e:
                print(f"✗ Error processing {filename}: {e}")
                import traceback
                traceback.print_exc()
                error_count += 1
        else:
            print(f"⚠️  File not found: {filename}")
            error_count += 1

    print("=" * 60)
    print("POST-PROCESSING SUMMARY")
    print("=" * 60)
    print(f"✅ Successfully processed: {success_count} files")
    if error_count > 0:
        print(f"❌ Errors: {error_count} files")
    print("=" * 60)

    return 0 if error_count == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
