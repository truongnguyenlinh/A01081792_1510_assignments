from unittest import TestCase
from character import get_hp


class TestGetHp(TestCase):
    def test_get_hp_output(self):
        """Determine users most updated HP."""
        self.assertEqual(get_hp(), 10)

    def test_get_hp_type(self):
        """Determine if user HP is an int."""
        self.assertEqual(type(get_hp()), int)
