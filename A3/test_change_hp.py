from unittest import TestCase
from character import change_hp, pokemon


class TestChangeHp(TestCase):
    def test_change_hp(self):
        """Return new global variable HP value."""
        change_hp(-1)
        self.assertEqual(pokemon['HP'], 9)
