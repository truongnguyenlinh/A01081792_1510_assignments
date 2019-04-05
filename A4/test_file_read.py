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

    @patch('builtins.open', new_callable=mock_open, read_data="Remy Truong A09876543 False 49 60 57\n"
                                                              "May Chau A98898999 True 80 90\n"
                                                              "Linh Truong A01081792 True")
    def test_file_read_information(self, mock_file):
        list_students = []
        student_instance = Student("Remy", "Truong", "A09876543", False)
        student_instance.update_grades(49)
        student_instance.update_grades(60)
        student_instance.update_grades(57)
        student_instance_1 = Student("May", "Chau", "A98898999", True)
        student_instance_1.update_grades(80)
        student_instance_1.update_grades(90)
        student_instance_2 = Student("Linh", "Truong", "A01081792", True)
        list_students.append(student_instance)
        list_students.append(student_instance_1)
        list_students.append(student_instance_2)
        actual = file_read()
        self.assertEqual(str(list_students), str(actual))

    @patch('builtins.open', new_callable=mock_open, read_data="First Last A12345678 True 49\n"
                                                              "Linh Truong A00000000 False")
    def test_file_read_len(self, mock_file):
        actual = file_read()
        self.assertEqual(len(actual), 2)

    @patch("builtins.open", new_callable=mock_open, read_data="Remy Truong A00000000 True 63")
    def test_file_read_values(self, mock_file):
        student_list = file_read()
        self.assertEqual(student_list[0].__str__(), "Remy Truong A00000000 True 63")
