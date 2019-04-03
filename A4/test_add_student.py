from unittest import TestCase
from crud import add_student
from student import Student
from unittest import mock
from unittest.mock import patch
from unittest.mock import mock_open
import os


class TestAddStudent(TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="First Last A12345678 True 49")
    @patch('crud.file_write', called=[True])
    def test_add_student(self, mock_open, mock_function):
        pass
        # not sure how to test this will come back