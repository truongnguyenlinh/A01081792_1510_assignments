from unittest import TestCase
from crud import file_read
from student import Student
from unittest.mock import patch, mock_open


class TestFileRead(TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="First Last A12345678 True 49\n")
    def test_file_read_list(self, mock_file):
        student_instance = Student("First", "Last", "A12345678", True)
        student_instance.update_grades(49)
        self.assertEqual(type(file_read()), list)

    @patch('builtins.open', new_callable=mock_open, read_data="First Last A12345678 True 49\n")
    def test_file_read_content(self, mock_file):
        student_instance = Student("First", "Last", "A12345678", True)
        student_instance.update_grades(49)
        actual = file_read()
        self.assertEqual(str([student_instance]), str(actual))
