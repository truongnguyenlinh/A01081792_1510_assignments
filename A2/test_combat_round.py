from unittest import TestCase
import dungeonsanddragons
from unittest.mock import patch
import io
import unittest.mock
import random


class TestCombatRound(TestCase):
    @patch('builtins.input', side_effect=[True])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_p1_attack(self, mock_stdout, mock_user_input):
        random.seed(15)
        character_one = {'Name': 'Bena', 'Class': 'monk', 'HP': 10,
                         'Strength': 8, 'Dexterity': 1, 'Constitution': 2,
                         'Intelligence': 4, 'Wisdom': 18, 'Charisma': 18,
                         'XP': 0, 'Inventory': []}
        character_two = {'Name': 'Xena', 'Class': 'ranger', 'HP': 4,
                         'Strength': 10, 'Dexterity': 1, 'Constitution': 6,
                         'Intelligence': 10, 'Wisdom': 5, 'Charisma': 7,
                         'XP': 0, 'Inventory': []}
        dungeonsanddragons.combat_round(character_one, character_two)
        expected_output = "Bena hit Xena a total of 1 damage and Xena now has HP of 3\n" \
                          "Xena hit Bena a total of 1 damage and Bena now has HP of 9\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()

    @patch('builtins.input', side_effect=[True])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_p1_missed(self, mock_stdout, mock_user_input):
        random.seed(10)
        character_one = {'Name': 'Bena', 'Class': 'monk', 'HP': 10,
                         'Strength': 8, 'Dexterity': 1, 'Constitution': 2,
                         'Intelligence': 4, 'Wisdom': 18, 'Charisma': 18,
                         'XP': 0, 'Inventory': []}
        character_two = {'Name': 'Xena', 'Class': 'ranger', 'HP': 4,
                         'Strength': 10, 'Dexterity': 18, 'Constitution': 6,
                         'Intelligence': 10, 'Wisdom': 5, 'Charisma': 7,
                         'XP': 0, 'Inventory': []}
        dungeonsanddragons.combat_round(character_one, character_two)
        expected_output = "Bena missed, Xena has a total of 4 HP\n" \
                          "Xena hit Bena a total of 1 damage and Bena now has HP of 9\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()

    @patch('builtins.input', side_effect=[True])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_p1_dies(self, mock_stdout, mock_user_input):
        random.seed(15)
        character_one = {'Name': 'Bena', 'Class': 'monk', 'HP': 1,
                         'Strength': 8, 'Dexterity': 1, 'Constitution': 2,
                         'Intelligence': 4, 'Wisdom': 18, 'Charisma': 18,
                         'XP': 0, 'Inventory': []}
        character_two = {'Name': 'Xena', 'Class': 'ranger', 'HP': 4,
                         'Strength': 10, 'Dexterity': 1, 'Constitution': 6,
                         'Intelligence': 10, 'Wisdom': 5, 'Charisma': 7,
                         'XP': 0, 'Inventory': []}
        dungeonsanddragons.combat_round(character_one, character_two)
        expected_output = "Bena hit Xena a total of 1 damage and Xena now has HP of 3\n" \
                          "Xena hit Bena a total of 1 damage and Bena now has HP of 0\n" \
                          "Bena has died\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()

    @patch('builtins.input', side_effect=[True])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_both_missed(self, mock_stdout, mock_user_input):
        random.seed(18)
        character_one = {'Name': 'Bena', 'Class': 'monk', 'HP': 10,
                         'Strength': 8, 'Dexterity': 18, 'Constitution': 2,
                         'Intelligence': 4, 'Wisdom': 18, 'Charisma': 18,
                         'XP': 0, 'Inventory': []}
        character_two = {'Name': 'Xena', 'Class': 'ranger', 'HP': 4,
                         'Strength': 10, 'Dexterity': 18, 'Constitution': 6,
                         'Intelligence': 10, 'Wisdom': 5, 'Charisma': 7,
                         'XP': 0, 'Inventory': []}
        dungeonsanddragons.combat_round(character_one, character_two)
        expected_output = "Bena missed, Xena has a total of 4 HP\n" \
                          "Xena missed, Bena has a total of 10 HP\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()

    @patch('builtins.input', side_effect=[True])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_attack_miss(self, mock_stdout, mock_user_input):
        random.seed(5)
        character_one = {'Name': 'Bena', 'Class': 'monk', 'HP': 10,
                         'Strength': 8, 'Dexterity': 18, 'Constitution': 2,
                         'Intelligence': 4, 'Wisdom': 18, 'Charisma': 18,
                         'XP': 0, 'Inventory': []}
        character_two = {'Name': 'Xena', 'Class': 'ranger', 'HP': 10,
                         'Strength': 10, 'Dexterity': 1, 'Constitution': 6,
                         'Intelligence': 10, 'Wisdom': 5, 'Charisma': 7,
                         'XP': 0, 'Inventory': []}
        dungeonsanddragons.combat_round(character_one, character_two)
        expected_output = "Bena hit Xena a total of 1 damage and Xena now has HP of 9\n" \
                          "Xena missed, Bena has a total of 10 HP\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()

    @patch('builtins.input', side_effect=[True])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_attack_die(self, mock_stdout, mock_user_input):
        random.seed(25)
        character_one = {'Name': 'Bena', 'Class': 'monk', 'HP': 10,
                         'Strength': 8, 'Dexterity': 18, 'Constitution': 2,
                         'Intelligence': 18, 'Wisdom': 8, 'Charisma': 1,
                         'XP': 0, 'Inventory': []}
        character_two = {'Name': 'Xena', 'Class': 'ranger', 'HP': 1,
                         'Strength': 10, 'Dexterity': 1, 'Constitution': 6,
                         'Intelligence': 10, 'Wisdom': 5, 'Charisma': 7,
                         'XP': 0, 'Inventory': []}
        dungeonsanddragons.combat_round(character_one, character_two)
        expected_output = "Bena hit Xena a total of 4 damage and Xena now has HP of -3\n" \
                          "Xena has died\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()

