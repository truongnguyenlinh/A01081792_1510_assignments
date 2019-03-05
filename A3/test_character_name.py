from unittest import TestCase
from character import character_name
from unittest.mock import patch
import unittest
import io


class TestCharacterName(TestCase):
    @patch('builtins.input', side_effect=["CHICKEN", "Y"])
    def test_character_name_title_case(self, mock_user_input):
        """Determine if input is converted to title case."""
        self.assertTrue(character_name().istitle())

    @patch('builtins.input', side_effect=["helios", "Y"])
    def test_character_name_type(self, mock_user_input):
        """Determine if output type is a string."""
        self.assertEqual(type(character_name()), str)

    @patch('builtins.input', side_effect=["zeus", "Y"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_character_name_output(self, mock_user_input, mock_stdout):
        """Determine output type from user input."""
        self.assertEqual(character_name(), "Zeus")
