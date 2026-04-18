---
title: tidas-sdk AI Working Guide
docType: contract
scope: repo
status: active
authoritative: true
owner: tidas-sdk
language: en
whenToUse:
  - when a task may change generated TypeScript or Python SDK surfaces, package release automation, or the upstream-refresh workflow
  - when routing work from the workspace root into tidas-sdk
  - when deciding whether a change belongs here, in tidas-tools, in tidas, or in lca-workspace
whenToUpdate:
  - when package ownership or upstream-generation rules change
  - when release or verification scripts change
  - when the repo-local AI bootstrap docs under ai/ change
checkPaths:
  - AGENTS.md
  - README.md
  - docs/**
  - ai/**/*.md
  - ai/**/*.yaml
  - package.json
  - scripts/ci/**
  - sdks/typescript/**
  - sdks/python/**
  - .github/workflows/**
lastReviewedAt: 2026-04-18
lastReviewedCommit: 5deaf6884cb7d78d9d23213fc0a90f6c2867af35
related:
  - ai/repo.yaml
  - ai/task-router.md
  - ai/validation.md
  - ai/architecture.md
  - docs/release-setup.md
  - docs/upstream-automation.md
---

## Repo Contract

`tidas-sdk` owns the generated developer package surface for TIDAS: the published TypeScript package, the in-repo Python SDK, and the release automation that verifies and publishes them. Start here when the task may change SDK outputs, package metadata, or upstream-refresh automation.

## AI Load Order

Load docs in this order:

1. `AGENTS.md`
2. `ai/repo.yaml`
3. `ai/task-router.md`
4. `ai/validation.md`
5. `ai/architecture.md`
6. `docs/upstream-automation.md` or `docs/release-setup.md` only when the task touches automation or publishing

Do not assume the spec docs site is the immediate executable upstream. In current practice, `tidas-tools` is the generation upstream for both SDK packages.

## Repo Ownership

This repo owns:

- `sdks/typescript/**` for the published `@tiangong-lca/tidas-sdk` package
- `sdks/python/**` for the in-repo Python SDK surface
- `scripts/ci/**` for generation, verify, and publish helpers
- `.github/workflows/**` for CI, upstream sync, tag automation, and publish workflows
- `docs/release-setup.md` and `docs/upstream-automation.md` for release and automation contracts

This repo does not own:

- standalone conversion, export, or batch validation tooling
- the public spec/docs site
- workspace integration state after merge

Route those tasks to:

- `tidas-tools` for generation upstream, runtime assets, methodologies, and standalone tooling behavior
- `tidas` for spec/docs-site content
- `lca-workspace` for root integration after merge

## Runtime Facts

- Root package manager: `npm`
- Published packages:
  - `@tiangong-lca/tidas-sdk` from `sdks/typescript/`
  - `tidas-sdk` from `sdks/python/`
- The canonical verification scripts are:
  - `./scripts/ci/verify-typescript-package.sh`
  - `./scripts/ci/verify-python-package.sh`
- The upstream refresh helpers are:
  - `./scripts/ci/generate-typescript-sdk.sh`
  - `./scripts/ci/generate-python-sdk.sh`

## Hard Boundaries

- Do not treat `tidas` as the immediate code-generation upstream when the actual refresh path depends on `tidas-tools`
- Do not move standalone conversion or export logic into the SDK packages
- Do not treat a merged repo PR here as workspace-delivery complete if the root repo still needs a submodule bump

## Workspace Integration

A merged PR in `tidas-sdk` is repo-complete, not delivery-complete.

If the change must ship through the workspace:

1. merge the child PR into `tidas-sdk`
2. update the `lca-workspace` submodule pointer deliberately
3. complete any later workspace-level validation that depends on the updated SDK snapshot
