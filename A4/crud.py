import student


def confirm_standing():
    """Confirm student's current standing."""
    input_standing = input("Is the student in good standing (Y/N)?")
    if input_standing.strip().upper() == "Y":
        return True
    elif input_standing.strip().upper() == "N":
        return False
    else:
        print("Please enter one of the listed options by number!")


def add_student():
    """Obtain user input to generate a Student instance."""
    first_name = input("Enter the student's first name.")
    last_name = input("Enter the student's last name.")
    student_num = input("Enter the student's id number.\n")
    student_instance = student.Student(first_name, last_name, student_num, confirm_standing())
    file_write(student_instance)


def file_write(student_object: object):
    """Append student_object to the end of students.txt file.

    PARAM student_object must be an instance of class Student
    RETURN True if student_object was successfully appended to file, False otherwise"""
    filename = "students.txt"
    with open(filename, "a") as file_object:
        try:
            file_object.write(str(student_object) + "n")
            return True
        except AttributeError: #some type of error
            return False


def file_read():
    """Create Student object from each record in file."""
    student_list = []
    file_object = open("students.txt", "r")
    for line in file_object:
        line.split()
        first_name = line[0]
        last_name = line[1]
        student_num = line[3]
        student_standing = line[4]
        grades = line[4:]
        student_instance = student.Student(first_name, last_name, student_num, student_standing)
        student_instance.get_final_grades().append(grades)
        student_list.append(student_instance)
    return student_list


def user_selection(user_input: str):
    """Determine user input to perform action.

    PRECONDITION: user_input must be an int."""
    if user_input == "1":
        add_student()
    # add student to students.txt
    elif user_input == "2":
        pass
    # delete student from students.txt
    elif user_input == "3":
        pass
    # calculate class average
    elif user_input == "4":
        pass
    # print class list
    elif user_input == "5":
        quit()
    else:
        print("Please enter a valid action!\n")


def main():
    while True:
        print("1. Add student\n2. Delete student\n3. Calculate class average\n4. Print class list\n5. Quit\n")
        action_input = input("Enter a menu number that represents your desired action:\n")
        user_selection(action_input)


if __name__ == '__main__':
    main()
