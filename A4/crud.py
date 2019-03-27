import student


def obtain_standing():
    """Confirm student's current standing.

    RETURN True if user input is Y, False if N"""
    input_standing = input("Is the student in good standing (Y/N)?")
    if input_standing.strip().upper() == "Y":
        return True
    elif input_standing.strip().upper() == "N":
        return False
    else:
        print("Please enter one of the listed options by number!")


def obtain_grades(student_obj):
    """Confirm if user would like to input final grades. Add to final grades list if so.

    PRECONDITION student_obj must be valid class from Student"""
    grades_input = ""
    while grades_input.strip().title() != "None":
        grades_input = input("Enter the student's final grade for a single course.\n"
                             "Otherwise, type 'None'.\n")
        if grades_input.strip().isdigit():
            student_obj.append_grades(int(grades_input))


def add_student():
    """Obtain user input to generate a Student instance."""
    first_name = input("Enter the student's first name (must only be alphabetical characters).")
    last_name = input("Enter the student's last name (must only be alphabetical characters).")
    student_num = input("Enter the student's id number (must be of length 9 and begin with 'a').")
    try:
        student_instance = student.Student(first_name, last_name, student_num, obtain_standing())
        obtain_grades(student_instance)
        file_write(student_instance)
    except ValueError:
        print("An incorrect value was entered representing student first name, last name or student number!")


def file_write(student_object):
    """Append student_object to the end of students.txt file.

    PARAM student_object must be an instance of class Student
    RETURN True if student_object was successfully appended to file"""
    filename = "students.txt"
    # FileNotFoundError will never occur, as 'a' mode will always create a new file if not existing
    with open(filename, "a") as file_object:
        file_object.write("%s %s %s %s %s" % (student_object.get_f_name(), student_object.get_l_name(),
                                              student_object.get_id(), student_object.get_standing(),
                                              student_object.string_grades()))
        file_object.write("\n")
    return True


def file_delete_student(student_num):
    """Determine if student was removed from text-file.

    PRECONDITION student_num must be formatted as seen in Student ID attribute
    RETURN True if student_num is not found on file, False otherwise"""
    file_object = open("students.txt", "r")
    file = file_object.read()
    file_object.close()
    if student_num not in file:
        return True
    else:
        return False


def exclude_student(student_num):
    """Create new file excluding line with student_num.

    PRECONDITION student_num must be formatted as seen in Student ID attribute"""
    with open("students.txt", "r+") as file_object:
        file = [line for line in file_object.readlines() if student_num not in line]
        file_object.seek(0)
        for line in file:
            file_object.write(line)
        file_object.truncate()


def del_student():
    """Delete a Student from students.txt given their student number."""
    student_num = input("Enter the student number you would like to remove.")
    student_num = student_num.upper()
    with open("students.txt", "r"):
        if file_delete_student(student_num):
            print("This student is no longer on file.")
        else:
            print("Deleted!")
            exclude_student(student_num)


def calc_average():
    """Calculate the average of all students in students.txt, excluding students with no grades."""
    student_total = 0
    count = 0
    class_avg_list = []
    with open("students.txt", "r") as file_object:
        file = file_object.readlines()

    try:
        for line in file:
            words_list = line.split()
            if len(words_list) > 4:
                count += 1
                for grade in words_list[4:]:
                    student_total += int(grade)
                class_avg_list.append(student_total/len(words_list[4:]))
        print("The class average is " + str(sum(class_avg_list) / count) + ".\n")
    except ZeroDivisionError:
        print("The class currently has no grades!")


def user_selection(user_input):
    """Determine user input to perform action.

    PRECONDITION user_input must be a string within range 1 to 5"""
    if user_input == "1":
        add_student()
    elif user_input == "2":
        del_student()
    elif user_input == "3":
        calc_average()
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
