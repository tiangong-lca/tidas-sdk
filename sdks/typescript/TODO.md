# TypeScript Non-Export Tools Migration TODO

Goal: absorb the non-export capabilities from `tidas-tools` into the TypeScript SDK, while keeping database / export / S3 features in `tidas-tools`.

Scope:
- XML <-> JS object conversion via `xmltodict`
- package/category validation on top of the existing parity module
- directory-level `.json <-> .xml` conversion utilities
- static asset copying for `tidas/` and `eilcd/`
- packaging and tests needed to ship the above in `@tiangong-lca/tidas-sdk`

Out of scope:
- database export
- zip publishing
- S3 download logic
- Python SDK changes

Status:
- [x] Phase 1: Add migration scaffolding and Node 24 baseline
- [x] Phase 2: Add XML module backed by Node `xmltodict`
- [x] Phase 3: Add runtime assets and asset-copy helpers
- [x] Phase 4: Add directory conversion tools and exports
- [x] Phase 5: Add tests for XML round-trip, asset copying, and directory conversion
- [x] Phase 6: Update docs, package exports, and verification scripts as needed
- [x] Phase 7: Run validation (`lint`, `typecheck`, `test`, `build`) and finalize
