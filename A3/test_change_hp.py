# Linh Truong
# A01081792
# 03/06/2019


from unittest import TestCase
from character import change_hp, pokemon


class TestChangeHp(TestCase):
    def setUp(self):
        """Assert that global variable pokemon HP is setup for unit testing."""
        pokemon["HP"] = 10

    def test_change_hp_subtract(self):
        """Assert new global variable HP value."""
        change_hp(-1)
        self.assertEqual(pokemon["HP"], 9)

    def test_change_hp_add(self):
        """Assert new global variable HP value."""
        change_hp(1)
        self.assertEqual(pokemon["HP"], 11)

    def test_change_hp_add_2(self):
        """Assert new global variable is subtracted by 2."""
        change_hp(-2)
        self.assertEqual(pokemon["HP"], 8)
