# Changelog

All notable product, architecture, implementation, release, and deployment changes are recorded here.

## Unreleased

### Product
- 2026-07-16 — Made fork/product/distribution identity the blocking product decision for the inherited AionUi 1.7.0 application.
- 2026-07-16 — Defined the first user outcome as one clearly attributed, reproducible, security-reviewed platform build rather than new feature development.
- 2026-07-19 — Added a browser-safe portfolio-console demonstration that exposes public repository navigation and metadata without privileged runtime authority.
- 2026-07-21 — Proposed AionUi as a non-authoritative human-facing workspace shell that may host a QSO-STUDIO-compatible portable-trust review adapter; approval, adapter activation, and application release remain blocked.
- 2026-07-21 — Clarified that AionUi's desktop, local WebUI, remote WebUI, static Pages, and packaging surfaces are separate product and security profiles rather than one inherited support claim.
- 2026-07-23 — Added accessibility and review-state assurance as a separate acceptance boundary: documentation defines the required state semantics and evidence, but no mode is certified or release-ready.

### Architecture
- The active chain separates upstream provenance, inherited baseline reproduction, review-contract adoption, runtime-mode adoption, accessibility-state adoption, packaging/security/accessibility verification, and later local product changes.
- 2026-07-19 — Documented the observed desktop, renderer, preload/IPC, WebUI/WebSocket, process, persistence, agent/provider, preview, and packaging boundaries without changing implementation scope.
- 2026-07-19 — Defined a static Pages adapter boundary: public metadata is available directly; authenticated reads, draft actions, and approved writes require a separately deployed policy gateway.
- 2026-07-21 — Defined the candidate portable-trust review path across observation adapters, Repository `0`, Repository `1`, bounded executors, QSO-STUDIO, and external human approval records.
- 2026-07-21 — Added an eighteen-item obstruction ledger covering fork identity, runtime modes, display/approval collapse, AionUi/QSO-STUDIO overlap, record identity, local/canonical state, subject binding, capability classes, replay, privacy, transformations, providers/agents, remote WebUI, correction/revocation, partial states, topology, recovery, and evidence mismatch.
- 2026-07-21 — Added pairwise and triple-overlap witness requirements and negative fixtures for the portable-trust and source-evidence review graph.
- 2026-07-21 — Added ADR-0001, aligned with QSO-STUDIO ADR-0002, proposing that QSO-STUDIO own the neutral review contract while AionUi remains an optional host shell and Repository `1` remains the candidate authority source.
- 2026-07-21 — Added a runtime-mode topology separating public static Pages, Electron desktop, local WebUI, remote WebUI, and packaging data, adapter, credential, network, storage, evidence, incident, and recovery boundaries.
- 2026-07-23 — Defined canonical presentation guidance for current, stale, superseded, partial, conflicting, unknown, unsupported, corrected, revoked, withdrawn, privacy-restricted, rejected, quarantined, recovering, and restored states.
- 2026-07-23 — Required observation, interpretation, proposal, review annotation, capability, execution receipt, disposition, and external human approval to remain separately identified and perceivable in text.

### Documentation
- 2026-07-19 — Added a GitHub Pages-ready project overview, architecture guide, developer onboarding, security/privacy review model, and fork-baseline decision record.
- 2026-07-19 — Added Mermaid component, startup, bridge, persistence, packaging, trust-boundary, and verification diagrams.
- 2026-07-19 — Clarified that the inherited repository uses multiple persistence mechanisms and that WebUI remote access is a distinct deployment and security boundary.
- 2026-07-19 — Preserved the P0 architectural hold: the documentation does not approve a mirror/fork/derivative identity, public binaries, supported platforms, or release readiness.
- 2026-07-19 — Added an accessible responsive AionUi-style console with repository directory, portfolio roles, capability boundaries, architecture guidance, session-only activity log, and disabled backend configuration seam.
- 2026-07-20 — Recorded exact-head validation evidence in `taskchain.md` and reconciled release claims with what the workflow actually verifies; Jekyll rendering, browser checks, and Pages publication remain explicitly pending.
- 2026-07-21 — Added `docs/portable-trust-review-profile.md`, `docs/obstruction-and-gluing.md`, and `punchlist.md`.
- 2026-07-21 — Updated the Pages home and navigation to distinguish static, desktop, local WebUI, remote WebUI, review, capability, and canonical-state boundaries.
- 2026-07-21 — Updated the static portfolio dataset to reflect the current governance, portable-trust, runtime, evidence, interface, transport, payment, kernel, and consolidation roles of all nineteen accessible portfolio repositories.
- 2026-07-21 — Added `docs/decisions/0001-host-shell-and-review-contract-boundary.md` and `docs/runtime-mode-topology.md`, then aligned Pages navigation, task chain, punch list, release plan, changelog, and validation requirements.
- 2026-07-23 — Added `docs/accessibility-and-review-state.md`, covering user-critical questions, explicit state meanings, authority classes, keyboard/focus, names/roles/values, announcements, errors, contrast, zoom/reflow, reduced motion, diagrams, mode-specific evidence, review sequencing, and stop conditions.
- 2026-07-23 — Added the FYSA-120 mapping and proposed `019-M — Epistemic and authority-state accessibility assurance` without treating the taxonomy as certification or authorization.

