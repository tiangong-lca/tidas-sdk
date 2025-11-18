# Release Guide for `tidas-sdk` (Python)

This document describes the process for publishing the TIDAS Python SDK to PyPI using [uv](https://docs.astral.sh/uv/) for environment management and command execution.

## Prerequisites

- Python 3.12 (matches the library target)
- uv installed (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- Access to the [tiangong-lca](https://pypi.org/user/tiangong-lca/) PyPI organization (or appropriate credentials)
- Git access to the `tiangong-lca/tidas-sdk` repository

## Pre-release Checklist

Complete these steps before cutting a release:

- [ ] Update `sdks/python/pyproject.toml` with the new version number
- [ ] Regenerate code or schemas if upstream inputs changed
- [ ] Documentation (`README.md`, `README-zh.md`, examples) reviewed for accuracy
- [ ] Install dependencies: `uv sync --group dev`
- [ ] Static checks succeed: `uv run ruff check`, `uv run ruff format --check`, `uv run mypy`
- [ ] Tests pass: `uv run pytest`
- [ ] Review `git diff` to ensure generated artifacts are committed

## Release Steps

### 1. Prepare the workspace

```bash
cd sdks/python
uv sync --group dev
```

Ensure the repository is up to date:

```bash
git checkout main
git pull origin main
```

### 2. Refresh generated SDK code (if schemas changed)

Update the bundled schemas and regenerate Pydantic models whenever `tidas-tools` (or other schema sources) change:

```bash
# Update submodules to pull latest schemas
git submodule update --init --recursive
git submodule update --remote tidas-tools

# Regenerate Python SDK artifacts
uv run python scripts/generate_sdk.py \
  --schemas ../../tidas-tools/src/tidas_tools/tidas/schemas \
  --output src/tidas_sdk/generated
```

Inspect the resulting diffs under `src/tidas_sdk/generated` and rerun the verification step inside the script output if needed.

### 3. Final verification

```bash
uv run ruff check src
uv run ruff format --check src
uv run mypy src
uv run pytest
```

### 4. Bump the version

1. Edit `pyproject.toml` and update the `[project] version` field.
2. Optionally update `CHANGELOG.md` (if maintained) with release notes.
3. Commit the version bump:

```bash
git commit -am "chore(python): release vX.Y.Z"
```

### 5. Build distributions

```bash
rm -rf dist build
uv run python -m build
uv run twine check dist/*
```

### 6. Publish to PyPI

```bash
# TestPyPI (optional dry run)
uv run twine upload --repository testpypi dist/*

# PyPI (official release)
uv run twine upload dist/*
```

Provide credentials when prompted or configure a `.pypirc` file for automation.

### 7. Tag and push

```bash
git tag python-vX.Y.Z
git push origin main --tags
```

### 8. Announce (optional)

- Create a GitHub release using the new tag and include key changes.
- Notify dependent teams or community channels.

## Troubleshooting

### Upload fails with 403

- Confirm you have publish rights on the organization.
- Ensure two-factor authentication tokens are configured if enforced.

### Build artifacts missing files

- Verify `MANIFEST.in` (if present) and `[tool.setuptools.package-data]` include required assets.
- Run builds from a clean tree (`git clean -xfd` for local cleanup if necessary).

### Version already exists

- Check published versions: `twine list tidas-sdk` or `pip install tidas-sdk==<version>` to confirm.
- Increment the version in `pyproject.toml` and rebuild.

## Useful Commands

```bash
# Clean environment
uv pip uninstall tidas-sdk

# Install built wheel locally
uv pip install dist/tidas_sdk-*.whl

# Inspect package metadata
uv run python -m importlib.metadata tidas-sdk
```

Keep this guide current—update when the release tooling or workflow changes.
