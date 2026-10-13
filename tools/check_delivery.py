
"""Validation of delivery documentation contracts."""

import re


IDENTIFIER_PATTERNS = {
    "lot": re.compile(r"LOT-\d{2}"),
    "epic": re.compile(r"EPIC-\d{2}-\d{2}"),
    "task": re.compile(r"TASK-\d{2}-\d{2}-\d{2}"),
    "gate": re.compile(r"GATE-\d{2}"),
}


def validate_identifier(record_type: str, identifier: str) -> bool:
    """Return whether an identifier matches its record type."""
    pattern = IDENTIFIER_PATTERNS.get(record_type)

    if pattern is None:
        return False

    return pattern.fullmatch(identifier) is not None


WORK_ITEM_STATUSES = frozenset({
    "planned",
    "ready",
    "in-progress",
    "blocked",
    "in-validation",
    "validated",
    "cancelled",
})

GATE_STATUSES = frozenset({
    "pending",
    "in-review",
    "passed",
    "failed",
    "waived",
})

VALID_STATUSES = {
    "lot": WORK_ITEM_STATUSES,
    "epic": WORK_ITEM_STATUSES,
    "task": WORK_ITEM_STATUSES,
    "gate": GATE_STATUSES,
}


def validate_status(record_type: str, status: str) -> bool:
    """Return whether a status is valid for a record type."""
    allowed = VALID_STATUSES.get(record_type)

    if allowed is None:
        return False

    return status in allowed
