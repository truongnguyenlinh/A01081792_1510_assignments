class Student:

    def __init__(self, f_name: str, l_name: str, student_num: str, status: bool):
        if not (f_name.isalpha() and l_name.isalpha()):
            raise ValueError("Please enter a first and last name with alphabetic characters!")
        else:
            self.first_name = f_name.title()
            self.last_name = l_name.title()

        if not (student_num[0].upper() == "A" and student_num[1:].isdigit() and len(student_num) == 9):
            raise ValueError("Enter a nine character student number beginning in 'A' and remaining values as digits.")
        else:
            self.id = student_num.upper()
        self.status = None
        self.confirm_standing(status)
        self.final_grades = []

    def confirm_standing(self, status: bool):
        if status is True:
            self.status = "in-good-standing"
        elif status is False:
            self.status = "academic probation"
        else:
            raise ValueError("Please enter whether the student is 'in-good-standing' or on 'academic probation'.")

    def get_final_grades(self):
        return self.final_grades

    def get_status(self):
        return self.status

    def return_info(self):
        return self.first_name, self.last_name, self.id, self.status, self.final_grades


def main():
    student_one = Student("angus", "mundy", "a01081792", True)
    print(student_one.return_info())


if __name__ == '__main__':
    main()
