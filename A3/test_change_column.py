# Linh Truong
# A01081792
# 03/06/2019


from unittest import TestCase
from character import change_column, get_column, pokemon


class TestChangeColumn(TestCase):
    def setUp(self):
        """Assert that global variable pokemon row position is setup for unit testing."""
        pokemon["Position"][1] = 5

    def test_change_column_add(self):
        """Assert that users current column position is added by 1."""
        change_column(1)
        self.assertEqual(get_column(), 6)

    def test_change_column_subtract(self):
        """Assert that users current column position is subtracted by 1."""
        change_column(-1)
        self.assertEqual(get_column(), 4)

    def test_change_column_add_large(self):
        """Assert that users current column position is added by 2."""
        change_column(2)
        self.assertEqual(get_column(), 7)