### Implementation
- Existing application code, scripts, tests, and lockfile are inherited candidate assets and are not recorded as newly completed aevespers2 work.
- The Pages console is isolated under `docs/console/` and does not modify the inherited Electron renderer, preload, main process, WebUI server, storage, or agent/provider implementation.
- No portable-trust adapter, backend, private device record, approval action, capability, cache integration, runtime-mode policy enforcement, accessibility implementation, or QSO-STUDIO contract implementation was added.

### Security
- 2026-07-21 — Required public static mode to reject device inventories, local paths, credentials, tokens, private records, and privileged endpoints.
- 2026-07-21 — Required explicit mode, subject identity, provenance, freshness, privacy, correction, revocation, partial-state, capability, and reconciliation display semantics.
- 2026-07-21 — Clarified that providers, CLI agents, UI events, authenticated sessions, delivery receipts, and successful execution do not inherit approval or canonical-state authority.
- 2026-07-21 — Blocked remote WebUI portable-trust use until TLS, proxy, authentication, session, origin, firewall, privacy, monitoring, incident, disaster-recovery, and rollback architecture is accepted.
- 2026-07-21 — Clarified that inherited Electron filesystem, process, provider, and agent permissions are not ambient grants to a future review adapter.
- 2026-07-23 — Added stop conditions for inaccessible authority or freshness meaning, color/pointer/animation-only critical states, lost focus, unannounced revocation or recovery failure, and stale or unknown actionable state.

### Accessibility
- 2026-07-23 — Added a documentation-level accessibility assurance profile; no accessibility standard or application mode is certified.
- 2026-07-23 — Required exact-artifact keyboard, focus, screen-reader, zoom/reflow, high-contrast, reduced-motion, plain-language, correction/revocation, privacy, and recovery evidence.
- 2026-07-23 — Required diagrams and charts to have prose equivalents and required status badges, tables, live updates, and errors to expose meaningful text rather than color or icons alone.
- 2026-07-23 — Required accessibility review records to bind repository, exact commit, artifact digest, mode, environment, assistive technology, scenarios, findings, repairs, residual risk, and approval boundary.

### Release
- Release remains blocked until mirror/fork/derivative status, naming, attribution, supported platform, tests/build, security, review-contract ownership, runtime-mode policies, rendered accessibility evidence, gluing fixtures, SBOM, checksums, provenance, and rollback are approved and verified.
- The static console is not an AionUi application release and does not satisfy desktop, WebUI, adapter, portable-trust, or rendered-accessibility acceptance gates.
- 2026-07-20 — Pages Console Validation run `29753309482` passed exact-source, required-file, JSON, local-link, evidence-generation, and artifact-retention checks at `4b9c370baa05b3065a014cd377021c159f2e8bd4`; artifact digest `sha256:83b8326f021c52a34084917b7d5963c30b322e0a8a9fee66292a4312419df0fd`.
- 2026-07-21 — Pages Console Validation run `29812421794` passed at `2c049c619db35c52746a7c11f9aed851463dd1e3`; retained artifact digest `sha256:786ea6f443619f5a4f59f443ee78928a748ae50223bc28611a21bfe9fe751c77`.
- 2026-07-22 — Pages Console Validation run `29904565915` passed at `7eff1ab9274a9ba7c519aa3aac64b032027560df`; retained artifact digest `sha256:3ab8aec9339ea4fb9f7e1d049268c0063c3f40f2bbc805a8cd764961d7c2b984`.
- 2026-07-23 — Exact-head validation for the accessibility-documentation candidate is pending; rendered browser and assistive-technology review remains separately blocked.

### Deployment
- No public binary, update channel, privileged adapter, remote administration path, remote WebUI, or portable-trust backend is authorized before the fork, review-role, runtime-mode, security, accessibility, and distribution decisions.
- GitHub Pages content is prepared under `docs/`; publication configuration remains a repository setting and does not constitute an Electron/WebUI application deployment.
- The least-privilege Pages validation workflow validates static documentation and console assets; deployment remains dependent on repository Pages settings, review, branch integration, rendered accessibility review, and explicit publication approval.

## Entry Format
- Date
- Category: Product / Architecture / Added / Changed / Fixed / Security / Accessibility / Release / Deployment
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable
