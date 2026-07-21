# Release Plan

## Current Decision

Status: `BLOCKED — FORK, REVIEW-ROLE, RUNTIME-MODE, AND DISTRIBUTION APPROVAL REQUIRED`

AionUi contains an existing Electron application identified as version `1.7.0`, with a lockfile, build/package commands, linting, formatting, Jest suites, and cross-platform distribution scripts. No aevespers2 application release is eligible because P0 is blocked on approval of mirror/fork/derivative identity, inherited and local work are not separated, and the reviewed implementation baseline lacks current install, build, test, security, accessibility, provenance, signing, distribution, and rollback evidence.

The documentation candidate now includes a static Pages console, a portable-trust review profile, an obstruction/gluing ledger, ADR-0001 separating the AionUi host shell from the QSO-STUDIO review contract, a runtime-mode topology, and an evidence-oriented punch list. It proposes AionUi as a non-authoritative host shell that may render a QSO-STUDIO-compatible contract. This does not activate an adapter, backend, private records, credentials, approval workflow, application release, or remote service.

## Versioning

- Preserve the upstream application version lineage beginning at `1.7.0`.
- Approve mirror, maintained fork, or independently distributed derivative status before tagging.
- A documentation-only baseline may use `1.7.0-aevespers.1` after provenance and naming approval.
- Functional changes must be versioned and attributed against the approved upstream baseline.
- Review/display contracts require independent semantic versions and compatibility manifests; application versioning must not substitute for contract versioning.
- Runtime-mode profiles and adapter compatibility require their own version identities.
- The static Pages console is a documentation/demo artifact and is not assigned an application version.

## Release Scope

### Documentation candidate

- Exact upstream identity and fork/distribution decision guidance.
- Pages overview, architecture, onboarding, security/privacy, fork baseline, portable-trust review profile, host-shell ADR, runtime-mode topology, obstruction ledger, and punch list.
- Public, credential-free static console with current portfolio roles.
- Exact-head documentation/source validation and retained evidence.

### Later application candidate

- Exact upstream commit/history, divergence report, license/notices, product name, supported platform, and distribution channel.
- Clean `npm ci`, lint, format, unit/contract/integration tests, and one approved platform build and primary-workflow smoke test.
- Electron, storage, credentials, network, updater, parser, accessibility, packaging, signing, and rollback review.
- Approved QSO-STUDIO/AionUi contract split and neutral review/display profile if a portable-trust adapter is included.
- Accepted static, desktop, local-WebUI, remote-WebUI, and packaging policies for every included mode.
- Checksummed artifact, SBOM, provenance, and explicit release approval.

## Selected Completed Work

- Documentation-only candidate: GitHub Pages overview, architecture, developer onboarding, security/privacy review model, fork-baseline decision record, diagrams, static portfolio console, portable-trust review profile, obstruction/gluing analysis, ADR-0001, runtime-mode topology, and punch list.
- Static console boundary: public GitHub metadata and repository navigation only; no backend credentials, local files, SQLite, CLI agents, MCP processes, model calls, device inventories, writes, approvals, releases, or deployments.
- Candidate contract split: QSO-STUDIO owns the neutral review model; AionUi remains an optional host shell; Repository `1` remains the candidate authority source; human approval remains separately recorded.
- Mode separation: static Pages, desktop, local WebUI, remote WebUI, and packaging are documented as distinct trust, evidence, and release profiles.
- Portfolio role map updated to distinguish governance, portable-trust, runtime, evidence, interface, transport, payment, kernel, and consolidation candidates.
- Least-privilege exact-head validation workflow for documentation and console assets, subject to successful validation of the current head before publication.
- No inherited application implementation, build, test, security, accessibility, packaging, privileged adapter, or release work is selected as complete.

## Planned Changelog Entries

- `Fork`: upstream baseline, divergence, attribution, and distribution identity.
- `Architecture`: accepted AionUi/QSO-STUDIO role, host-shell ADR, portable-trust review boundary, and runtime-mode topology.
- `Contracts`: neutral review/display profile, identity namespaces, corrections, revocations, mode profiles, and gluing fixtures.
- `Changed`: local changes made after the approved baseline.
- `Security`: Electron, storage, credential, network, updater, parser, dependency, adapter, privacy, cache, mode, and workflow findings.
- `Accessibility`: primary workflow, evidence-state, unknown/error, partial-state, correction/revocation, privacy, and authority-class evidence.
- `Documentation`: verified setup, architecture, privacy behavior, supported matrix, mode allowlists, signing, limitations, and rollback.
- `Release`: selected platform artifact, signing status, SBOM, checksums, provenance, distribution profile, and approval.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Fork/product decision | BLOCKED | Approve identity, upstream baseline, naming, supported platforms, distribution channels, and support/security ownership. |
| Host-shell/review-contract ADR | REVIEW | Approve or revise ADR-0001 and QSO-STUDIO ADR-0002, the neutral review contract owner, Repository `1` authority boundary, human-approval separation, adapter scope, and rollback. |
| Runtime-mode topology | REVIEW | Approve static Pages, desktop, local WebUI, remote WebUI, and packaging data, adapter, credential, network, storage, privacy, incident, recovery, and release profiles. |
| Task completion | FAIL | Blocking tasks in `taskchain.md` and `punchlist.md` are complete with evidence. |
| Install/build | NO CURRENT EVIDENCE | Clean install and the selected platform build/package pass. |
| Tests/static | NO CURRENT EVIDENCE | Lint, format, unit, contract, integration, and primary smoke tests pass. |
| Gluing fixtures | NO CURRENT EVIDENCE | Pairwise and triple-overlap fixtures pass across observation adapters, Repository `0`, Repository `1`, executor receipts, QSO-STUDIO, Bridge/Digitalis, approval authority, correction, revocation, mode boundaries, and recovery. |
| Security | NO CURRENT EVIDENCE | Electron, credentials, local data, network, updater, parser, provider/agent, adapter, privacy, secret, remote exposure, mode isolation, and CI checks pass. |
| Accessibility | NO CURRENT EVIDENCE | Keyboard, focus, labels, contrast, scaling, record state, unknown/error, partial-state, privacy, authority, correction, and revocation behavior are verified. |
| Documentation | PARTIAL | Overview, architecture, onboarding, security/privacy, fork decision, review profile, ADR, runtime topology, obstruction ledger, punch list, and static console exist; approved identity, supported matrix, final contracts, verified workflows, signing, and rollback evidence remain incomplete. |
| Static Pages validation | PENDING CURRENT HEAD | Run `29812421794` passed at `2c049c619db35c52746a7c11f9aed851463dd1e3`; the ADR/topology head requires a new exact-head run. Jekyll rendering, browser keyboard/responsive checks, and publication approval remain separate. |
| Provenance | PARTIAL | Documentation commits and prior evidence are recorded; upstream/candidate commits, Node/npm/OS versions, commands, application artifacts, SBOM, and attestations remain absent. |
| Approval | PENDING | Documentation publication, adapter acceptance, remote exposure, and application release approvals remain separate and occur only after their blocking gates pass. |

