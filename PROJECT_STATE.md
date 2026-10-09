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

| Field               | Value                               |
| ------------------- | ----------------------------------- |
| Phase               | Phase 0 — Project Governance        |
| Lot                 | LOT-00 — Project Foundation         |
| Epic                | EPIC-00-01 — Governance Foundations |
| Current Task        | TASK-00-01-04                       |
| Current Task status | in-progress                         |
| Last validated Gate | None confirmed                      |

The Lot, Epic and Task identifiers are provisional
planning references until their authoritative delivery
documents are created.

## 3. Git checkpoint

**Last verified commit:** Not yet reconciled
**Working tree:** Not yet verified
**Uncommitted changes:** Unknown until inspected

Run:

```bash
git branch --show-current
git status --short
git log -5 --oneline
```

Record only verified Git information.

Do not assume a clean working tree.

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

**Task:** TASK-00-01-04

**Objective:**
Establish a reliable project state snapshot and a recovery
procedure that can be followed after a long interruption.

**Expected changes:**

- Create PROJECT_STATE.md.
- Create RECOVERY_PROTOCOL.md.
- Verify document references.
- Record the actual Git checkpoint.
- Review and commit the changes.

## 6. Known blockers and open questions

No blocker has been formally confirmed.

The following verification remains open:

- Reconcile this snapshot with the local Git history.
- Confirm which previous governance Tasks satisfy their
  acceptance criteria.

## 7. Next actionable step

**Action:** Review and validate TASK-00-01-04.

1. Read the current Project State.
2. Review RECOVERY_PROTOCOL.md.
3. Verify the local Git branch and working tree.
4. Check documentation consistency.
5. Commit the approved recovery documentation.
6. Record the resulting commit in the next checkpoint.

**Proposed commit:**

`docs(governance): establish project recovery protocol`

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
