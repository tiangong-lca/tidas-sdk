# AGENTS.md — tidas-sdk Release & Delivery Guide

This repository publishes two independently versioned packages:

- `@tiangong-lca/tidas-sdk` from `sdks/typescript/`
- `tidas-sdk` from `sdks/python/`

## Default Delivery Rules

- Start all new repo work from the latest `origin/main` unless the work is intentionally stacked on another branch.
- Use a dedicated issue branch such as `feature/issue-<id>` or `chore/issue-<id>`.
- Keep human-managed package release prep in a normal PR.
- The upstream sync automation may push automation branches and open release-prep PRs when `tiangong-lca/tidas-tools` changes.
- If this repo change is consumed by `lca-workspace`, complete the later submodule bump before treating the parent delivery as fully done.

## Release Model

Normal releases follow this path:

1. Open a release-prep PR from `origin/main`.
2. Update only the package that is being released:
   - version metadata
   - release notes / changelog content when maintained
   - generated artifacts if upstream schemas changed
   - package docs if install or API guidance changed
3. Let CI validate the package with the same commands used by release automation.
4. Merge the PR.
5. Let the repository automation create a tag on the merged commit:
   - TypeScript: `typescript-vX.Y.Z`
   - Python: `python-vX.Y.Z`
6. GitHub Actions publishes from that immutable tagged commit after the protected release environment is approved.
7. If the auto-tagging workflow is unavailable, a maintainer may create the matching tag manually as a fallback.
8. Verify the published package, create or update the GitHub Release note if needed, and close out the tracked issue / PR state.

Releases are package-specific. Do not force the TypeScript and Python packages to share a version number or a release date.

## CI/CD Contract

Repository workflows live under `.github/workflows/`:

- `ci.yml`
  - validates package build, tests, generated artifacts, and packability on pull requests and `main`
- `sync-from-tidas-tools.yml`
  - regenerates SDK artifacts from an exact upstream `tiangong-lca/tidas-tools` commit
  - bumps only affected package versions
  - opens or updates a release-prep PR on an automation branch
- `tag-release-from-merge.yml`
  - watches pushes to `main`
  - creates package tags when a merged commit changes package versions
- `publish.yml`
  - publishes only from package tags
  - refuses to publish if the tag does not match the package version in source control

Package tags are the only supported path for routine publishing:

- `typescript-v*` triggers npm publish for `@tiangong-lca/tidas-sdk`
- `python-v*` triggers PyPI publish for `tidas-sdk`

Do not move formal package publishing into reusable workflows. PyPI Trusted Publishing currently requires a concrete workflow file in `.github/workflows/publish.yml`.

## Protected Release Environments

The publish workflow currently requires one GitHub environment:

- `pypi-release`

`pypi-release` should require reviewer approval and should not allow self-review. `npm-release` is optional and should only be added if TypeScript publishes are later gated with a GitHub environment. The one-time registry and repository setup lives in `docs/release-setup.md`.

Automation that pushes branches, opens PRs, or creates tags also requires the repository secret `TIDAS_RELEASE_AUTOMATION_TOKEN`.

## Local Validation

Run these before opening a release-prep PR when the corresponding package is affected:

```bash
./scripts/ci/verify-typescript-package.sh
./scripts/ci/verify-python-package.sh
```

These verification scripts default to a fresh temporary clone of `tiangong-lca/tidas-tools` so local validation matches CI. If you intentionally want to validate against a local checkout instead, set `TIDAS_TOOLS_SOURCE_MODE=auto` and optionally `TIDAS_TOOLS_PATH=/path/to/tidas-tools`.

## Local Publish Fallback

Local publishing is an emergency-only fallback for platform outages or broken CI infrastructure.

- Preferred path: GitHub Actions + Trusted Publishing
- Fallback path: local maintainer publish with an issue / PR comment recording why CI release was bypassed

The existing `scripts/ci/publish-python-sdk.sh` helper is retained only for that fallback path. If a manual fallback release happens, update the durable GitHub record in the same working session.

## Post-Release Checklist

- Confirm the registry shows the new version.
- Confirm install / metadata sanity:
  - npm: package page, provenance badge, install smoke test if needed
  - PyPI: project page, version metadata, install smoke test if needed
- Create or update release notes for the tagged commit when useful.
- If the package release was part of tracked workspace delivery, complete the later `lca-workspace` integration step and move the related Project / Issue / PR items to `Done`.
