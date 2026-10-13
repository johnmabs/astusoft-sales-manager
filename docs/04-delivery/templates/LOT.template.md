# LOT-XX — [Lot title]

**ID:** LOT-XX
**Status:** planned
**Owner:** [Responsible person or role]
**Phase:** [Phase identifier or name]

## 1. Objective

[Describe the delivery objective and its expected value.]

## 2. Expected outcome

[Describe the observable result expected at the end
of this Lot.]

## 3. Scope

### Included

- [Included work]

### Excluded

- [Explicitly excluded work]

## 4. Epic inventory

| Epic         | Objective   | Status  | Reference                  |
| ------------ | ----------- | ------- | -------------------------- |
| `EPIC-XX-01` | [Objective] | planned | `epics/EPIC-XX-01/EPIC.md` |

The reference is a placeholder, not an active Markdown link.

When creating an operational Lot document:

1. Replace the Epic identifier with its actual ID.
2. Create the corresponding Epic document.
3. Replace the reference with a valid relative Markdown link.
4. Verify that the target file exists.

Example of an operational reference:

    [EPIC-00-01](../lots/LOT-00/epics/EPIC-00-01/EPIC.md)

Epic records own their authoritative statuses.
The inventory must be reconciled when an Epic status changes.

## 5. Dependencies

| Dependency      | Reason | Required state |
| --------------- | ------ | -------------- |
| None identified | —      | —              |

Dependencies must be declared explicitly.

## 6. Risks and blockers

| ID              | Description | Impact | Mitigation |
| --------------- | ----------- | ------ | ---------- |
| None identified | —           | —      | —          |

## 7. Acceptance criteria

- [ ] [Observable criterion]
- [ ] [Observable criterion]

## 8. Validation strategy

- [Required integration checks]
- [Required documentation or architecture checks]

## 9. Gate

**Gate ID:** `GATE-XX`
**Gate document:** `GATE.md` (placeholder)

When instantiating this template, create the operational
Gate document and replace the placeholder with a valid link.

Example:

    **Gate:** [GATE-00](../lots/LOT-00/GATE.md)

The Lot may be validated only when its required Epics
are validated, its acceptance criteria are satisfied
and its Gate has passed.

## 10. Open questions

- [Unresolved question or "None"]

## 11. Change history

| Date       | Change             | Reference                    |
| ---------- | ------------------ | ---------------------------- |
| YYYY-MM-DD | Initial definition | [Commit or review reference] |
