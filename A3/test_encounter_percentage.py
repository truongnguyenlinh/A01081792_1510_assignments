from unittest import TestCase
from combat import encounter_percentage
from character import get_hp
from unittest.mock import patch
import unittest
import random
import io


class TestEncounterPercentage(TestCase):
    @patch('builtins.input', side_effect=["Fight"])
    def test_encounter_percentage_fight(self, mock_user_input):
        """Test for HP change after completed combat."""
        random.seed(31)
        encounter_percentage({"Name": "Egg", "Attack": "Punch", "HP": 5})
        self.assertEqual(get_hp(), 9)
        random.seed()

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["Flee"])
    def test_encounter_percentage_output(self, mock_user_input, mock_stdout):
        """Test for expected output dependent on user input of "Flee"."""
        random.seed(19)
        opponent = {"Name": "Palkia", "Class": "Water", "Attack": "Pressure", "HP": 5}
        expected_value = "You encountered another Pokemon!\nYou fled successfully!\n"
        encounter_percentage(opponent)
        self.assertEqual(mock_stdout.getvalue(), expected_value)
        random.seed()

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["Fight"])
    def test_encounter_percentage_output(self, mock_user_input, mock_stdout):
        """Test for expected output dependent on user input of "Fight"."""
        random.seed(19)
        opponent = {"Name": "Marowak", "Class": "Ground", "Attack": "Rock Head", "HP": 5}
        expected_value = "You encountered another Pokemon!\nMarowak | HP: 5 \nYou encountered Marowak! It's time for a "\
                         "Poke-Battle.\n\nYou attacked Marowak with a slap and he took 5 damage.\n"\
                         "Success! Your opponent has fainted and you gained 20 prize dollars from your battle.\n\n"
        encounter_percentage(opponent)
        self.assertEqual(mock_stdout.getvalue(), expected_value)
        random.seed()
