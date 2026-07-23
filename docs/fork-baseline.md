---
layout: default
title: Fork Baseline Decision
---

# Fork baseline decision

**Status:** architectural approval required  
**Decision owner:** Architect / repository owner  
**Blocks:** `taskchain.md` P0, release naming, public distribution, updater ownership, supported-platform claims, and local feature planning

## Context

This repository contains an inherited AionUi application identified in `package.json` as version `1.7.0`. Its existing source, scripts, tests, assets, license, and history are candidate inputs. They must not be represented as newly created aevespers2 work.

Before implementation or distribution proceeds, the repository needs one explicit identity:

1. **upstream mirror** — preserves an approved upstream source with little or no local product divergence;
2. **maintained fork** — preserves upstream attribution while accepting ongoing local patches under a clearly differentiated fork identity;
3. **independently distributed derivative** — creates a distinct product/distribution identity with documented compatibility, attribution, ownership, support, and update responsibilities.

This document does not select an option. It defines the evidence and consequences required for approval.

## Decision matrix

| Dimension | Upstream mirror | Maintained fork | Independent derivative |
|---|---|---|---|
| Primary purpose | Preserve or review upstream source | Maintain a bounded, attributed variation | Distribute a separately named product derived from upstream |
| Local feature work | Normally none or minimal | Allowed after baseline approval and explicit divergence records | Allowed under a distinct product roadmap after legal/technical review |
| Versioning | Upstream tags/commits, no misleading local release line | Upstream lineage plus fork-specific prerelease/build identifiers | Distinct release namespace with compatibility mapping to upstream |
| Branding | Upstream identity and notices | Fork-qualified identity; no implication of upstream endorsement | Separately approved name, marks, notices, and user-facing ownership |
| Distribution | Usually source reference or synchronized mirror | Fork-owned artifacts and channels after verification | Derivative-owned artifacts, channels, signing, support, and policies |
| Updates | Follow upstream source | Fork-controlled update channel with upstream merge policy | Independent update policy and migration path |
| Support | Point users upstream unless local issue | Define fork support boundaries | Full derivative support statement required |
| Security response | Track upstream advisories and mirror integrity | Track upstream plus local advisories and patches | Own complete security response and disclosure process |
| Documentation | Preserve upstream docs plus mirror status | Separate inherited docs from fork-specific docs | Independent product docs with explicit upstream attribution |
| Operational burden | Lowest | Moderate | Highest |

## Required provenance record

Approval requires a reproducible upstream/fork record containing:

```yaml
repository_identity:
  decision: mirror | maintained-fork | independent-derivative
  approved_name: null
  approved_owner: null
  approved_date: null

upstream:
  repository_url: null
  default_branch: null
  commit_sha: null
  tag_or_version: 1.7.0
  license: Apache-2.0
  notices_reviewed: false

fork:
  repository_url: https://github.com/aevespers2/AionUi
  imported_head: null
  inherited_history_preserved: null
  first_local_commit: null
  current_candidate_commit: null

distribution:
  supported_platforms: []
  artifact_names: []
  release_namespace: null
  signing_identity: null
  update_channel: null
  support_contact: null
```

Null fields are blockers, not values to infer from branding or package metadata.

## Divergence report

Create a machine-readable and human-readable report that separates:

- commits inherited unchanged from upstream;
- upstream commits omitted from the fork;
- local planning/documentation commits;
- local implementation changes;
- dependency and lockfile differences;
- build, packaging, signing, updater, endpoint, telemetry, branding, and policy differences;
- generated or vendored artifacts not attributable through normal commit history.

The report should include exact commands and both repository commit identifiers. A simple file count is not enough; review security-sensitive and user-visible divergence separately.

## Naming and attribution questions

The approval record must answer:

- May the fork continue to use “AionUi” in repository, package, executable, installer, application, website, and update-channel names?
- What wording makes clear that an aevespers2 build is not an official upstream binary unless upstream explicitly authorizes that representation?
- Which copyright notices, license files, contributor lists, source offers, and third-party notices must ship?
- Which URLs, communities, issue trackers, websites, badges, screenshots, and download links remain upstream references?
- Where should fork-specific support, security, privacy, and release information live?
- How will inherited version `1.7.0` map to the first fork documentation or binary candidate?

Until answered, documentation should use “inherited AionUi `1.7.0` repository” and “proposed aevespers2 fork” rather than implying an approved product release.

## Platform decision

The first baseline should select exactly one platform/architecture combination for full reproduction. Approval should record:

- operating system and minimum version;
- target architecture;
- Node/npm and build tool versions;
- native module strategy;
- package/installer format;
- signing and notarization expectation;
- primary workflow smoke test;
- uninstall and rollback method;
- whether WebUI local or remote mode is in scope.

Other platforms remain inherited build targets, not fork support commitments, until they receive equivalent evidence.

## Distribution decision

Before publishing an artifact, approve:

- source-only, prerelease, internal test, or public distribution status;
- artifact host and retention policy;
- release and update namespaces;
- signing identity and key custody;
- checksum and SBOM publication;
- vulnerability reporting and support contact;
- privacy notice and terms appropriate to the actual fork behavior;
- rollback, withdrawal, and compromised-release procedure.

No public update channel should point at upstream infrastructure unless the binary and update protocol are demonstrably compatible and the relationship is authorized.

## Architecture consequences

### If approved as a mirror

- freeze local feature development;
- document synchronization and integrity verification;
- preserve upstream docs and direct users to upstream releases/support;
- avoid fork-branded binaries unless explicitly approved;
- keep local planning files clearly separated from mirrored source.

### If approved as a maintained fork

- choose a fork-qualified product/release identity;
- establish an upstream merge/rebase policy;
- require divergence entries for every local patch;
- own fork artifacts, signing, updates, privacy, security response, and rollback;
- preserve upstream attribution in documentation and binaries.

### If approved as an independent derivative

- complete naming, branding, license, notice, compatibility, migration, and support review;
- create a separately governed product roadmap after the inherited baseline is accepted;
- document all endpoints, providers, storage, security, accessibility, packaging, and update behavior under the derivative identity;
- prevent users from confusing derivative releases with upstream releases.

## Approval checklist

- [ ] Repository identity selected: mirror, maintained fork, or independent derivative.
- [ ] Exact upstream repository and commit recorded.
- [ ] Inherited history and first local commit identified.
- [ ] Divergence report generated and reviewed.
- [ ] License, notices, marks, links, and contributor attribution approved.
- [ ] Product/repository/package/executable/installer names approved.
- [ ] One platform and architecture selected for the first baseline.
- [ ] Source/artifact distribution channel and release namespace approved.
- [ ] Signing/notarization and update ownership approved.
- [ ] Privacy, security reporting, support, and vulnerability contacts approved.
- [ ] Versioning rule approved.
- [ ] `taskchain.md`, `release.md`, `changelog.md`, README, and Pages content updated consistently.

## Decision record template

```markdown
## AionUi repository identity decision

- Decision: mirror | maintained fork | independent derivative
- Approved name:
- Upstream repository:
- Upstream commit/tag:
- First local commit:
- Supported first platform:
- Distribution channel:
- Versioning rule:
- Signing/update owner:
- Support/security contact:
- Required notices:
- Effective date:
- Approver:

### Rationale

### Accepted consequences

### Rejected alternatives

### Review date or trigger
```

## Current blocker

Architectural clarification is required to select the repository identity and complete the null fields above. Documentation and read-only provenance work may continue; feature development, rebranding, public binaries, update channels, and support claims should remain blocked.
