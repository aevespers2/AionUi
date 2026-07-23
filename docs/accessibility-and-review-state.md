---
layout: default
title: Accessibility and Review-State Assurance
---

# Accessibility and Review-State Assurance

Status: **documentation and review plan only; no accessibility certification, runtime approval, or publication authority**

AionUi is being evaluated as an optional human-facing host shell for a separately governed QSO-STUDIO-compatible review contract. That role makes accessibility more than a visual-quality concern: a user must be able to perceive **what a record is**, **how current it is**, **whether it is complete**, **what authority it carries**, and **what action is actually available** without relying on color, animation, pointer precision, or unstated domain knowledge.

This guide defines the review-state vocabulary, accessible presentation requirements, test evidence, and stop conditions for the static Pages console and any future desktop or WebUI review adapter. It does not modify the inherited Electron or WebUI implementation.

## Assurance boundary

This document:

- defines requirements and evidence expectations;
- distinguishes static Pages, desktop, local WebUI, remote WebUI, and packaging profiles;
- requires prose equivalents for diagrams and visible text equivalents for machine states;
- prevents display, selection, annotation, authentication, export, delivery, or execution from being presented as approval;
- keeps unknown, stale, partial, corrected, revoked, withdrawn, private, and unsupported states explicit;
- requires rendered and assistive-technology review before any accessibility claim.

This document does **not**:

- certify conformance to WCAG, Section 508, EN 301 549, or another standard;
- approve an application release or GitHub Pages publication;
- authorize a review adapter, credential, backend, network exposure, repository write, capability, payment, or canonical-state mutation;
- infer accessibility from source inspection alone.

## User-critical questions

Every review surface must answer these questions in text that is available to keyboard and assistive-technology users:

1. **Identity:** What record, subject, repository, commit, workspace, device, profile, and generation am I viewing?
2. **Provenance:** Who or what produced it, from which sources, and at what exact version?
3. **Freshness:** Is it current, stale, superseded, replayed, corrected, withdrawn, or unverifiable?
4. **Completeness:** Is the source set complete, partial, conflicting, redacted, inaccessible, or unsupported?
5. **Authority:** Is this an observation, interpretation, proposal, review annotation, capability, receipt, disposition, correction, revocation, recovery checkpoint, or external human approval record?
6. **Effect:** Does it create no authority, request review, constrain an existing authorization, record execution evidence, or carry a separately approved authority effect?
7. **Action:** What can the user safely do next, and what cannot be done from this surface?
8. **Recovery:** How can the state be corrected, revoked, reloaded, exported, or reconstructed without losing provenance?

A surface that cannot answer these questions must show `UNKNOWN` or remain unavailable. It must not substitute icons, color, confidence styling, or implied workflow position for explicit text.

## Canonical presentation states

The following display vocabulary is documentation-level guidance. Final record names and machine values remain governed by the neutral review contract and Repository `1` authority decisions.

