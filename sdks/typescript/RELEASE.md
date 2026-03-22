# Release Guide for `@tiangong-lca/tidas-sdk`

This package is released through the repository-owned GitHub Actions flow in `.github/workflows/publish.yml`.

## Default Path

Use this sequence for normal releases:

1. Start from the latest `origin/main`.
2. Prepare a release PR that includes:
   - the TypeScript package version metadata bump
   - any generated source updates required by upstream schema changes
   - documentation updates that should ship with the release
3. Run repository validation:

```bash
./scripts/ci/verify-typescript-package.sh
```

4. Merge the PR.
5. Create a tag on the merged commit:

```bash
git tag typescript-vX.Y.Z
git push origin typescript-vX.Y.Z
```

6. Approve the `npm-release` environment in GitHub Actions.
7. Confirm the new version is visible on npm and installable.

## Versioning

- Use semantic versioning.
- The Git tag must match `sdks/typescript/package.json` exactly:
  - package version `0.1.30` -> tag `typescript-v0.1.30`
- TypeScript and Python releases are independent. Do not wait for a Python release just to publish TypeScript.

## Validation Details

`./scripts/ci/verify-typescript-package.sh` performs the same checks expected by CI:

- `npm ci`
- regenerate TypeScript artifacts from `tidas-tools`
- fail if generated source changes are not committed
- `npm run lint`
- `npm run typecheck`
- `npm test`
- `npm run build`
- `npm pack --dry-run`

If generation needs a specific local checkout of `tidas-tools`, provide it explicitly:

```bash
TIDAS_TOOLS_PATH=../tidas-tools ./scripts/ci/verify-typescript-package.sh
```

## Preparing the Version Bump

If you want a local helper for version editing without publishing, use:

```bash
npm run release:prepare:patch
npm run release:prepare:minor
npm run release:prepare:major
```

These commands only update local version metadata files. They do not publish, create a git tag, or push anything.

## Publish Automation

The publish workflow:

- only reacts to `typescript-v*` tags
- validates that the tag matches the version in source control
- reruns package verification
- publishes with npm provenance enabled

One-time maintainer configuration is documented in `../../docs/release-setup.md`.

## Fallback Publishing

Local `npm publish` is not the normal path.

Only use a local fallback if GitHub Actions or trusted publishing is unavailable and a maintainer explicitly decides to bypass CI. If that happens:

- record the reason in the release issue or PR
- publish from the exact merged release commit
- create the same `typescript-vX.Y.Z` tag after the manual publish if the version was successfully released

## Post-Release Checklist

- Confirm the npm package page shows the new version.
- Smoke-test install if the change is high risk:

```bash
npm install @tiangong-lca/tidas-sdk@X.Y.Z
```

- Create or update GitHub release notes if useful for consumers.
- If the release is part of tracked `lca-workspace` delivery, complete the later submodule integration step.
