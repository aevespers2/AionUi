---
layout: default
title: Obstruction and Gluing Analysis
---

# Obstruction and Gluing Analysis

## Method

This ledger treats each repository or service as a local architectural section and each versioned contract as a proposed gluing map. A portfolio feature is considered composable only when pairwise contracts agree and the relevant triple-overlap paths produce equivalent, independently verifiable results.

This is an engineering compatibility analysis. It is not a claim that formal sheaf cohomology or homology groups have been computed.

## Active obstructions

| ID | Obstruction | Why the sections do not glue | Lowest-coupling repair candidate |
|---|---|---|---|
| AUI-O01 | Fork identity | AionUi may be an upstream mirror, maintained fork, or independent derivative, producing different naming, support, release, security, and update obligations. | Approve one identity, exact upstream baseline, divergence manifest, support owner, and rollback path before runtime claims. |
| AUI-O02 | Runtime-mode ambiguity | Desktop, local WebUI, remote WebUI, and static Pages cross different trust boundaries but can look like one product mode. | Require an explicit mode banner, authority manifest, network exposure, storage location, and credential boundary in every surface. |
| AUI-O03 | Display/approval collapse | Selecting, annotating, exporting, or clicking an action in a review UI could be mistaken for canonical approval. | Make UI records non-authoritative; bind consequential approvals to immutable external records and named authorities. |
| AUI-O04 | AionUi/QSO-STUDIO overlap | Both repositories describe evidence-review surfaces, but annotation, comparison, export, and approval semantics are not jointly versioned. | Use one neutral review-record and display contract; keep QSO-STUDIO domain-neutral and AionUi the host shell unless another disposition is approved. |
| AUI-O05 | Record identity collapse | Observation, interpretation, proposal, capability, receipt, disposition, annotation, and checkpoint identities can be merged into a generic UI item. | Preserve type-specific IDs, namespaces, profile versions, hashes, and transformation lineage throughout views and exports. |
| AUI-O06 | Local versus canonical state | SQLite, files, session state, and UI caches may retain values that differ from Repository `1` canonical state. | Treat local state as a cache; require freshness, canonical checkpoint, correction, revocation, and invalidation semantics. |
| AUI-O07 | Device/workspace collision | A valid device record may be shown in the wrong repository workspace, or a repository capability may be shown for the wrong device. | Independently bind device, workspace, repository, base commit, expected head, profile, and executor identities. |
| AUI-O08 | Capability-class confusion | Device remediation, repository edits, model/provider use, filesystem access, release, deployment, and payment can appear as generic actions. | Use typed capability classes with visible resource, command, path, network, provider, expiry, and revocation boundaries. |
| AUI-O09 | Stale/replayed evidence | Cached or imported records may be stale, replayed, unsupported, superseded, or corrected. | Validate freshness, replay IDs, profile versions, source hashes, and supersession chains; visibly fail closed. |
| AUI-O10 | Privacy downgrade | Sensitive host inventories, local paths, prompts, conversations, device IDs, or credentials could cross into public Pages or broadly accessible WebUI. | Enforce classification and redaction before rendering, prohibit private adapters in static mode, and test forbidden-field rejection. |
| AUI-O11 | Transformation opacity | Rendering, normalization, redaction, preview parsing, or export may alter evidence without a declared transformation record. | Record input/output hashes, transformation type, tool version, lossiness, redactions, and retained source reference. |
| AUI-O12 | Provider/agent authority confusion | A provider or CLI agent connected through the UI may be assumed to inherit device, repository, or canonical-state authority. | Treat each provider/agent as an independently admitted adapter with scoped credentials and no ambient authority. |
| AUI-O13 | Remote WebUI exposure | Remote WebUI may expose sessions, filesystem operations, agents, or providers through unclear TLS, proxy, CORS, cookie, and firewall assumptions. | Keep remote mode blocked until deployment topology, authentication, session revocation, origin, TLS, rate, logging, and incident controls pass review. |
| AUI-O14 | Correction and revocation divergence | An item may remain visible as valid after correction, revocation, emergency stop, or recovery. | Define push/poll invalidation, cache versioning, immutable correction chains, and fail-closed offline behavior. |
| AUI-O15 | Partial-state optimism | Partial collection or partial execution may be reduced to a successful summary card. | Require per-check status, partial-failure display, unresolved findings, and independent canonical reconciliation. |
| AUI-O16 | Public/private topology | Static Pages, local desktop, authenticated local WebUI, and remote WebUI need distinct data and adapter allowlists. | Publish a topology matrix and enforce separate builds/configurations rather than runtime inference. |
| AUI-O17 | Incident recovery dependence | Recovery could rely on the same compromised local application, cache, or credentials. | Reconstruct from Repository `1` and external evidence, revoke sessions independently, and restore adapters in bounded order. |
| AUI-O18 | Release-evidence mismatch | Static documentation validation could be misread as Electron/WebUI security or application release evidence. | Keep documentation, application build, platform package, security, accessibility, signing, and deployment evidence as separate gates. |

