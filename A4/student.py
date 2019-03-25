class Student:

    def __init__(self, f_name: str, l_name: str, student_num: str, status: str):
        if not (f_name.isalpha() and l_name.isalpha()):
            raise ValueError("Please enter a first and last name with alphabetic characters!")
        else:
            self.first_name = f_name.title()
            self.last_name = l_name.title()

        if not (student_num[0].upper() == "A" and student_num[1:].isdigit() and len(student_num) == 9):
            raise ValueError("Enter a nine character student number beginning in 'A' and remaining values as digits.")
        else:
            self.id = student_num.title()
        self.standing = self.confirm_standing(status)
        self.status = status
        self.final_grades = []

    def confirm_standing(self, status: str):
        if status.strip() == "in-good-standing":
            return True
        elif status.strip() == "academic probation":
            return False
        else:
            raise ValueError("Please enter whether the student is 'in-good-standing' or on 'academic probation'.")

    def gather_grades(self):
        grades = input("Please enter your grade in percentages in the following format:\nGrade1 Grade2 Grade3 ...")
        grades = grades.split()
        try:
            for grade in grades:
                self.final_grades.append(int(grade))
        except ValueError:
            print("Please enter valid grade-percentages in the given format!")

    def get_final_grades(self):
        return self.final_grades

    def get_status(self):
        return self.status

    def print_info(self):
        print(self.first_name, self.last_name, self.id, self.status, self.standing, self.final_grades)


def main():
    student_one = Student("angus", "mundy", "a01081792", "in-good-standing")
    student_one.print_info()
    student_one.gather_grades()
    student_one.print_info()


if __name__ == '__main__':
    main()
