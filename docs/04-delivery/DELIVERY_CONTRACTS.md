# Delivery Documentation Contracts

**Document ID:** GOV-006
**Status:** In Review
**Owner:** Project Maintainer

## 1. Purpose

Define the structure, ownership and relationships of
delivery documentation in Astusoft Sales Manager.

This document complements:

- `docs/00-governance/DOCUMENTATION_POLICY.md`
- `docs/00-governance/STATUS_MODEL.md`
- `docs/00-governance/DELIVERY_WORKFLOW.md`

It does not replace their lifecycle and workflow rules.

## 2. Delivery hierarchy

Delivery work is organized as:

Phase → Lot → Epic → Task

Each Lot also has a Gate responsible for its final
acceptance decision.

Every Lot, Epic, Task and Gate MUST have an
authoritative Markdown record.

## 3. Directory structure

Use the following structure:

    docs/04-delivery/
    ├── DELIVERY_CONTRACTS.md
    ├── templates/
    │   ├── README.md
    │   ├── LOT.template.md
    │   ├── EPIC.template.md
    │   ├── TASK.template.md
    │   └── GATE.template.md
    └── lots/
        └── LOT-00/
            ├── LOT.md
            ├── GATE.md
            └── epics/
                └── EPIC-00-01/
                    ├── EPIC.md
                    └── tasks/
                        └── TASK-00-01-01.md

Directories and files are introduced progressively.

The example above describes the naming convention,
not a claim that these files already exist.

## 4. Identifiers

Identifiers MUST be stable and unique.

### Lot

Format:

    LOT-XX

Example:

    LOT-00

### Epic

Format:

    EPIC-XX-YY

Where XX identifies the parent Lot and YY identifies
the Epic within that Lot.

Example:

    EPIC-00-02

### Task

Format:

    TASK-XX-YY-ZZ

Where:

- XX identifies the parent Lot.
- YY identifies the parent Epic.
- ZZ identifies the Task within that Epic.

Example:

    TASK-00-02-01

### Gate

Format:

    GATE-XX

A Gate belongs to one Lot.

Example:

    GATE-00

Identifiers MUST NOT be reassigned to unrelated work.

An item moved between Lots or Epics requires an explicit
migration decision because its identifier contains
its original parent reference.

## 5. Source-of-truth ownership

| Record           | Authoritative information                           |
| ---------------- | --------------------------------------------------- |
| LOT.md           | Lot objective, scope, status, acceptance criteria   |
| EPIC.md          | Epic objective, scope, status, task inventory       |
| TASK-\*.md       | Task objective, status, work, verification evidence |
| GATE.md          | Gate criteria, evidence and approval decision       |
| PROJECT_STATE.md | Recovery summary and next action                    |
| Git              | Commits, branches and working tree                  |

The Project State is not an authoritative substitute
for the underlying Task, Epic, Lot or Gate records.

## 6. Required Lot contract

Every LOT.md MUST contain:

1. Stable identifier and title.
2. Current status.
3. Objective and expected outcome.
4. Scope and exclusions.
5. Epic inventory with references.
6. Dependencies and risks.
7. Acceptance criteria.
8. Reference to its Gate.

A Lot may not be validated unless its Gate has passed
and all other Lot validation conditions are satisfied.

## 7. Required Epic contract

Every EPIC.md MUST contain:

1. Stable identifier and title.
2. Parent Lot reference.
3. Current status.
4. Objective.
5. Scope and exclusions.
6. Task inventory with references.
7. Dependencies.
8. Acceptance criteria.
9. Integration verification requirements.

An Epic MUST NOT be validated solely because its Tasks
have been committed.

## 8. Required Task contract

Every Task record MUST contain:

1. Stable identifier and title.
2. Parent Epic reference.
3. Current status.
4. Objective and motivation.
5. Scope and exclusions.
6. Dependencies and prerequisites.
7. Implementation steps.
8. Acceptance criteria.
9. Verification strategy.
10. Evidence of actual verification.
11. Git references where applicable.
12. Blockers and unresolved questions.
13. Exact next action when unfinished.

A Task MUST preserve enough context to be resumed
independently of previous conversations.

## 9. Required Gate contract

Every GATE.md MUST contain:

1. Stable Gate identifier.
2. Parent Lot reference.
3. Current Gate status.
4. Validation criteria.
5. Evidence references.
6. Known limitations and risks.
7. Explicit review decision.
8. Reviewer and review date.

A Gate MUST NOT be marked passed without verification
of its mandatory criteria.

Waivers follow STATUS_MODEL.md.

## 10. Status rules

Task, Epic and Lot statuses MUST use the values
defined in STATUS_MODEL.md.

Gate statuses MUST use the separate Gate lifecycle.

Document approval status MUST NOT be confused with
delivery implementation status.

A Git commit MUST NOT introduce a new delivery status.

For example, "committed" is evidence, not a Task status.

## 11. Dependency rules

Dependencies MUST be declared explicitly.

A smaller identifier does not automatically imply
a prerequisite.

Example:

    Depends on: TASK-00-02-01

A dependency MUST explain why it exists when
the relationship is not obvious.

A Task cannot enter ready while mandatory blocking
dependencies remain unsatisfied.

## 12. Acceptance criteria

Acceptance criteria MUST be observable and verifiable.

Avoid vague criteria such as:

- Documentation is good.
- Architecture is clean.
- Feature works correctly.

Prefer criteria such as:

- Required Markdown files exist at specified paths.
- The documentation validator reports no broken links.
- Relevant automated tests pass.
- The specified business invariant is verified.

## 13. Validation evidence

Evidence MUST identify:

- What was verified.
- How it was verified.
- When it was verified.
- The result.
- The relevant revision or artifact.
- Known limitations.

Do not invent commands, results or commit SHAs.

A successful commit does not prove that acceptance
criteria have been satisfied.

## 14. Atomic commits

Prefer focused commits containing one coherent change.

A Task may require multiple commits.

A commit may contain a necessary combination of code,
tests and documentation.

Task records SHOULD reference meaningful commits,
but PROJECT_STATE.md MUST NOT duplicate the current
Git HEAD merely to remain synchronized.

## 15. Change management

When scope changes:

1. Identify the reason.
2. Determine whether the change belongs to the
   existing Task.
3. Create a separate Task when appropriate.
4. Update dependencies and acceptance criteria.
5. Preserve relevant historical decisions.
6. Review the impact on parent delivery items.

Do not silently broaden a Task's responsibility.

## 16. Interruption and recovery

When unfinished work is interrupted, its Task record
MUST preserve:

- Last completed action.
- Remaining work.
- Tests already executed.
- Uncommitted work, when known.
- Open questions and blockers.
- Exact next executable action.

The repository's current Git state MUST always be
inspected directly during recovery.

## 17. Documentary consistency

The delivery documentation MUST remain navigable.

Every child record MUST reference its parent.

Parent documents MUST list their required children.

Missing or invalid references MUST be corrected before
formal acceptance.

Automated checks SHOULD verify these contracts once
the templates and validator are implemented.

## 18. Migration of provisional references

Earlier governance work used provisional identifiers
before authoritative delivery records existed.

When those records are created:

1. Preserve the established identifiers.
2. Reconstruct completed work from actual Git evidence.
3. Separate versioning evidence from validation evidence.
4. Avoid inventing historical verification results.
5. Establish parent-child links.
6. Reconcile PROJECT_STATE.md.

Do not retroactively mark Tasks validated simply
because their associated files have been committed.
