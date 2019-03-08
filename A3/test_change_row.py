# Linh Truong
# A01081792
# 03/06/2019


from unittest import TestCase
from character import change_row, get_row


class TestChangeRow(TestCase):
    def test_change_row_add(self):
        """Add 1 to users current row position."""
        change_row(1)
        self.assertEqual(get_row()['Position'][0], 1)

    def test_change_row_subtract(self):
        """Subtract 1 to users current row position."""
        change_row(-1)
        self.assertEqual(get_row()['Position'][0], 0)
