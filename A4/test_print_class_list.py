from unittest import TestCase
from crud import print_class_list
from unittest.mock import patch, mock_open
import io


class TestPrintClassList(TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="First Last A12345678 True 49")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_class_list(self, mock_stdout, mock_file):
        expected = "First Last A12345678 True 49"
        print_class_list()
        self.assertEqual(mock_stdout.getvalue(), expected)
