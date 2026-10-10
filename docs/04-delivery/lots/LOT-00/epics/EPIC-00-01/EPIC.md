# EPIC-00-01 — Initial Governance Foundations

**ID:** EPIC-00-01
**Status:** in-validation
**Owner:** Project Maintainer
**Parent Lot:** [LOT-00](../../LOT.md)

## 1. Objective

Establish the initial project governance required to
develop Astusoft Sales Manager in a consistent,
traceable and recoverable manner.

The governance foundation must remain usable by
human contributors and AI coding assistants.

## 2. Motivation

Software projects often lose important knowledge
when development is interrupted.

Decisions, implementation progress and validation
results may become scattered across conversations,
commit messages and informal notes.

This Epic establishes repository-based governance
so that development can be resumed using verifiable
project information.

## 3. Scope

### Included

- Initial Git repository and project identity.
- Documentation governance rules.
- Delivery workflow and status model.
- Project recovery protocol.
- AI collaboration instructions.
- Initial governance review.
- Basic automated governance verification.

### Excluded

- Complete delivery planning infrastructure.
- Detailed domain discovery.
- Technical architecture selection.
- Business feature implementation.
- Deployment and operations.

## 4. Task inventory

| Task          | Objective                               | Status                          |
| ------------- | --------------------------------------- | ------------------------------- |
| TASK-00-01-01 | Initialize Git repository               | Historical review pending       |
| TASK-00-01-02 | Define documentation policy             | Historical review pending       |
| TASK-00-01-03 | Define workflow and status model        | Historical review pending       |
| TASK-00-01-04 | Establish project recovery protocol     | Historical review pending       |
| TASK-00-01-05 | Establish AI collaboration instructions | Historical review pending       |
| TASK-00-01-06 | Validate initial governance framework   | Evidence reconciliation pending |

The descriptions above are historical observations,
not authoritative Task statuses.

Once the Task records exist, their statuses must use
STATUS_MODEL.md and this inventory must be reconciled.

## 5. Dependencies

No prerequisite delivery Epic has been identified.

Internal dependencies:

- Documentation policy precedes formal review
  of governance documents.
- The status model informs recovery and handoff rules.
- Recovery rules inform AI collaboration instructions.
- Governance review evaluates the completed foundation.

Dependencies are recorded for traceability and do not
imply that acceptance has already occurred.

## 6. Applicable requirements and decisions

- [Documentation Policy](../../../../../00-governance/DOCUMENTATION_POLICY.md)
- [Status Model](../../../../../00-governance/STATUS_MODEL.md)
- [Delivery Workflow](../../../../../00-governance/DELIVERY_WORKFLOW.md)
- [Recovery Protocol](../../../../../00-governance/RECOVERY_PROTOCOL.md)
- [Delivery Contracts](../../../../DELIVERY_CONTRACTS.md)

No application architecture ADR is required for this Epic.

## 7. Acceptance criteria

- [ ] The repository provides a clear project identity.
- [ ] Documentation responsibilities are explicit.
- [ ] Delivery statuses and transitions are defined.
- [ ] The recovery procedure does not duplicate volatile
      Git state.
- [ ] AGENTS.md defines safe collaboration rules.
- [ ] Governance documents have been reviewed.
- [ ] The governance validator has been executed.
- [ ] Validation evidence and remaining limitations
      are documented.
- [ ] All required Tasks have verified completion
      records.

## 8. Integration verification

Review the initial governance as a complete system.

Verification must establish that:

1. Documentation ownership does not conflict.
2. Git remains authoritative for commit history.
3. Task validation requires evidence.
4. Project State provides a usable recovery summary.
5. AGENTS.md follows the established governance.
6. A recovery exercise can identify the next action.
7. Documentary links and required files are valid.

## 9. Risks and blockers

| ID      | Description                                 | Mitigation                                   |
| ------- | ------------------------------------------- | -------------------------------------------- |
| RISK-01 | Historical Tasks lack authoritative records | Reconstruct using Git and existing documents |
| RISK-02 | Git commits may be confused with validation | Require explicit acceptance evidence         |
| RISK-03 | Recovery snapshot may become stale          | Verify Git and use canonical Task records    |

No blocking issue has been confirmed.

## 10. Historical Git evidence

The following commits were previously confirmed:

| Commit  | Change                           | Related Task  |
| ------- | -------------------------------- | ------------- |
| bbe959d | Initialize repository            | TASK-00-01-01 |
| c254226 | Define documentation policy      | TASK-00-01-02 |
| 10f0ef3 | Define workflow and status model | TASK-00-01-03 |
| 37536c7 | Establish recovery protocol      | TASK-00-01-04 |
| f1692eb | Establish AI instructions        | TASK-00-01-05 |

These commits are evidence of versioned work.

They are not sufficient by themselves to establish
that all Task acceptance criteria were satisfied.

Any later commits must be reconciled using the actual
repository history.

## 11. Validation evidence

| Check                          | Result                                    | Evidence             |
| ------------------------------ | ----------------------------------------- | -------------------- |
| Required governance files      | Not independently verified in this record | Pending              |
| Documentation links            | Not independently verified in this record | Pending              |
| Governance consistency         | Not independently verified in this record | Pending              |
| Recovery simulation            | Not independently verified in this record | Pending              |
| Historical Task reconciliation | Incomplete                                | Task records pending |

Do not replace pending results with assumed success.

## 12. Open questions

- Which later commits contain the governance review
  and reconciliation corrections?
- Which acceptance criteria have documented proof?
- Does the recovery simulation pass using repository
  files alone?

## 13. Completion decision

**Decision:** Pending
**Reviewer:** Project Maintainer
**Date:** Not recorded

This Epic remains `in-validation` until all mandatory
criteria and the required Task records are verified.

The Lot and its Gate remain independently governed.
