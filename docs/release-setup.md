# Release Setup

This document captures the one-time repository and registry configuration required for the `tidas-sdk` release workflows.

## GitHub Repository

Create these protected environments in `tiangong-lca/tidas-sdk`:

- `npm-release`
- `pypi-release`

Recommended settings for both environments:

- required reviewers enabled
- prevent self-review enabled
- only maintainers who can approve package releases listed as reviewers

The publish workflow file is fixed at:

- `.github/workflows/publish.yml`

Do not rename that workflow file without updating the registry-side trusted publisher configuration.

## npm Trusted Publisher

Configure Trusted Publishing for `@tiangong-lca/tidas-sdk` on npm with:

- organization or user: `tiangong-lca`
- repository: `tidas-sdk`
- workflow filename: `publish.yml`
- environment name: `npm-release`

The TypeScript publish job expects tags named `typescript-vX.Y.Z`.

## PyPI Trusted Publisher

Configure a Trusted Publisher for project `tidas-sdk` on PyPI with:

- owner: `tiangong-lca`
- repository name: `tidas-sdk`
- workflow filename: `publish.yml`
- environment name: `pypi-release`

The Python publish job expects tags named `python-vX.Y.Z`.

If the PyPI project does not exist yet, register a pending publisher first so the first trusted publish can create it.

## Repository Settings

- GitHub Actions must be enabled for the repository.
- GitHub-hosted runners must be used for trusted publishing.
- Maintainers should avoid long-lived `NPM_TOKEN` / `PYPI_API_TOKEN` secrets once Trusted Publishing is configured.

## Operational Notes

- `publish.yml` validates that the Git tag matches the package version before upload.
- npm and PyPI releases are independent; configure both publishers even if only one package is released initially.
- If a repository or package rename ever happens, update both the workflow and the trusted publisher registration before the next release.
