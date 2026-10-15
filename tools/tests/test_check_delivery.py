
import unittest

from pathlib import Path
from tempfile import TemporaryDirectory
from tools.check_delivery import read_delivery_metadata
from tools.check_delivery import validate_parent_reference
from tools.check_delivery import validate_canonical_path

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


class ParentReferenceValidationTests(unittest.TestCase):
    def setUp(self):
        self.directory = TemporaryDirectory()
        self.root = Path(self.directory.name)

        self.lot = self.root / "docs/04-delivery/lots/LOT-00"
        self.epic = self.lot / "epics/EPIC-00-02"
        self.tasks = self.epic / "tasks"

        self.tasks.mkdir(parents=True)

        self.lot_file = self.lot / "LOT.md"
        self.epic_file = self.epic / "EPIC.md"
        self.task_file = self.tasks / "TASK-00-02-04.md"
        self.gate_file = self.lot / "GATE.md"

        self.lot_file.write_text(
            "# LOT-00\n\n"
            "**ID:** LOT-00\n"
            "**Status:** in-progress\n",
            encoding="utf-8",
        )

        self.epic_file.write_text(
            "# EPIC-00-02\n\n"
            "**ID:** EPIC-00-02\n"
            "**Status:** in-progress\n"
            "**Parent Lot:** [LOT-00](../../LOT.md)\n",
            encoding="utf-8",
        )

        self.task_file.write_text(
            "# TASK-00-02-04\n\n"
            "**ID:** TASK-00-02-04\n"
            "**Status:** in-progress\n"
            "**Parent Epic:** [EPIC-00-02](../EPIC.md)\n",
            encoding="utf-8",
        )

        self.gate_file.write_text(
            "# GATE-00\n\n"
            "**ID:** GATE-00\n"
            "**Status:** pending\n"
            "**Parent Lot:** [LOT-00](LOT.md)\n",
            encoding="utf-8",
        )

    def tearDown(self):
        self.directory.cleanup()

    def assert_invalid(self, path, record_type, message):
        with self.assertRaisesRegex(
            DeliveryMetadataError, message
        ):
            validate_parent_reference(
                path, record_type, self.root
            )

    def test_valid_task_parent(self):
        self.assertEqual(
            validate_parent_reference(
                self.task_file, "task", self.root
            ),
            self.epic_file.resolve(),
        )

    def test_valid_epic_parent(self):
        self.assertEqual(
            validate_parent_reference(
                self.epic_file, "epic", self.root
            ),
            self.lot_file.resolve(),
        )

    def test_valid_gate_parent(self):
        self.assertEqual(
            validate_parent_reference(
                self.gate_file, "gate", self.root
            ),
            self.lot_file.resolve(),
        )

    def test_rejects_missing_parent_file(self):
        self.epic_file.unlink()

        self.assert_invalid(
            self.task_file, "task", "Parent file not found"
        )

    def test_rejects_parent_identifier_mismatch(self):
        self.epic_file.write_text(
            "**ID:** EPIC-00-03\n"
            "**Status:** in-progress\n"
            "**Parent Lot:** [LOT-00](../../LOT.md)\n",
            encoding="utf-8",
        )

        self.assert_invalid(
            self.task_file, "task", "Parent ID mismatch"
        )

    def test_rejects_inconsistent_task_numbering(self):
        self.task_file.write_text(
            "**ID:** TASK-00-03-04\n"
            "**Status:** in-progress\n"
            "**Parent Epic:** [EPIC-00-02](../EPIC.md)\n",
            encoding="utf-8",
        )

        self.assert_invalid(
            self.task_file, "task", "Parent hierarchy mismatch"
        )

    def test_rejects_inconsistent_epic_numbering(self):
        self.epic_file.write_text(
            "**ID:** EPIC-01-02\n"
            "**Status:** in-progress\n"
            "**Parent Lot:** [LOT-00](../../LOT.md)\n",
            encoding="utf-8",
        )

        self.assert_invalid(
            self.epic_file, "epic", "Parent hierarchy mismatch"
        )

    def test_rejects_inconsistent_gate_numbering(self):
        self.gate_file.write_text(
            "**ID:** GATE-01\n"
            "**Status:** pending\n"
            "**Parent Lot:** [LOT-00](LOT.md)\n",
            encoding="utf-8",
        )

        self.assert_invalid(
            self.gate_file, "gate", "Parent hierarchy mismatch"
        )

    def test_rejects_parent_path_outside_repository(self):
        outside = self.root.parent / "external-parent.md"

        self.task_file.write_text(
            "**ID:** TASK-00-02-04\n"
            "**Status:** in-progress\n"
            f"**Parent Epic:** [EPIC-00-02]"
            f"({outside.as_posix()})\n",
            encoding="utf-8",
        )

        self.assert_invalid(
            self.task_file, "task", "Parent path escapes repository"
        )

    def test_rejects_parent_directory_instead_of_file(self):
        self.task_file.write_text(
            "**ID:** TASK-00-02-04\n"
            "**Status:** in-progress\n"
            "**Parent Epic:** [EPIC-00-02](../)\n",
            encoding="utf-8",
        )

        self.assert_invalid(
            self.task_file, "task", "Parent file not found"
        )


