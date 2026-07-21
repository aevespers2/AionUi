# Task Chain

## Purpose

Architect-controlled execution chain for the inherited AionUi 1.7.0 application and its candidate role as a bounded A.L.I.S.T.A.I.R.E. human-review workspace. Builders preserve upstream provenance, exact record identity, mode-specific security boundaries, evidence, and rollback paths.

## States

`PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Decide and document whether this repository is an upstream mirror, maintained fork, or independently distributed derivative; approve or revise ADR-0001 separating the AionUi host shell from the QSO-STUDIO review contract; approve mode-specific static, desktop, local-WebUI, remote-WebUI, and packaging boundaries; then reproduce the inherited 1.7.0 baseline.
- **User outcome:** A user can install a clearly named and attributed AionUi build for an explicitly supported platform, understand its local data, credentials, network, update, and rollback behavior, and review bounded portfolio evidence without confusing display, authentication, annotation, or execution with approval.
- **MVP scope:** exact upstream commit/history and divergence report; license/notices; product/distribution identity; supported-platform decision; clean `npm ci`; lint/format/tests; one approved platform build and primary workflow smoke; Electron/storage/network/credential security review; neutral review/display contract; runtime-mode topology; portable-trust gluing fixtures; checksums, SBOM, provenance, and rollback.
- **Priority:** Fork identity and baseline verification precede new features, rebranding, public binaries, privileged adapters, or claims of cross-platform support. Review-contract ownership and runtime-mode boundaries must be settled before AionUi is treated as a portable-trust interface.
- **Success criteria:** upstream relationship and name are approved; inherited versus local work is separated; clean install/checks pass at one immutable commit; one platform artifact is reproducible; primary workflow, accessibility, data handling, and security boundaries are evidenced; ADR-0001 is accepted or replaced; static/desktop/local/remote profiles are approved; AionUi/QSO-STUDIO review semantics and Repository `0`/`1` record flows pass shared fail-closed fixtures.
- **Non-goals:** representing upstream 1.7.0 as newly created work, resetting version history, publishing unsigned/unreviewed binaries, guaranteeing every platform in the first candidate, adding new AI/provider features before baseline acceptance, making UI interaction authoritative, allowing inherited process or provider access to become ambient adapter authority, activating private portable-trust records in static Pages, or treating local WebUI acceptance as remote-WebUI approval.
- **Release rationale:** A provenance-correct fork baseline, a non-authoritative review contract, and mode-specific security profiles protect users and upstream attribution while creating a trustworthy point from which local improvements can be measured.

## Authority boundary

AionUi may host, display, compare, annotate, and export review records only through an approved QSO-STUDIO-compatible contract and separately admitted adapter. It does not own the neutral review contract, device observation, Repository `0` proposals, Repository `1` dispositions or capabilities, execution, canonical reconciliation, releases, deployments, credentials, or payments. Static Pages is public, read-only, and non-sensitive. Desktop, local WebUI, remote WebUI, and packaging remain separate trust and release profiles.

## Active Chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Approve fork/product/distribution identity and record upstream baseline | Architect | Human approval | BLOCKED | Mirror/fork/derivative status, exact upstream commit, divergence, name, license/notices, supported platforms, distribution channels, and support/security owners are approved and documented. |
| P0R | Approve ADR-0001 and the AionUi/QSO-STUDIO relationship | Architect | Human approval, QSO-STUDIO ADR-0002, portfolio governance | REVIEW | Host-shell/review-contract split, neutral profile owner, authority source, human-approval separation, privileged-adapter boundary, and rollback are accepted at immutable commits. |
| P0T | Approve runtime-mode topology and allowlists | Architect | P0R, security/privacy review | REVIEW | Static Pages, desktop, local WebUI, remote WebUI, and packaging have accepted data, adapter, credential, network, storage, privacy, incident, recovery, and release profiles. |
| P1 | Reproduce the inherited 1.7.0 health baseline | Architect | P0 | PROPOSED | `npm ci`, lint, format, unit/contract/integration tests, and the selected platform build/smoke pass with commands and retained evidence. |
| P1R | Create shared review and gluing fixtures | Builder | P0R, P0T, Repository `0`/`1` contract profile, QSO-STUDIO review contract | PROPOSED | Pairwise and triple-overlap fixtures pass for observations, proposals, dispositions, capabilities, receipts, corrections, revocations, partial states, wrong subjects, stale/replayed records, privacy, UI non-authority, and cross-mode rejection. |
| P2 | Verify security, accessibility, packaging, and rollback | Builder | P1, P1R | PROPOSED | Electron, storage, network, credentials, updater, parser, adapters, accessibility, artifact signing status, checksums, SBOM, provenance, cache invalidation, incident response, and rollback are recorded per accepted mode. |
| P3 | Define the first bounded local product change | Architect | P2 | PROPOSED | Scope identifies a user outcome, local divergence, files, tests, migration, privacy/authority effects, and rollback without obscuring upstream history. |

## Builder rules

Builders may perform documentation, read-only analysis, static validation, isolated tests, and reviewable proposals. No task authorizes credentials, private device inventories, local filesystem access outside an approved test environment, provider calls, agent execution, remote WebUI exposure, repository writes by the application, approval issuance, release, signing, deployment, payment, or canonical-state mutation. A permission observed in the inherited Electron or WebUI runtime is not an approved adapter capability.

## Evidence rules

For each task record:

- exact upstream, base, and head commits;
- platform, runtime mode, dependency, command, configuration, and environment versions;
- observed, proposed, implemented, and validated states;
- record and subject identities, schemas/profiles, hashes, freshness, and limitations;
- data and adapter allowlists for the applicable mode;
- privacy classification, redaction, retention, deletion, export, correction, and revocation behavior;
- requester, implementer, verifier, approver, revoker, incident owner, and rollback owner where applicable;
- test results, artifacts, checksums, migration, recovery, and rollback instructions.

## Builder Log

- 2026-07-19 — Prepared the documentation-only candidate in draft PR #1: project overview, architecture and trust-boundary guidance, Mermaid diagrams, developer onboarding, security/privacy review model, fork-baseline decision record, and an isolated static portfolio console under `docs/console/`. No inherited application implementation or release gate was changed.
- 2026-07-20 — Exact-head Pages Console Validation run `29753309482` passed at `4b9c370baa05b3065a014cd377021c159f2e8bd4`, including submitted-source identity, required-file and JSON checks, local Markdown-link validation, SHA-256 evidence generation, and retained artifact upload. Artifact digest: `sha256:83b8326f021c52a34084917b7d5963c30b322e0a8a9fee66292a4312419df0fd`. Jekyll rendering, browser accessibility/responsiveness, and Pages publication remain separate pending checks.
- 2026-07-21 — Added the portable-trust review profile, obstruction/gluing ledger, evidence-oriented punch list, current portfolio-role map, and aligned Pages, planning, release, and changelog documentation. No runtime or privileged authority was added.
- 2026-07-21 — Pages Console Validation run `29812421794` passed at `2c049c619db35c52746a7c11f9aed851463dd1e3`; retained artifact digest `sha256:786ea6f443619f5a4f59f443ee78928a748ae50223bc28611a21bfe9fe751c77`. This validates static source checks only.
- 2026-07-21 — Added ADR-0001 and the runtime-mode topology, aligning AionUi with QSO-STUDIO ADR-0002 and separating static Pages, desktop, local WebUI, remote WebUI, and packaging policy. No adapter or application authority was activated.

Record approvals, upstream/local commits, install/build/test commands, mode and platform details, artifact hashes, security/accessibility findings, contract fixtures, rollback evidence, and follow-ups.
