from unittest import TestCase
from student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.test_student = Student("chris", "thompson", "a00000000", True)
        self.test_student_1 = Student("ANGUS", "MUNDY", "A09987654", False)

    def test_append_grades(self):
        expected = [78]
        actual = self.test_student.append_grades(78)
        self.assertEqual(expected, actual)

    def test_string_grades(self):
        expected = ""
        actual = self.test_student.string_grades()
        self.assertEqual(expected, actual)

    def test_get_f_name(self):
        expected = "Chris"
        actual = self.test_student.get_f_name()
        self.assertEqual(expected, actual)

    def test_get_l_name(self):
        expected = "Mundy"
        actual = self.test_student_1.get_l_name()
        self.assertEqual(expected, actual)

    def test_get_id(self):
        expected = "A09987654"
        actual = self.test_student_1.get_id()
        self.assertEqual(expected, actual)

    def test_get_standing(self):
        expected = True
        actual = self.test_student.get_standing()
        self.assertEqual(expected, actual)

    def test_get_final_grades(self):
        expected = []
        actual = self.test_student.get_final_grades()
        self.assertEqual(expected, actual)