if __name__ == "__main__":
    unittest.main()


class CanonicalPathValidationTests(unittest.TestCase):
    def setUp(self):
        self.directory = TemporaryDirectory()
        self.root = Path(self.directory.name)

    def tearDown(self):
        self.directory.cleanup()

    def create_record(self, relative_path, identifier, record_type):
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        parents = {
            "lot": "",
            "epic": "**Parent Lot:** [LOT-00](../../LOT.md)\\n",
            "task": "**Parent Epic:** [EPIC-00-02](../EPIC.md)\\n",
            "gate": "**Parent Lot:** [LOT-00](LOT.md)\\n",
        }
        path.write_text(
            f"**ID:** {identifier}\\n**Status:** in-progress\\n".replace("\\n", "\n")
            + parents[record_type].replace("\\n", "\n"),
            encoding="utf-8",
        )
        return path

    def test_accepts_canonical_lot_epic_task_paths(self):
        examples = [
            ("lot", "LOT-00", "docs/04-delivery/lots/LOT-00/LOT.md"),
            ("epic", "EPIC-00-02", "docs/04-delivery/lots/LOT-00/epics/EPIC-00-02/EPIC.md"),
            ("task", "TASK-00-02-04", "docs/04-delivery/lots/LOT-00/epics/EPIC-00-02/tasks/TASK-00-02-04.md"),
        ]
        for kind, identifier, relative in examples:
            with self.subTest(kind=kind):
                path = self.create_record(relative, identifier, kind)
                self.assertEqual(
                    validate_canonical_path(path, kind, self.root), path.resolve()
                )

    def test_accepts_canonical_gate_path(self):
        path = self.create_record(
            "docs/04-delivery/lots/LOT-00/GATE.md", "GATE-00", "gate"
        )
        path.write_text(path.read_text().replace("in-progress", "pending"))
        self.assertEqual(validate_canonical_path(path, "gate", self.root), path.resolve())

    def test_rejects_noncanonical_path(self):
        path = self.create_record(
            "docs/04-delivery/lots/LOT-00/tasks/TASK-00-02-04.md",
            "TASK-00-02-04", "task",
        )
        with self.assertRaisesRegex(DeliveryMetadataError, "Non-canonical path"):
            validate_canonical_path(path, "task", self.root)

    def test_rejects_document_outside_repository(self):
        with TemporaryDirectory() as other:
            path = Path(other) / "LOT.md"
            path.write_text("**ID:** LOT-00\n**Status:** in-progress\n")
            with self.assertRaisesRegex(DeliveryMetadataError, "escapes repository"):
                validate_canonical_path(path, "lot", self.root)