| Display state | Required meaning | Required accessible presentation | Forbidden implication |
|---|---|---|---|
| `CURRENT` | The exact record generation is the current accepted view for its bounded source and profile | Visible text, timestamp, source generation, and freshness explanation | Current does not mean approved, safe, complete, or canonical |
| `STALE` | A newer generation exists or the freshness window expired | Text label, reason, newer-generation link when public, and disabled authority-sensitive controls | Stale records must not appear actionable |
| `SUPERSEDED` | A later record replaces this record while preserving history | Text label, replacement identity, and preserved prior rationale | Superseded does not mean deleted or false |
| `PARTIAL` | Some expected sources, acknowledgments, fields, or consumers are missing | Text label, explicit missing items, impact, and next verification step | Partial must not be rounded up to complete |
| `CONFLICTING` | Two or more validly identified sources disagree | Text label, source-by-source comparison, unresolved fields, and review owner | Conflict must not be hidden by an aggregate score |
| `UNKNOWN` | The system lacks enough verified information to classify the state | Text label, missing evidence, and safe next step | Unknown must not be styled as a weak success |
| `UNSUPPORTED` | The profile, schema, version, mode, or record class is not accepted by this consumer | Text label, rejected version, accepted alternatives, and migration route if available | Parsing success must not imply semantic support |
| `CORRECTED` | A correction record changes the interpretation or valid fields of an earlier record | Text label, correction identity, affected fields, and original-history link | Correction must not silently overwrite history |
| `REVOKED` | Previously granted authority or accepted state has been withdrawn by an authorized record | Prominent text, effective time, scope, issuer, and disabled dependent actions | Revoked state must never remain visually actionable |
| `WITHDRAWN` | A claim, publication, or evidence presentation is no longer offered as current | Text label, withdrawal reason, effective generation, and residual-copy warning | Withdrawal must not be represented as deletion from uncontrolled copies |
| `PRIVACY-RESTRICTED` | Some data cannot be shown in this mode or to this audience | Text label, purpose-limited explanation, and safe access route | Redaction must not imply absence or failure |
| `REJECTED` | A separately authorized decision rejected the proposal or claim | Text label, decision identity, reason class, appeal or correction route | Rejection must not be inferred from an error or missing data |
| `QUARANTINED` | The record is preserved but withheld from promotion pending review | Text label, trigger, review owner, and prohibited effects | Quarantine must not be displayed as deletion or guilt |
| `RECOVERING` | A bounded recovery process is active and resulting state is not yet verified | Text label, recovery checkpoint, affected functions, and stop conditions | In-progress recovery must not be presented as restored |
| `RESTORED` | Recovery completed and the resulting state was independently verified | Text label, restored generation, verification evidence, and residual limitations | Restored does not erase the incident or failed state |

## Authority-class presentation

Every record card, table row, detail view, export, and announcement must expose an authority class in text. The minimum classes are:

- **Observation** — reports a bounded fact or measurement; no approval effect.
- **Interpretation** — explains or classifies evidence; no independent authority effect.
- **Proposal** — requests consideration; no approval or execution effect.
- **Review annotation** — records reviewer notes or comparison; not a disposition.
- **Capability** — narrowly permits an action only when separately issued, current, correctly scoped, and independently verified.
- **Execution receipt** — reports an attempted action and result; not approval, settlement, or canonical acceptance.
- **Disposition** — a separately governed accept, reject, quarantine, correct, revoke, or recover decision.
- **External human approval** — an independently identified approval record; never inferred from UI session state.

The interface must never use generic labels such as `approved`, `complete`, `success`, or `verified` without naming the authority class, scope, issuer, subject, generation, and evidence boundary.

## Interaction requirements

### Keyboard and focus

- All interactive elements must be reachable and operable using a keyboard alone.
- Focus order must follow the reading and task sequence, not visual coordinates or DOM accidents.
- A visible focus indicator must remain perceivable at 200% and 400% zoom and in forced-colors or high-contrast modes.
- Modal, drawer, and menu focus must be contained while open and restored to the invoking control when closed.
- Skip links must allow direct movement to the primary content, record list, active finding, and evidence details.
- Dynamic updates must not move focus unexpectedly.
- Destructive, authority-sensitive, or externally consequential actions remain unavailable unless separately authorized and must never be triggered by a single ambiguous keystroke.

### Names, roles, and values

- Controls require stable accessible names that match or include their visible labels.
- Icons require text labels or accessible names; decorative icons must be hidden from assistive technology.
- Tables require headers, captions where needed, and a reading order that preserves record identity and state relationships.
- Status badges must expose their complete text and reason, not only a tooltip.
- Links must describe their destination or purpose without relying on surrounding visual context.

### Announcements and live updates

- Loading, validation, correction, revocation, withdrawal, error, and recovery changes require concise announcements.
- Routine background refreshes should not interrupt the user.
- High-impact changes such as revocation, privacy restriction, or failed recovery require a persistent visible message in addition to any live-region announcement.
- Announcement text must identify the affected record and state change without exposing restricted data.
- Repeated polling must not create duplicate announcements for an unchanged generation.

### Error and recovery behavior

