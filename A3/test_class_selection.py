# Linh Truong
# A01081792
# 03/06/2019


from unittest import TestCase
from character import class_selection
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
