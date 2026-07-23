# Release Plan

## Current Decision

Status: `BLOCKED — FORK, REVIEW-ROLE, RUNTIME-MODE, ACCESSIBILITY-EVIDENCE, AND DISTRIBUTION APPROVAL REQUIRED`

AionUi contains an existing Electron application identified as version `1.7.0`, with a lockfile, build/package commands, linting, formatting, Jest suites, and cross-platform distribution scripts. No aevespers2 application release is eligible because P0 is blocked on approval of mirror/fork/derivative identity, inherited and local work are not separated, and the reviewed implementation baseline lacks current install, build, test, security, accessibility, provenance, signing, distribution, and rollback evidence.

The documentation candidate now includes a static Pages console, a portable-trust review profile, an obstruction/gluing ledger, ADR-0001 separating the AionUi host shell from the QSO-STUDIO review contract, a runtime-mode topology, an accessibility and review-state assurance plan, and an evidence-oriented punch list. It proposes AionUi as a non-authoritative host shell that may render a QSO-STUDIO-compatible contract. This does not activate an adapter, backend, private records, credentials, approval workflow, application release, or remote service.

## Versioning

- Preserve the upstream application version lineage beginning at `1.7.0`.
- Approve mirror, maintained fork, or independently distributed derivative status before tagging.
- A documentation-only baseline may use `1.7.0-aevespers.1` after provenance and naming approval.
- Functional changes must be versioned and attributed against the approved upstream baseline.
- Review/display contracts require independent semantic versions and compatibility manifests; application versioning must not substitute for contract versioning.
- Runtime-mode profiles and adapter compatibility require their own version identities.
- Accessibility review records must bind the exact artifact, mode, environment, assistive-technology versions, scenarios, and findings; they do not alter the application version or create certification.
- The static Pages console is a documentation/demo artifact and is not assigned an application version.

## Release Scope

### Documentation candidate

- Exact upstream identity and fork/distribution decision guidance.
- Pages overview, architecture, onboarding, security/privacy, fork baseline, portable-trust review profile, host-shell ADR, runtime-mode topology, accessibility and review-state assurance, obstruction ledger, and punch list.
- Public, credential-free static console with current portfolio roles.
- Exact-head documentation/source validation and retained evidence.

### Later application candidate

- Exact upstream commit/history, divergence report, license/notices, product name, supported platform, and distribution channel.
- Clean `npm ci`, lint, format, unit/contract/integration tests, and one approved platform build and primary-workflow smoke test.
- Electron, storage, credentials, network, updater, parser, accessibility, packaging, signing, and rollback review.
- Approved QSO-STUDIO/AionUi contract split and neutral review/display profile if a portable-trust adapter is included.
- Accepted static, desktop, local-WebUI, remote-WebUI, and packaging policies for every included mode.
- Exact-artifact keyboard, focus, names/roles/values, announcements, contrast, zoom/reflow, reduced-motion, screen-reader, state-semantics, privacy, correction, revocation, withdrawal, error, and recovery evidence for every included mode.
- Checksummed artifact, SBOM, provenance, and explicit release approval.

## Selected Completed Work

- Documentation-only candidate: GitHub Pages overview, architecture, developer onboarding, security/privacy review model, fork-baseline decision record, diagrams, static portfolio console, portable-trust review profile, obstruction/gluing analysis, ADR-0001, runtime-mode topology, accessibility and review-state assurance, and punch list.
- Static console boundary: public GitHub metadata and repository navigation only; no backend credentials, local files, SQLite, CLI agents, MCP processes, model calls, device inventories, writes, approvals, releases, or deployments.
- Candidate contract split: QSO-STUDIO owns the neutral review model; AionUi remains an optional host shell; Repository `1` remains the candidate authority source; human approval remains separately recorded.
- Mode separation: static Pages, desktop, local WebUI, remote WebUI, and packaging are documented as distinct trust, evidence, accessibility, and release profiles.
- Accessibility review plan: explicit state vocabulary, authority classes, keyboard/focus, names/roles/values, announcements, errors, zoom/reflow, contrast, reduced motion, diagram alternatives, evidence records, mode-specific review matrix, and stop conditions.
- Portfolio role map updated to distinguish governance, portable-trust, runtime, evidence, interface, transport, payment, kernel, and consolidation candidates.
- Least-privilege exact-head validation workflow for documentation and console assets, subject to successful validation of the current head before publication.
- No inherited application implementation, build, test, security, rendered accessibility, packaging, privileged adapter, or release work is selected as complete.

