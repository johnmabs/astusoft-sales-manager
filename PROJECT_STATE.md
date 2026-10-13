# Astusoft Sales Manager — Project State

**State ID:** STATE-001
**Last reviewed:** 2026-10-09
**State status:** Pending Git reconciliation
**Expected branch:** main

> This file is a navigation and recovery snapshot.
> Git and authoritative delivery documents take precedence
> whenever discrepancies are detected.

## 1. Project overview

Astusoft Sales Manager is currently establishing its
engineering governance and documentation foundations.

No technical architecture or detailed business model has
yet been accepted.

## 2. Current delivery focus

| Field               | Value                                              |
| ------------------- | -------------------------------------------------- |
| Phase               | Phase 0 — Project Foundation                       |
| Lot                 | LOT-00 — Project Foundation                        |
| Epic                | EPIC-00-02 — Delivery Documentation Infrastructure |
| Current Task        | TASK-00-02-03                                      |
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

**Task:** TASK-00-02-05

**Objective:**
Establish the AI collaboration entry point and progressive
context-loading rules.

**Expected changes:**

- Create AGENTS.md.
- Review context-loading instructions.
- Review implementation and verification rules.
- Verify consistency with governance documents.
- Update the project recovery snapshot.
- Commit the approved changes.

**Validation status:** In progress.

## 6. Known blockers and open questions

No blocker has been formally confirmed.

The following verification remains open:

- Reconcile this snapshot with the local Git history.
- Confirm which previous governance Tasks satisfy their
  acceptance criteria.

## 7. Next actionable step

**Task:** TASK-00-02-03

**Action:** Complete operational delivery record reconciliation.

1. Verify the five EPIC-00-02 Task records.
2. Verify all parent-child Markdown links.
3. Reconcile historical commit references using Git.
4. Review statuses against available evidence.
5. Record actual verification results.
6. Validate and commit TASK-00-02-03 documentation.
7. Transition to TASK-00-02-04 when its prerequisites
   have been satisfied.

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
