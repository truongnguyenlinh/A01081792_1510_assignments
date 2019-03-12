# Linh Truong
# A01081792
# 03/06/2019


from unittest import TestCase
from character import class_selection, pokemon
from unittest.mock import patch
import unittest
import io


class TestClassSelection(TestCase):
    def setUp(self):
        """Assert that global variable pokemon name is setup for unit testing."""
        pokemon["Name"] = "Dave"

    @patch('builtins.input', side_effect=["Y", "2"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_class_selection(self, mock_stdout, mock_user_input):
        """Assert incorrect output message based on user input."""
        expected_output = "Please enter a number to choose your Pokemon type!\n"
        class_selection()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["1"])
    def test_class_selection_global_first(self, mock_user_input):
        """Assert that class selection is updated in global variable."""
        class_selection()
        self.assertEqual(pokemon, {'Name': 'Dave', 'Class': 'Squirtle', 'Position': [0, 0], 'HP': 10})

    @patch('builtins.input', side_effect=["2"])
    def test_class_selection_global_second(self, mock_user_input):
        """Assert that class selection is updated in character global variable."""
        class_selection()
        self.assertEqual(pokemon, {'Name': 'Dave', 'Class': 'Charmander', 'Position': [0, 0], 'HP': 10})

    @patch('builtins.input', side_effect=["3"])
    def test_class_selection_global_third(self, mock_user_input):
        """Assert that class selection is updated in character global variable."""
        class_selection()
        self.assertEqual(pokemon, {'Name': 'Dave', 'Class': 'Bulbasaur\n', 'Position': [0, 0], 'HP': 10})

    @patch('builtins.input', side_effect=[3])
    def test_class_selection_error(self, mock_user_input):
        """Assert an AttributeError with an int."""
        with self.assertRaises(AttributeError):
            class_selection()
