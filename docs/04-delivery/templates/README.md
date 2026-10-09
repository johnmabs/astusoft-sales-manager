# Delivery Templates

This directory contains the canonical Markdown templates
for Lots, Epics, Tasks and Gates.

## Purpose

Templates ensure that delivery records are consistent,
traceable and resumable.

Templates define the required structure of a document.
They do not contain authoritative project progress.

## Planned templates

| Template         | Purpose                                |
| ---------------- | -------------------------------------- |
| LOT.template.md  | Lot definition and acceptance criteria |
| EPIC.template.md | Epic definition and Task inventory     |
| TASK.template.md | Task execution and verification        |
| GATE.template.md | Lot validation decision                |

The four canonical templates are available in this
directory.

When creating an operational document, copy the
appropriate template into its canonical delivery path
and replace every placeholder.

Relative links in a template are designed for its
destination directory and must be verified after copying.

## Usage rules

When creating a delivery record:

1. Select the correct template.
2. Assign a stable identifier.
3. Create the file in the corresponding Lot or Epic.
4. Replace all placeholders.
5. Record explicit parent references.
6. Define observable acceptance criteria.
7. Use a valid lifecycle status.
8. Verify links and dependencies.
9. Commit the new record.

Do not mark work validated before evidence exists.

Do not assume that a Git commit automatically closes
its associated Task.

## Canonical rules

See [Delivery Documentation Contracts](../DELIVERY_CONTRACTS.md).

Lifecycle statuses are defined in
[Status Model](../../00-governance/STATUS_MODEL.md).

The implementation workflow is defined in
[Delivery Workflow](../../00-governance/DELIVERY_WORKFLOW.md).
