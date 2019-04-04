from unittest import TestCase
from crud import del_student
from unittest.mock import patch, mock_open
import io


class TestDelStudent(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.open', new_callable=mock_open, read_data="Last First A12345678 True 49")
    @patch('builtins.input', side_effect=["A03921845"])
    def test_del_student_no_num(self, mock_user_input, mock_file, mock_stdout):
        expected = "This student is no longer on file.\n"
        del_student()
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.open', new_callable=mock_open, read_data="Linh Truong A01081792 False")
    @patch('builtins.input', side_effect=["A01081792"])
    def test_del_student_deleted(self, mock_user_input, mock_file, mock_stdout):
        expected = "Deleted!\n"
        del_student()
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.open', new_callable=mock_open, read_data="Linh Truong A01081792 True 78 90")
    @patch('builtins.input', side_effect=["EHGAWEGAWEG"])
    def test_del_student_deleted(self, mock_user_input, mock_file, mock_stdout):
        expected = "Please enter a student number beginning with 'A', followed by 8 digits.\n"
        del_student()
        self.assertEqual(mock_stdout.getvalue(), expected)
