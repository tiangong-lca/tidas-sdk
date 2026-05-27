---
title: TIDAS SDKs
docType: guide
scope: repo
status: active
authoritative: false
owner: tidas-sdk
language: en
whenToUse:
  - when getting oriented to the tidas-sdk repository
  - when looking for package locations, setup commands, or verification entrypoints
whenToUpdate:
  - when package status, setup commands, generation flow, or verification entrypoints change
checkPaths:
  - README.md
  - AGENTS.md
  - docs/agents/repo-validation.md
  - docs/agents/repo-architecture.md
  - sdks/typescript/**
  - sdks/python/**
  - scripts/ci/**
lastReviewedAt: 2026-05-22
lastReviewedCommit: 893aa12cab10d0a6791e8c8aa42bb2624d665ee8
---

# TIDAS SDKs

A multi-language SDK repository for TIDAS (TianGong Life Cycle Assessment data format), providing the generated TypeScript package, the in-repo Python SDK, and the automation that refreshes and releases them from `tidas-tools`.

## AI Docs Entry

For AI-first repo work, load docs in this order:

1. [AGENTS.md](./AGENTS.md)
2. [.docpact/config.yaml](./.docpact/config.yaml)
3. [docs/agents/repo-validation.md](./docs/agents/repo-validation.md) or [docs/agents/repo-architecture.md](./docs/agents/repo-architecture.md)
4. [docs/upstream-automation.md](./docs/upstream-automation.md) or [docs/release-setup.md](./docs/release-setup.md) when automation or publishing is part of the task

## Quick Start

### TypeScript SDK

```bash
npm install @tiangong-lca/tidas-sdk
```

### Python SDK (Development)

```bash
cd sdks/python && uv sync
```

### Upstream Tools

`tidas-tools` remains the executable upstream for generation, runtime assets, and standalone tooling behavior:

```bash
pip install tidas-tools
```

## Available Packages

### @tiangong-lca/tidas-sdk (TypeScript)

- Status: production package
- Features: type-safe data manipulation, validation, XML conversion, directory tools, and packaged runtime assets
- Installation: `npm install @tiangong-lca/tidas-sdk`
- Location: `sdks/typescript/`

### tidas-sdk (Python, Development)

- Status: in development
- Features: generated Python models, validation helpers, and utilities
- Installation: source-only for now
- Location: `sdks/python/`

### tidas-tools (External Upstream)

- Status: separate upstream package
- Role: generation source, upstream schemas/assets, and standalone conversion / export tooling
- Repository: `tiangong-lca/tidas-tools`

## Documentation

- Repository Contract: [AGENTS.md](./AGENTS.md)
- Validation Guide: [docs/agents/repo-validation.md](./docs/agents/repo-validation.md)
- Architecture Notes: [docs/agents/repo-architecture.md](./docs/agents/repo-architecture.md)
- Release Setup: [docs/release-setup.md](./docs/release-setup.md)
- Upstream Automation Design: [docs/upstream-automation.md](./docs/upstream-automation.md)
- TypeScript Release Guide: [sdks/typescript/RELEASE.md](./sdks/typescript/RELEASE.md)
- Python Release Guide: [sdks/python/RELEASE.md](./sdks/python/RELEASE.md)

## Development

### Prerequisites

- TypeScript SDK: Node.js 24+, npm
- Python SDK: Python 3.12+, uv

### Setup

#### TypeScript SDK

```bash
cd sdks/typescript
npm install
npm run build
npm test
```

#### Python SDK

```bash
cd sdks/python
uv sync
uv run pytest
uv run mypy .
```

#### Refresh Upstream TIDAS Sources

```bash
./scripts/ci/generate-typescript-sdk.sh
./scripts/ci/generate-python-sdk.sh
```

Both generation scripts resolve `tidas-tools` in this order:

1. `TIDAS_TOOLS_PATH`
2. a sibling checkout at `../tidas-tools`
3. a temporary clone of `tiangong-lca/tidas-tools`

For the TypeScript package, this refresh also syncs the packaged runtime conversion assets copied from `tidas-tools/src/tidas_tools/{tidas,eilcd}`.

### Release Workflow

Normal releases are tag-driven and published by GitHub Actions:

- TypeScript package: `typescript-vX.Y.Z`
- Python package: `python-vX.Y.Z`

Use these local verification commands before opening a release PR:

```bash
./scripts/ci/verify-typescript-package.sh
./scripts/ci/verify-python-package.sh
```

The local `pre-push` hook runs docpact and then both verification scripts. The repository `CI` workflow is manual-dispatch only; package tags and publish workflows still verify the relevant package before release.

If you want `tidas-tools` changes to automatically regenerate and release these packages, see [docs/upstream-automation.md](./docs/upstream-automation.md).

## Current Status

### Completed

- TypeScript SDK with committed schemas and runtime assets
- XML conversion and directory tooling for the non-export `tidas-tools` workflow
- Python SDK code generation and validation helpers
- Tag-driven release automation for TypeScript and Python packages

### In Progress

- Python SDK maturation and test coverage improvements
- cross-repository automation from `tidas-tools` into `tidas-sdk`

## Contributing

Review [AGENTS.md](./AGENTS.md) first for:

- repo boundaries
- validation expectations
- branch and delivery rules
- workspace integration expectations
