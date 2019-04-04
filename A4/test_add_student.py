from unittest import TestCase
from crud import add_student
from unittest.mock import patch
from unittest.mock import mock_open

new_file = "First Last A12345678 True 49\nAngus Mundy A87630912 True 67 85 92"


class TestAddStudent(TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="First Last A12345678 True 49")
    @patch('builtins.input', side_effect=["Angus", "Mundy", "A87630912", "Y", "67", "85", "92", "None"])
    @patch('crud.file_write', side_effect=[True])
    def test_add_student(self, mock_write, mock_open, mock_input):
        self.assertEqual(add_student(), True)
