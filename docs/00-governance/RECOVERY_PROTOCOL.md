# Project Recovery Protocol — Astusoft Sales Manager

**Document ID:** GOV-004
**Status:** Draft
**Owner:** Project Maintainer

## 1. Purpose

Define a repeatable procedure for resuming development
after an interruption, including interruptions lasting
several months.

Recovery MUST rely on repository evidence, not on
previous conversations or assumptions.

## 2. Sources of truth

Use the following order when reconciling project state:

1. Git for committed history and working tree state.
2. Accepted requirements and architectural decisions
   for normative rules.
3. Task records for Task status and validation evidence.
4. Epic, Lot and Gate records for delivery status.
5. PROJECT_STATE.md for navigation and handoff context.

Git proves that a change was recorded; it does not prove
that the change satisfies its requirements.

Project State MUST NOT override contradictory evidence.

## 3. Recovery phase A — Inspect Git

Run from the project root:

```bash
git status --short
git branch --show-current
git log -5 --oneline --decorate
```

Record:

- Active branch.
- Last commit.
- Uncommitted files.
- Untracked files.
- Any merge or rebase in progress.

Never run destructive recovery commands automatically.

In particular, do not run `git reset --hard` or
`git clean -fd` without explicit approval.

## 4. Recovery phase B — Read project context

Read in this order:

1. README.md
2. PROJECT_STATE.md
3. The active Task when its record exists.
4. Its parent Epic and Lot.
5. Governing requirements and decisions.
6. Relevant implementation and tests.

Do not recursively load every project document.

Load only the smallest sufficient context.

## 5. Recovery phase C — Reconcile progress

For the active Task:

- Compare reported status with evidence.
- Check whether the stated commit exists.
- Review uncommitted changes.
- Identify validation results and their revisions.
- Identify unfinished acceptance criteria.
- Check blockers and open decisions.

If evidence is insufficient, keep the Task unvalidated.

Do not infer task completion from a commit message.

## 6. Recovery phase D — Restore the environment

Inspect the project's setup instructions.

Verify:

- Required tool versions.
- Environment configuration.
- Local service dependencies.
- Database or migration state when applicable.
- Available testing commands.

Never assume that dependencies or external services
remain unchanged after a long interruption.

Do not execute destructive migration or cleanup commands
as part of automatic recovery.

## 7. Recovery phase E — Establish a baseline

Run the smallest relevant verification commands.

Record:

- Command.
- Revision tested.
- Result.
- Failure details.
- Environment limitations.

Differentiate new regressions from previously known
failures whenever evidence permits.

## 8. Recovery phase F — Resume work

Before making modifications, produce a short recovery
summary containing:

- Current verified Git state.
- Current delivery objective.
- Last confirmed completed work.
- Unfinished changes.
- Active blockers.
- Exact next action.
- Relevant verification commands.

Proceed only within the approved Task scope.

## 9. End-of-session handoff

At the end of a session:

1. Inspect Git status.
2. Summarize completed modifications.
3. Record tests actually executed.
4. Update the active Task record when available.
5. Record blockers and open decisions.
6. Update PROJECT_STATE.md.
7. Identify the next concrete action.
8. Review the diff.
9. Commit coherent documentation updates.

Uncommitted work MUST be explicitly described.

## 10. Handling inconsistencies

When two records disagree:

1. Identify the conflicting claims.
2. Inspect the underlying evidence.
3. Determine which source owns the information.
4. Correct the non-authoritative summary.
5. Preserve relevant historical evidence.
6. Record the reconciliation in Git.

Never silently mark work completed to make status
documents appear consistent.

## 11. Recovery after six months

When an extended interruption is detected, additionally
review:

- Dependency and runtime compatibility.
- Security advisories for the chosen stack.
- External API and service changes.
- Migrations and schema changes.
- Operational access and credentials.
- Outdated decisions and unresolved assumptions.

Any new decision MUST follow the project's established
decision process.

## 12. Recovery success criteria

Recovery is successful when another engineer or
AI assistant can identify, from repository evidence:

- What the project is building.
- What has been verified.
- What remains unfinished.
- Why the current decisions exist.
- Which Task to execute next.
- How to validate its result.

No historical conversation should be required.
