# Release Plan

## Current Decision
Status: `BLOCKED — FORK AND DISTRIBUTION DECISION REQUIRED`

This repository contains an existing Electron application identified as AionUi `1.7.0`, with a lockfile, build/package commands, linting, formatting, Jest suites, and cross-platform distribution scripts. It is not an empty pre-alpha project. No aevespers2 release is eligible, however, because P0 is not complete, `punchlist.md` is absent, no current CI/check result is attached to reviewed implementation head `74dc849efaa1e8a386029ccfc6a889b6a754a220`, and the relationship to the upstream AionUi project and intended distribution identity have not been approved.

## Versioning
- Preserve the existing application version line beginning at `1.7.0`; do not reset to `0.1.0`.
- Before publishing, decide whether this repository is a mirror, a maintained fork, or an independently distributed derivative.
- A documentation-only fork-baseline candidate may use `1.7.0-aevespers.1` without implying new product functionality.
- Functional changes must be classified against the upstream `1.7.0` baseline and use a clearly differentiated pre-release or fork version until compatibility and ownership are settled.

## Candidate Scope
- Record the exact upstream/fork baseline, divergence, license/notice obligations, product identity, supported platforms, and distribution channels.
- Reproduce `npm ci`, lint, format check, Jest unit/contract/integration suites, and Electron build/package commands.
- Verify macOS, Windows, Linux, and web/remote modes included in the candidate.
- Review authentication, local storage, SQLite, network listeners, remote access, updates, document parsing, model/provider credentials, and Electron security settings.
- Verify accessibility and the primary user workflows.
- Produce signed or explicitly unsigned artifacts with checksums, SBOM, provenance, and rollback instructions.

## Existing Candidate Assets
- `package.json` and `package-lock.json` identify AionUi version `1.7.0` and a reproducible npm lockfile.
- Build, package, lint, format, Jest, contract, integration, and platform-distribution scripts are defined.
- Apache-2.0 licensing is declared.

These are inherited or existing implementation assets, not evidence that an aevespers2 distribution is approved or releasable.

## Selected Completed Work
None. No locally defined task is `DONE`, no candidate divergence is approved, and no complete test/security/build/provenance bundle is tied to an immutable release commit.

## Planned Changelog Entries
- `Fork`: recorded upstream baseline, divergence, attribution, and product/distribution identity.
- `Changed`: only changes made after the approved baseline, separated from upstream history.
- `Security`: Electron hardening, dependency/secret review, remote-access and credential-boundary findings.
- `Documentation`: supported platforms, setup, user workflows, accessibility, artifact signing, update behavior, and rollback.
- `Release`: checksummed platform artifacts, SBOM, provenance, and approval decision.

## Acceptance Gates
| Gate | Status | Requirement |
|---|---|---|
| Fork/product decision | BLOCKED | Approve mirror vs maintained fork vs independent derivative, naming, upstream attribution, and distribution channels. |
| Task completion | FAIL | P0 completed, `punchlist.md` created, and included work marked `DONE` with evidence. |
| Install/build | NO CURRENT EVIDENCE | `npm ci` and selected Electron/web builds pass from clean supported environments. |
| Static validation | NO CURRENT EVIDENCE | Lint, format check, TypeScript/build-time checks, and configuration validation pass. |
| Tests | NO CURRENT EVIDENCE | Unit, contract, integration, and primary UI smoke tests pass. |
| Security | NO CURRENT EVIDENCE | Dependency, secret, Electron, storage, credential, network, updater, parser, and workflow-permission checks pass. |
| Accessibility | NO CURRENT EVIDENCE | Keyboard, focus, labels, contrast, scaling, and error-state review recorded. |
| Documentation | PARTIAL | Scripts and metadata exist; fork identity, supported matrix, verified setup/workflows, limitations, signing, and rollback remain incomplete. |
| Provenance | NO EVIDENCE | Upstream baseline, candidate commit, Node/npm/OS versions, commands, artifact hashes, SBOM, and attestations recorded. |
| Approval | PENDING | Explicit release approval after every blocking gate passes. |

## Artifact Requirements
- Upstream/fork baseline and divergence report.
- Reproducible source archive plus selected macOS, Windows, Linux, and/or web artifacts.
- Lint, format, test, accessibility, build, and smoke-test reports.
- Dependency/security report and SBOM.
- Signing/notarization status, SHA-256 checksums, and provenance manifest for every artifact.

## Rollback Criteria
Withdraw or roll back if fork attribution or product identity is unclear, the primary workflow fails, a platform artifact is not reproducible, Electron or remote-access boundaries are unsafe, credentials or local data are exposed, accessibility regressions block use, updater/signing behavior is invalid, or artifact hashes differ. Restore the previous verified fork tag or the recorded upstream baseline and preserve failed-candidate evidence.

## Unresolved Blockers
- Approval is required for the repository's relationship to upstream AionUi, release naming, and distribution identity.
- P0 is only `READY`, `punchlist.md` is absent, and no local Builder evidence is recorded.
- No current clean install, lint, format, test, build, accessibility, security, or provenance evidence is attached to the candidate commit.
- Cross-platform packaging, native dependencies, code signing/notarization, update channels, and remote web mode require platform-specific verification.
- Existing upstream history and version `1.7.0` must not be represented as newly completed aevespers2 work.

## Release Log
- 2026-07-16: Corrected the candidate from a hypothetical `0.1.0-alpha.1` to an existing `1.7.0` fork baseline; release remains `BLOCKED — FORK AND DISTRIBUTION DECISION REQUIRED`.