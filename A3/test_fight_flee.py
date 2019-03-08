from unittest import TestCase
from combat import fight_flee
from character import get_hp
from unittest.mock import patch
import unittest
import random
import io


class TestFightFlee(TestCase):
    @patch('builtins.input', side_effect=["Hi", "Flee"])
    def test_fight_flee_flee(self, mock_user_input):
        fight_flee({"Name": "Gordon", "Attack": "Tackle", "HP": 5})
        random.seed(87)
        self.assertEqual(get_hp(), 10)
        random.seed()

    @patch('builtins.input', side_effect=["Fight"])
    def test_fight_flee_fight(self, mock_user_input):
        random.seed(31)
        fight_flee({"Name": "Egg", "Attack": "Punch", "HP": 5})
        self.assertEqual(get_hp(), 9)
        random.seed()
