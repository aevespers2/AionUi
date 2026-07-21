# Release Plan

## Current Decision

Status: `BLOCKED — FORK, REVIEW-ROLE, AND DISTRIBUTION APPROVAL REQUIRED`

AionUi contains an existing Electron application identified as version `1.7.0`, with a lockfile, build/package commands, linting, formatting, Jest suites, and cross-platform distribution scripts. No aevespers2 application release is eligible because P0 is blocked on approval of mirror/fork/derivative identity, inherited and local work are not separated, and the reviewed implementation baseline lacks current install, build, test, security, accessibility, provenance, signing, and rollback evidence.

The documentation candidate now includes a static Pages console, a portable-trust review profile, an obstruction/gluing ledger, and an evidence-oriented punch list. It proposes AionUi as a non-authoritative human-facing workspace shell that may host a QSO-STUDIO-compatible review adapter for Repository `0`/`1` evidence. This does not activate an adapter, backend, private records, credentials, approval workflow, or application release.

## Versioning

- Preserve the upstream application version lineage beginning at `1.7.0`.
- Approve mirror, maintained fork, or independently distributed derivative status before tagging.
- A documentation-only baseline may use `1.7.0-aevespers.1` after provenance and naming approval.
- Functional changes must be versioned and attributed against the approved upstream baseline.
- Review/display contracts require independent semantic versions and compatibility manifests; application versioning must not substitute for contract versioning.
- The static Pages console is a documentation/demo artifact and is not assigned an application version.

## Release Scope

### Documentation candidate

- Exact upstream identity and fork/distribution decision guidance.
- Pages overview, architecture, onboarding, security/privacy, fork baseline, portable-trust review profile, obstruction ledger, and punch list.
- Public, credential-free static console with current portfolio roles.
- Exact-head documentation/source validation and retained evidence.

### Later application candidate

- Exact upstream commit/history, divergence report, license/notices, product name, supported platform, and distribution channel.
- Clean `npm ci`, lint, format, unit/contract/integration tests, and one approved platform build and primary-workflow smoke test.
- Electron, storage, credentials, network, updater, parser, accessibility, packaging, signing, and rollback review.
- Approved QSO-STUDIO/AionUi review-role disposition and neutral review/display contract if a portable-trust adapter is included.
- Checksummed artifact, SBOM, provenance, and explicit release approval.

## Selected Completed Work

- Documentation-only candidate: GitHub Pages overview, architecture, developer onboarding, security/privacy review model, fork-baseline decision record, diagrams, static portfolio console, portable-trust review profile, obstruction/gluing analysis, and punch list.
- Static console boundary: public GitHub metadata and repository navigation only; no backend credentials, local files, SQLite, CLI agents, MCP processes, model calls, device inventories, writes, approvals, releases, or deployments.
- Portfolio role map updated to distinguish governance, portable-trust, evidence, runtime, interface, transport, payment, and consolidation candidates.
- Least-privilege exact-head validation workflow for documentation and console assets, subject to successful review before publication.
- No inherited application implementation, build, test, security, accessibility, packaging, privileged adapter, or release work is selected as complete.

## Planned Changelog Entries

