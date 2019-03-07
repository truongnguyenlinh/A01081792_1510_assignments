# Linh Truong
# A01081792
# 03/06/2019


from unittest import TestCase
from global_helper import user_input_type
from unittest.mock import patch


class TestUserInputType(TestCase):
    @patch('builtins.input', side_effect=["Hello"])
    def test_user_input_type_type(self, mock_user_input):
        """Determine if output type is a string."""
        self.assertEqual(type(user_input_type("Hello")), str)

    @patch('builtins.input', side_effect=["cello"])
    def test_user_input_type_output(self, mock_user_input):
        """Determine if input is the same as output."""
        self.assertEqual(user_input_type("cello"), "cello")

    @patch('builtins.input', side_effect=["quit"])
    def test_user_input_type_quit(self, mock_user_input):
        """Determine if SystemExit is raised when input is quit."""
        with self.assertRaises(SystemExit):
            user_input_type("quit")

    @patch('builtins.input', side_effect=["Quit"])
    def test_user_input_type_quit_lower(self, mock_user_input):
        """Determine if SystemExit is raised when input is Quit."""
        with self.assertRaises(SystemExit):
            user_input_type("Quit")
