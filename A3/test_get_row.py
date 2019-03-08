from unittest import TestCase
from character import get_row


class TestGetRow(TestCase):
    def test_get_row_output(self):
        """Obtain users most updated position"""
        self.assertEqual(get_row(), 0)

    def test_get_row_type(self):
        """Determine if row position is an int."""
        self.assertEqual(type(get_row()), int)
