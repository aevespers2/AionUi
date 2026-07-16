# Release Plan

## Current Decision
Status: `BLOCKED`

No AionUi work is currently releasable. P0 repository-health work is only `READY`, `punchlist.md` is absent, the Builder log contains no verification evidence, and reviewed commit `4b552d9154b45ff66a19c813640a1ad104bebd28` has no reported commit-status checks.

## Versioning
- Scheme: Semantic Versioning.
- First eligible implementation candidate: `0.1.0-alpha.1`.
- Pre-release identifiers are required until the UI purpose, supported platforms, compatibility contract, and end-to-end acceptance path are verified.

## Candidate Scope
- Repository health and dependency baseline.
- Defined UI purpose, target users, supported runtimes, and backend/API assumptions.
- One bounded user workflow with reproducible build, lint, type, unit, integration, and smoke-test evidence.
- Accessibility, error-state, configuration, security, and rollback documentation.

## Selected Completed Work
None. Coordination files and `changelog.md` do not establish a tested UI release.

## Planned Changelog Entries
- `Added`: first bounded, verified user workflow.
- `Changed`: documented runtime, configuration, and compatibility assumptions.
- `Fixed`: defects found during the baseline and smoke-test pass.
- `Security`: dependency, secret, content-handling, and workflow-permission findings.
- `Documentation`: setup, user workflow, accessibility, and rollback guidance.

## Acceptance Gates
| Gate | Status | Requirement |
|---|---|---|
| Task completion | FAIL | P0 completed and next bounded implementation task reaches `DONE`. |
| Build/static validation | NO EVIDENCE | Clean install/build, formatting, lint, type, and configuration checks pass. |
| Tests | NO EVIDENCE | Unit/integration/UI smoke tests pass on supported platforms. |
| Security | NO EVIDENCE | Dependency, secret, browser/content, and CI permission checks pass. |
| Accessibility | NO EVIDENCE | Keyboard path, labels, contrast, focus, and error-state checks recorded. |
| Documentation | NO EVIDENCE | Setup, configuration, workflow, limitations, and rollback are current. |
| Provenance | NO EVIDENCE | Build inputs, commit, tool versions, artifact hashes, and commands recorded. |
| Approval | PENDING | Release approval after every blocking gate passes. |

## Artifact Requirements
- Reproducible UI build bundle and source archive.
- Test, lint, type, accessibility, and security reports.
- Software bill of materials where dependencies are packaged.
- Checksums and provenance manifest for every distributable artifact.

## Rollback Criteria
Withdraw or roll back if the primary workflow fails, accessibility regressions block use, backend/API compatibility is broken, severe dependency/security findings appear, or artifact hashes cannot be reproduced. Rollback returns to the last verified tag; before the first tag, remove the candidate release and restore the reviewed pre-release commit.

## Unresolved Blockers
- Repository-health baseline is incomplete.
- Product purpose and first bounded UI workflow are not yet release-defined.
- `punchlist.md`, test evidence, security evidence, accessibility evidence, and provenance are missing.
- No CI status is attached to the reviewed commit.

## Release Log
- 2026-07-16: Initial AionUi candidate held `BLOCKED`; no completed work selected.