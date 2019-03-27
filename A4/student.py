class Student:

    def __init__(self, f_name: str, l_name: str, student_num: str, status: bool):
        if not (f_name.isalpha() and l_name.isalpha()):
            raise ValueError("Please enter a first and last name with alphabetic characters!")
        else:
            self.first_name = f_name.strip().title()
            self.last_name = l_name.strip().title()

        if not (student_num[0].upper() == "A" and student_num[1:].isdigit() and len(student_num) == 9):
            raise ValueError("Enter a nine character student number beginning in 'A' and remaining values as digits.")
        else:
            self.id = student_num.upper()
        self.status = status
        self.final_grades = []

    def append_grades(self, grade):
        grades_list = self.get_final_grades()
        grades_list.append(grade)
        return self.get_final_grades()

    def string_grades(self):
        grades_list = self.get_final_grades()
        grades_string = ""
        for grade in grades_list:
            grades_string = grades_string + str(grade) + " "
        return grades_string

    def get_f_name(self):
        return self.first_name

    def get_l_name(self):
        return self.last_name

    def get_id(self):
        return self.id

    def get_standing(self):
        return self.status

    def get_final_grades(self):
        return self.final_grades
