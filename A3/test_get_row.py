from unittest import TestCase
from character import get_row, pokemon


class TestGetRow(TestCase):
    def setUp(self):
        """Assert that global variable pokemon row position is setup for unit testing."""
        pokemon['Position'][0] = 7

    def test_get_row_output(self):
        """Assert users most updated position"""
        self.assertEqual(get_row(), 7)

    def test_get_row_type(self):
        """Assert that row position is an int."""
        self.assertEqual(type(get_row()), int)
