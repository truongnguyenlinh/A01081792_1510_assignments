from unittest import TestCase
from crud import obtain_standing
from unittest.mock import patch
import unittest
import io


class TestObtainStanding(TestCase):
    @patch('builtins.input', side_effect=["y"])
    def test_obtain_standing_true(self, mock_user_input):
        self.assertEqual(obtain_standing(), True)

    @patch('builtins.input', side_effect=["n"])
    def test_obtain_standing_false(self, mock_user_input):
        self.assertEqual(obtain_standing(), False)

    @patch('builtins.input', side_effect=["g", "y"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_obtain_standing_incorrect(self, mock_stdout, mock_user_input):
        expected = "Please enter one of the listed options by number!\n"
        obtain_standing()
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('builtins.input', side_effect=["2", "n"])
    def test_obtain_standing_recursion(self, mock_user_input):
        self.assertEqual(obtain_standing(), False)

    @patch('builtins.input', side_effect=["Y"])
    def test_obtain_standing_type(self, mock_user_input):
        self.assertEqual(type(obtain_standing()), bool)
