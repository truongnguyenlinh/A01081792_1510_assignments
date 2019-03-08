# Linh Truong
# A01081792
# 03/06/2019


from unittest import TestCase
from character import class_selection, get_pokemon
from unittest.mock import patch
import unittest
import io


class TestClassSelection(TestCase):
    @patch('builtins.input', side_effect=["Y", "2"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_class_selection(self, mock_stdout, mock_user_input):
        expected_output = "Please enter a number to choose your Pokemon type!\n"
        class_selection()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["3"])
    def test_class_selection_global_updated(self, mock_user_input):
        self.assertEqual(class_selection(), get_pokemon())

    @patch('builtins.input', side_effect=["n", "1"])
    def test_class_selection_global_variable(self, mock_user_input):
        class_selection()
        self.assertEqual(get_pokemon(), {'Position': [0, 0], 'HP': 10, 'Class': 'Squirtle'})

    @patch('builtins.input', side_effect=["g", "2"])
    def test_class_selection_type(self, mock_user_input):
        self.assertEqual(type(class_selection()), dict)

    @patch('builtins.input', side_effect=["wweawega", "3"])
    def test_class_selection_len(self, mock_user_input):
        self.assertEqual(len(class_selection()), 3)
