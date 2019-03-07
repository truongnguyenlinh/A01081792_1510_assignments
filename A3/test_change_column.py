from unittest import TestCase
from character import change_column, pokemon


class TestChangeColumn(TestCase):
    def test_change_column_add(self):
        """Add 1 to users current row position."""
        change_column(1)
        self.assertEqual(pokemon['Position'][1], 1)

    def test_change_column_subtract(self):
        """Subtract 1 to users current row position."""
        change_column(-1)
        self.assertEqual(pokemon['Position'][1], 0)
