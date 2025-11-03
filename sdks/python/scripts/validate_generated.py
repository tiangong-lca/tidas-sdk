#!/usr/bin/env python3
"""Validate generated types."""

import sys
from pathlib import Path


def check_files_exist():
    """Check all expected files exist."""
    types_dir = Path("src/tidas_sdk/types")
    expected = 18  # 18 schemas

    py_files = list(types_dir.glob("tidas_*.py"))
    actual = len(py_files)

    if actual != expected:
        print(f"❌ Expected {expected} files, found {actual}")
        return False

    print(f"✅ All {expected} type files exist")
    return True


def check_imports():
    """Check files can be imported."""
    try:
        from tidas_sdk.types import tidas_contacts
        from tidas_sdk.types import tidas_flows
        print("✅ Type files can be imported")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False


def main():
    """Run all checks."""
    checks = [
        check_files_exist,
        check_imports,
    ]

    results = [check() for check in checks]

    if all(results):
        print("\n✅ All validation checks passed!")
        return 0
    else:
        print("\n❌ Some validation checks failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
