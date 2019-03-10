from unittest import TestCase
from character import get_column, pokemon


class TestGetColumn(TestCase):
    def setUp(self):
        """Assert that global variable pokemon column position is setup for unit testing."""
        pokemon['Position'][1] = 2

    def test_get_column_output(self):
        """Obtain users most updated column position."""
        self.assertEqual(get_column(), 2)

    def test_get_column_type(self):
        """Determine if user column position is an int."""
        self.assertEqual(type(get_column()), int)
