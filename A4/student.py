class Student:

    def __init__(self, f_name: str, l_name: str, student_num: str, status: bool, grades: list = None):
        """Initialize a Student with their first name, last name, student number, standing and grades."""
        if not (f_name.isalpha() and l_name.isalpha()):
            raise ValueError("Please enter a first and last name with alphabetic characters only!")
        else:
            self.__first_name = f_name.strip().title()
            self.__last_name = l_name.strip().title()

        if not (student_num[0].upper() == "A" and student_num[1:].isdigit() and len(student_num) == 9):
            raise ValueError("Please enter a student number beginning with 'A', followed by 8 digits.")
        else:
            self.__id = student_num.upper()

        if type(status) != bool:
            raise TypeError("Please pass True or False!")
        else:
            self.__status = status
        self.__final_grades = []

    def get_f_name(self):
        """Get a Student's first name."""
        return self.__first_name

    def get_l_name(self):
        """Get a Student's last name."""
        return self.__last_name

    def get_id(self):
        """Get a Student's student number."""
        return self.__id

    def get_standing(self):
        """Get a Student's current standing."""
        return self.__status

    def get_final_grades(self):
        """Get a Student's current grades list."""
        return self.__final_grades

    def set_f_name(self, new_f_name: str):
        """Set a Student object with updated first name."""
        if not new_f_name.isalpha():
            raise ValueError("New first name must consist of alphabet characters!")
        else:
            self.__first_name = new_f_name.strip().title()

    def set_l_name(self, new_l_name: str):
        """Set a Student object with updated last name."""
        if not new_l_name.isalpha():
            raise ValueError("New first name must consist of alphabet characters!")
        else:
            self.__last_name = new_l_name.strip().title()

    def set_standing(self, new_standing: bool):
        """Set Student object standing of True or False."""
        if type(new_standing) != bool:
            raise ValueError("Standing must be True or False!")
        else:
            self.__status = new_standing

    def update_grades(self, new_grade: int):
        """Add a grade for every input from user if between 0 and 100."""
        if not (100 > new_grade > 0):
            raise ValueError("Please enter final grade(s) between 0 and 100 percent.")
        else:
            self.__final_grades.append(new_grade)

    def get_gpa(self) -> float:
        """Calculate and return the student's gpa as a float."""
        student_total = 0
        for grade in self.get_final_grades():
            student_total += grade
        return student_total / len(self.get_final_grades())

    def __str__(self) -> str:
        """Return a string representation of this student that looks like:
        FirstName LastName A######## True 90 80 76 100 62 42"""
        return self.__first_name + " " + self.__last_name + " " + self.__id + " " + str(self.__status) + " " \
               + " ".join(str(grade) for grade in self.get_final_grades())
