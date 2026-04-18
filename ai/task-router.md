---
title: tidas-sdk Task Router
docType: router
scope: repo
status: active
authoritative: false
owner: tidas-sdk
language: en
whenToUse:
  - when you already know the task belongs in tidas-sdk but need the right next file or next doc
  - when deciding whether a change belongs in TypeScript package code, Python package code, generation scripts, or another repo
  - when routing between SDK work and handoffs to tidas-tools, tidas, or lca-workspace
whenToUpdate:
  - when new package surfaces or release flows appear
  - when upstream-generation boundaries change
  - when validation routing becomes misleading
checkPaths:
  - AGENTS.md
  - ai/repo.yaml
  - ai/task-router.md
  - ai/validation.md
  - ai/architecture.md
  - scripts/ci/**
  - sdks/typescript/**
  - sdks/python/**
  - docs/**
lastReviewedAt: 2026-04-18
lastReviewedCommit: 5deaf6884cb7d78d9d23213fc0a90f6c2867af35
related:
  - ../AGENTS.md
  - ./repo.yaml
  - ./validation.md
  - ./architecture.md
  - ../docs/release-setup.md
  - ../docs/upstream-automation.md
---

## Repo Load Order

When working inside `tidas-sdk`, load docs in this order:

1. `AGENTS.md`
2. `ai/repo.yaml`
3. this file
4. `ai/validation.md` or `ai/architecture.md`
5. `docs/upstream-automation.md` or `docs/release-setup.md` only when automation or publishing is part of the task

## High-Frequency Task Routing

| Task intent | First code paths to inspect | Next docs to load | Notes |
| --- | --- | --- | --- |
| Change TypeScript package API, runtime assets, or generated schemas | `sdks/typescript/src/**`, `sdks/typescript/scripts/**`, `sdks/typescript/package.json` | `ai/validation.md`, `ai/architecture.md` | This package mirrors only the non-export part of `tidas-tools`. |
| Change Python SDK models or tests | `sdks/python/src/**`, `sdks/python/scripts/**`, `sdks/python/tests/**`, `sdks/python/pyproject.toml` | `ai/validation.md`, `ai/architecture.md` | This repo owns the generated Python SDK surface, not standalone tooling. |
| Change upstream refresh behavior | `scripts/ci/generate-typescript-sdk.sh`, `scripts/ci/generate-python-sdk.sh`, `scripts/ci/lib/tidas-tools-source.sh` | `ai/validation.md`, `ai/architecture.md`, `docs/upstream-automation.md` | Current generation resolves `tidas-tools` first, not the docs site. |
| Change verify, tag, or publish flow | `scripts/ci/verify-*.sh`, `scripts/ci/check-release-tag.sh`, `scripts/ci/release-version.py`, `.github/workflows/**` | `ai/validation.md`, `docs/release-setup.md`, `docs/upstream-automation.md` | Tag-driven release is the normal path. |
| Change spec/docs-site wording only | `tidas`, not this repo | root `ai/task-router.md` | Public spec docs live in `tidas`. |
| Change standalone conversion, export, or methodology assets | `tidas-tools`, not this repo | root `ai/task-router.md` | `tidas-tools` is the executable upstream for current package refreshes. |
| Change repo-local AI-doc maintenance only | `AGENTS.md`, `ai/**`, `.github/workflows/ai-doc-lint.yml`, `.github/scripts/ai-doc-lint.*` | `ai/validation.md` when present, otherwise `ai/repo.yaml` | Keep the repo-local maintenance gate aligned with root `ai/ci-lint-spec.md` and `ai/review-matrix.md`. |
| Decide whether work is delivery-complete after merge | root workspace docs, not repo code paths | root `AGENTS.md`, `_docs/workspace-branch-policy-contract.md` | Root integration remains a separate phase. |

## Wrong Turns To Avoid

### Treating tidas as the immediate generation upstream

If the task is about generated package output, start by checking `tidas-tools`. The docs site is not the current executable upstream.

### Moving standalone tooling into the SDK package

Conversion, export, and batch validation still belong in `tidas-tools`.

### Treating generated output as the only source of truth

When generation behavior changes, update the scripts and package docs that explain the source, not only the generated files.

## Cross-Repo Handoffs

Use these handoffs when work crosses boundaries:

1. upstream schema or methodology change drives SDK refresh
   - start in `tidas-tools`
   - then update `tidas-sdk`
2. public spec/docs wording change
   - route to `tidas`
3. merged repo PR still needs to ship through the workspace
   - return to `lca-workspace`
   - do the submodule pointer bump there