- Errors must identify the affected field, record, or operation and provide a safe correction path.
- Validation errors must not clear valid user input or erase review notes.
- Network or backend failure must preserve the last verified state with an explicit stale/offline label.
- Retrying must be idempotent or clearly warn when it is not.
- A failed correction, revocation, export, or recovery request must not be displayed as complete.
- Error summaries must link to the affected controls or records.

## Visual and cognitive accessibility

- Text and essential graphical elements require sufficient contrast under the selected review standard.
- Color may reinforce a state but must never be the only distinction.
- The interface must remain usable at 200% zoom and support reflow at 400% without two-dimensional scrolling except where intrinsically necessary, such as a large data table or diagram.
- State names, reason classes, and next steps should use consistent plain language across Pages, desktop, and WebUI modes.
- Dense evidence views should support progressive disclosure while keeping identity, authority, freshness, and critical warnings visible.
- Motion must be optional; reduced-motion preferences must suppress nonessential transitions and animations.
- Timed interactions must be absent or adjustable unless a separate security requirement justifies them and an accessible alternative exists.
- Reading order and heading structure must remain logical when styles are disabled.

## Diagrams, charts, and logs

Every Mermaid diagram, architecture image, chart, timeline, and activity log requires:

- a descriptive title;
- a concise purpose statement;
- a prose equivalent describing nodes, edges, direction, state, and limitations;
- source and generation identity where the content is evidence-bearing;
- text representation of color, line style, shape, or icon semantics;
- a non-visual way to reach the same decision or next step.

The prose equivalent is normative for accessibility review when the rendered diagram cannot be independently interpreted by assistive technology.

## Mode-specific assurance matrix

| Mode | Minimum documentation evidence | Additional rendered evidence required before acceptance |
|---|---|---|
| Static Pages | Public-data allowlist, no credentials, semantic HTML plan, state vocabulary, local-link and publication-safety validation | Keyboard walkthrough, focus visibility, zoom/reflow, contrast, reduced motion, screen-reader smoke, responsive layout, and no-private-data review |
| Electron desktop | Renderer/preload/main-process boundary, OS integration, storage, process, file, provider, and notification semantics | Platform-specific keyboard and screen-reader review, native dialog behavior, scaling, high contrast, updater/error flows, and selected workflow completion |
| Local WebUI | Bind address, authentication/session, browser bridge, origin, cookie, CORS, WebSocket, and offline behavior | Browser/assistive-technology matrix, session expiry and revocation announcements, reconnect behavior, focus restoration, and local-network failure handling |
| Remote WebUI | Deployment, TLS/proxy, identity, session, monitoring, incident, privacy, retention, and disaster-recovery architecture | Independent security and accessibility review in the deployed environment; remains blocked until separately authorized |
| Packaging and updates | Installer/updater identity, signing status, artifact provenance, supported platform, migration, and rollback | Accessible install/update/error/recovery flows and verified rollback on the selected platform |

Acceptance in one mode does not transfer to another. Static Pages success does not validate Electron or WebUI accessibility, and local WebUI success does not approve remote deployment.

## Evidence record template

Each accessibility review should preserve:

| Field | Required content |
|---|---|
| Candidate identity | Repository, exact commit, branch or PR, build or rendered artifact digest |
| Mode and environment | Static Pages, desktop, local WebUI, remote WebUI, or packaging; OS, browser, application, viewport, zoom, theme, language |
| Assistive technology | Product, version, input method, and relevant configuration |
| Scenario | User goal, starting state, records involved, and expected outcome |
| State coverage | Current, stale, partial, unknown, conflicting, corrected, revoked, withdrawn, privacy-restricted, error, and recovery states exercised |
| Authority coverage | Observation, interpretation, proposal, annotation, capability, receipt, disposition, and external human approval |
| Result | Pass, fail, blocked, not applicable, or not tested |
| Finding | Reproduction steps, expected versus observed behavior, severity, affected users, and evidence |
| Repair | Proposed change, implementation owner, verification owner, migration or compatibility effect, and rollback |
| Residual risk | Known limitation, unsupported route, or unresolved dependency |
| Approval boundary | Explicit statement that review evidence does not itself authorize release, publication, adapter activation, or authority expansion |

