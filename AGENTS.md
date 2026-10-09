# AGENTS.md — Astusoft Sales Manager

## 1. Purpose

This file defines the operating instructions for AI coding
assistants working on Astusoft Sales Manager.

The repository is the authoritative source of project
knowledge, decisions, implementation progress and
validation evidence.

Previous conversations are not required to understand
or resume the project.

## 2. Core operating principles

All AI assistants MUST:

- Respect accepted business and architectural decisions.
- Prefer repository evidence over assumptions.
- Read only the context required by the current task.
- Keep changes small, coherent and verifiable.
- Preserve existing behavior unless modification is intended.
- Distinguish planned, implemented and verified behavior.
- Report uncertainty and incomplete verification explicitly.
- Maintain accurate project recovery information.

AI assistants MUST NOT:

- Invent business rules.
- Assume undocumented architectural decisions.
- Treat a Git commit as proof of functional correctness.
- Claim tests passed without executing them.
- Silently expand the scope of an implementation task.
- Rewrite accepted decisions without following governance.
- Mark work validated without supporting evidence.
- Destroy uncommitted changes automatically.

## 3. Project entry points

Read these documents according to the current objective.

| Document                                   | Responsibility                |
| ------------------------------------------ | ----------------------------- |
| README.md                                  | Project overview              |
| PROJECT_STATE.md                           | Current progress and recovery |
| docs/00-governance/DOCUMENTATION_POLICY.md | Documentation rules           |
| docs/00-governance/STATUS_MODEL.md         | Delivery status definitions   |
| docs/00-governance/DELIVERY_WORKFLOW.md    | Development workflow          |
| docs/00-governance/RECOVERY_PROTOCOL.md    | Recovery and reconciliation   |

Future requirements, domain models, ADRs and delivery
documents will be referenced through the project
documentation structure.

Do not assume a planned document already exists.

## 4. Session initialization

Before starting an implementation task:

1. Read PROJECT_STATE.md.
2. Inspect the current Git branch and working tree.
3. Identify the active Task.
4. Locate its parent Epic and Lot when available.
5. Read the Task acceptance criteria.
6. Identify applicable requirements and decisions.
7. Inspect the relevant existing implementation.
8. Check blockers and unfinished changes.

Recommended Git inspection commands:

    git status --short
    git branch --show-current
    git log -5 --oneline

If PROJECT_STATE.md disagrees with Git or authoritative
delivery records, reconcile the discrepancy before
continuing.

Never invent missing Git history.

## 5. Context loading policy

Apply progressive context loading.

### Level 1 — Project orientation

Read:

- AGENTS.md
- PROJECT_STATE.md

### Level 2 — Task context

Read only:

- Active Task
- Parent Epic
- Parent Lot
- Directly referenced requirements

### Level 3 — Domain and architecture context

Read only the relevant:

- Business rules
- Domain specifications
- Bounded-context contracts
- Architecture decisions
- Cross-cutting constraints

### Level 4 — Implementation context

Inspect:

- Relevant source files
- Nearby implementation patterns
- Interfaces and dependencies
- Related tests

Do not scan the entire repository or documentation tree
when a smaller context is sufficient.

Expand context only when necessary to resolve a concrete
dependency, ambiguity or risk.

## 6. Domain-Driven Design

The project follows a Domain-Driven Design approach
to understanding and modeling business complexity.

Before implementing business behavior:

1. Identify the applicable business requirements.
2. Use the established ubiquitous language.
3. Determine the responsible bounded context.
4. Identify relevant invariants and business rules.
5. Respect aggregate boundaries when defined.
6. Identify transactional and consistency constraints.
7. Verify the behavior through appropriate tests.

Do not assume that every feature requires an aggregate,
repository, domain service or domain event.

Do not introduce design patterns without a demonstrated
need.

The technical architecture and dependency rules will be
defined through project-specific architectural decisions.

Until then, do not assume a particular framework,
database, persistence strategy or deployment model.

## 7. Implementation workflow

Follow the delivery workflow defined in:

docs/00-governance/DELIVERY_WORKFLOW.md

The normal execution cycle is:

RESUME -> CONTEXT -> PLAN -> IMPLEMENT -> VERIFY -> HANDOFF

### RESUME

Recover the verified project state.

### CONTEXT

Load the smallest sufficient set of documents and source
files.

### PLAN

Identify:

- Objective
- Scope
- Expected modifications
- Constraints
- Acceptance criteria
- Verification strategy

### IMPLEMENT

Implement the smallest coherent change that satisfies
the task requirements.

Avoid unrelated modifications.

### VERIFY

Execute the relevant checks.

Record:

- Commands executed
- Results
- Failures
- Limitations
- Revision tested

Never report an unexecuted check as passed.

### HANDOFF

Update the appropriate delivery records and
PROJECT_STATE.md.

Record the next concrete action.

## 8. Task scope management

Work only within the approved Task scope.

When additional work is discovered:

- Record it as a separate Task if independent.
- Record a blocker if it prevents progress.
- Escalate a conflicting business requirement.
- Request an architectural decision when required.

Do not perform unrelated refactoring opportunistically.

## 9. Testing and validation

Tests must verify observable behavior and relevant
business invariants.

Use the project's established testing strategy once
it has been defined.

For each Task, determine the relevant combination of:

- Unit tests
- Integration tests
- Contract tests
- End-to-end tests
- Architecture checks
- Documentation checks

Not every Task requires every test category.

Validation evidence MUST correspond to actual execution.

The Task lifecycle is defined in:

docs/00-governance/STATUS_MODEL.md

## 10. Git and commits

Use focused commits following Conventional Commits.

Format:

    type(scope): short description

Examples:

    docs(governance): define AI collaboration rules
    feat(catalog): implement product registration
    test(inventory): verify stock adjustment invariants

A Task may require multiple commits.

Do not automatically commit, amend, reset, rebase or
push changes without the user's authorization or an
explicitly approved workflow.

Never include credentials or secrets in commits.

## 11. Documentation updates

Update documentation when:

- An accepted decision changes.
- A business rule is introduced or revised.
- An implementation Task changes status.
- Validation evidence becomes available.
- A blocker appears or is resolved.
- The next actionable step changes.

Avoid duplicating authoritative information.

Prefer stable references to copying entire sections
between documents.

## 12. Session handoff

Before ending a work session:

1. Inspect Git status.
2. Identify completed and unfinished changes.
3. Record actual verification results.
4. Update the active Task when appropriate.
5. Reconcile parent delivery statuses.
6. Update PROJECT_STATE.md.
7. Identify the exact next action.
8. Report unresolved blockers and decisions.

A successful handoff MUST allow another engineer or
assistant to resume the task without previous chat history.

## 13. Required response format

For implementation work, provide a concise report:

### Objective

What was requested.

### Changes

What was actually modified.

### Verification

Commands executed and actual results.

### Git state

Relevant commits and uncommitted changes.

### Remaining work

Incomplete acceptance criteria or blockers.

### Next action

One concrete, immediately executable step.

Omit sections that provide no useful information for
the current task.

## 14. Conflict resolution

When documentation, implementation and Git disagree:

1. Identify the discrepancy.
2. Determine which source owns the disputed information.
3. Inspect the available evidence.
4. Preserve accepted decisions.
5. Correct outdated summaries.
6. Document unresolved uncertainty.

Never silently choose the interpretation that makes
the project appear more complete.

## 15. Guiding rule

Optimize for long-term maintainability, correctness,
traceability and recoverability.

The goal is not to maximize generated code or document
volume.

The goal is to deliver understandable, verified and
resumable software.
