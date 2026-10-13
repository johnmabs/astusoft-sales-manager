# EPIC-00-02 — Delivery Documentation Infrastructure

**ID:** EPIC-00-02
**Status:** in-progress
**Owner:** Project Maintainer
**Parent Lot:** [LOT-00](../../LOT.md)

## 1. Objective

Establish the authoritative documentation infrastructure
used to plan, implement, verify and resume delivery work
in Astusoft Sales Manager.

## 2. Motivation

The project requires an explicit and verifiable structure
for tracking delivery work.

Each Lot, Epic, Task and Gate must have an identifiable
owner, scope, lifecycle status and acceptance evidence.

The documentation must remain coherent with Git and
must not depend on previous conversations.

## 3. Scope

### Included

- Delivery documentation contracts.
- Lot, Epic, Task and Gate templates.
- Template reference conventions.
- Operational LOT-00 and GATE-00 records.
- Historical governance Epic and Task records.
- Operational EPIC-00-02 and Task records.
- Documentation consistency checks.
- Delivery documentation review.

### Excluded

- Domain discovery.
- Technical architecture selection.
- Application feature implementation.
- Production deployment.
- Final LOT-00 acceptance decision.

## 4. Task inventory

| Task          | Objective                     | Status        | Reference                               |
| ------------- | ----------------------------- | ------------- | --------------------------------------- |
| TASK-00-02-01 | Define delivery contracts     | in-validation | [TASK-00-02-01](tasks/TASK-00-02-01.md) |
| TASK-00-02-02 | Create delivery templates     | in-validation | [TASK-00-02-02](tasks/TASK-00-02-02.md) |
| TASK-00-02-03 | Establish operational records | in-progress   | [TASK-00-02-03](tasks/TASK-00-02-03.md) |
| TASK-00-02-04 | Automate documentation checks | planned       | [TASK-00-02-04](tasks/TASK-00-02-04.md) |
| TASK-00-02-05 | Review delivery documentation | planned       | [TASK-00-02-05](tasks/TASK-00-02-05.md) |

Each Task record owns its authoritative status.

This inventory is a navigation snapshot and must be
reconciled whenever a Task status changes.

## 5. Dependencies

| Dependency    | Required state             | Reason                                         |
| ------------- | -------------------------- | ---------------------------------------------- |
| EPIC-00-01    | Governance rules available | Delivery records follow governance conventions |
| TASK-00-02-01 | Contracts available        | Templates depend on the documented contracts   |
| TASK-00-02-02 | Templates available        | Operational records use the templates          |
| TASK-00-02-03 | Records available          | Automated validation needs real documents      |

These dependencies describe the planning sequence.

They do not imply that the referenced work has already
been formally validated.

## 6. Applicable requirements and decisions

- [Documentation Policy](../../../../../00-governance/DOCUMENTATION_POLICY.md)
- [Status Model](../../../../../00-governance/STATUS_MODEL.md)
- [Delivery Workflow](../../../../../00-governance/DELIVERY_WORKFLOW.md)
- [Recovery Protocol](../../../../../00-governance/RECOVERY_PROTOCOL.md)
- [Delivery Contracts](../../../../DELIVERY_CONTRACTS.md)

No application architecture ADR is required.

## 7. Acceptance criteria

- [ ] Delivery documentation contracts are reviewed.
- [ ] All four canonical templates exist.
- [ ] Templates contain no unresolved active links.
- [ ] Operational Lot, Epic, Task and Gate records exist.
- [ ] Parent-child references are valid and navigable.
- [ ] All delivery statuses conform to STATUS_MODEL.md.
- [ ] Historical Git evidence is recorded without
      inventing validation results.
- [ ] Automated documentation checks execute successfully.
- [ ] A manual consistency review is completed.
- [ ] Outstanding limitations are documented.
- [ ] Required Tasks are validated.

## 8. Integration verification

Verification must include:

1. Check required delivery directories and files.
2. Validate active relative Markdown links.
3. Detect duplicate or malformed delivery IDs.
4. Verify that each Task references its actual Epic.
5. Verify that each Epic references its actual Lot.
6. Verify that Gate records reference their actual Lot.
7. Compare parent inventories with child records.
8. Verify that documented statuses use valid values.
9. Review recovery navigation from PROJECT_STATE.md.
10. Record actual results and unresolved limitations.

Not all checks are automated yet.

## 9. Risks and blockers

| ID         | Description                              | Mitigation                        |
| ---------- | ---------------------------------------- | --------------------------------- |
| RISK-02-01 | Incomplete historical Git reconciliation | Inspect actual repository history |
| RISK-02-02 | Broken references in templates           | Use non-clickable placeholders    |
| RISK-02-03 | Parent and child statuses diverge        | Introduce consistency validation  |
| RISK-02-04 | Documentation overhead grows excessively | Keep records focused and reusable |

No current blocking issue has been independently confirmed.

## 10. Validation evidence

| Check                        | Result        | Evidence |
| ---------------------------- | ------------- | -------- |
| Delivery contracts review    | Not recorded  | Pending  |
| Template reference review    | Not recorded  | Pending  |
| Operational records review   | Incomplete    | Pending  |
| Automated consistency checks | Not completed | Pending  |
| Epic integration review      | Not executed  | Pending  |

Existing Git commits must be reconciled with the
corresponding Task records.

## 11. Open questions

- Which commits correspond to template corrections?
- Which historical Task acceptance criteria have
  already been verified?
- Which documentation consistency checks should be
  mandatory before GATE-00?

## 12. Completion decision

**Decision:** Pending
**Reviewer:** Project Maintainer
**Date:** Not recorded

This Epic must not be marked validated until all
mandatory acceptance criteria have supporting evidence.
