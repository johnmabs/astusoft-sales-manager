
"""Validation of delivery documentation contracts."""

import re
from dataclasses import dataclass
from pathlib import Path

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


@dataclass(frozen=True)
class DeliveryMetadata:
    identifier: str
    status: str
    parent_identifier: str | None = None
    parent_path: str | None = None


class DeliveryMetadataError(ValueError):
    """Raised when delivery metadata violates its contract."""


PARENT_FIELDS = {
    "epic": "Parent Lot",
    "task": "Parent Epic",
    "gate": "Parent Lot",
}

PARENT_TYPES = {
    "epic": "lot",
    "task": "epic",
    "gate": "lot",
}

FIELD_PATTERN = re.compile(
    r"^\*\*(ID|Status|Parent Lot|Parent Epic):\*\*[ \t]*(.*)$",
    re.MULTILINE,
)

MARKDOWN_LINK_PATTERN = re.compile(
    r"^\[([^\]\n]+)\]\(([^)\n]+)\)$"
)


def _extract_fields(content: str) -> dict[str, str]:
    fields: dict[str, str] = {}

    for match in FIELD_PATTERN.finditer(content):
        name, value = match.groups()

        if name in fields:
            raise DeliveryMetadataError(
                f"Duplicate {name} field"
            )

        fields[name] = value.strip()

    return fields


def _require_field(
    fields: dict[str, str],
    name: str,
) -> str:
    value = fields.get(name)

    if not value:
        raise DeliveryMetadataError(
            f"Missing {name} field"
        )

    return value


def parse_delivery_metadata(
    content: str,
    record_type: str,
) -> DeliveryMetadata:
    """Parse and validate metadata from a delivery document."""

    if record_type not in IDENTIFIER_PATTERNS:
        raise DeliveryMetadataError(
            f"Unknown record type: {record_type}"
        )

    fields = _extract_fields(content)

    identifier = _require_field(fields, "ID")
    status = _require_field(fields, "Status")

    if not validate_identifier(record_type, identifier):
        raise DeliveryMetadataError(
            f"Invalid ID for {record_type}: {identifier}"
        )

    if not validate_status(record_type, status):
        raise DeliveryMetadataError(
            f"Invalid Status for {record_type}: {status}"
        )

    if record_type == "lot":
        return DeliveryMetadata(
            identifier=identifier,
            status=status,
        )

    parent_field = PARENT_FIELDS[record_type]
    parent_type = PARENT_TYPES[record_type]

    parent_value = _require_field(fields, parent_field)

    link_match = MARKDOWN_LINK_PATTERN.fullmatch(
        parent_value
    )

    if link_match is None:
        raise DeliveryMetadataError(
            f"Invalid {parent_field}: expected Markdown link"
        )

    parent_identifier, parent_path = link_match.groups()

    if not validate_identifier(parent_type, parent_identifier):
        raise DeliveryMetadataError(
            f"Invalid {parent_field} identifier: "
            f"{parent_identifier}"
        )

    if not parent_path.strip():
        raise DeliveryMetadataError(
            f"Invalid {parent_field}: empty path"
        )

    return DeliveryMetadata(
        identifier=identifier,
        status=status,
        parent_identifier=parent_identifier,
        parent_path=parent_path,
    )


def read_delivery_metadata(
    path: Path,
    record_type: str,
) -> DeliveryMetadata:
    """Read and parse metadata from a Markdown file."""

    content = path.read_text(encoding="utf-8")

    return parse_delivery_metadata(content, record_type)


def _expected_parent_identifier(
    identifier: str,
    record_type: str,
) -> str:
    """Derive the expected parent ID from the child ID."""

    parts = identifier.split("-")

    if record_type == "task":
        return f"EPIC-{parts[1]}-{parts[2]}"

    if record_type == "epic":
        return f"LOT-{parts[1]}"

    if record_type == "gate":
        return f"LOT-{parts[1]}"

    raise DeliveryMetadataError(
        f"Unsupported parent relationship: {record_type}"
    )


def validate_parent_reference(
    path: Path,
    record_type: str,
    repository_root: Path,
) -> Path:
    """Validate an operational document's parent reference.

    Returns the resolved parent file path on success.
    """

    if record_type not in PARENT_TYPES:
        raise DeliveryMetadataError(
            f"Unsupported parent relationship: {record_type}"
        )

    root = repository_root.resolve()
    document = path.resolve()

    if not document.is_relative_to(root):
        raise DeliveryMetadataError(
            "Document path escapes repository"
        )

    metadata = read_delivery_metadata(document, record_type)

    if metadata.parent_identifier is None:
        raise DeliveryMetadataError(
            "Missing parent identifier"
        )

    if metadata.parent_path is None:
        raise DeliveryMetadataError(
            "Missing parent path"
        )

    expected_parent = _expected_parent_identifier(
        metadata.identifier,
        record_type,
    )

    if metadata.parent_identifier != expected_parent:
        raise DeliveryMetadataError(
            "Parent hierarchy mismatch: "
            f"{metadata.identifier} requires {expected_parent}"
        )

    parent = (
        document.parent / metadata.parent_path
    ).resolve()

    if not parent.is_relative_to(root):
        raise DeliveryMetadataError(
            "Parent path escapes repository"
        )

    if not parent.is_file():
        raise DeliveryMetadataError(
            f"Parent file not found: {parent}"
        )

    parent_type = PARENT_TYPES[record_type]
    parent_metadata = read_delivery_metadata(
        parent,
        parent_type,
    )

    if parent_metadata.identifier != metadata.parent_identifier:
        raise DeliveryMetadataError(
            "Parent ID mismatch: "
            f"declared {metadata.parent_identifier}, "
            f"found {parent_metadata.identifier}"
        )

    return parent


