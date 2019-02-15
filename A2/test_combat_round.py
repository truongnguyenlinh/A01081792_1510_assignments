from unittest import TestCase
import dungeonsanddragons
from unittest.mock import patch
import io
import unittest.mock
import random


class TestCombatRound(TestCase):
    @patch('builtins.input', side_effect=[False])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_p2_missed(self, mock_stdout, mock_user_input):
        random.seed(8)
        character_one = {'Name': 'Bena', 'Class': 'rogue', 'HP': 18, 'Strength': 10,
                         'Dexterity': 18, 'Constitution': 2,
                         'Intelligence': 4, 'Wisdom': 18, 'Charisma': 18,
                         'XP': 0, 'Inventory': []}
        character_two = {'Name': 'Xena', 'Class': 'bard', 'HP': 10, 'Strength': 1,
                         'Dexterity': 1, 'Constitution': 2,
                         'Intelligence': 4, 'Wisdom': 18, 'Charisma': 18,
                         'XP': 0, 'Inventory': []}
        dungeonsanddragons.combat_round(character_one, character_two)
        expected_output = "Xena missed, Bena has a total of 18 HP\n"\
                          "Bena hit Xena a total of 1 damage and Xena now has HP of 9\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()

    @patch('builtins.input', side_effect=[False])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_p2_attack(self, mock_stdout, mock_user_input):
        random.seed(3)
        character_one = {'Name': 'Cadi', 'Class': 'monk', 'HP': 10,
                         'Strength': 8, 'Dexterity': 1, 'Constitution': 2,
                         'Intelligence': 4, 'Wisdom': 18, 'Charisma': 18,
                         'XP': 0, 'Inventory': []}
        character_two = {'Name': 'Kuwe', 'Class': 'ranger', 'HP': 4,
                         'Strength': 10, 'Dexterity': 18, 'Constitution': 6,
                         'Intelligence': 10, 'Wisdom': 5, 'Charisma': 7,
                         'XP': 0, 'Inventory': []}
        dungeonsanddragons.combat_round(character_one, character_two)
        expected_output = "Kuwe hit Cadi a total of 2 damage and Cadi now has HP of 8\n" \
                          "Cadi hit Kuwe a total of 2 damage and Kuwe now has HP of 2\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()

    @patch('builtins.input', side_effect=[True])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_p1_attack(self, mock_stdout, mock_user_input):
        random.seed(15)
        character_one = {'Name': 'Felicity', 'Class': 'monk', 'HP': 10,
                         'Strength': 8, 'Dexterity': 18, 'Constitution': 2,
                         'Intelligence': 4, 'Wisdom': 18, 'Charisma': 18,
                         'XP': 0, 'Inventory': []}
        character_two = {'Name': 'Susana', 'Class': 'ranger', 'HP': 4,
                         'Strength': 10, 'Dexterity': 1, 'Constitution': 6,
                         'Intelligence': 10, 'Wisdom': 5, 'Charisma': 7,
                         'XP': 0, 'Inventory': []}
        dungeonsanddragons.combat_round(character_one, character_two)
        expected_output = "Felicity hit Susana a total of 1 damage and Susana now has HP of 3\n" \
                          "Susana missed, Felicity has a total of 10 HP\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()

