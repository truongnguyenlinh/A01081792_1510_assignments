from unittest import TestCase
from crud import exclude_student, file_read
from student import Student
from unittest.mock import patch
from unittest.mock import mock_open
from unittest.mock import call


class TestExcludeStudent(TestCase):
    @patch("builtins.open", new_callable=mock_open)
    def test_exclude_student_calls(self, mock_file):
        list_of_students = [Student("Linh", "Truong", "A01081792", True),
                            Student("Dave", "Mundy", "A00000000", False),
                            Student("Angus", "Mundy", "A12345678", True),
                            Student("Ben", "Spratt", "A77886655", False)]
        exclude_student(list_of_students)
        mock_file().write.assert_has_calls([call('Linh Truong A01081792 True \n'),
                                            call('Dave Mundy A00000000 False \n'),
                                            call('Angus Mundy A12345678 True \n'),
                                            call('Ben Spratt A77886655 False \n')])

    @patch('builtins.open', new_callable=mock_open, read_data="Linh Truong A01081792 True\n"
                                                              "Dave Mundy A00000000 False\n"
                                                              "Angus Mundy A12345678 True\n"
                                                              "Ben Spratt A77886655 False")
    @patch("builtins.open", new_callable=mock_open)
    def test_exclude_student(self, mock_file, mock_data):
        list_of_students = [Student("Linh", "Truong", "A01081792", True),
                            Student("Dave", "Mundy", "A00000000", False),
                            Student("Angus", "Mundy", "A12345678", True),
                            Student("Ben", "Spratt", "A77886655", False)]
        exclude_student(list_of_students)
        self.assertEqual(str(list_of_students), str(file_read()))
