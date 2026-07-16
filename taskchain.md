# Task Chain

## Purpose
Architect-controlled execution chain for this repository. Builders take the highest-priority unblocked task and preserve tests, evidence, and rollback paths.

## Roles
- **Architect:** owns dependencies, acceptance criteria, sequencing, and architecture.
- **Builder:** implements one bounded task, verifies it, and reports blockers without changing scope silently.

## States
`PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Active Chain
| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Repository health baseline | Architect | — | READY | Workflows, tests, dependencies, and known defects are inventoried. |
| P1 | Define next bounded implementation task | Architect | P0 | PROPOSED | Builder-ready scope names files, tests, constraints, and rollback guidance. |

## Builder Log
Record commits, test commands and results, residual risks, and follow-up tasks here.
