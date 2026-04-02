#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from pathlib import Path

VERSION_PATTERN = re.compile(r'(?m)^version = "(?P<version>\d+\.\d+\.\d+)"$')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Bump or set the Python SDK version in sdks/python/pyproject.toml."
    )
    parser.add_argument(
        "part",
        nargs="?",
        choices=("major", "minor", "patch"),
        help="Semantic version segment to increment.",
    )
    parser.add_argument(
        "--version",
        help="Set an exact semantic version instead of incrementing one segment.",
    )
    parser.add_argument(
        "--file",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "sdks/python/pyproject.toml",
        help="Path to the pyproject.toml file to update.",
    )
    return parser.parse_args()


def validate_version(version: str) -> str:
    if VERSION_PATTERN.fullmatch(f'version = "{version}"') is None:
        raise ValueError(f"unsupported semantic version '{version}'")
    return version


def bump_version(version: str, part: str) -> str:
    major, minor, patch = (int(piece) for piece in version.split("."))
    if part == "major":
        return f"{major + 1}.0.0"
    if part == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def main() -> int:
    args = parse_args()
    if bool(args.part) == bool(args.version):
        raise SystemExit("error: provide exactly one of <part> or --version")

    content = args.file.read_text(encoding="utf-8")
    match = VERSION_PATTERN.search(content)
    if match is None:
        raise SystemExit(f"error: could not find a version entry in {args.file}")

    current_version = match.group("version")
    next_version = validate_version(args.version) if args.version else bump_version(current_version, args.part)
    updated = VERSION_PATTERN.sub(f'version = "{next_version}"', content, count=1)
    args.file.write_text(updated, encoding="utf-8")
    print(next_version)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
