from unittest import TestCase
from crud import obtain_grades
from student import Student
from unittest.mock import patch
import unittest
import io


class TestObtainGrades(TestCase):

    def setUp(self):
        self.test_student = Student("Linh", "Truong", "a01081792", True)

    @patch('builtins.input', side_effect=["76", "65", "98", "none"])
    def test_obtain_grades(self, mock_user_input):
        expected = [76, 65, 98]
        obtain_grades(self.test_student)
        actual = self.test_student.get_final_grades()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["79", "g", "none"])
    def test_obtain_grades_alpha(self, mock_user_input):
        expected = [79]
        obtain_grades(self.test_student)
        actual = self.test_student.get_final_grades()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["gaewga", "g", "none"])
    def test_obtain_grades_none(self, mock_user_input):
        expected = []
        obtain_grades(self.test_student)
        actual = self.test_student.get_final_grades()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["1000", "none"])
    def test_obtain_grades_range(self, mock_user_input):
        expected = []
        obtain_grades(self.test_student)
        actual = self.test_student.get_final_grades()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[18])
    def test_obtain_grades_type(self, mock_user_input):
        with self.assertRaises(AttributeError):
            obtain_grades(self.test_student)
