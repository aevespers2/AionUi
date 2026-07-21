# Punch List

## P0 — Repository and product identity

- [ ] Approve AionUi as an upstream mirror, maintained fork, or independent derivative.
- [ ] Record the exact upstream repository and immutable baseline commit.
- [ ] Record the first local commit and produce a file/commit divergence manifest.
- [ ] Approve product name, package identifiers, version suffix, attribution, and public notices.
- [ ] Select the first supported platform and distribution channel.
- [ ] Name support, security, signing, update, privacy, incident, and rollback owners.
- [ ] Define the non-goals and disposition of unsupported desktop/WebUI modes.

## P1 — Host-shell and review-contract boundary

- [x] Add `docs/decisions/0001-host-shell-and-review-contract-boundary.md` aligned with QSO-STUDIO ADR-0002.
- [ ] Approve or revise ADR-0001 in both repositories at immutable commits.
- [ ] Decide whether AionUi hosts a QSO-STUDIO-compatible review adapter, defines a separate role, or is excluded from portable-trust review.
- [ ] Assign ownership for the neutral review/display record, profile registry, compatibility policy, and deprecation process.
- [ ] Approve record namespaces for observations, interpretations, proposals, capabilities, receipts, dispositions, annotations, corrections, revocations, and checkpoints.
- [ ] Define exact device, workspace, repository, commit, platform-profile, and baseline-policy binding.
- [ ] Define privacy classification, redaction, retention, deletion, export, and cache-invalidation rules.
- [ ] Define correction, revocation, emergency-stop, recovery, and offline behavior.
- [ ] Represent human approval as a separate immutable record rather than UI session state.

## P2 — Runtime-mode topology

- [x] Add `docs/runtime-mode-topology.md` separating static Pages, desktop, local WebUI, remote WebUI, and packaging boundaries.
- [ ] Approve the static Pages data and adapter allowlist.
- [ ] Approve the Electron desktop data, adapter, credential, filesystem, process, network, and storage profile.
- [ ] Approve the local WebUI bind, authentication, session, cookie, CSRF, CORS, origin, WebSocket, logging, and firewall profile.
- [ ] Keep remote WebUI blocked until deployment, TLS, proxy, authentication, session-revocation, monitoring, incident, privacy, and disaster-recovery architecture is accepted.
- [ ] Approve packaging, signing, notarization, update, distribution, support, and rollback ownership.
- [ ] Define migration evidence required when moving a workflow or adapter between modes.
- [ ] Verify that a capability accepted in one mode fails closed in every other mode unless explicitly reissued.

## P3 — Gluing fixtures

- [ ] Add observation-adapter → AionUi display fixtures.
- [ ] Add Repository `0` proposal → AionUi review fixtures.
- [ ] Add Repository `1` disposition/capability/revocation → AionUi fixtures.
- [ ] Add executor receipt → AionUi partial-state and reconciliation fixtures.
- [ ] Add QSO-STUDIO ↔ AionUi review-record compatibility fixtures.
- [ ] Add Seeker/Digitalis/Bridge → Repository `1` → AionUi lineage fixtures.
- [ ] Add wrong-device, wrong-workspace, wrong-repository, and wrong-head rejection fixtures.
- [ ] Add stale, replayed, unsupported-version, malformed, and digest-mismatch fixtures.
- [ ] Add duplicate/conflicting JusticeForMe and PhantomBlock observation fixtures.
- [ ] Add privacy downgrade and forbidden public-mode field fixtures.
- [ ] Add broadened, expired, revoked, and executor-mismatched capability fixtures.
- [ ] Add partial execution, rollback, correction, revocation, and cache invalidation fixtures.
- [ ] Add UI-annotation-is-not-approval and delivery-is-not-acceptance fixtures.
- [ ] Add static-to-desktop, desktop-to-local-WebUI, and local-to-remote mode-confusion rejection fixtures.
- [ ] Add inherited ambient filesystem/provider/process permission rejection fixtures for the review adapter.

## P4 — Inherited baseline reproduction

- [ ] Record Node, npm, operating system, architecture, and native toolchain versions.
- [ ] Run clean `npm ci` from the approved immutable baseline.
- [ ] Run lint, formatting checks, unit tests, contract tests, integration tests, and primary workflow smoke tests.
- [ ] Reproduce one selected platform build/package.
- [ ] Record native dependency rebuilds and Electron packaging inputs.
- [ ] Produce an SBOM, source archive, package checksum manifest, and provenance statement.
- [ ] Record signing, notarization, updater, and installer status without overstating support.

## P5 — Security, privacy, and accessibility

- [ ] Review Electron main, renderer, preload, IPC, context isolation, sandboxing, and navigation controls.
- [ ] Review local WebUI and remote WebUI authentication, sessions, cookies, CORS, TLS/proxy assumptions, rate limits, logging, and firewall requirements.
- [ ] Review providers, CLI agents, MCP processes, filesystem access, shell/process execution, and credential storage.
- [ ] Review SQLite and file persistence, local paths, prompt/conversation data, deletion, backup, and migration behavior.
- [ ] Review parsers, document previews, imported files, external URLs, and untrusted content.
- [ ] Review dependency, workflow, release, artifact, and update supply-chain controls.
- [ ] Test keyboard navigation, focus order, labels, announcements, contrast, scaling, reduced motion, and error/unknown states.
- [ ] Test accessibility semantics for corrections, revocations, partial state, stale state, privacy redaction, and authority class.
- [ ] Perform static Pages publication-safety review separately from Electron/WebUI security review.

## P6 — Operations and recovery

- [ ] Define session revocation and credential rotation procedures independent of the local app.
- [ ] Define adapter disablement independent of the AionUi host shell.
- [ ] Define cache invalidation and canonical-state reconstruction from Repository `1`.
- [ ] Define lost/stolen/replaced-device recovery and re-enrollment.
- [ ] Define local-data export, preservation, wipe, reinstall, and restore procedures.
- [ ] Define remote WebUI emergency disable and network containment.
- [ ] Run a tabletop exercise for stale capability, privacy exposure, compromised adapter, partial execution, mode confusion, and rollback.
- [ ] Record recovery order from least authority to greatest authority.

## P7 — Documentation and release evidence

- [x] Add project overview, architecture, onboarding, security/privacy, and fork-baseline documentation.
- [x] Add a read-only static portfolio console and exact-head source validation.
- [x] Add portable-trust review profile and obstruction/gluing analysis.
- [x] Add host-shell ADR and runtime-mode topology.
- [x] Add this punch list and align `taskchain.md`, `release.md`, and `changelog.md`.
- [ ] Render Jekyll locally or in CI with pinned tooling.
- [ ] Run internal link, accessibility, responsive layout, and publication-safety checks.
- [ ] Retain exact-head site and evidence artifacts with SHA-256 manifests.
- [ ] Record explicit human approval before Pages publication, application release, distribution, remote WebUI exposure, or privileged adapter activation.

## Stop conditions

Stop and preserve evidence when:

- fork identity, provenance, or attribution is uncertain;
- a task requires credentials, network exposure, local file access, repository writes, model calls, or process execution not explicitly authorized;
- a UI interaction, authenticated session, export, delivery, or execution could be mistaken for approval or canonical-state mutation;
- a private record could enter static Pages or an unauthorized WebUI mode;
- source, profile, device, workspace, repository, or expected-head identity does not match;
- a capability or adapter appears outside its approved runtime mode;
- inherited filesystem, provider, agent, or process access is being treated as ambient review-adapter authority;
- correction, revocation, emergency-stop, or recovery state cannot be verified;
- tests, artifacts, hashes, or rollback evidence are missing or inconsistent.
