# Astusoft Sales Manager — Project State

**State ID:** STATE-001
**Last reviewed:** 2026-10-15
**State status:** Delivery Epic review accepted; LOT-00 governance/Gate still pending
**Expected branch:** main

> This file is a navigation and recovery snapshot.
> Git and authoritative delivery documents take precedence
> whenever discrepancies are detected.

## 1. Project overview

Astusoft Sales Manager is currently establishing its
engineering governance and documentation foundations.

No technical architecture has yet been accepted. Initial business decisions on cash sessions and daily opening have been documented; they are not implemented software.

## 2. Current delivery focus

| Field               | Value                                              |
| ------------------- | -------------------------------------------------- |
| Phase               | Phase 0 — Project Foundation                       |
| Lot                 | LOT-00 — Project Foundation                        |
| Epic                | EPIC-00-02 — Delivery Documentation Infrastructure |
| Current Task        | TASK-00-01-06 (governance validation work)          |
| Current Task status | in-progress                                        |
| Last validated Gate | None confirmed                                     |

Authoritative delivery statuses belong to the corresponding
Lot, Epic, Task and Gate records.

## 3. Git checkpoint

Git is the authoritative source for the current branch,
HEAD commit, working tree and untracked files.

This document does not duplicate the latest commit SHA
or a potentially outdated working tree status.

### Inspect the current repository state

Run from the repository root:

```bash
git branch --show-current
git status --short
git log -5 --oneline --decorate
```

### Recovery rules

1. Read the actual Git state before starting work.
2. Inspect modified and untracked files before editing.
3. Preserve unfinished work.
4. Consult Task records for implementation status and
   validation evidence.
5. Reconcile any inconsistency between Git, delivery
   documentation and PROJECT_STATE.md.

A Git commit is evidence of versioning, not proof that
the corresponding Task has been validated.

Do not update this section solely because HEAD changes.

## 4. Governance documents

| Document                                     | Intended responsibility    |
| -------------------------------------------- | -------------------------- |
| `README.md`                                  | Project introduction       |
| `docs/00-governance/DOCUMENTATION_POLICY.md` | Documentation rules        |
| `docs/00-governance/STATUS_MODEL.md`         | Delivery statuses          |
| `docs/00-governance/DELIVERY_WORKFLOW.md`    | Development workflow       |
| `docs/00-governance/RECOVERY_PROTOCOL.md`    | Project recovery procedure |

Presence in this table does not prove that the document
has been reviewed, committed or accepted.

## 5. Current work

**Task:** TASK-00-01-06 (see its authoritative task record).

**Context:** The repository contains AGENTS.md, governance checks, delivery checks and tests. Existing commits demonstrate tracked changes, not successful validation. Daily cash opening and configurable variance policy are documented in `docs/02-domain/discovery/CASH_SESSION_DAILY_OPENING.md`.

**Validation status:** GitHub Actions passed for merge commit `551f473` ([run #2](https://github.com/johnmabs/astusoft-sales-manager/actions/runs/38726684776)); TASK-00-02-04 formally accepted on 2026-10-15; parent Epic and LOT-00 remain in progress.

## 6. Known blockers and open questions

No blocker has been formally confirmed. The current state of the local uncommitted working tree cannot be established from the remote repository.

The following verification remains open:

- Reconcile this snapshot with the local Git history.
- Confirm which previous governance Tasks satisfy their
  acceptance criteria.

## 7. Next actionable step

**Task:** TASK-00-02-04

**Action:** Review remaining governance evidence, perform required Gate preparation and recovery check.

1. Inspect Git state locally and read TASK-00-01-06 and EPIC-00-01.
2. Reconcile outstanding governance-document approvals and Task evidence.
3. Perform an actual local recovery exercise, including Git working tree inspection.
4. Review remaining LOT-00 acceptance criteria and GATE-00 evidence.
5. Do not mark LOT-00 validated or GATE-00 passed without their own verification.

Git remains authoritative for branch, HEAD and working
tree status. Do not duplicate volatile Git metadata here.

## 8. Recovery entry point

After an interruption:

1. Execute the Git inspection commands.
2. Read this file.
3. Follow RECOVERY_PROTOCOL.md.
4. Resolve discrepancies before editing code.
5. Open the active Task and its parent documents
   when available.
6. Resume the recorded next action.

## 9. Update rules

This file MUST be updated when:

- The active Task changes.
- A significant blocker appears or is resolved.
- A delivery milestone is validated.
- The next action changes.
- A work session is intentionally handed off.

Do not duplicate detailed task histories here.

Keep the document concise and link to authoritative
sources as soon as they exist.
