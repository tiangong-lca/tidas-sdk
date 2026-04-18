---
title: tidas-sdk Validation Guide
docType: guide
scope: repo
status: active
authoritative: false
owner: tidas-sdk
language: en
whenToUse:
  - when a tidas-sdk change is ready for local validation
  - when deciding the minimum proof required for package, generation, automation, or docs changes
  - when writing PR validation notes for tidas-sdk work
whenToUpdate:
  - when the repo gains new canonical verify wrappers
  - when change categories require different proof
  - when release automation or upstream-resolution behavior changes
checkPaths:
  - ai/validation.md
  - ai/task-router.md
  - scripts/ci/**
  - sdks/typescript/**
  - sdks/python/**
  - docs/**
  - .github/workflows/**
lastReviewedAt: 2026-04-18
lastReviewedCommit: 5deaf6884cb7d78d9d23213fc0a90f6c2867af35
related:
  - ../AGENTS.md
  - ./repo.yaml
  - ./task-router.md
  - ./architecture.md
  - ../docs/release-setup.md
  - ../docs/upstream-automation.md
---

## Default Baseline

Unless the change is doc-only, the canonical verification scripts are:

```bash
./scripts/ci/verify-typescript-package.sh
./scripts/ci/verify-python-package.sh
```

These scripts are the best repo-wide proof because they mirror CI expectations and upstream-resolution behavior.

## Validation Matrix

| Change type | Minimum local proof | Additional proof when risk is higher | Notes |
| --- | --- | --- | --- |
| TypeScript package source or scripts | `./scripts/ci/verify-typescript-package.sh` | run the relevant example or focused local package script if the change touches one narrow feature | This verify script covers build, tests, generated artifacts, and packability. |
| Python package source, scripts, or tests | `./scripts/ci/verify-python-package.sh` | run one focused pytest or generation step when the change is isolated | Record if the Python package still depends on generated artifacts from a specific upstream commit. |
| shared generation helpers under `scripts/ci/**` | run both verify scripts | run the matching `generate-*.sh` path if the task explicitly changes refresh behavior | Generation changes can affect both packages even if only one output changed. |
| release setup, tag, or publish workflows | run both verify scripts | inspect `.github/workflows/**` and record any tag or environment assumptions checked locally | Tag creation and registry publication are separate from local package verification. |
| AI docs only | run repo-local `ai-doc-lint` against touched files or the equivalent local PR check | do one scenario-based routing check from root into this repo | Refresh review metadata even when prose-only docs change. |

## Upstream Resolution Notes

Facts that matter:

- TypeScript and Python generation resolve `tidas-tools` in this order:
  1. `TIDAS_TOOLS_PATH`
  2. sibling `../tidas-tools`
  3. temporary clone
- This means local verification may exercise different upstream content depending on the environment

If you intentionally validate against a local checkout, record that in the PR note.

## Minimum PR Note Quality

A good PR note for this repo should say:

1. which verify scripts ran
2. whether generation used a local `tidas-tools` checkout or the default resolution path
3. whether tag or publish proof is deferred to GitHub Actions
