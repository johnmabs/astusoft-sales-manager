# EPIC-01-01 — Sales and cash business discovery

**ID:** EPIC-01-01
**Status:** in-progress
**Owner:** Project Maintainer
**Parent Lot:** [LOT-01](../../LOT.md)

## 1. Objective

Establish verifiable business language, decisions and scenarios for a simple but scalable POS and its cash operations.

## 2. Motivation

The discovery must match small-shop reality without pre-selecting an architecture or inheriting unreviewed behavior from another codebase.

## 3. Scope

### Included

Sales process, cashier roles, register and session ownership, daily opening, handover, negative scenarios and source-code study.

### Excluded

Implementation and infrastructure decisions.

## 4. Task inventory

| Task | Objective | Status | Reference |
| --- | --- | --- | --- |
| TASK-01-01-01 | Establish evidence map and domain glossary | in-progress | [TASK-01-01-01](tasks/TASK-01-01-01.md) |
| TASK-01-01-02 | Review sales scenarios and payment rules | planned | [TASK-01-01-02](tasks/TASK-01-01-02.md) |
| TASK-01-01-03 | Review cash sessions, handover and exceptions | planned | [TASK-01-01-03](tasks/TASK-01-01-03.md) |
| TASK-01-01-04 | Consolidate decisions and acceptance review | planned | [TASK-01-01-04](tasks/TASK-01-01-04.md) |

## 5. Dependencies

The first Task collects sources for subsequent reviews. Accepted business rules remain authoritative irrespective of legacy examples.

## 6. Applicable requirements and decisions

- [Sales process](../../../../../02-domain/discovery/SALES_PROCESS.md)
- [Daily cash opening](../../../../../02-domain/discovery/CASH_SESSION_DAILY_OPENING.md)
- [Reference study](../../../../../02-domain/references/LEGACY_REPOSITORY_STUDY.md)

## 7. Acceptance criteria

- [ ] All Task reviews have evidence and recorded decisions.
- [ ] Scenarios distinguish approved rules, inferred behavior and open questions.
- [ ] Cross-references are valid.

## 8. Integration verification

Validate with documentary tooling and scenario walkthroughs after the final Tasks.

## 9. Risks and blockers

Legacy model mismatches and unresolved operational policy details are tracked in LOT-01.

## 10. Validation evidence

Not executed. This Epic is not validated.

## 11. Open questions

See LOT-01 and Task records.

## 12. Completion decision

**Decision:** Pending
**Reviewer:** Project Maintainer
**Date:** Not recorded