- `Fork`: upstream baseline, divergence, attribution, and distribution identity.
- `Architecture`: accepted AionUi/QSO-STUDIO role and portable-trust review boundary.
- `Contracts`: neutral review/display profile, identity namespaces, corrections, revocations, and gluing fixtures.
- `Changed`: local changes made after the approved baseline.
- `Security`: Electron, storage, credential, network, updater, parser, dependency, adapter, privacy, cache, and workflow findings.
- `Accessibility`: primary workflow, evidence-state, unknown/error, and platform accessibility evidence.
- `Documentation`: verified setup, architecture, privacy behavior, supported matrix, signing, limitations, and rollback.
- `Release`: selected platform artifact, signing status, SBOM, checksums, provenance, and approval.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Fork/product decision | BLOCKED | Approve identity, upstream baseline, naming, supported platforms, distribution channels, and support/security ownership. |
| Portable-trust review role | REVIEW | Approve or revise the AionUi/QSO-STUDIO relationship, neutral review/display contract owner, mode allowlists, privacy, correction, revocation, and recovery boundaries. |
| Task completion | FAIL | Blocking tasks in `taskchain.md` and `punchlist.md` are complete with evidence. |
| Install/build | NO CURRENT EVIDENCE | Clean install and the selected platform build/package pass. |
| Tests/static | NO CURRENT EVIDENCE | Lint, format, unit, contract, integration, and primary smoke tests pass. |
| Gluing fixtures | NO CURRENT EVIDENCE | Pairwise and triple-overlap fixtures pass across observation adapters, Repository `0`, Repository `1`, executor receipts, QSO-STUDIO, Bridge/Digitalis, approval authority, correction, revocation, and recovery. |
| Security | NO CURRENT EVIDENCE | Electron, credentials, local data, network, updater, parser, provider/agent, adapter, privacy, secret, and CI checks pass. |
| Accessibility | NO CURRENT EVIDENCE | Keyboard, focus, labels, contrast, scaling, record state, unknown/error, partial-state, and correction/revocation behavior are verified. |
| Documentation | PARTIAL | Overview, architecture, onboarding, security/privacy, fork decision, review profile, obstruction ledger, punch list, and static console exist; approved identity, supported matrix, final contracts, verified workflows, signing, and rollback evidence remain incomplete. |
| Static Pages validation | PENDING CURRENT HEAD | The previous exact-head run passed at `4b9c370baa05b3065a014cd377021c159f2e8bd4`; the expanded documentation head requires a new exact-head run, Jekyll rendering, browser keyboard/responsive checks, publication-safety review, and artifact retention. |
| Provenance | PARTIAL | Documentation commits and prior evidence are recorded; upstream/candidate commits, Node/npm/OS versions, commands, application artifacts, SBOM, and attestations remain absent. |
| Approval | PENDING | Explicit documentation publication and application release approvals remain separate and occur only after their blocking gates pass. |

## Artifact Requirements

### Documentation

- Exact source commit and tool versions.
- Rendered Pages archive and public-safety report.
- Internal-link, JSON, accessibility, responsiveness, and forbidden-field validation.
- SHA-256 manifest and retained review artifact.

### Application

- Upstream/fork provenance and divergence report.
- Reproducible source archive and one approved platform artifact.
- Complete lint, format, test, build, smoke, accessibility, security, and review-contract fixture reports.
- Signing/notarization status, SBOM, SHA-256 checksums, and provenance manifest.
- Incident, correction, revocation, cache invalidation, recovery, and rollback evidence.

## Rollback Criteria

Withdraw or roll back if attribution or identity is unclear, the primary workflow fails, the artifact is non-reproducible, credentials or local data are exposed, Electron/network/updater boundaries are unsafe, accessibility blocks use, signing behavior is invalid, hashes differ, review records lose identity or lineage, UI interaction is treated as approval, stale/revoked records remain authoritative, or private records cross into static Pages.

Restore the recorded upstream baseline or previous verified fork tag and preserve failed-candidate evidence. Disable privileged adapters and remote WebUI independently. Reconstruct canonical review state from Repository `1` and immutable evidence rather than trusting a compromised local cache. The static console can be rolled back by reverting documentation commits or disabling Pages; it is not a substitute for restoring the application runtime.

## Unresolved Blockers

- Approval is required for mirror/fork/derivative status, release naming, platform scope, distribution identity, and support/security ownership.
- The exact upstream commit, inherited/local boundary, and divergence report are not recorded.
- AionUi's relationship to QSO-STUDIO and the neutral review/display contract owner are not approved.
- Device/workspace/repository/commit binding, identity namespaces, privacy, correction, revocation, emergency-stop, cache, offline, and recovery semantics are not accepted.
- No current clean install, lint, format, test, build, accessibility, security, signing, SBOM, application provenance, or shared gluing-fixture bundle exists.
- A privileged web backend and remote WebUI deployment are not approved; GitHub Pages remains public, read-only, and credential-free.

## Release Log

- 2026-07-16: Aligned the candidate with the fork-identity gate; release remained blocked pending identity approval and a reproduced platform baseline.
- 2026-07-19: Added a fork-specific documentation baseline and review diagrams; release remained blocked and no implementation or verification gate changed to PASS.
- 2026-07-19: Added a static AionUi portfolio console and Pages validation workflow; this is a documentation/demo milestone only.
- 2026-07-20: Exact-head validation run `29753309482` passed required-file, JSON, link, evidence-generation, and artifact-retention checks at `4b9c370baa05b3065a014cd377021c159f2e8bd4`; artifact digest `sha256:83b8326f021c52a34084917b7d5963c30b322e0a8a9fee66292a4312419df0fd`.
- 2026-07-21: Added the portable-trust review profile, obstruction/gluing ledger, punch list, updated portfolio map, and aligned planning/release documentation. Exact-head validation for the expanded candidate is pending.