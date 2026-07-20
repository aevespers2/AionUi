# Changelog

All notable product, architecture, implementation, release, and deployment changes are recorded here.

## Unreleased

### Product
- 2026-07-16 — Made fork/product/distribution identity the blocking product decision for the inherited AionUi 1.7.0 application.
- 2026-07-16 — Defined the first user outcome as one clearly attributed, reproducible, security-reviewed platform build rather than new feature development.
- 2026-07-19 — Added a browser-safe portfolio-console demonstration that exposes public repository navigation and metadata without privileged runtime authority.

### Architecture
- The active chain now separates upstream provenance, inherited baseline reproduction, packaging/security/accessibility, and later local product changes.
- 2026-07-19 — Documented the observed desktop, renderer, preload/IPC, WebUI/WebSocket, process-service, persistence, agent/provider, preview, and packaging boundaries without changing implementation scope.
- 2026-07-19 — Defined a static Pages adapter boundary: public metadata is available directly; authenticated reads, draft actions, and approved writes require a separately deployed policy gateway.

### Documentation
- 2026-07-19 — Added a GitHub Pages-ready project overview, architecture guide, developer onboarding, security/privacy review model, and fork-baseline decision record.
- 2026-07-19 — Added Mermaid component, startup, bridge, persistence, packaging, trust-boundary, and verification diagrams.
- 2026-07-19 — Clarified that the inherited repository uses multiple persistence mechanisms and that WebUI remote access is a distinct deployment and security boundary.
- 2026-07-19 — Preserved the P0 architectural hold: the documentation does not approve a mirror/fork/derivative identity, public binaries, supported platforms, or release readiness.
- 2026-07-19 — Added an accessible responsive AionUi-style console with repository directory, portfolio roles, capability boundaries, architecture guidance, session-only activity log, and disabled backend configuration seam.
- 2026-07-20 — Recorded exact-head validation evidence in `taskchain.md` and reconciled release claims with what the workflow actually verifies; Jekyll rendering, browser checks, and Pages publication remain explicitly pending.

### Implementation
- Existing application code, scripts, tests, and lockfile are inherited candidate assets and are not recorded as newly completed aevespers2 work.
- The Pages console is isolated under `docs/console/` and does not modify the inherited Electron renderer, preload, main process, WebUI server, storage, or agent/provider implementation.

### Release
- Release remains blocked until mirror/fork/derivative status, naming, attribution, supported platform, tests/build, security, SBOM, checksums, provenance, and rollback are approved and verified.
- The static console is not an AionUi application release and does not satisfy desktop or WebUI acceptance gates.
- 2026-07-20 — Pages Console Validation run `29712123942` passed exact-source, required-file, JSON, local-link, evidence-generation, and artifact-retention checks at `d9269277999ff0640497ee3bdc00020dc61f9a84`; artifact digest `sha256:a42adcf6a4dbdf1a9452a6c59607e1ec2d8f8455505068922413100f7c2fe53a`.

### Deployment
- No public binary or update channel is authorized before the fork and distribution decision.
- GitHub Pages content is prepared under `docs/`; publication configuration remains a repository setting and does not constitute an Electron/WebUI application deployment.
- Added a least-privilege Pages validation workflow for static documentation and console assets; deployment remains dependent on repository Pages settings, review, and branch merge.

## Entry Format
- Date
- Category: Product / Architecture / Added / Changed / Fixed / Security / Release / Deployment
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable
