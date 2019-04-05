from unittest import TestCase
from crud import file_write
from student import Student
from unittest.mock import patch
from unittest.mock import mock_open


class TestFileWrite(TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="Linh Truong A01081702 True 78")
    def test_file_write(self, mock_file):
        student_instance = Student("Linh", "Truong", "A01081792", True)
        student_instance.update_grades(90)
        value = file_write(student_instance)
        mock_file().read()
        mock_file().write.assert_called_once_with("Linh Truong A01081792 True 90\n")
        self.assertEqual(value, True)
