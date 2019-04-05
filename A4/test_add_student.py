from unittest import TestCase
from crud import add_student, file_write
from student import Student
from unittest.mock import patch
from unittest.mock import mock_open
import io


class TestAddStudent(TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="First Last A12345678 True 49")
    @patch("builtins.input", side_effect=["Angus", "Mundy", "A87630912", "Y", "67", "85", "92", "None"])
    @patch("crud.file_write", side_effect=[True])
    def test_add_student_bool(self, mock_write, mock_open, mock_input):
        self.assertEqual(add_student(), True)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.open", new_callable=mock_open, read_data="First Last A12345678 True 49")
    @patch("builtins.input", side_effect=["Angus", "Mundy", "A87630912", "Y", "67", "85", "92", "None"])
    @patch("crud.file_write", side_effect=[True])
    def test_add_student_print(self, mock_write, mock_open, mock_input, mock_stdout):
        add_student()
        self.assertEqual(mock_stdout.getvalue(), "\nStudent was added successfully!\n\n")

    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.input", side_effect=["Linh", "Truong", "A01081792", "Y", "90", "None"])
    def test_file_write_student_called_once(self, mock_input, mock_file):
        student_instance = Student("Linh", "Truong", "A01081792", True)
        student_instance.update_grades(90)
        file_write(student_instance)
        mock_file().write.assert_called_once_with("Linh Truong A01081792 True 90\n")
