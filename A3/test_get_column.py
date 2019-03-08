from unittest import TestCase
from character import get_column


class TestGetColumn(TestCase):
    def test_get_column_output(self):
        """Obtain users most updated column position."""
        self.assertEqual(get_column(), 0)

    def test_get_column_type(self):
        """Determine if user column position is an int."""
        self.assertEqual(type(get_column()), int)
