from unittest import TestCase
from crud import file_delete_student
from unittest.mock import patch, mock_open


class TestFileDeleteStudent(TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="Shake Will A00000000 False 53 78")
    def test_file_delete_student_true(self, mock_file):
        self.assertEqual(file_delete_student("A98394820"), True)

    @patch('builtins.open', new_callable=mock_open, read_data="Shake Will A00000000 False 53 78")
    def test_file_delete_student_false(self, mock_file):
        self.assertEqual(file_delete_student("A00000000"), False)
