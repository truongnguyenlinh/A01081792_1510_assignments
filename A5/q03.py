def backup(file_name: str):
    """Create new file in same directory, same content but with file extension .bak.

    PRECONDITION file_name must end in .txt
    POSTCONDITION file has been copied in memory
    """
    try:
        with open(file_name) as file_object:
            file = file_object.readlines()
        with open(file_name[:-3] + "bak", "a") as bak_file:
            for line in file:
                bak_file.write(line)
            print("generated %s" % file_name[:-3] + "bak")
    except FileNotFoundError:
        print("File entered does not currently exist!")


def main():
    backup("students.txt")


if __name__ == '__main__':
    main()
