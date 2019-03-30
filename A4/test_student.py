from unittest import TestCase
from student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.test_student = Student("chris", "thompson", "a00000000", True)
        self.test_student_1 = Student("ANGUS", "MUNDY", "A09987654", False)
        # self.test_student_2_incorrect = Student("H3LEN", "NG73N", "G", False)

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
        actual = self.test_student_1.get_final_grades()
        self.assertEqual(expected, actual)

    def test_set_f_name(self):
        expected = "Henry"
        self.test_student.set_f_name("Henry")
        actual = self.test_student.get_f_name()
        self.assertEqual(expected, actual)

    def test_set_l_name(self):
        expected = "Welp"
        self.test_student.set_l_name("welp")
        actual = self.test_student.get_l_name()
        self.assertEqual(expected, actual)

    def test_set_standing(self):
        expected = True
        self.test_student_1.set_standing(True)
        actual = self.test_student_1.get_standing()
        self.assertEqual(expected, actual)
