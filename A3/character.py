from sud import user_input_type


def character_name() -> str:
    """Obtain input of user-name.

    RETURN string of name entered
    """
    name = user_input_type("Enter your name, adventurer.")
    name = name.title()
    if not name.isalpha():
        print("I'm sorry, I don't quite understand!")
        return character_name()

    confirm_name = user_input_type("Did I get that right, %s (Y/N)?" % name)
    if confirm_name.strip().upper() == "N":
        print("I'm sorry!")
        return character_name()
    elif confirm_name.strip().upper() == "Y":
        print("Welcome to the magical Pokemon SUD, %s!\n"
              "Before we begin, you will need to choose your pokemon.\n"
              "From there, the adventure will begin." % name)
        return name
    else:
        print("I'm sorry, I didn't quite understand that.")
        return character_name()


def class_selection() -> str:
    """Obtain class-selection from user.

    RETURN selected class from set list.
    """
    class_type = ["Squirtle", "Charmander", "Bulbasaur"]
    class_input = user_input_type("Enter your desired Pokemon type from the following: " + ", ".join(class_type))
    class_input = class_input.strip().title()
    if class_input.strip().title() in class_type:
        return class_input
    else:
        print("That is not a familiar Pokemon type, please try again!")
        return class_selection()


def select_gender() -> str:
    """Return selected gender from Male or Female.

    RETURN a string of either male or female"""
    gender_input = user_input_type("Please choose your gender:\n1. Male\n2. Female\n")
    if "Male" in gender_input.strip().title():
        return "Male"
    elif "Female" in gender_input.strip().title():
        return "Female"
    else:
        print("I'm sorry, I don't quite understand.")
        return select_gender()


def character_information() -> dict:
    """Store all user input into a list.

    RETURN dictionary of character information"""
    character = {"Name": character_name(), "Class": class_selection(),
                 "Gender": select_gender(), "Position": [0, 0], "HP": 10}
    
    print("Hello, %s the %s! The goal of this world is to roam the regions, defeating all Pokemon encountered.\n"
          "If you encounter a Pokemon, you may flee or flight; however, the battle will be a combat to the death.\n"
          "Fear not, if you leave a battle wounded, 1HP will be added to your health until you reach a max of 10HP,\n"
          "for every move where you are not in battle. "
          "Additionally, if you choose to flee from a battle, \nthere is a chance that your opponent will attack at "
          "the same time; keep this in mind moving forward.\n"
          "You may only move in directions of North, East, South and West within the constraints of our \n"
          "fantastic world and at any time, enter 'quit' to end the game. Good Luck!"
          % (character["Name"], character["Class"]))
    return character
