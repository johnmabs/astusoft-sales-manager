
import unittest

from pathlib import Path
from tempfile import TemporaryDirectory
from tools.check_delivery import read_delivery_metadata

from tools.check_delivery import (
    DeliveryMetadataError,
    parse_delivery_metadata,
    validate_identifier,
    validate_status,
)

class IdentifierValidationTests(unittest.TestCase):
    def test_accepts_valid_lot_identifier(self):
        self.assertTrue(validate_identifier("lot", "LOT-00"))

    def test_accepts_valid_epic_identifier(self):
        self.assertTrue(validate_identifier("epic", "EPIC-00-02"))

    def test_accepts_valid_task_identifier(self):
        self.assertTrue(
            validate_identifier("task", "TASK-00-02-04")
        )

    def test_accepts_valid_gate_identifier(self):
        self.assertTrue(validate_identifier("gate", "GATE-00"))

    def test_rejects_invalid_identifier(self):
        self.assertFalse(validate_identifier("task", "TASK-2-4"))

    def test_rejects_wrong_identifier_type(self):
        self.assertFalse(validate_identifier("epic", "LOT-00"))

    def test_rejects_unknown_record_type(self):
        self.assertFalse(validate_identifier("unknown", "LOT-00"))
    
    def test_rejects_extra_characters(self):
        self.assertFalse(
            validate_identifier("task", "TASK-00-02-04-extra")
        )

    def test_rejects_lowercase_identifier(self):
        self.assertFalse(validate_identifier("lot", "lot-00"))

class StatusValidationTests(unittest.TestCase):
    def test_accepts_valid_task_status(self):
        self.assertTrue(validate_status("task", "in-progress"))

    def test_accepts_valid_epic_status(self):
        self.assertTrue(validate_status("epic", "in-validation"))

    def test_accepts_valid_lot_status(self):
        self.assertTrue(validate_status("lot", "validated"))

    def test_accepts_valid_gate_status(self):
        self.assertTrue(validate_status("gate", "pending"))

    def test_rejects_committed_as_task_status(self):
        self.assertFalse(validate_status("task", "committed"))

    def test_rejects_gate_status_for_task(self):
        self.assertFalse(validate_status("task", "passed"))

    def test_rejects_task_status_for_gate(self):
        self.assertFalse(validate_status("gate", "in-progress"))

    def test_rejects_unknown_record_type(self):
        self.assertFalse(validate_status("unknown", "planned"))


class DeliveryMetadataParsingTests(unittest.TestCase):
    def test_parses_task_metadata(self):
        content = """\
# TASK-00-02-04 — Automated checks

**ID:** TASK-00-02-04
**Status:** in-progress
**Owner:** Project Maintainer
**Parent Epic:** [EPIC-00-02](../EPIC.md)
"""
        metadata = parse_delivery_metadata(content, "task")

        self.assertEqual(metadata.identifier, "TASK-00-02-04")
        self.assertEqual(metadata.status, "in-progress")
        self.assertEqual(metadata.parent_identifier, "EPIC-00-02")
        self.assertEqual(metadata.parent_path, "../EPIC.md")

    def test_parses_lot_without_parent(self):
        content = """\
# LOT-00 — Project Foundation

**ID:** LOT-00
**Status:** in-progress
**Owner:** Project Maintainer
"""
        metadata = parse_delivery_metadata(content, "lot")

        self.assertEqual(metadata.identifier, "LOT-00")
        self.assertEqual(metadata.status, "in-progress")
        self.assertIsNone(metadata.parent_identifier)
        self.assertIsNone(metadata.parent_path)

    def test_parses_gate_metadata(self):
        content = """\
# GATE-00 — Foundation Acceptance

**ID:** GATE-00
**Status:** pending
**Parent Lot:** [LOT-00](LOT.md)
"""
        metadata = parse_delivery_metadata(content, "gate")

        self.assertEqual(metadata.identifier, "GATE-00")
        self.assertEqual(metadata.status, "pending")
        self.assertEqual(metadata.parent_identifier, "LOT-00")
        self.assertEqual(metadata.parent_path, "LOT.md")

    def test_parses_epic_metadata(self):
        content = """\
# EPIC-00-02 — Delivery Documentation

**ID:** EPIC-00-02
**Status:** in-progress
**Parent Lot:** [LOT-00](../../LOT.md)
"""
        metadata = parse_delivery_metadata(content, "epic")

        self.assertEqual(metadata.parent_identifier, "LOT-00")
        self.assertEqual(metadata.parent_path, "../../LOT.md")

    def test_rejects_missing_identifier(self):
        content = "**Status:** planned"

        with self.assertRaisesRegex(
            DeliveryMetadataError, "Missing ID"
        ):
            parse_delivery_metadata(content, "task")

    def test_rejects_invalid_identifier(self):
        content = """\
**ID:** TASK-2-4
**Status:** planned
**Parent Epic:** [EPIC-00-02](../EPIC.md)
"""
        with self.assertRaisesRegex(
            DeliveryMetadataError, "Invalid ID"
        ):
            parse_delivery_metadata(content, "task")

    def test_rejects_invalid_status(self):
        content = """\
**ID:** TASK-00-02-04
**Status:** committed
**Parent Epic:** [EPIC-00-02](../EPIC.md)
"""
        with self.assertRaisesRegex(
            DeliveryMetadataError, "Invalid Status"
        ):
            parse_delivery_metadata(content, "task")

    def test_rejects_missing_parent(self):
        content = """\
**ID:** TASK-00-02-04
**Status:** planned
"""
        with self.assertRaisesRegex(
            DeliveryMetadataError, "Missing Parent Epic"
        ):
            parse_delivery_metadata(content, "task")

    def test_rejects_duplicate_identifier_field(self):
        content = """\
**ID:** TASK-00-02-04
**ID:** TASK-00-02-05
**Status:** planned
**Parent Epic:** [EPIC-00-02](../EPIC.md)
"""
        with self.assertRaisesRegex(
            DeliveryMetadataError, "Duplicate ID"
        ):
            parse_delivery_metadata(content, "task")

    def test_rejects_parent_without_markdown_link(self):
        content = """\
**ID:** TASK-00-02-04
**Status:** planned
**Parent Epic:** EPIC-00-02
"""
        with self.assertRaisesRegex(
            DeliveryMetadataError, "Invalid Parent Epic"
        ):
            parse_delivery_metadata(content, "task")

    def test_rejects_unknown_record_type(self):
        with self.assertRaisesRegex(
            DeliveryMetadataError, "Unknown record type"
        ):
            parse_delivery_metadata("", "unknown")


class DeliveryMetadataFileTests(unittest.TestCase):
    def test_reads_metadata_from_markdown_file(self):
        content = """\
# TASK-00-02-04 — Automated checks

**ID:** TASK-00-02-04
**Status:** in-progress
**Parent Epic:** [EPIC-00-02](../EPIC.md)
"""

        with TemporaryDirectory() as directory:
            path = Path(directory) / "TASK-00-02-04.md"
            path.write_text(content, encoding="utf-8")

            metadata = read_delivery_metadata(
                path,
                "task",
            )

        self.assertEqual(
            metadata.identifier,
            "TASK-00-02-04",
        )
        self.assertEqual(
            metadata.status,
            "in-progress",
        )


if __name__ == "__main__":
    unittest.main()
