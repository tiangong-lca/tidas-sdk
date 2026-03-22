# Release Guide for `tidas-sdk` (Python)

This package is released through the repository-owned GitHub Actions flow in `.github/workflows/publish.yml`.

## Default Path

Use this sequence for normal releases:

1. Start from the latest `origin/main`.
2. Prepare a release PR that includes:
   - the `pyproject.toml` version bump
   - any regenerated models required by upstream schema changes
   - documentation updates that should ship with the release
3. Run repository validation:

```bash
./scripts/ci/verify-python-package.sh
```

4. Merge the PR.
5. Create a tag on the merged commit:

```bash
git tag python-vX.Y.Z
git push origin python-vX.Y.Z
```

6. Approve the `pypi-release` environment in GitHub Actions.
7. Confirm the new version is visible on PyPI and installable.

## Versioning

- Use semantic versioning.
- The Git tag must match `sdks/python/pyproject.toml` exactly:
  - package version `0.1.6` -> tag `python-v0.1.6`
- Python and TypeScript releases are independent. Do not bundle them unless both packages actually need a release.

## Validation Details

`./scripts/ci/verify-python-package.sh` performs the same checks expected by CI:

- `uv sync --group dev`
- regenerate Python artifacts from `tidas-tools`
- fail if generated source changes are not committed
- `uv run ruff check src tests`
- `uv run pytest`
- `uv run python -m build`
- `uv run twine check dist/*`

If generation needs a specific local checkout of `tidas-tools`, provide it explicitly:

```bash
TIDAS_TOOLS_SOURCE_MODE=auto TIDAS_TOOLS_PATH=../tidas-tools ./scripts/ci/verify-python-package.sh
```

## Publish Automation

The publish workflow:

- only reacts to `python-v*` tags
- validates that the tag matches the version in source control
- rebuilds distributions from the tagged commit
- publishes via PyPI Trusted Publishing after environment approval

One-time maintainer configuration is documented in `../../docs/release-setup.md`.

## Fallback Publishing

Local publishing is not the normal path.

The repository retains `scripts/ci/publish-python-sdk.sh` only as an emergency fallback for maintainers. Use it only when GitHub Actions or trusted publishing is unavailable and the release cannot wait. If that happens:

- publish from the exact merged release commit
- record the reason in the release issue or PR
- create the matching `python-vX.Y.Z` tag after the manual release succeeds

## Post-Release Checklist

- Confirm the PyPI project page shows the new version.
- Smoke-test install if the change is high risk:

```bash
uv pip install tidas-sdk==X.Y.Z
```

- Create or update GitHub release notes if useful for consumers.
- If the release is part of tracked `lca-workspace` delivery, complete the later submodule integration step.
