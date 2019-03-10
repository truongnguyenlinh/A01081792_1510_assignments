# Linh Truong
# A01081792
# 03/06/2019


from unittest import TestCase
from combat import combat_round
import unittest
from character import pokemon
from unittest.mock import patch
import random
import io


class TestCombatRound(TestCase):
    def setUp(self):
        """Assert global variable key-value pairs for unit testing. """
        pokemon['Name'] = 'Richard'
        pokemon['Class'] = 'Bulbasaur'
        pokemon['Position'] = [0, 2]
        pokemon['HP'] = 10

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_output(self, mock_stdout):
        """Assert expected print output of function after execution."""
        random.seed(6)
        expected_output = "You attacked Pikachu with a slap and he took 5 damage.\n" \
                          "Success! Your opponent has fainted and you gained 20 prize dollars from your battle.\n\n"
        opponent = {"Name": "Pikachu", "Class": "Electric", "Attack": "Static", "HP": 5}
        combat_round(opponent)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_type(self, mock_stdout):
        """Assert print output type."""
        random.seed(0)
        opponent = {"Name": "Charizard", "Class": "Fire", "Attack": "Tackle", "HP": 5}
        combat_round(opponent)
        self.assertEqual(type(mock_stdout.getvalue()), str)
        random.seed()

    def test_combat_round_exit(self):
        """Assert that SystemExit is called when user has 0 HP."""
        opponent = {"Name": "Mew", "Class": "Psychic", "Attack": "Hypnosis", "HP": 5}
        random.seed(1)
        with self.assertRaises(SystemExit):
            combat_round(opponent)
        random.seed()

    def test_combat_round_global(self):
        """Assert that character HP is updated in global variable."""
        random.seed(32)
        opponent = {"Name": "Dratini", "Class": "Dragon", "Attack": "Fly", "HP": 5}
        combat_round(opponent)
        self.assertEqual(pokemon, {'Name': 'Richard', 'Class': 'Bulbasaur', 'Position': [0, 2], 'HP': 5})
        random.seed()
