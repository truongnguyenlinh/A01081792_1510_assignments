class Student:

    def __init__(self, f_name: str, l_name: str, student_num: str, status: bool, grades: list):
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

        if type(grades) != list:
            raise TypeError
        else:
            self.__final_grades = grades

    def get_f_name(self):
        return self.__first_name

    def get_l_name(self):
        return self.__last_name

    def get_id(self):
        return self.__id

    def get_standing(self):
        return self.__status

    def get_final_grades(self):
        return self.__final_grades

    def set_f_name(self, new_f_name: str):
        if not new_f_name.isalpha():
            raise ValueError("New first name must consist of alphabet characters!")
        else:
            self.__first_name = new_f_name.strip().title()

    def set_l_name(self, new_l_name: str):
        if not new_l_name.isalpha():
            raise ValueError("New first name must consist of alphabet characters!")
        else:
            self.__last_name = new_l_name.strip().title()

    def set_standing(self, new_standing: bool):
        if type(new_standing) != bool:
            raise ValueError("Standing must be True or False!")
        else:
            self.__status = new_standing

    def __str__(self):
        return self.__last_name + " " + self.__first_name + " " + self.__id + " " + str(self.__status) \
               + " " + " ".join(str(grade) for grade in self.__final_grades)
