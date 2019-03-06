from unittest import TestCase
from character import character_information, pokemon
from unittest.mock import patch
import unittest
import io


class TestCharacterInformation(TestCase):
    @patch('builtins.input', side_effect=["helios", "y", "3"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_character_information(self, mock_stdout, mock_user_input):
        """Expected value print output when all input is correct."""
        expected_value = "Welcome to the magical Pokemon SUD, Helios!\n"\
                         "Before we begin, you will need to choose your pokemon.\n"\
                         "From there, the adventure will begin.\n\n" \
                         "Hello, Helios the Bulbasaur\n! The goal of this world is to roam the regions, " \
                         "defeating all Pokemon encountered.\n" \
                         "If you encounter a Pokemon, you may flee or flight; however, " \
                         "the battle will be a combat to the death.\n" \
                         "Fear not, if you leave a battle wounded, 1HP will be added to your health " \
                         "until you reach a max of 10HP.\n" \
                         "Your HP will only go up, for every move where you are not in battle. " \
                         "If you choose to flee from a battle,\n" \
                         "there is a chance that your opponent will attack at the same time; " \
                         "keep this in mind moving forward.\n\n" \
                         "You may only move in directions of North, East, South and West " \
                         "within the constraints of our \n" \
                         "fantastic world and at any time, enter 'quit' to end the game. Good Luck!\n\n"
        character_information()
        self.assertEqual(mock_stdout.getvalue(), expected_value)

    @patch('builtins.input', side_effect=["Trae", "y", "2"])
    def test_character_information_return(self, mock_user_input):
        """Global variable is updated with new user input."""
        self.assertEqual(character_information(), {"Name":"Trae", "Class":"Charmander", "Position": [0, 0], "HP": 10})

    @patch('builtins.input', side_effect=["ALLEN", "n", "MAY", "y", "1"])
    def test_character_information_len(self, mock_user_input):
        """Length of global variable is updated from 2 to 4."""
        self.assertEqual(len(character_information()), 4)

    @patch('builtins.input', side_effect=["TrOyE", "Y", "3"])
    def test_character_information_same_global(self, mock_user_input):
        """User input is updated in global variable."""
        self.assertEqual(character_information(), pokemon)

