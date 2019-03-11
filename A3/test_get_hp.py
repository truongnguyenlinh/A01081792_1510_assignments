from unittest import TestCase
from character import get_hp, pokemon


class TestGetHp(TestCase):
    def setUp(self):
        """Assert that global variable pokemon HP is setup for unit testing."""
        pokemon['HP'] = 9

    def test_get_hp_output(self):
        """Assert users most updated HP."""
        self.assertEqual(get_hp(), 9)

    def test_get_hp_type(self):
        """Assert that users HP is an int."""
        self.assertEqual(type(get_hp()), int)