## Planned Changelog Entries

- `Fork`: upstream baseline, divergence, attribution, and distribution identity.
- `Architecture`: accepted AionUi/QSO-STUDIO role, host-shell ADR, portable-trust review boundary, and runtime-mode topology.
- `Contracts`: neutral review/display profile, identity namespaces, corrections, revocations, mode profiles, state semantics, and gluing fixtures.
- `Changed`: local changes made after the approved baseline.
- `Security`: Electron, storage, credential, network, updater, parser, dependency, adapter, privacy, cache, mode, and workflow findings.
- `Accessibility`: exact-artifact primary workflow, keyboard/focus, names/roles/values, announcements, contrast, zoom/reflow, reduced motion, screen-reader, evidence-state, unknown/error, partial-state, correction/revocation, privacy, authority-class, and recovery evidence.
- `Documentation`: verified setup, architecture, privacy behavior, supported matrix, mode allowlists, accessibility review plan, signing, limitations, and rollback.
- `Release`: selected platform artifact, signing status, SBOM, checksums, provenance, distribution profile, and approval.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Fork/product decision | BLOCKED | Approve identity, upstream baseline, naming, supported platforms, distribution channels, and support/security ownership. |
| Host-shell/review-contract ADR | REVIEW | Approve or revise ADR-0001 and QSO-STUDIO ADR-0002, the neutral review contract owner, Repository `1` authority boundary, human-approval separation, adapter scope, and rollback. |
| Runtime-mode topology | REVIEW | Approve static Pages, desktop, local WebUI, remote WebUI, and packaging data, adapter, credential, network, storage, privacy, incident, recovery, and release profiles. |
| Accessibility/review-state profile | REVIEW | Approve or revise the documented state vocabulary, authority classes, mode-specific requirements, evidence record, review sequence, and stop conditions without treating documentation as certification. |
| Task completion | FAIL | Blocking tasks in `taskchain.md` and `punchlist.md` are complete with evidence. |
| Install/build | NO CURRENT EVIDENCE | Clean install and the selected platform build/package pass. |
| Tests/static | NO CURRENT EVIDENCE | Lint, format, unit, contract, integration, and primary smoke tests pass. |
| Gluing fixtures | NO CURRENT EVIDENCE | Pairwise and triple-overlap fixtures pass across observation adapters, Repository `0`, Repository `1`, executor receipts, QSO-STUDIO, Bridge/Digitalis, approval authority, correction, revocation, mode boundaries, accessibility state semantics, and recovery. |
| Security | NO CURRENT EVIDENCE | Electron, credentials, local data, network, updater, parser, provider/agent, adapter, privacy, secret, remote exposure, mode isolation, and CI checks pass. |
| Accessibility | PARTIAL — REVIEW PLAN DOCUMENTED | Requirements and evidence templates exist. Exact rendered artifacts still require keyboard, focus, names/roles/values, announcements, contrast, zoom/reflow, reduced-motion, screen-reader, error/unknown/partial/conflicting/corrected/revoked/withdrawn/privacy/recovery-state, and mode-specific verification. |
| Documentation | PARTIAL | Overview, architecture, onboarding, security/privacy, fork decision, review profile, ADR, runtime topology, accessibility assurance, obstruction ledger, punch list, and static console exist; approved identity, supported matrix, final contracts, verified workflows, signing, and rollback evidence remain incomplete. |
| Static Pages validation | PENDING CURRENT HEAD | Prior run `29904565915` passed at `7eff1ab9274a9ba7c519aa3aac64b032027560df`; the accessibility-documentation head requires new exact-head validation. Jekyll rendering, browser keyboard/responsive/assistive-technology checks, and publication approval remain separate. |
| Provenance | PARTIAL | Documentation commits and prior evidence are recorded; upstream/candidate commits, Node/npm/OS versions, commands, application artifacts, SBOM, and attestations remain absent. |
| Approval | PENDING | Documentation publication, adapter acceptance, remote exposure, accessibility disposition, and application release approvals remain separate and occur only after their blocking gates pass. |

## Artifact Requirements

### Documentation

- Exact source commit and tool versions.
- Rendered Pages archive and public-safety report.
- Internal-link, JSON, automated accessibility, responsive-layout, state-vocabulary, authority-boundary, and forbidden-field validation.
- Manual keyboard, focus, screen-reader, zoom/reflow, high-contrast, reduced-motion, and plain-language review record for the exact rendered artifact.
- SHA-256 manifest and retained review artifact.

