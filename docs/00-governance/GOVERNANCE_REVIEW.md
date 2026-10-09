# Governance Review — Astusoft Sales Manager

**Document ID:** GOV-005
**Status:** Draft
**Review scope:** EPIC-00-01
**Review date:** To be recorded
**Reviewer:** To be recorded

## 1. Objective

Verify that the initial governance documents form a
coherent, understandable and recoverable project
management foundation.

This review is not an architecture or business-domain
validation.

## 2. Documents under review

| Document                | Responsibility           | Result  |
| ----------------------- | ------------------------ | ------- |
| README.md               | Project introduction     | Pending |
| AGENTS.md               | AI collaboration         | Pending |
| PROJECT_STATE.md        | Current project state    | Pending |
| DOCUMENTATION_POLICY.md | Documentation governance | Pending |
| STATUS_MODEL.md         | Delivery lifecycle       | Pending |
| DELIVERY_WORKFLOW.md    | Development workflow     | Pending |
| RECOVERY_PROTOCOL.md    | Recovery procedure       | Pending |

## 3. Review checklist

### Documentation

- [ ] Every document has a distinct responsibility.
- [ ] No contradictory source-of-truth rules exist.
- [ ] Referenced documents exist.
- [ ] Document lifecycle is consistent.
- [ ] Unconfirmed information is identified explicitly.

### Delivery governance

- [ ] Task, Epic, Lot and Gate statuses are distinguished.
- [ ] Commit existence is not treated as validation.
- [ ] Status transitions require evidence.
- [ ] Validation requirements are explicit.

### Project recovery

- [ ] Git inspection instructions are correct.
- [ ] The active Task is identifiable.
- [ ] The next action is concrete.
- [ ] Uncommitted work is not ignored.
- [ ] A new contributor can identify applicable documents.

### AI collaboration

- [ ] AGENTS.md follows governance rules.
- [ ] Context loading is progressive.
- [ ] Business assumptions are not silently accepted.
- [ ] Tests cannot be claimed without execution.
- [ ] Handoff requirements are explicit.

## 4. Known limitations

- Authoritative Lot, Epic and Task files have not yet
  been introduced.
- Task identifiers in PROJECT_STATE.md currently
  represent provisional planning references.
- Domain discovery and architectural decisions have
  not started.
- Automated verification covers only initial
  governance consistency.

These limitations do not automatically block acceptance
of the initial governance framework.

## 5. Verification evidence

| Check               | Command or method   | Result       | Revision |
| ------------------- | ------------------- | ------------ | -------- |
| Required files      | check_governance.py | Not executed | —        |
| Markdown links      | check_governance.py | Not executed | —        |
| Git diff            | git diff --check    | Not executed | —        |
| Recovery simulation | Manual review       | Not executed | —        |
| Working tree        | git status --short  | Not executed | —        |

## 6. Findings

Record each inconsistency with:

- Identifier
- Affected document
- Description
- Severity
- Required correction
- Resolution evidence

No findings have been verified yet.

## 7. Review decision

**Decision:** Pending

Possible outcomes:

- Accepted
- Changes required

Acceptance requires a completed checklist, recorded
verification evidence and explicit maintainer approval.

## 8. Next step

If accepted, proceed to defining the authoritative
delivery documentation structure for Lots, Epics,
Tasks and Gates.
