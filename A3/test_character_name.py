# Linh Truong
# A01081792
# 03/06/2019


from unittest import TestCase
from character import character_name, pokemon
from unittest.mock import patch
import unittest
import io


class TestCharacterName(TestCase):
    @patch('builtins.input', side_effect=["helios", "Y"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_character_name_type(self, mock_stdout, mock_user_input):
        expected_output = "Welcome to the magical Pokemon SUD, Helios!\n" \
                          "Before we begin, you will need to choose your pokemon.\n"\
                          "From there, the adventure will begin.\n\n"
        character_name()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["TYSON", "n", "RICK","y"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_character_name_type(self, mock_stdout, mock_user_input):
        expected_output = "I'm sorry!\n"\
                          "Welcome to the magical Pokemon SUD, Rick!\n" \
                          "Before we begin, you will need to choose your pokemon.\n" \
                          "From there, the adventure will begin.\n\n"
        character_name()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["MoRtY", "y"])
    def test_character_name_global_variable(self, mock_user_input):
        self.assertEqual(character_name(), pokemon)

    @patch('builtins.input', side_effect=["AllEN", "Y"])
    def test_character_name_global_variable_len(self, mock_user_input):
        self.assertEqual(len(character_name()), 3)

    @patch('builtins.input', side_effect=["pikachu", "n", "will", "n", "ben", "y"])
    def test_character_name_global_variable_output(self, mock_user_input):
        self.assertEqual(character_name(), {'Name': 'Ben', 'Position': [0, 0], 'HP': 10})

    @patch('builtins.input', side_effect=["g", "n", "darsale", "Y"])
    def test_character_name_global_equal(self, mock_user_input):
        character_name()
        self.assertEqual({'Name': 'Darsale', 'Position': [0, 0], 'HP': 10}, pokemon)
