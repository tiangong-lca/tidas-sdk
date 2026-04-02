#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


REPO_ROOT = Path(__file__).resolve().parents[2]
PYTHON_PACKAGE = REPO_ROOT / "sdks/python/pyproject.toml"
TYPESCRIPT_PACKAGE = REPO_ROOT / "sdks/typescript/package.json"
PYTHON_VERSION_PATTERN = re.compile(r'(?m)^version = "(?P<version>\d+\.\d+\.\d+)"$')
SEMVER_PATTERN = re.compile(r"^(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)$")
HTTP_TIMEOUT_SECONDS = 15


@dataclass(frozen=True)
class PackageSpec:
    kind: str
    display_name: str
    registry_name: str
    metadata_path: Path
    registry_label: str


PACKAGE_SPECS = {
    "typescript": PackageSpec(
        kind="typescript",
        display_name="@tiangong-lca/tidas-sdk",
        registry_name="@tiangong-lca/tidas-sdk",
        metadata_path=TYPESCRIPT_PACKAGE,
        registry_label="npm",
    ),
    "python": PackageSpec(
        kind="python",
        display_name="tidas-sdk",
        registry_name="tidas-sdk",
        metadata_path=PYTHON_PACKAGE,
        registry_label="PyPI",
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Resolve and validate release versions against npm and PyPI."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    next_version_parser = subparsers.add_parser(
        "next-version",
        help="Print the next safe package version after applying the requested bump.",
    )
    next_version_parser.add_argument(
        "--package",
        required=True,
        choices=sorted(PACKAGE_SPECS),
        help="Package family to inspect.",
    )
    next_version_parser.add_argument(
        "--part",
        required=True,
        choices=("major", "minor", "patch"),
        help="Semantic version segment to increment.",
    )

    assert_parser = subparsers.add_parser(
        "assert-unpublished",
        help="Fail when the target package version already exists in the registry.",
    )
    assert_parser.add_argument(
        "--package",
        required=True,
        choices=sorted(PACKAGE_SPECS),
        help="Package family to inspect.",
    )
    assert_parser.add_argument(
        "--version",
        help="Specific version to check. Defaults to the version in repository metadata.",
    )

    return parser.parse_args()


def parse_version(raw: str) -> tuple[int, int, int]:
    match = SEMVER_PATTERN.fullmatch(raw.strip())
    if match is None:
        raise ValueError(f"unsupported semantic version '{raw}'")
    return tuple(int(match.group(part)) for part in ("major", "minor", "patch"))


def format_version(parts: tuple[int, int, int]) -> str:
    return ".".join(str(piece) for piece in parts)


def bump_version(version: str, part: str) -> str:
    major, minor, patch = parse_version(version)
    if part == "major":
        return format_version((major + 1, 0, 0))
    if part == "minor":
        return format_version((major, minor + 1, 0))
    return format_version((major, minor, patch + 1))


def load_repository_version(spec: PackageSpec) -> str:
    raw = spec.metadata_path.read_text(encoding="utf-8")
    if spec.kind == "typescript":
        return json.loads(raw)["version"]

    match = PYTHON_VERSION_PATTERN.search(raw)
    if match is None:
        raise ValueError(f"could not locate Python version in {spec.metadata_path}")
    return match.group("version")


def load_json(url: str) -> dict:
    request = Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "tidas-sdk-release-automation/1.0",
        },
    )
    try:
        with urlopen(request, timeout=HTTP_TIMEOUT_SECONDS) as response:
            return json.load(response)
    except HTTPError as exc:
        if exc.code == 404:
            return {}
        raise RuntimeError(f"failed to fetch {url}: HTTP {exc.code}") from exc
    except URLError as exc:
        raise RuntimeError(f"failed to fetch {url}: {exc.reason}") from exc


def iter_registry_versions(spec: PackageSpec) -> Iterable[str]:
    if spec.kind == "typescript":
        payload = load_json(
            f"https://registry.npmjs.org/{quote(spec.registry_name, safe='')}"
        )
        versions = payload.get("versions", {})
        return versions.keys()

    payload = load_json(f"https://pypi.org/pypi/{quote(spec.registry_name, safe='')}/json")
    releases = payload.get("releases", {})
    return releases.keys()


def published_versions(spec: PackageSpec) -> list[str]:
    versions: list[str] = []
    for version in iter_registry_versions(spec):
        try:
            parse_version(version)
        except ValueError:
            continue
        versions.append(version)
    return sorted(versions, key=parse_version)


def latest_published_version(versions: list[str]) -> str | None:
    if not versions:
        return None
    return max(versions, key=parse_version)


def resolve_next_version(spec: PackageSpec, part: str) -> str:
    repo_version = load_repository_version(spec)
    published = published_versions(spec)
    latest_published = latest_published_version(published)
    base_version = repo_version

    if latest_published is not None and parse_version(latest_published) > parse_version(base_version):
        base_version = latest_published

    next_version = bump_version(base_version, part)

    published_note = latest_published if latest_published is not None else "none"
    print(
        (
            f"Resolved {spec.display_name} release version: repo={repo_version}, "
            f"latest_published={published_note}, base={base_version}, "
            f"bump={part}, next={next_version}"
        ),
        file=sys.stderr,
    )
    return next_version


def assert_unpublished(spec: PackageSpec, version: str | None) -> str:
    target_version = version or load_repository_version(spec)
    parse_version(target_version)

    published = published_versions(spec)
    latest_published = latest_published_version(published)
    if target_version in published:
        published_note = latest_published if latest_published is not None else "unknown"
        raise SystemExit(
            (
                f"error: {spec.display_name} version {target_version} already exists in "
                f"{spec.registry_label}. Latest published version: {published_note}."
            )
        )

    published_note = latest_published if latest_published is not None else "none"
    print(
        (
            f"Validated {spec.display_name} version {target_version} is not yet published "
            f"to {spec.registry_label}. Latest published version: {published_note}."
        )
    )
    return target_version


def main() -> int:
    args = parse_args()
    spec = PACKAGE_SPECS[args.package]

    if args.command == "next-version":
        print(resolve_next_version(spec, args.part))
        return 0

    assert_unpublished(spec, args.version)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
