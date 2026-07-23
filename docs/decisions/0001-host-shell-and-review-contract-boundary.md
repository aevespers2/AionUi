# ADR-0001: Separate the AionUi Host Shell from the Review Contract

- **Status:** Proposed
- **Date:** 2026-07-21
- **Decision owners:** A.L.I.S.T.A.I.R.E. Architect, AionUi owner, QSO-STUDIO owner, Repository `1` authority owner
- **Related:** QSO-STUDIO ADR-0002, `../portable-trust-review-profile.md`, `../runtime-mode-topology.md`, `../obstruction-and-gluing.md`

## Context

AionUi is an inherited Electron and WebUI application shell with local files, provider and agent integration, persistence, previews, process execution, and packaging behavior. QSO-STUDIO is a focused candidate for domain-neutral evidence review semantics. Both can present observations, proposals, dispositions, capabilities, receipts, corrections, revocations, annotations, and recovery state.

Without an explicit boundary, AionUi could accidentally become the owner of review semantics or operational authority merely because it provides the richer host shell. The same record could also be interpreted differently in AionUi and QSO-STUDIO, while a click, annotation, export, authenticated session, or successful command might be mistaken for approval or canonical acceptance.

The portfolio already separates these concerns:

- source repositories and adapters own source records;
- Repository `0` prepares bounded proposals and evidence;
- Repository `1` or an approved successor owns candidate canonical disposition, capabilities, revocation, and recovery state;
- QSO-STUDIO proposes the domain-neutral review contract;
- named human or domain authorities own consequential approvals;
- execution, repository mutation, release, deployment, publication, and payment remain external to a review surface.

## Decision

Adopt the following candidate split:

1. **AionUi is an optional host shell, not the review-contract authority.** It may render an accepted QSO-STUDIO contract through a separately versioned adapter, but it must not redefine record identity, review states, approval, capability, correction, revocation, or canonical-state semantics.
2. **QSO-STUDIO owns the candidate domain-neutral review contract.** The contract includes record normalization, comparison, annotation, non-authoritative export, accessibility semantics, authority-state vocabulary, and compatibility fixtures.
3. **Repository `1` remains the candidate authority source.** AionUi displays dispositions, capabilities, revocations, corrections, and checkpoints but cannot create them from local session or cache state.
4. **Human approval remains a separate immutable record.** An annotation or selection may be referenced by an external approval, but it is not itself approval.
5. **Runtime modes remain separate products and trust boundaries.** Static Pages, desktop, local WebUI, and remote WebUI require distinct data, adapter, credential, network, storage, and release policies.
6. **Privileged integration requires a separate decision.** Any authenticated write, process execution, filesystem mutation, repository change, model/provider credential, payment, signing, release, deployment, or remote-administration path requires its own ADR, capability contract, threat model, tests, incident plan, and approval.
7. **Fork identity remains independently blocked.** Accepting this architectural split does not decide whether AionUi is an upstream mirror, maintained fork, or independent derivative and does not authorize distribution.

## Contract boundary

```text
source or authority record
        ↓
QSO-STUDIO review contract
        ↓
AionUi host adapter or native Studio renderer
        ↓
non-authoritative display, annotation, comparison, or export
        ↓
external approval or authority system
```

The AionUi adapter must preserve:

- typed record and subject identifiers;
- contract and profile versions;
- immutable source repository and commit or artifact identity;
- integrity, attribution, temporal, replay, correction, and revocation state;
- privacy classification, redaction, retention, and export restrictions;
- authority class and explicit non-authority of UI state;
- deterministic transformation and comparison parameters;
- accessibility semantics and text alternatives;
- cache freshness and Repository `1` reconciliation references.

## Runtime-mode consequences

| Mode | Permitted contract role | Prohibited inheritance |
|---|---|---|
| Static Pages | Public documentation and non-sensitive fixtures | Credentials, private records, authenticated adapters, local files, authority-bearing controls |
| Desktop | Local rendering through explicitly admitted adapters | Ambient filesystem, provider, process, repository, payment, or canonical-state authority |
| Local WebUI | Authenticated local rendering under a reviewed deployment profile | Automatic equivalence to desktop trust or unrestricted host access |
| Remote WebUI | No accepted portable-trust role until topology and security gates pass | Exposure based only on existing inherited commands or successful login |

## Consequences

### Positive

- one review vocabulary can be tested across QSO-STUDIO and AionUi;
- the inherited shell can remain replaceable without changing portfolio authority;
- accessibility and hostile-input fixtures can be shared;
- local cache or session state cannot silently become canonical state;
- fork, application, adapter, and contract versions remain distinct;
- static Pages can remain useful without carrying private or privileged functionality.

### Costs

- AionUi must implement explicit mappings instead of ad hoc record cards;
- both repositories require shared fixtures and coordinated compatibility releases;
- some inherited provider, agent, filesystem, or WebUI features may remain outside the accepted adapter boundary;
- mode-specific configuration and release evidence must be maintained separately;
- the portfolio must designate a neutral profile registry and versioning process.

## Rejected alternatives

### Make AionUi the canonical review and approval system

Rejected because the inherited shell would acquire private-data, credential, authority, recovery, and release responsibilities before its fork identity and security baseline are accepted.

### Let AionUi and QSO-STUDIO define separate review models

Rejected because correction, revocation, partial-state, identity, and authority semantics could diverge silently and prevent deterministic cross-interface review.

### Treat authenticated UI actions as approval

Rejected because authentication identifies a session or actor but does not prove the exact policy, capability, scope, expected state, separation of duties, or recovery authority required for a consequential action.

### Collapse all runtime modes into one product profile

Rejected because static Pages, Electron desktop, local WebUI, and remote WebUI cross materially different trust boundaries and require different evidence.

## Acceptance conditions

This ADR may move to `Accepted` only when:

- AionUi and QSO-STUDIO owners approve the split;
- Repository `1` or another authority owner approves the display-only disposition boundary;
- the first exact review-record profile and deterministic fixture set are selected;
- identity, annotation, comparison, export, correction, revocation, cache, and recovery schemas are versioned;
- static, desktop, local-WebUI, and remote-WebUI allowlists are approved;
- privacy, retention, redaction, export, offline, and diagnostic rules are accepted;
- compatibility fixtures pass in QSO-STUDIO and an AionUi adapter candidate;
- accessibility, hostile-input, stale-state, replay, partial-state, correction, revocation, freeze, and recovery tests pass;
- no direct execution, credential, repository-write, payment, release, deployment, or self-approval path is present in the review adapter;
- fork identity and application distribution remain governed by their separate release gates.

## Rollback

If the adapter introduces authority ambiguity, privacy downgrade, stale revocation handling, inaccessible state, incompatible interpretation, mode confusion, or recovery dependence on a compromised shell:

1. disable the AionUi adapter independently of the application shell;
2. revoke adapter sessions and invalidate affected caches;
3. preserve source records, annotations, exports, fixtures, and incident evidence;
4. return to the last accepted QSO-STUDIO contract or static fixture renderer;
5. reconstruct authoritative state from Repository `1` and immutable evidence;
6. require a new ADR and compatibility bundle before re-enabling integration.

Rollback does not delete source evidence, rewrite historical review records, or change the accepted fork baseline.
