def user_input_type(msg: str) -> str:
    """End program if user input is quit.

    RETURN user input if not quit"""
    user_input = input(msg)
    if user_input.strip().lower() == "quit":
        exit()
    else:
        return user_input


def character_name() -> str:
    """Obtain input of user-name.

    RETURN string of name entered
    """
    name = input("Enter your name, adventurer.\n")
    name = name.title()
    if not name.isalpha():
        print("I'm sorry, I don't quite understand!")
        return character_name()

    confirm_name = input("Did I get that right, %s (Y/N)?\n" % name)
    if confirm_name.strip().upper() == "N":
        print("I'm sorry!")
        return character_name()
    elif confirm_name.strip().upper() == "Y":
        print("Welcome to the magical Pokemon SUD, %s!\n"
              "Before we begin, you will need to choose your pokemon.\n"
              "From there, the adventure will begin.\n" % name)
        return name
    else:
        print("I'm sorry, I didn't quite understand that.")
        return character_name()


def class_selection() -> str:
    """Obtain class-selection from user.

    RETURN selected class from set list.
    """
    class_type = {"1": "Squirtle", "2": "Charmander", "3": "Bulbasaur\n"}
    class_input = input("Enter a number of your desired Pokemon type from the following:\n"
                        "1. Squirtle\n2. Charmander\n3. Bulbasaur\n")
    class_input = class_input.strip()
    if class_input in class_type.keys():
        return class_type[class_input]
    else:
        print("Please enter a number to choose your Pokemon type!")
        return class_selection()


def select_gender() -> str:
    """Return selected gender from Male or Female.

    RETURN a string of either male or female"""
    gender_types = {"1": "Male", "2": "Female"}
    gender_input = input("Please enter one of the two numbers to select your gender:\n1. Male\n2. Female\n")
    gender_input = gender_input.strip()
    if gender_input in gender_types.keys():
        return gender_types[gender_input]
    else:
        print("I'm sorry, I didn't quite get that.")
        return select_gender()


def character_information() -> dict:
    """Store all user input into a list.

    RETURN dictionary of character information"""
    character = {"Name": character_name(), "Class": class_selection(),
                 "Gender": select_gender(), "Position": [0, 0], "HP": 10}
    
    print("Hello, %s the %s! The goal of this world is to roam the regions, defeating all Pokemon encountered.\n"
          "If you encounter a Pokemon, you may flee or flight; however, the battle will be a combat to the death.\n"
          "Fear not, if you leave a battle wounded, 1HP will be added to your health until you reach a max of 10HP.\n"
          "Your HP will only go up, for every move where you are not in battle. "
          "If you choose to flee from a battle,\nthere is a chance that your opponent will attack at "
          "the same time; keep this in mind moving forward.\n\n"
          "You may only move in directions of North, East, South and West within the constraints of our \n"
          "fantastic world and at any time, enter 'quit' to end the game. Good Luck!\n"
          % (character["Name"], character["Class"]))
    return character
