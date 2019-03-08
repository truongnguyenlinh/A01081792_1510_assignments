# Linh Truong
# A01081792
# 03/06/2019


from unittest import TestCase
from character import change_hp, get_pokemon


class TestChangeHp(TestCase):
    def test_change_hp(self):
        """Return new global variable HP value."""
        change_hp(-1)
        self.assertEqual(get_pokemon()['HP'], 9)