## Pairwise gluing matrix

| Edge | Required shared contract | Required witness |
|---|---|---|
| Observation adapter → AionUi | observation envelope and display profile | supported and partial collection render with source hashes and limitations |
| Repository `0` → AionUi | proposal schema and state vocabulary | exact device/workspace proposal with pre-state, expected state, rollback, and `UNKNOWN` handling |
| Repository `1` → AionUi | disposition, capability, revocation, correction, and checkpoint schemas | canonical view agrees with immutable Repository `1` record and invalidates stale cache |
| Executor → AionUi | execution and resulting-state receipt | partial failure cannot render as reconciled success |
| QSO-STUDIO → AionUi | neutral review/annotation/export record | identical annotation semantics and non-authoritative status in both surfaces |
| Bridge → AionUi | transport artifact and delivery receipt | delivery status remains distinct from truth and canonical acceptance |
| Digitalis → AionUi | interpretation/projection lineage | interpretation remains distinct from source observation |
| AionUi → external approval authority | exact approval-reference contract | UI selection alone cannot produce approval; immutable approval record is required |
| AionUi → public Pages | publication profile | forbidden private fields and privileged endpoints are rejected |

## Triple-overlap witnesses

### Observation → Repository `0` → AionUi

The device, observation, collection status, source hash, profile version, and limitations shown by AionUi must match the proposal inputs used by Repository `0`. Duplicate adapters must not inflate confidence.

### Repository `0` → Repository `1` → AionUi

The proposal admitted to Repository `1` quarantine must be the same immutable proposal displayed for review. AionUi must show rejection, review, capability, correction, or revocation without inventing a new state.

### Repository `1` → executor → AionUi

The executor must be bound to the capability's exact device, workspace, action class, resources, time, and expected state. AionUi must keep execution success separate from Repository `1` reconciliation.

### Seeker/Digitalis/Bridge → Repository `1` → AionUi

Source observation, interpretation, transport artifact, delivery receipt, and canonical disposition must remain separately identified. Display transformations must retain lineage.

### QSO-STUDIO → AionUi → approval authority

An annotation or exported proposal should produce equivalent review evidence in either interface, but neither may grant approval. The final approval reference must bind the exact immutable item reviewed.

### Incident authority → Repository `1` → AionUi

Emergency stop, correction, or revocation must invalidate local sessions, cached capabilities, exports, and displayed state. Offline mode must not continue privileged operations from stale authority.

## Required negative fixtures

- wrong-device, wrong-workspace, wrong-repository, and wrong-head records;
- unsupported profile, malformed record, digest mismatch, stale record, and replayed record;
- duplicate and conflicting observations from JusticeForMe and PhantomBlock;
- privacy-classification downgrade and forbidden static-mode fields;
- expired, broadened, revoked, or executor-mismatched capability;
- partial execution and rollback-required receipt;
- successful transport displayed as canonical acceptance;
- UI annotation or confirmation displayed as approval;
- correction or revocation missing from local cache and export;
- remote WebUI request without accepted topology and session evidence;
- provider or CLI agent attempting ambient filesystem, repository, device, or payment authority.

## Release obstruction summary

The highest-priority architectural obstruction remains AionUi's unresolved fork/distribution identity. The highest-priority portfolio gluing obstruction is the absence of one accepted neutral review/display contract shared with QSO-STUDIO and the portable-trust evidence path. Until both are resolved, AionUi remains a documentation and interface candidate rather than an approved control or review authority.

## Scope status

This analysis adds no runtime, backend, adapter, credential, host inspection, model call, filesystem access, repository write, approval, release, deployment, payment, or canonical-state authority.