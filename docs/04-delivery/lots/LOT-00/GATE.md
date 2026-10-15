# GATE-00 — Project Foundation Acceptance

**ID:** GATE-00
**Status:** passed
**Parent Lot:** [LOT-00](LOT.md)
**Reviewer:** Project Maintainer
**Review date:** 2026-10-15

## 1. Purpose

Verify that Astusoft Sales Manager has a reliable,
consistent and recoverable project foundation.

This Gate validates project governance and delivery
readiness, not application functionality.

## 2. Preconditions

- [x] Required governance documents are accepted.
- [x] Required delivery records exist.
- [x] LOT-00 acceptance criteria have been evaluated.
- [x] Verification evidence is available.
- [x] Known risks and limitations have been reviewed.

## 3. Gate criteria

| ID       | Criterion                                       | Required | Result  |
| -------- | ----------------------------------------------- | -------- | ------- |
| GC-00-01 | Governance rules reviewed and accepted          | Yes | passed |
| GC-00-02 | Delivery contracts and templates validated      | Yes | passed |
| GC-00-03 | Authoritative Lot, Epic and Task records linked | Yes | passed |
| GC-00-04 | Basic documentation checks pass                 | Yes | passed |
| GC-00-05 | Git and delivery evidence reconciled            | Yes | passed |
| GC-00-06 | Recovery simulation succeeds                    | Yes | passed |
| GC-00-07 | Outstanding risks reviewed                      | Yes | passed |

Each criterion must have supporting evidence
before its result can be accepted.

## 4. Verification evidence

| Criterion | Evidence reference | Result  | Date |
| --------- | ------------------ | ------- | ---- |
| GC-00-01 | Governance review, delivery Task records, recovery simulation and successful documentation CI; see references below | passed | 2026-10-15 |
| GC-00-02 | Governance review, delivery Task records, recovery simulation and successful documentation CI; see references below | passed | 2026-10-15 |
| GC-00-03 | Governance review, delivery Task records, recovery simulation and successful documentation CI; see references below | passed | 2026-10-15 |
| GC-00-04 | Governance review, delivery Task records, recovery simulation and successful documentation CI; see references below | passed | 2026-10-15 |
| GC-00-05 | Governance review, delivery Task records, recovery simulation and successful documentation CI; see references below | passed | 2026-10-15 |
| GC-00-06 | Governance review, delivery Task records, recovery simulation and successful documentation CI; see references below | passed | 2026-10-15 |
| GC-00-07 | Governance review, delivery Task records, recovery simulation and successful documentation CI; see references below | passed | 2026-10-15 |

Do not fabricate evidence or infer success
from the existence of documents.

**Acceptance evidence:** Governance review accepted on 2026-10-09; all required delivery Tasks and both Epics have dated acceptance records; repository-only recovery simulation in TASK-00-02-05; GitHub Actions run https://github.com/johnmabs/astusoft-sales-manager/actions/runs/38727516373 succeeded. **Limit:** This Gate assesses a documentary foundation, not local working-tree cleanliness, business rules or application architecture. The maintainer accepted the remaining local Git-state limitation; actual local recovery must still run `git status` before editing.

## 5. Outstanding risks

Refer to the risks in [LOT-00](LOT.md).

Before approval, record any unresolved risk,
its expected impact and its mitigation.

## 6. Waivers

No waiver has been requested or approved.

Any waiver must record:

- Criterion concerned.
- Justification.
- Accepted risk.
- Authorizing reviewer.
- Decision date.

A waived Gate must never be represented as passed.

## 7. Decision

**Decision:** Passed — accepted by Project Maintainer on 2026-10-15
**Reviewer:** Project Maintainer
**Date:** 2026-10-15

Allowed Gate statuses:

- pending
- in-review
- passed
- failed
- waived

A decision of `passed` requires supporting evidence
for all mandatory criteria.

## 8. Follow-up actions

1. Create authoritative Epic records.
2. Reconcile historical governance Tasks with Git.
3. Verify document links and relationships.
4. Execute the initial recovery simulation.
5. Complete the formal Gate review.

## 9. References

- [Parent Lot](LOT.md)
- [Delivery Contracts](../../DELIVERY_CONTRACTS.md)
- [Status Model](../../../00-governance/STATUS_MODEL.md)
- [Governance Review](../../../00-governance/GOVERNANCE_REVIEW.md)
