# LOT-00 — Project Foundation

**ID:** LOT-00
**Status:** in-progress
**Owner:** Project Maintainer
**Phase:** Phase 0 — Project Foundation

## 1. Objective

Establish a reliable engineering and documentation
foundation for Astusoft Sales Manager.

The project must become understandable, traceable
and resumable without relying on previous conversations.

## 2. Expected outcome

At the end of this Lot, the repository must provide:

- Accepted governance rules.
- A documented delivery workflow.
- A consistent status and validation model.
- Authoritative Lot, Epic, Task and Gate records.
- A reliable project recovery entry point.
- AI collaboration instructions.
- Basic automated documentation checks.
- A documented and evidence-based Gate decision.

## 3. Scope

### Included

- Repository documentation foundations.
- Documentation governance.
- Delivery lifecycle and status rules.
- Project recovery protocol.
- AI collaboration instructions.
- Delivery document contracts and templates.
- Initial operational delivery records.
- Basic documentary consistency checks.
- Formal Lot acceptance review.

### Excluded

- Application framework selection.
- Detailed business requirements.
- Domain aggregate implementation.
- Persistence and API implementation.
- Production deployment.
- Business module delivery.

These subjects will be addressed through subsequent
planning and discovery activities.

## 4. Epic inventory

| Epic       | Objective                        | Status        | Reference                              |
| ---------- | -------------------------------- | ------------- | -------------------------------------- |
| EPIC-00-01 | Establish initial governance     | in-validation | [EPIC-00-01](epics/EPIC-00-01/EPIC.md) |
| EPIC-00-02 | Establish delivery documentation | in-progress   | Not yet created                        |

Epic files own their authoritative statuses.

The EPIC-00-02 record will be introduced during
delivery documentation formalization.

This inventory must be reconciled when its authoritative
record is created or a status changes.

## 5. Dependencies

No external delivery Lot dependency has been confirmed.

Internal work sequencing:

- Governance rules are needed before formal delivery
  documentation can be validated.
- Delivery contracts are needed before operational
  Lot, Epic and Task records can be accepted.
- The Gate review requires evidence from the
  relevant completed work.

Sequence alone does not imply validation.

## 6. Risks and blockers

| ID         | Description                                    | Impact                       | Mitigation                                        |
| ---------- | ---------------------------------------------- | ---------------------------- | ------------------------------------------------- |
| RISK-00-01 | Documentation becomes inconsistent             | Unreliable recovery          | Cross-document review and validation              |
| RISK-00-02 | Commits are mistaken for acceptance            | Incorrect progress reporting | Separate Git and validation evidence              |
| RISK-00-03 | Excessive documentation overhead               | Slower delivery              | Keep documents concise and responsibility-focused |
| RISK-00-04 | LLM-generated assumptions become authoritative | Incorrect project decisions  | Require explicit review and evidence              |

No currently blocking issue is confirmed.

## 7. Acceptance criteria

- [ ] Governance documents have been reviewed and accepted.
- [ ] Delivery contracts and templates are available.
- [ ] Required Lot, Epic, Task and Gate records exist.
- [ ] Parent-child relationships are navigable.
- [ ] Previous governance work has been reconciled against available Git evidence.
- [ ] Documentation checks execute successfully.
- [ ] A recovery exercise identifies the current work and next action without chat history.
- [ ] Unresolved limitations are documented.
- [ ] GATE-00 has passed.

The criteria must be verified using actual evidence.

## 8. Validation strategy

Verification includes:

1. Repository structure inspection.
2. Documentation contract review.
3. Markdown link validation.
4. Identifier and relationship consistency review.
5. Inspection of recorded Git evidence.
6. Recovery simulation using repository files only.
7. Formal review of GATE-00.

The exact executed checks and results must be
recorded in the relevant evidence documents.

## 9. Gate

**Gate:** [GATE-00](GATE.md)

LOT-00 may enter `validated` only after its mandatory
criteria are met and GATE-00 has passed.

## 10. Open questions

- What additional automated consistency checks
  are required before closing LOT-00?
- What minimum evidence should the initial recovery
  exercise produce?

These questions must be resolved before the Gate
decision when they affect mandatory acceptance criteria.

## 11. Change history

Git maintains the authoritative document history.

Significant scope changes must be explained through
the corresponding review or delivery records.
