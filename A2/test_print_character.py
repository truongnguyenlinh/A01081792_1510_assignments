from unittest import TestCase
import dungeonsanddragons
from unittest.mock import patch
import unittest
import io


class TestPrintCharacter(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_type(self, mock_stdout):
        character_details = {'Name': 'Kuwe', 'Class': 'druid', 'HP': 4, 'Strength': 14, 'Dexterity': 18,
                             'Constitution': 5, 'Intelligence': 3, 'Wisdom': 18, 'Charisma': 11,
                             'XP': 0, 'Inventory': []}
        dungeonsanddragons.print_character(character_details)
        self.assertEqual(type(mock_stdout.getvalue()), str)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_error(self, mock_stdout):
        character_details = {'Name': 'Kuwe', 'Class': 'druid', 'HP': 4, 'Strength': 14, 'Dexterity': 18,
                             'Constitution': 5, 'Intelligence': 3, 'Wisdom': 18, 'Charisma': 11,
                             'XP': 0, 'Inventory': []}
        expected_output = ("Name: Kuwe\n"
                           "Class: druid\n"
                           "HP: 4\n"
                           "Strength: 14\n"
                           "Dexterity: 18\n"
                           "Constitution: 5\n"
                           "Intelligence: 3\n"
                           "Wisdom: 18\n"
                           "Charisma: 11\n"
                           "XP: 0\n"
                           "Inventory: []\n")
        dungeonsanddragons.print_character(character_details)
        self.assertEqual(mock_stdout.getvalue(), expected_output)


