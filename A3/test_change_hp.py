# Linh Truong
# A01081792
# 03/06/2019


from unittest import TestCase
from character import change_hp, pokemon


class TestChangeHp(TestCase):
    def setUp(self):
        pokemon["HP"] = 10

    def test_change_hp_subtract(self):
        """Return new global variable HP value."""
        change_hp(-1)
        self.assertEqual(pokemon["HP"], 9)

    def test_change_hp_add(self):
        """Return new global variable HP value."""
        change_hp(1)
        self.assertEqual(pokemon["HP"], 11)
