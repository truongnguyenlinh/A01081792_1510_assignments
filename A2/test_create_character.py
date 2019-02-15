from unittest import TestCase
import dungeonsanddragons
from unittest.mock import patch
import io
import unittest.mock
import random


class TestCreateCharacter(TestCase):
    @patch('builtins.input', side_effect=["ranger"])
    def test_create_character_type(self, mock_user_input):
        self.assertEqual(type(dungeonsanddragons.create_character(4)), dict)

    def test_create_character_with_str(self):
        with self.assertRaises(TypeError):
            dungeonsanddragons.create_character('')

    @patch('builtins.input', side_effect=["rogue"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_create_character_syllable_error(self, mock_stdout, mock_input):
        expected_output = 'Error: Given length must be a positive, non-zero integer.\n'
        dungeonsanddragons.create_character(-10)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["druid"])
    def test_create_character_output(self, mock_user_input):
        random.seed(3)
        self.assertEqual(dungeonsanddragons.create_character(2), {'Name': 'Kuwe', 'Class': 'druid', 'HP': 4,
                                                                  'Strength': 14, 'Dexterity': 18, 'Constitution': 5,
                                                                  'Intelligence': 3, 'Wisdom': 18, 'Charisma': 11,
                                                                  'XP': 0, 'Inventory': []})
        random.seed()

    @patch('builtins.input', side_effect=["warlock"])
    def test_create_character_length(self, mock_user_input):
        self.assertEqual(len(dungeonsanddragons.create_character(2)), 11)