CANONICAL_RECORD_PATHS = {
    "lot": lambda identifier: Path("docs/04-delivery/lots") / identifier / "LOT.md",
    "epic": lambda identifier: (
        Path("docs/04-delivery/lots") / f"LOT-{identifier.split('-')[1]}"
        / "epics" / identifier / "EPIC.md"
    ),
    "task": lambda identifier: (
        Path("docs/04-delivery/lots") / f"LOT-{identifier.split('-')[1]}"
        / "epics" / f"EPIC-{identifier.split('-')[1]}-{identifier.split('-')[2]}"
        / "tasks" / f"{identifier}.md"
    ),
    "gate": lambda identifier: (
        Path("docs/04-delivery/lots") / f"LOT-{identifier.split('-')[1]}" / "GATE.md"
    ),
}


def validate_canonical_path(
    path: Path,
    record_type: str,
    repository_root: Path,
) -> Path:
    """Verify the location of a delivery record using its parsed ID."""
    root = repository_root.resolve()
    document = path.resolve()

    if not document.is_relative_to(root):
        raise DeliveryMetadataError("Document path escapes repository")

    if record_type not in CANONICAL_RECORD_PATHS:
        raise DeliveryMetadataError(f"Unknown record type: {record_type}")

    metadata = read_delivery_metadata(document, record_type)
    expected = (root / CANONICAL_RECORD_PATHS[record_type](metadata.identifier)).resolve()

    if document != expected:
        raise DeliveryMetadataError(
            f"Non-canonical path for {metadata.identifier}: "
            f"expected {expected.relative_to(root)}"
        )

    return expected


INVENTORY_HEADINGS = {
    "lot": "## 4. Epic inventory",
    "epic": "## 4. Task inventory",
}


def validate_child_inventory(
    path: Path,
    record_type: str,
    repository_root: Path,
) -> None:
    """Check an operational Lot/Epic inventory against child records."""
    if record_type not in INVENTORY_HEADINGS:
        raise DeliveryMetadataError(f"Unsupported inventory type: {record_type}")

    validate_canonical_path(path, record_type, repository_root)
    content = path.read_text(encoding="utf-8")
    heading = INVENTORY_HEADINGS[record_type]
    if heading not in content:
        raise DeliveryMetadataError(f"Missing inventory section: {heading}")

    section = content.split(heading, 1)[1].split("\\n## ", 1)[0]
    child_type = "epic" if record_type == "lot" else "task"
    child_dir = path.parent / ("epics" if record_type == "lot" else "tasks")
    discovered = (
        list(child_dir.glob("EPIC-*/EPIC.md")) if record_type == "lot"
        else list(child_dir.glob("TASK-*.md"))
    )
    expected_ids = set()
    for child in discovered:
        validate_canonical_path(child, child_type, repository_root)
        expected_ids.add(read_delivery_metadata(child, child_type).identifier)

    declared = set()
    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        identifier, _, status, reference = cells[:4]
        if not validate_identifier(child_type, identifier):
            continue
        if identifier in declared:
            raise DeliveryMetadataError(f"Duplicate inventory ID: {identifier}")
        declared.add(identifier)
        match = MARKDOWN_LINK_PATTERN.fullmatch(reference)
        if match is None:
            raise DeliveryMetadataError(f"Missing inventory link: {identifier}")
        _, target = match.groups()
        target_file = (path.parent / target).resolve()
        if not target_file.is_relative_to(repository_root.resolve()):
            raise DeliveryMetadataError(f"Inventory link escapes repository: {identifier}")
        if not target_file.is_file():
            raise DeliveryMetadataError(f"Missing inventory child: {identifier}")
        metadata = read_delivery_metadata(target_file, child_type)
        if metadata.identifier != identifier:
            raise DeliveryMetadataError(f"Inventory ID mismatch: {identifier}")
        if metadata.status != status:
            raise DeliveryMetadataError(f"Inventory status mismatch: {identifier}")
        validate_canonical_path(target_file, child_type, repository_root)
        validate_parent_reference(target_file, child_type, repository_root)
        if target_file.parent != (
            child_dir / identifier if record_type == "lot" else child_dir
        ).resolve():
            raise DeliveryMetadataError(f"Inventory path mismatch: {identifier}")

    if expected_ids != declared:
        raise DeliveryMetadataError(
            f"Inventory mismatch: missing={sorted(expected_ids - declared)}, "
            f"unexpected={sorted(declared - expected_ids)}"
        )
