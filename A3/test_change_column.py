# Linh Truong
# A01081792
# 03/06/2019


from unittest import TestCase
from character import change_column, get_column


class TestChangeColumn(TestCase):
    def test_change_column_add(self):
        """Add 1 to users current row position."""
        change_column(1)
        self.assertEqual(get_column(), 1)

    def test_change_column_subtract(self):
        """Subtract 1 to users current row position."""
        change_column(-1)
        self.assertEqual(get_column(), 0)
