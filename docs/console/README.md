# AionUi Portfolio Console

The console is a static GitHub Pages demonstration under `docs/console/`.

## What it does

- presents an AionUi-style responsive workspace;
- reads the checked-in portfolio configuration;
- optionally fetches public repository metadata from the unauthenticated GitHub REST API;
- links to active repositories and documentation;
- explains the adapter and authority boundaries required for future integrations;
- keeps a session-only browser activity log.

## What it does not do

- run Electron, preload, IPC, Express, WebSocket, SQLite, local-file, CLI-agent, MCP, provider, model, update, signing, or packaging code;
- store tokens or credentials;
- write to repositories, issues, pull requests, workflows, releases, or deployments;
- claim that the inherited AionUi application is browser-compatible or released.

## Future backend contract

A non-static backend may be added only after approval of:

1. authenticated user and service identities;
2. explicit read and write scopes;
3. allowed origins and transport security;
4. secret storage and rotation;
5. input/output schemas and size limits;
6. audit, rate-limit, timeout, retry, and idempotency behavior;
7. human approval gates for consequential actions;
8. incident response and rollback.

The recommended progression is public reads, authenticated reads, inert draft actions, and then explicitly approved writes. GitHub Pages itself remains a static, credential-free client.

## Local preview

From the repository root:

```bash
python3 -m http.server 8000 --directory docs
```

Then open `http://localhost:8000/console/`.

## Files

- `index.html` — semantic shell and views.
- `styles.css` — responsive accessible visual system.
- `app.js` — navigation, public metadata refresh, filtering, and in-memory activity.
- `portfolio.json` — checked-in repository roles and maturity labels.
