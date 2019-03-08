# Linh Truong
# A01081792
# 03/06/2019


from unittest import TestCase
from character import character_information
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
