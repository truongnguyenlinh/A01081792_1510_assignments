from unittest import TestCase
from crud import confirm_unique
from unittest.mock import patch, mock_open
import unittest.mock
import io


class TestConfirmUnique(TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="First Last A12345678 True 49")
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_confirm_unique(self, mock_stdout, mock_file):
        self.assertEqual(confirm_unique("A12349087"), "A12349087")

    @patch('builtins.open', new_callable=mock_open, read_data="First Last A12345678 True 49")
    @patch('builtins.input', side_effect=["A10374653"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_confirm_unique_false(self, mock_stdout, mock_user_input, mock_file):
        self.assertEqual(confirm_unique("A12345678"), "A10374653")

    @patch('builtins.open', new_callable=mock_open, read_data="First Last A12345678 True 49")
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_confirm_unique_true(self, mock_stdout, mock_file):
        self.assertEqual(confirm_unique("A00000000"), "A00000000")

    @patch('builtins.open', new_callable=mock_open, read_data="First Last A12345678 True 49")
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_confirm_unique_type(self, mock_stdout, mock_file):
        self.assertEqual(type(confirm_unique("A00000000")), str)

    @patch('builtins.open', new_callable=mock_open, read_data="First Last A12345678 True 49")
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_confirm_unique_length_stud_num(self, mock_stdout, mock_file):
        self.assertEqual(len(confirm_unique("A00000000")), 9)