## Artifact Requirements

### Documentation

- Exact source commit and tool versions.
- Rendered Pages archive and public-safety report.
- Internal-link, JSON, accessibility, responsiveness, mode-topology, and forbidden-field validation.
- SHA-256 manifest and retained review artifact.

### Review contract and adapters

- Accepted ADRs and exact review-contract version.
- Shared QSO-STUDIO/AionUi positive and negative fixture bundle.
- Mode-specific adapter allowlists and configuration identities.
- Identity, privacy, correction, revocation, cache, offline, emergency-stop, and recovery evidence.
- Proof that display, annotation, authentication, delivery, and execution are non-authoritative.

### Application

- Upstream/fork provenance and divergence report.
- Reproducible source archive and one approved platform artifact.
- Complete lint, format, test, build, smoke, accessibility, security, and review-contract fixture reports.
- Signing/notarization status, SBOM, SHA-256 checksums, and provenance manifest.
- Incident, correction, revocation, cache invalidation, recovery, and rollback evidence.

## Rollback Criteria

Withdraw or roll back if attribution or identity is unclear, the primary workflow fails, the artifact is non-reproducible, credentials or local data are exposed, Electron/network/updater boundaries are unsafe, accessibility blocks use, signing behavior is invalid, hashes differ, review records lose identity or lineage, UI interaction is treated as approval, stale/revoked records remain authoritative, inherited ambient permissions escape the adapter contract, one runtime mode inherits another mode's authority, or private records cross into static Pages.

Restore the recorded upstream baseline or previous verified fork tag and preserve failed-candidate evidence. Disable the review adapter independently of the host shell. Disable privileged adapters and remote WebUI independently. Reconstruct canonical review state from Repository `1` and immutable evidence rather than trusting a compromised local cache. The static console can be rolled back by reverting documentation commits or disabling Pages; it is not a substitute for restoring the application runtime.

## Unresolved Blockers

- Approval is required for mirror/fork/derivative status, release naming, platform scope, distribution identity, and support/security ownership.
- The exact upstream commit, inherited/local boundary, and divergence report are not recorded.
- ADR-0001 and QSO-STUDIO ADR-0002 are proposed, not accepted.
- The neutral review/display contract, registry, identity namespaces, privacy, correction, revocation, emergency-stop, cache, offline, and recovery semantics are not accepted.
- Static, desktop, local-WebUI, remote-WebUI, and packaging policies are not approved.
- No current clean install, lint, format, test, build, accessibility, security, signing, SBOM, application provenance, or shared gluing-fixture bundle exists.
- A privileged web backend and remote WebUI deployment are not approved; GitHub Pages remains public, read-only, and credential-free.

## Release Log

- 2026-07-16: Aligned the candidate with the fork-identity gate; release remained blocked pending identity approval and a reproduced platform baseline.
- 2026-07-19: Added a fork-specific documentation baseline and review diagrams; release remained blocked and no implementation or verification gate changed to PASS.
- 2026-07-19: Added a static AionUi portfolio console and Pages validation workflow; this is a documentation/demo milestone only.
- 2026-07-20: Exact-head validation run `29753309482` passed required-file, JSON, link, evidence-generation, and artifact-retention checks at `4b9c370baa05b3065a014cd377021c159f2e8bd4`; artifact digest `sha256:83b8326f021c52a34084917b7d5963c30b322e0a8a9fee66292a4312419df0fd`.
- 2026-07-21: Added the portable-trust review profile, obstruction/gluing ledger, punch list, updated portfolio map, and aligned planning/release documentation.
- 2026-07-21: Pages Console Validation run `29812421794` passed at `2c049c619db35c52746a7c11f9aed851463dd1e3`; retained artifact digest `sha256:786ea6f443619f5a4f59f443ee78928a748ae50223bc28611a21bfe9fe751c77`.
- 2026-07-21: Added ADR-0001 and runtime-mode topology; current exact-head validation is pending and no application authority changed.
