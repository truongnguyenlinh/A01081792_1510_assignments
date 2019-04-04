from unittest import TestCase
from crud import print_class_list
from unittest.mock import patch, mock_open
import io


class TestPrintClassList(TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="First Last A12345678 False 49\n"
                                                              "Hello World A00098888 True 88")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_class_list(self, mock_stdout, mock_file):
        expected = "First Last A12345678 False 49\n" \
                   "Hello World A00098888 True 88"
        print_class_list()
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('builtins.open', new_callable=mock_open, read_data="Linh Truong A01081792 True\n"
                                                              "Jason Zhou A00000000 True 78 98")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_class_list(self, mock_stdout, mock_file):
        expected = "Jason Zhou A00000000 True 78 98\n"\
                   "Linh Truong A01081792 True \n"
        print_class_list()
        self.assertEqual(mock_stdout.getvalue(), expected)
