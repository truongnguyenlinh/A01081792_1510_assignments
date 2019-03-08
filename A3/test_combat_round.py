# Linh Truong
# A01081792
# 03/06/2019


from unittest import TestCase
from combat import combat_round
import unittest
from unittest.mock import patch
import random
import io


class TestCombatRound(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_output(self, mock_stdout):
        """Determine expected print output of function after execution."""
        random.seed(6)
        expected_output = "You attacked Pikachu with a slap and he took 5 damage.\n" \
                          "Success! Your opponent has fainted and you gained 20 prize dollars from your battle.\n\n"
        opponent = {"Name": "Pikachu", "Class": "Electric", "Attack": "Static", "HP": 5}
        combat_round(opponent)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_type(self, mock_stdout):
        """Determine print output type."""
        random.seed(0)
        opponent = {"Name": "Charizard", "Class": "Fire", "Attack": "Tackle", "HP": 5}
        combat_round(opponent)
        self.assertEqual(type(mock_stdout.getvalue()), str)
        random.seed()

    def test_combat_round_exit(self):
        """Determine that SystemExit is called when user has 0 HP."""
        opponent = {"Name": "Mew", "Class": "Psychic", "Attack": "Hypnosis", "HP": 5}
        random.seed(1)
        with self.assertRaises(SystemExit):
            combat_round(opponent)
        random.seed()