### Review contract and adapters

- Accepted ADRs and exact review-contract version.
- Shared QSO-STUDIO/AionUi positive and negative fixture bundle.
- Mode-specific adapter allowlists and configuration identities.
- Identity, privacy, correction, revocation, withdrawal, cache, offline, emergency-stop, accessibility-state, and recovery evidence.
- Proof that display, annotation, authentication, delivery, automated scoring, and execution are non-authoritative.

### Application

- Upstream/fork provenance and divergence report.
- Reproducible source archive and one approved platform artifact.
- Complete lint, format, test, build, smoke, accessibility, security, and review-contract fixture reports.
- Signing/notarization status, SBOM, SHA-256 checksums, and provenance manifest.
- Incident, correction, revocation, cache invalidation, recovery, and rollback evidence.

## Rollback Criteria

Withdraw or roll back if attribution or identity is unclear, the primary workflow fails, the artifact is non-reproducible, credentials or local data are exposed, Electron/network/updater boundaries are unsafe, accessibility blocks use, critical state or authority meaning depends on color/pointer/animation, keyboard focus fails, stale or revoked records remain actionable, signing behavior is invalid, hashes differ, review records lose identity or lineage, UI interaction is treated as approval, inherited ambient permissions escape the adapter contract, one runtime mode inherits another mode's authority, or private records cross into static Pages.

Restore the recorded upstream baseline or previous verified fork tag and preserve failed-candidate evidence. Disable the review adapter independently of the host shell. Disable privileged adapters and remote WebUI independently. Reconstruct canonical review state from Repository `1` and immutable evidence rather than trusting a compromised local cache. The static console can be rolled back by reverting documentation commits or disabling Pages; it is not a substitute for restoring the application runtime.

## Unresolved Blockers

- Approval is required for mirror/fork/derivative status, release naming, platform scope, distribution identity, and support/security/accessibility ownership.
- The exact upstream commit, inherited/local boundary, and divergence report are not recorded.
- ADR-0001 and QSO-STUDIO ADR-0002 are proposed, not accepted.
- The neutral review/display contract, registry, identity namespaces, privacy, correction, revocation, emergency-stop, cache, offline, accessibility-state, and recovery semantics are not accepted.
- Static, desktop, local-WebUI, remote-WebUI, and packaging policies are not approved.
- No current clean install, lint, format, test, build, rendered accessibility, security, signing, SBOM, application provenance, or complete shared gluing-fixture bundle exists.
- A privileged web backend and remote WebUI deployment are not approved; GitHub Pages remains public, read-only, and credential-free.

## Release Log

- 2026-07-16: Aligned the candidate with the fork-identity gate; release remained blocked pending identity approval and a reproduced platform baseline.
- 2026-07-19: Added a fork-specific documentation baseline and review diagrams; release remained blocked and no implementation or verification gate changed to PASS.
- 2026-07-19: Added a static AionUi portfolio console and Pages validation workflow; this is a documentation/demo milestone only.
- 2026-07-20: Exact-head validation run `29753309482` passed required-file, JSON, link, evidence-generation, and artifact-retention checks at `4b9c370baa05b3065a014cd377021c159f2e8bd4`; artifact digest `sha256:83b8326f021c52a34084917b7d5963c30b322e0a8a9fee66292a4312419df0fd`.
- 2026-07-21: Added the portable-trust review profile, obstruction/gluing ledger, punch list, updated portfolio map, and aligned planning/release documentation.
- 2026-07-21: Pages Console Validation run `29812421794` passed at `2c049c619db35c52746a7c11f9aed851463dd1e3`; retained artifact digest `sha256:786ea6f443619f5a4f59f443ee78928a748ae50223bc28611a21bfe9fe751c77`.
- 2026-07-21: Added ADR-0001 and runtime-mode topology; no application authority changed.
- 2026-07-22: Pages Console Validation run `29904565915` passed at `7eff1ab9274a9ba7c519aa3aac64b032027560df`; retained artifact digest `sha256:3ab8aec9339ea4fb9f7e1d049268c0063c3f40f2bbc805a8cd764961d7c2b984`.
- 2026-07-23: Added the accessibility and review-state assurance plan and aligned repository overview, Pages navigation, task chain, punch list, release gates, changelog, and exact-head validation requirements. Rendered accessibility evidence and publication approval remain blocked.
