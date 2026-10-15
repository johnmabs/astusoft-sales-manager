# Astusoft Sales Manager — Project State

**State ID:** STATE-001
**Last reviewed:** 2026-10-15
**State status:** LOT-01 domain discovery in progress; first source-study Task active
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
| Phase               | Phase 1 — Business discovery                       |
| Lot                 | LOT-01 — Domain discovery                        |
| Epic                | EPIC-01-01 — Sales and cash business discovery |
| Current Task        | TASK-01-01-01 — Source evidence and glossary          |
| Current Task status | in-progress                                        |
| Last validated Gate | GATE-00 passed on 2026-10-15                                     |

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

**Task:** TASK-01-01-01 — source-study evidence and glossary. LOT-00 is closed; LOT-01 is underway.

**Context:** The repository contains AGENTS.md, governance checks, delivery checks and tests. Existing commits demonstrate tracked changes, not successful validation. Daily cash opening and configurable variance policy are documented in `docs/02-domain/discovery/CASH_SESSION_DAILY_OPENING.md`.

**Validation status:** LOT-00 / GATE-00 accepted. LOT-01, EPIC-01-01 and TASK-01-01-01 remain in progress and require their own evidence. Reference repository study is non-normative and does not define Astusoft architecture.

## 6. Known blockers and open questions

No blocker has been formally confirmed. The current state of the local uncommitted working tree cannot be established from the remote repository.

The following verification remains open:

- Reconcile this snapshot with the local Git history.
- Confirm which previous governance Tasks satisfy their
  acceptance criteria.

## 7. Next actionable step

**Task:** TASK-01-01-01

**Action:** Inspect reference source CashSession tests and application handlers, record the business evidence and glossary, and distinguish accepted Astusoft rules from legacy implementation.

1. Inspect actual local Git state before further edits.
2. Read LOT-01, EPIC-01-01 and TASK-01-01-01.
3. Study the designated reference repository and update the evidence matrix.
4. Draft the business glossary and compare existing Astusoft rules.
5. Record unresolved choices without choosing software architecture.

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
