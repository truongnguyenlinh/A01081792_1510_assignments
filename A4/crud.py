import student


def obtain_standing():
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
    student_instance = student.Student(first_name, last_name, student_num, obtain_standing())
    file_write(student_instance.return_info())


def file_write(student_object: object):
    """Append student_object to the end of students.txt file.

    PARAM student_object must be an instance of class Student
    RETURN True if student_object was successfully appended to file, False otherwise"""
    filename = "students.txt"
    with open(filename, "a") as file_object:
        try:
            file_object.write(str(student_object))
            file_object.write("\n")
            return True
        except FileNotFoundError:
            return False


def del_student():
    """Delete a Student from students.txt given their student number."""
    student_num_del = input("Enter the student number of the student you would like to remove.")
    with open("students.txt", "r") as file_obj:
        lines = file_obj.readlines()
        with open("students.txt", "w") as file_object:
            for line in lines:
                if student_num_del.strip().upper() not in line:
                    file_object.write(line)


def user_selection(user_input: str):
    """Determine user input to perform action.

    PRECONDITION: user_input must be an int."""
    if user_input == "1":
        add_student()
    elif user_input == "2":
        del_student()
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
