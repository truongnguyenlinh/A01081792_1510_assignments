# Linh Truong
# A01081792
# 03/06/2019


from unittest import TestCase
from character import change_row, get_row, pokemon


class TestChangeRow(TestCase):
    def setUp(self):
        """Assert that global variable pokemon row position is setup for unit testing."""
        pokemon['Position'][0] = 0

    def test_change_row_add(self):
        """Assert that users current row position is added by 1."""
        change_row(1)
        self.assertEqual(get_row(), 1)

    def test_change_row_subtract(self):
        """Assert that users current row position is subtracted by 1."""
        change_row(-1)
        self.assertEqual(get_row(), -1)
