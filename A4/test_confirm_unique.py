from unittest import TestCase
from crud import confirm_unique, file_write
from student import Student
from unittest.mock import patch
import unittest.mock
import io


class TestConfirmUnique(TestCase):
    def setUp(self):
        self.test_student = Student("allen", "wong", "a00088888", True)
        file_write(self.test_student)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_confirm_unique(self, mock_stdout):
        self.assertEqual(confirm_unique("A00000000"), "A00000000")
