# Release Plan

## Current Decision

Status: `BLOCKED — FORK AND DISTRIBUTION APPROVAL REQUIRED`

AionUi contains an existing Electron application identified as version `1.7.0`, with a lockfile, build/package commands, linting, formatting, Jest suites, and cross-platform distribution scripts. No aevespers2 application release is eligible because P0 is blocked on approval of mirror/fork/derivative identity, `punchlist.md` is absent, inherited and local work are not separated, and the reviewed implementation baseline lacks current install, build, test, security, accessibility, provenance, signing, and rollback evidence. A fork-specific documentation package and static GitHub Pages portfolio console now describe the observed architecture, onboarding path, security/privacy review surface, P0 decision requirements, public repository metadata, and future integration seams, but they do not change any application release gate to PASS.

## Versioning

- Preserve the upstream application version lineage beginning at `1.7.0`.
- Approve mirror, maintained fork, or independently distributed derivative status before tagging.
- A documentation-only baseline may use `1.7.0-aevespers.1` after provenance and naming approval.
- Functional changes must be versioned and attributed against the approved upstream baseline.
- The static Pages console is a documentation/demo artifact and is not assigned an application version.

## Release Scope

- Exact upstream commit/history, divergence report, license/notices, product name, supported platform, and distribution channel.
- Clean `npm ci`, lint, format, unit/contract/integration tests, and one approved platform build and primary-workflow smoke test.
- Electron, storage, credentials, network, updater, parser, accessibility, packaging, signing, and rollback review.
- Checksummed artifact, SBOM, provenance, and release approval.

## Selected Completed Work

- Documentation-only candidate: GitHub Pages overview, architecture, developer onboarding, security/privacy review model, fork-baseline decision record, diagrams, and static portfolio console.
- Static console boundary: public GitHub metadata and repository navigation only; no backend credentials, local files, SQLite, CLI agents, MCP processes, model calls, writes, releases, or deployments.
- Least-privilege exact-head validation workflow for `docs/` static assets, subject to GitHub Pages repository settings and successful review before publication.
- No inherited application implementation, build, test, security, accessibility, packaging, or release work is selected as complete.
- The inherited `1.7.0` implementation and scripts remain candidate inputs, not newly completed aevespers2 work.

## Planned Changelog Entries

- `Fork`: upstream baseline, divergence, attribution, and distribution identity.
- `Changed`: local changes made after the approved baseline.
- `Security`: Electron, storage, credential, network, updater, parser, dependency, and workflow findings.
- `Accessibility`: primary workflow and platform accessibility evidence.
- `Documentation`: verified setup, architecture, privacy behavior, supported matrix, signing, limitations, and rollback.
- `Release`: selected platform artifact, signing status, SBOM, checksums, provenance, and approval.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Fork/product decision | BLOCKED | Approve identity, upstream baseline, naming, supported platforms, and distribution channels. |
| Task completion | FAIL | P0 is `DONE`; `punchlist.md` exists and included work has evidence. |
| Install/build | NO CURRENT EVIDENCE | Clean install and the selected platform build/package pass. |
| Tests/static | NO CURRENT EVIDENCE | Lint, format, unit, contract, integration, and primary smoke tests pass. |
| Security | NO CURRENT EVIDENCE | Electron, credentials, local data, network, updater, parser, dependency, secret, and CI checks pass. |
| Accessibility | NO CURRENT EVIDENCE | Keyboard, focus, labels, contrast, scaling, and error states are verified. |
| Documentation | PARTIAL | Overview, architecture, onboarding, security/privacy review, decision guidance, and static console exist; approved identity, supported matrix, verified workflows, final privacy/support statements, signing, and rollback evidence remain incomplete. |
| Static Pages validation | PARTIAL | Exact-head checkout, required console/documentation files, JSON syntax, local Markdown links, SHA-256 evidence, and retained artifact upload passed at `d9269277999ff0640497ee3bdc00020dc61f9a84`; Jekyll rendering, browser keyboard/responsive checks, and Pages publication remain pending. |
| Provenance | NO EVIDENCE | Upstream/candidate commits, Node/npm/OS versions, commands, artifacts, hashes, SBOM, and attestations are recorded. |
| Approval | PENDING | Explicit release approval after all blocking gates pass. |

## Artifact Requirements

- Upstream/fork provenance and divergence report.
- Reproducible source archive and one approved platform artifact.
- Complete lint, format, test, build, smoke, accessibility, and security reports.
- Signing/notarization status, SBOM, SHA-256 checksums, and provenance manifest.
- For Pages only: exact-head static-site build evidence and deployed artifact digest.

## Rollback Criteria

Withdraw or roll back if attribution or identity is unclear, the primary workflow fails, the artifact is non-reproducible, credentials or local data are exposed, Electron/network/updater boundaries are unsafe, accessibility blocks use, signing behavior is invalid, or hashes differ. Restore the recorded upstream baseline or previous verified fork tag and preserve failed-candidate evidence. The static console can be rolled back independently by reverting its documentation commits or disabling the Pages workflow; it must never be treated as a substitute for restoring the application runtime.

## Unresolved Blockers

- Approval is required for mirror/fork/derivative status, release naming, platform scope, and distribution identity.
- The exact upstream commit, inherited/local boundary, and divergence report are not recorded.
- `punchlist.md` and accepted local Builder evidence are absent.
- No current clean install, lint, format, test, build, accessibility, security, signing, SBOM, or provenance bundle exists.
- Existing upstream `1.7.0` history must not be represented as newly created aevespers2 work.
- A privileged web backend is not approved; GitHub Pages remains read-only and credential-free.

## Release Log

- 2026-07-16: Aligned the candidate with the fork-identity gate; release remained blocked pending identity approval and a reproduced platform baseline.
- 2026-07-19: Added a fork-specific documentation baseline and review diagrams; release remains blocked and no implementation or verification gate changed to PASS.
- 2026-07-19: Added a static AionUi portfolio console and Pages validation workflow; this is a documentation/demo milestone only and does not authorize or release the Electron/WebUI application.
- 2026-07-20: Exact-head validation run `29712123942` passed required-file, JSON, link, evidence-generation, and artifact-retention checks at `d9269277999ff0640497ee3bdc00020dc61f9a84`; artifact digest `sha256:a42adcf6a4dbdf1a9452a6c59607e1ec2d8f8455505068922413100f7c2fe53a`. Remaining Pages rendering, browser, and publication checks stay pending.