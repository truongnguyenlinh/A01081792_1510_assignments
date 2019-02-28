def character_name():
    """Obtain input of user-name.

    RETURN string of name entered
    """
    name = input("Enter your name, adventurer.")
    name = name.title()
    if not name.isalpha():
        print("I'm sorry, I don't quite understand!")
        return character_name()

    confirm_name = input("Did I get that right, %s (Y/N)?" % name)
    if confirm_name.strip().upper() == "N":
        print("I'm sorry!")
        return character_name()
    elif confirm_name.strip().upper() == "Y":
        print("Welcome to the whimsical and magical SUD, %s!\n"
              "Before we begin, we will need to create your character.\n"
              "From there, the adventure will begin." % name)
        return name
    else:
        print("I'm sorry, I didn't quite understand that.")
        return character_name()


def class_selection():
    """Obtain class-selection from user.

    RETURN selected class from set list.
    """
    class_filters = ["Cleric", "Warrior", "Thief", "Ranger"]
    # {"Cleric": {"HP": 100, "MANA": 80, "XP": 0, "MVS": 500, "INT": 0},
    #  "Warrior": {"HP": 160, "MANA": 20, "XP": 0, "MVS": 500, "INT": 0},
    #  "Thief": {"HP": 80, "MANA": 40, "XP": 0, "MVS": 500, "INT": 0},
    #  "Ranger": {"HP": 160, "MANA": 40, "XP": 0, "MVS": 500, "INT": 0}}

    class_input = input("Enter your desired class from the following: " + ", ".join(class_filters))
    class_input = class_input.strip().title()
    if class_input.strip().title() in class_filters:
        return class_input
    else:
        print("That is not a familiar class, please try again!")
        return class_selection()


def select_gender():
    """Return selected gender from Male or Female.

    RETURN a string of either male or female"""
    gender_input = input("Please choose your gender:\n1. Male\n2. Female\n")
    if "Male" in gender_input.strip().title():
        return "Male"
    elif "Female" in gender_input.strip().title():
        return "Female"
    else:
        print("I'm sorry, I don't quite understand.")
        return select_gender()


def character_information():
    character = [character_name(), class_selection(), select_gender()]
    print("Hello, %s the %s! The goal of this SUD is to roam the earth, defeating all monsters encountered.\n"
          "If you encounter a monster, you may flee or flight; however, the battle will be a combat to the death.\n"
          "Fear not, if you leave a battle wounded, 1HP will be added to your health until you reach a max of 10HP,\n"
          "for every move where you are not in battle. "
          "Additionally, if you choose to flee from a battle, \nthere is a chance that the monster will attack at "
          "the same time; keep this in mind moving forward.\n"
          "You may only move in directions of North, East, South and West within the constraints of our \n"
          "fantastic world and at any time, enter 'quit' to end the game. Good Luck!"
          % (character[0], character[1]))


def main():
    # character_information()
    pass


if __name__ == '__main__':
    main()
