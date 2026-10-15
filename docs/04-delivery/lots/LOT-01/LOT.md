# LOT-01 — Domain discovery and business rules

**ID:** LOT-01
**Status:** in-progress
**Owner:** Project Maintainer
**Phase:** Phase 1 — Business discovery

## 1. Objective

Document a coherent, validated business model for the initial sales and cash management journeys, understandable by a shop owner and implementable without relying on legacy assumptions.

## 2. Expected outcome

A reviewed glossary, actors, workflows, invariants, scenarios, exception paths and prioritized unresolved questions. Each accepted business rule includes an evidence/decision trail.

## 3. Scope

### Included

- Sales process and checkout scenarios.
- Cash register ownership, opening, closing and handover.
- Reconciliation of confirmed rules versus hypotheses.
- Source repository analysis as non-normative study material.
- Acceptance review and recovery-ready documentation.

### Excluded

- Selecting a programming language or application architecture.
- Copying old code or migrations.
- Implementing the backend, POS or database.
- Accepting assumptions solely because the reference implementation contains them.

## 4. Epic inventory

| Epic | Objective | Status | Reference |
| --- | --- | --- | --- |
| EPIC-01-01 | Discover sales and cash workflows | in-progress | [EPIC-01-01](epics/EPIC-01-01/EPIC.md) |

## 5. Dependencies

LOT-00 accepted. The present discovery is informed by the existing product vision, sales process and cash opening rules. Source repository remains non-normative.

## 6. Risks and blockers

| ID | Description | Impact | Mitigation |
| --- | --- | --- | --- |
| RISK-01-01 | Mistaking existing source behavior for approved business policy | Incorrect rules | Evidence matrix and explicit decisions |
| RISK-01-02 | Excessive complexity for single-person shops | Low adoption | Minimum-friction nominal path |
| RISK-01-03 | Cash discrepancy policy not fully arbitrated | Incomplete scenarios | Track thresholds, delegated approvals and offline behavior as open |

## 7. Acceptance criteria

- [ ] Business actors and glossary reviewed.
- [ ] Sales nominal and exception journeys reviewed.
- [ ] Cash session and handover invariants reconciled.
- [ ] Reference code observations separated from authoritative decisions.
- [ ] Outstanding questions prioritized.
- [ ] Required Tasks validated and Gate passed.

## 8. Validation strategy

Review workflow scenarios with explicit expected outcomes, trace rules to their sources, inspect cross-document links, execute documentation validators and record actual results.

## 9. Gate

**Gate:** [GATE-01](GATE.md)

## 10. Open questions

- Business-day boundary after midnight.
- Approval escalation when manager is unavailable.
- Offline opening and duplicate-session prevention.
- Mixed payments, credit and discounts in initial MVP.

## 11. Change history

Git holds the authoritative history. This Lot is proposed for discovery, not validated.
