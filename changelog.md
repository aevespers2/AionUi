# Changelog

All notable product, architecture, implementation, release, and deployment changes are recorded here.

## Unreleased

### Product
- 2026-07-16 — Made fork/product/distribution identity the blocking product decision for the inherited AionUi 1.7.0 application.
- 2026-07-16 — Defined the first user outcome as one clearly attributed, reproducible, security-reviewed platform build rather than new feature development.

### Architecture
- The active chain now separates upstream provenance, inherited baseline reproduction, packaging/security/accessibility, and later local product changes.
- 2026-07-19 — Documented the observed desktop, renderer, preload/IPC, WebUI/WebSocket, process-service, persistence, agent/provider, preview, and packaging boundaries without changing implementation scope.

### Documentation
- 2026-07-19 — Added a GitHub Pages-ready project overview, architecture guide, developer onboarding, security/privacy review model, and fork-baseline decision record.
- 2026-07-19 — Added Mermaid component, startup, bridge, persistence, packaging, trust-boundary, and verification diagrams.
- 2026-07-19 — Clarified that the inherited repository uses multiple persistence mechanisms and that WebUI remote access is a distinct deployment and security boundary.
- 2026-07-19 — Preserved the P0 architectural hold: the documentation does not approve a mirror/fork/derivative identity, public binaries, supported platforms, or release readiness.

### Implementation
- Existing application code, scripts, tests, and lockfile are inherited candidate assets and are not recorded as newly completed aevespers2 work.

### Release
- Release remains blocked until mirror/fork/derivative status, naming, attribution, supported platform, tests/build, security, SBOM, checksums, provenance, and rollback are approved and verified.

### Deployment
- No public binary or update channel is authorized before the fork and distribution decision.
- GitHub Pages content is prepared under `docs/`; publication configuration remains a repository setting and does not constitute an application deployment.

## Entry Format
- Date
- Category: Product / Architecture / Added / Changed / Fixed / Security / Release / Deployment
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable
