# Task Chain

## Purpose

Architect-controlled execution chain for the existing AionUi 1.7.0 application. Builders preserve upstream provenance, tests, evidence, and rollback paths.

## States

`PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Decide and document whether this repository is an upstream mirror, maintained fork, or independently distributed derivative, then reproduce the inherited 1.7.0 baseline.
- **User outcome:** A user can install a clearly named and attributed AionUi build for an explicitly supported platform and understand its local data, credentials, network, update, and rollback behavior.
- **MVP scope:** exact upstream commit/history and divergence report; license/notices; product/distribution identity; supported-platform decision; clean `npm ci`; lint/format/tests; one approved platform build and primary workflow smoke; Electron/storage/network/credential security review; checksums, SBOM, provenance, and rollback.
- **Priority:** Fork identity and baseline verification precede new features, rebranding, public binaries, or claims of cross-platform support.
- **Success criteria:** upstream relationship and name are approved; inherited versus local work is separated; clean install/checks pass at one immutable commit; one platform artifact is reproducible; primary workflow, accessibility, data handling, and security boundaries are evidenced.
- **Non-goals:** representing upstream 1.7.0 as newly created work, resetting version history, publishing unsigned/unreviewed binaries, guaranteeing every platform in the first candidate, or adding new AI/provider features before baseline acceptance.
- **Release rationale:** A provenance-correct fork baseline protects users and upstream attribution while creating a trustworthy point from which local improvements can be measured.

## Active Chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Approve fork/product/distribution identity and record upstream baseline | Architect | User approval | BLOCKED | Mirror/fork/derivative status, exact upstream commit, divergence, name, license/notices, supported platforms, and distribution channels are approved and documented. |
| P1 | Reproduce the inherited 1.7.0 health baseline | Architect | P0 | PROPOSED | `npm ci`, lint, format, unit/contract/integration tests, and the selected platform build/smoke pass with commands and retained evidence. |
| P2 | Verify security, accessibility, packaging, and rollback | Builder | P1 | PROPOSED | Electron, storage, network, credentials, updater, parser, accessibility, artifact signing status, checksums, SBOM, provenance, and rollback are recorded. |
| P3 | Define the first bounded local product change | Architect | P2 | PROPOSED | Scope identifies a user outcome, local divergence, files, tests, migration, and rollback without obscuring upstream history. |

## Builder Log

- 2026-07-19 — Prepared the documentation-only candidate in draft PR #1: project overview, architecture and trust-boundary guidance, Mermaid diagrams, developer onboarding, security/privacy review model, fork-baseline decision record, and an isolated static portfolio console under `docs/console/`. No inherited application implementation or release gate was changed.
- 2026-07-20 — Exact-head Pages Console Validation run `29712123942` passed at `d9269277999ff0640497ee3bdc00020dc61f9a84`, including submitted-source identity, required-file and JSON checks, local Markdown-link validation, SHA-256 evidence generation, and retained artifact upload. Artifact digest: `sha256:a42adcf6a4dbdf1a9452a6c59607e1ec2d8f8455505068922413100f7c2fe53a`. Jekyll rendering, browser accessibility/responsiveness, and Pages publication remain separate pending checks.

Record approvals, upstream/local commits, install/build/test commands, platform details, artifact hashes, security/accessibility findings, rollback evidence, and follow-ups.