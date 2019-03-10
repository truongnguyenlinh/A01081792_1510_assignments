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
        """Assert for expected output dependent on user input."""
        expected_output = "Welcome to the magical Pokemon SUD, Helios!\n" \
                          "Before we begin, you will need to choose your pokemon.\n"\
                          "From there, the adventure will begin.\n\n"
        character_name()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["TYSON", "n", "RICK","y"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_character_name_type(self, mock_stdout, mock_user_input):
        """Assert for expected output dependent on user input."""
        expected_output = "I'm sorry!\n"\
                          "Welcome to the magical Pokemon SUD, Rick!\n" \
                          "Before we begin, you will need to choose your pokemon.\n" \
                          "From there, the adventure will begin.\n\n"
        character_name()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["dave", "y"])
    def test_character_name_global(self, mock_user_input):
        """Assert that global variable is updated with user input."""
        character_name()
        self.assertEqual(pokemon, {'Name': 'Dave', 'Position': [0, 0], 'HP': 10})
