---
layout: default
title: AionUi Fork Documentation
---

# AionUi

AionUi is an inherited Electron application that presents command-line AI agents, model providers, local files, document previews, and WebUI access through a graphical workspace. This repository currently tracks an AionUi `1.7.0` codebase and is being evaluated as a possible mirror, maintained fork, or independently distributed derivative.

> **Release status: blocked.** No aevespers2 binary, update channel, or cross-platform support claim is approved until the fork identity, exact upstream baseline, naming, platform scope, distribution channel, verification evidence, and rollback plan are accepted.

## Static portfolio console

[Open the AionUi Portfolio Console](console/)

The console is a browser-safe GitHub Pages demonstration surface. It provides AionUi-style navigation, public repository metadata, portfolio roles, architectural boundaries, and future adapter seams. It does **not** run the Electron main process, WebSocket/Express backend, local files, SQLite, command-line agents, MCP processes, credentials, model providers, repository writes, releases, or deployments.

## Current objective

The active P0 objective is deliberately narrow:

1. identify the exact upstream source and inherited commit history;
2. approve whether this repository is a mirror, maintained fork, or derivative;
3. distinguish inherited work from local work;
4. reproduce one supported-platform baseline from a clean environment;
5. retain install, test, security, accessibility, artifact, provenance, and rollback evidence.

New AI-provider features, rebranding, public binaries, and broad cross-platform claims remain outside the approved scope until that baseline is complete.

## Documentation

| Guide | Purpose |
|---|---|
| [Portfolio console](console/) | Static AionUi-style shell wired to public repository metadata and bounded future integration points |
| [Architecture](architecture.md) | Runtime processes, adapters, data flows, storage, WebUI, packaging, and trust boundaries |
| [Developer onboarding](development.md) | Clean setup, commands, verification workflow, contribution discipline, and evidence capture |
| [Security and privacy](security-and-privacy.md) | Assets, boundaries, inherited risk areas, review checklist, and release-blocking controls |
| [Fork baseline decision](fork-baseline.md) | P0 decision record, approval matrix, provenance requirements, and consequences of each repository identity |
| [Task chain](https://github.com/aevespers2/AionUi/blob/main/taskchain.md) | Architect-controlled execution order and acceptance criteria |
| [Release plan](https://github.com/aevespers2/AionUi/blob/main/release.md) | Candidate scope, release gates, artifact requirements, and rollback criteria |
| [Changelog](https://github.com/aevespers2/AionUi/blob/main/changelog.md) | Product, architecture, documentation, release, and deployment history |

## Observed runtime shape

```mermaid
flowchart LR
    U[User] --> R[React renderer]
    R --> B{Runtime bridge}
    B -->|Desktop| P[Preload context bridge]
    P --> I[Electron IPC adapter]
    B -->|WebUI| W[Authenticated WebSocket adapter]
    I --> M[Electron main process]
    W --> S[Express and WebSocket server]
    M --> C[Process services]
    S --> C
    C --> D[(Local configuration, chat data, and SQLite)]
    C --> A[AI providers and command-line agents]
    C --> F[Local files and preview pipeline]
    M --> K[Electron packaging and platform integration]
```

The desktop and WebUI surfaces share a bridge abstraction, but they cross different security boundaries. Desktop messages traverse the preload/IPC path; browser messages traverse authenticated HTTP and WebSocket endpoints. Both ultimately reach process services that may access local data, files, external model APIs, or installed command-line agents.

## Supported operating modes in the inherited code

| Mode | Entry point | Boundary requiring review |
|---|---|---|
| Desktop | `npm start` | Electron renderer, preload bridge, main process, native modules, filesystem access |
| Local WebUI | `npm run webui` | Local HTTP/WebSocket server, login/session handling, browser bridge |
| Remote WebUI | `npm run webui:remote` | Network exposure, authentication, CORS, cookies, TLS/reverse proxy assumptions, host firewall |
| Static Pages console | GitHub Pages `docs/console/` | Public metadata only; no privileged runtime authority |
| Packaging | `npm run package`, `npm run make`, or platform distribution scripts | Native dependency rebuilds, code signing, notarization, installer identity, checksums, updater behavior |

These modes are inherited capabilities or bounded documentation demonstrations, not verified support commitments from this fork.

## Repository guardrails

- Preserve upstream copyright, license, notices, commit lineage, and contributor attribution.
- Do not describe inherited AionUi `1.7.0` implementation as newly created aevespers2 work.
- Use the package lock and exact tool versions for baseline reproduction.
- Prefer one verified platform over unverified cross-platform claims.
- Treat API keys, session tokens, local conversation data, filesystem access, remote WebUI, updates, and generated artifacts as security-sensitive.
- Keep patches bounded, reviewable, reversible, and tied to commands and evidence.
- Keep the Pages console read-only and credential-free.
- Stop when the requested change depends on an unresolved fork identity or distribution decision.

## Baseline release gates

A candidate remains blocked until all of the following are evidenced at one immutable commit:

- approved repository identity and product name;
- exact upstream baseline and divergence report;
- clean dependency installation;
- lint, format, unit, contract, integration, and primary-workflow smoke results;
- one reproducible platform build or package;
- Electron, WebUI, credential, storage, network, parser, updater, dependency, secret, and workflow review;
- keyboard, focus, label, contrast, scaling, and error-state accessibility review;
- SBOM, signing/notarization status, artifact checksums, provenance manifest, and rollback procedure.

## Documentation status

This site documents the observed inherited architecture and the controls required to evaluate it. The static console is a safe demonstration and integration scaffold; it does **not** approve a fork identity, certify security, promise support for a platform, authorize backend connections, or authorize distribution.
