from unittest import TestCase
from character import character_name
from unittest.mock import patch
import unittest
import io


class TestCharacterName(TestCase):
    @patch('builtins.input', side_effect=["helios", "Y"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_character_name_type(self, mock_user_input, mock_stdout):
        expected_output = "Welcome to the magical Pokemon SUD, Helios!\n"
        character_name()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

