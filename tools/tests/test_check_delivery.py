
import unittest

from tools.check_delivery import (
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
    
    def test_rejects_uppercase_status(self):
        self.assertFalse(validate_status("task", "IN-PROGRESS"))

    def test_rejects_unknown_status(self):
        self.assertFalse(validate_status("gate", "approved"))



if __name__ == "__main__":
    unittest.main()
