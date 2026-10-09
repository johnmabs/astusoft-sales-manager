# Status Model — Astusoft Sales Manager

**Document ID:** GOV-002
**Status:** In Review
**Owner:** Project Maintainer

## 1. Purpose

This document defines the official lifecycle of delivery work
within Astusoft Sales Manager.

It applies to:

- Lots
- Epics
- Tasks
- Delivery Gates

Document approval statuses are governed separately by
`DOCUMENTATION_POLICY.md`.

## 2. Core principles

- Every delivery item MUST have a stable identifier.
- Every delivery item MUST have an explicit status.
- Progress MUST NOT be inferred from file existence.
- A Git commit does not automatically imply validation.
- A status transition MUST be supported by evidence.
- Parent status MUST be consistent with child statuses.
- Unverified work MUST never be reported as validated.
- Interrupted work MUST retain sufficient resumption context.

## 3. Task lifecycle

Tasks use the following statuses:

| Status          | Meaning                                        |
| --------------- | ---------------------------------------------- |
| `planned`       | Task defined but not started                   |
| `ready`         | Dependencies and acceptance criteria satisfied |
| `in-progress`   | Implementation underway                        |
| `blocked`       | Progress prevented by an identified obstacle   |
| `in-validation` | Implementation submitted for verification      |
| `validated`     | Acceptance criteria verified                   |
| `cancelled`     | Task abandoned by an explicit decision         |

`committed` is NOT a Task status.

Commit information is tracked separately as evidence.

## 4. Task transitions

Allowed transitions:

| From          | To                                                    |
| ------------- | ----------------------------------------------------- |
| planned       | ready, blocked, cancelled                             |
| ready         | in-progress, blocked, cancelled                       |
| in-progress   | in-validation, blocked, cancelled                     |
| in-validation | validated, in-progress, blocked                       |
| blocked       | planned, ready, in-progress, in-validation, cancelled |
| validated     | in-progress                                           |
| cancelled     | planned                                               |

A transition from `validated` to `in-progress` is permitted
only when verification is invalidated by a relevant change
or an explicit review decision.

Such transitions MUST document their reason.

A cancelled Task may be reopened only with an explicit
decision and a new validation of its scope.

## 5. Task readiness

A Task may enter `ready` only when:

- Its objective is understandable.
- Its scope is defined.
- Acceptance criteria exist.
- Required dependencies are satisfied.
- Blocking questions are resolved.
- Necessary references are accessible.

## 6. Task validation

A Task may enter `validated` only when:

1. Acceptance criteria have been checked.
2. Required tests or document checks have been executed.
3. Results are recorded.
4. Relevant changes have been reviewed.
5. The Git state and commit references are documented.
6. No unresolved blocker prevents acceptance.

If a check cannot be executed, the limitation MUST be
recorded and validation MUST follow an explicit decision.

Evidence MUST identify the tested revision whenever
applicable.

## 7. Epic lifecycle

Epics use:

- `planned`
- `ready`
- `in-progress`
- `blocked`
- `in-validation`
- `validated`
- `cancelled`

An Epic may enter `validated` only when:

- All required Tasks are validated.
- Cancelled Tasks have documented scope decisions.
- Epic acceptance criteria are satisfied.
- Cross-Task integration checks have passed.
- No mandatory work remains unresolved.

An Epic MUST NOT be validated solely because every Task
has been committed.

## 8. Lot lifecycle

Lots use:

- `planned`
- `ready`
- `in-progress`
- `blocked`
- `in-validation`
- `validated`
- `cancelled`

A Lot may enter `validated` only when:

- Required Epics are validated.
- Lot-level acceptance criteria are satisfied.
- Integration and architecture checks are complete.
- Its Gate has passed.
- Evidence is documented.

Lot numbers are delivery identifiers, not implicit
technical dependency rules.

## 9. Gate lifecycle

Gates use:

- `pending`
- `in-review`
- `passed`
- `failed`
- `waived`

A Gate may be marked `passed` only when its required
checks have satisfactory evidence.

A Gate may be `waived` only through an explicit,
recorded decision identifying:

- The unmet condition.
- The justification.
- The associated risk.
- The authorizing person.
- The date.

A waived Gate MUST NOT be described as passed.

## 10. Blocked work

A blocked Task MUST record:

- The blocker identifier.
- The cause.
- Its impact.
- The responsible person or decision owner.
- The next unblocking action.
- The last verified work state.

A blocker MUST NOT erase previously completed work.

## 11. Work interruption

Pausing work does not automatically change its status.

For example, an unfinished Task may remain `in-progress`
during a long interruption.

Before ending a work session, record:

- The last completed action.
- The current working tree state.
- Uncommitted modifications.
- Tests already executed.
- Remaining tests.
- Open questions.
- The exact next action.

## 12. Evidence model

Validation evidence SHOULD include:

| Field    | Description                          |
| -------- | ------------------------------------ |
| Date     | Verification date                    |
| Revision | Git commit or working-tree reference |
| Command  | Executed verification command        |
| Result   | Pass, fail or not executed           |
| Reviewer | Person or process responsible        |
| Notes    | Limitations and observations         |

A test result MUST NOT be claimed without execution.

## 13. Source of truth

- Task files own Task status.
- Epic files own Epic status.
- Lot files own Lot status.
- Gate files own Gate status.
- Git owns commit history.
- Project State summarizes the current situation.

Project State MUST reference authoritative records
rather than inventing or duplicating their status.

## 14. Status synchronization

When a Task status changes:

1. Update the Task record.
2. Review the parent Epic status.
3. Review the parent Lot status.
4. Update the Project State summary.
5. Record validation evidence when applicable.
6. Commit the documentation update when appropriate.

If a disagreement is found, preserve the underlying
evidence and resolve the discrepancy before reporting
the work as validated.