Screenshots, recordings, logs, automated reports, and manual notes must be tied to the exact candidate and must avoid private records, credentials, local paths, or uncontrolled personal data.

## Review sequence

1. **Source review** — headings, landmarks, labels, links, tables, forms, status text, and non-color state distinctions.
2. **Automated checks** — useful for detectable markup and contrast issues, but never treated as complete coverage.
3. **Keyboard review** — complete the selected primary scenario without pointer input.
4. **Zoom and reflow** — test 200% and 400% with no hidden critical state or inaccessible control.
5. **Screen-reader smoke** — verify page title, landmarks, headings, record identity, state, authority class, errors, updates, and recovery notices.
6. **Reduced-motion and high-contrast review** — verify essential meaning and focus remain perceivable.
7. **Cognitive and plain-language review** — confirm a reader can distinguish evidence, uncertainty, authority, effect, and safe next step.
8. **Correction and revocation review** — verify old and new states remain traceable and dependent controls update safely.
9. **Privacy review** — verify redaction, restricted-state explanation, and public-mode field exclusion.
10. **Independent review and disposition** — preserve findings and require separate architecture, accessibility, security, release, and publication decisions.

## Stop conditions

Stop promotion and preserve evidence when:

- identity, freshness, completeness, authority class, or effect cannot be expressed in accessible text;
- color, position, animation, iconography, or pointer interaction is the only way to perceive a critical distinction;
- keyboard focus is lost, trapped incorrectly, or moved without user initiation;
- a correction, revocation, withdrawal, privacy restriction, or failed recovery is not announced and persistently visible;
- stale, unsupported, partial, unknown, or conflicting state appears actionable;
- a public mode exposes private records, credentials, local paths, device inventories, or privileged endpoints;
- an automated score is being treated as accessibility certification;
- the tested artifact, exact commit, environment, or assistive-technology version is missing;
- a review depends on an unapproved runtime mode, adapter, backend, credential, or deployment.

## FYSA-120 capability map

This documentation work uses:

- **CAT-011-B — Visual communication:** accessible diagram design and non-color state encoding;
- **CAT-011-E — Cross-modal integrity:** prose equivalents, text-state consistency, and accessibility adaptation;
- **CAT-012-A — Document architecture:** audience paths, progressive disclosure, navigation, and evidence templates;
- **CAT-012-B — Technical exposition:** requirements, procedures, state semantics, and decision-ready documentation;
- **CAT-012-D — Quality controls:** terminology consistency, link checking, documentation testing, and ambiguity review;
- **CAT-012-E — Lifecycle management:** synchronization with task chain, punch list, release plan, changelog, and exact-head evidence;
- **CAT-019-B — Plain-language design:** concrete authority and state explanations;
- **CAT-019-C — Accessibility:** screen-reader optimization, cognitive-access design, and low-assumption interaction guidance;
- **CAT-019-D — Public-risk communication:** explicit uncertainty, privacy, authority, and recovery limits;
- **CAT-031-A — Specification:** threat-aware acceptance criteria and state invariants;
- **CAT-031-D — Validation:** integration, differential, and runtime-oriented accessibility scenarios;
- **CAT-031-E — Lifecycle assurance:** regression prevention, evidence retention, and change-impact review.

Proposed non-authoritative subdivision:

**`019-M — Epistemic and authority-state accessibility assurance`**: make freshness, completeness, uncertainty, provenance, privacy, correction, revocation, recovery, and authority effects perceivable and operable across visual, keyboard, screen-reader, zoom/reflow, reduced-motion, and plain-language modes; preserve exact-artifact evidence without converting accessibility review into operational authority.

Skill mapping does not demonstrate conformance, appoint a reviewer, certify accessibility, or authorize publication or release.

## Approval boundary

The accessibility plan is a review prerequisite, not an acceptance result. AionUi remains blocked pending fork identity, exact provenance, selected platform, accepted review contract, mode-specific security profiles, rendered accessibility evidence, independent review, rollback evidence, and explicit human approval for the exact immutable candidate.