# Delivery Workflow — Astusoft Sales Manager

**Document ID:** GOV-003
**Status:** Accepted
**Owner:** Project Maintainer

## 1. Purpose

This document defines the operational workflow for planning,
implementing, verifying and recording project changes.

Its objective is to make each development session traceable,
repeatable and resumable.

## 2. Work hierarchy

Delivery work is organized as:

Phase → Lot → Epic → Task

### Phase

A strategic period grouping related delivery objectives.

### Lot

A coherent delivery milestone with explicit acceptance
criteria and a validation Gate.

### Epic

A significant functional or technical objective,
decomposed into verifiable Tasks.

### Task

The smallest independently manageable unit of work.

Tasks SHOULD remain limited enough to review, test and
resume without reconstructing excessive context.

One Task may require multiple commits. One commit may
also contain a necessary coherent supporting change.

The relationship between Tasks and commits MUST remain
traceable.

## 3. Planning rules

Before implementation:

1. Identify the business or technical objective.
2. Confirm the relevant source requirements.
3. Identify the governing decisions.
4. Define acceptance criteria.
5. Identify dependencies and risks.
6. Determine the relevant verification strategy.
7. Split the work into manageable Tasks.

Lot numbering MUST NOT imply architectural dependencies.

Only explicitly documented dependencies are authoritative.

## 4. Work session — START

Before editing files:

1. Read `AGENTS.md` when it exists.
2. Read `PROJECT_STATE.md` when it exists.
3. Inspect the Git branch and working tree.
4. Identify the active Task.
5. Read its parent Epic and applicable requirements.
6. Read only the relevant architecture rules and ADRs.
7. Check for existing unfinished modifications.
8. Confirm the next action.

Useful commands:

```bash
git status --short
git branch --show-current
git log -5 --oneline
```

Never discard uncommitted work automatically.

## 5. Work session — IMPLEMENT

During implementation:

1. Work within the approved Task scope.
2. Follow established project conventions.
3. Preserve domain and architecture invariants.
4. Implement the smallest coherent change.
5. Add or adjust relevant tests.
6. Avoid unrelated refactoring.
7. Record newly discovered questions.

If requirements are unclear, do not silently invent
business behavior.

## 6. Work session — VERIFY

Before validation:

1. Check acceptance criteria.
2. Execute relevant automated tests.
3. Execute architecture checks when applicable.
4. Review the complete diff.
5. Verify documentation consistency.
6. Record actual results.

A failed check MUST be reported.

An unexecuted check MUST NOT be reported as successful.

## 7. Commit policy

Use focused, meaningful commits.

Commit messages SHOULD follow Conventional Commits:

```text
type(scope): short imperative description
```

Common types:

- `feat`
- `fix`
- `refactor`
- `test`
- `docs`
- `chore`
- `build`
- `ci`

Examples:

```text
docs(governance): define status model
feat(catalog): add product creation use case
test(inventory): cover stock adjustment conflicts
```

A Task is not automatically validated after commit.

## 8. Work session — HANDOFF

Before stopping work:

1. Review the current Git state.
2. Record completed actions.
3. Record incomplete actions.
4. Record validation results.
5. Update the active Task.
6. Review parent statuses.
7. Update Project State.
8. Identify the exact next action.
9. Record any blocker or open decision.

The next action SHOULD be immediately executable.

Avoid vague instructions such as:

- Continue development.
- Finish the module.
- Improve the architecture.

Prefer:

- Implement the repository adapter for TASK-XX.
- Add the missing concurrency test.
- Validate the identified API contract.

## 9. Long interruption recovery

After an extended interruption:

1. Inspect the repository and Git history.
2. Read Project State.
3. Open the active Task and parent Epic.
4. Review applicable decisions and contracts.
5. Identify unfinished changes.
6. Check whether dependencies or tooling changed.
7. Run the smallest relevant verification.
8. Continue the documented next action.

Do not assume previously reported results still hold
for the current revision.

## 10. Handling discovered work

When new work is discovered:

- If it belongs to the active Task, update its scope
  only when the change remains small and justified.
- If it is independent, create a separate Task.
- If it changes accepted requirements, initiate
  the applicable decision or specification review.
- If it blocks progress, record a blocker.

Do not silently expand a Task into an unrelated Epic.

## 11. Definition of Done

A Task is done when:

- Its acceptance criteria are satisfied.
- Required tests and checks are recorded.
- Changes are reviewed.
- The documentation remains consistent.
- Evidence references the relevant revision.
- The Task is marked `validated`.

An Epic is done when its acceptance criteria and
required Task validations are complete.

A Lot is done when its Gate has passed and the Lot
has been marked `validated`.

## 12. Continuous improvement

Workflow problems SHOULD be recorded and corrected.

Significant changes to the process MUST be reflected
in governance documentation.

The workflow SHOULD remain lightweight enough to
support development rather than obstruct it.
