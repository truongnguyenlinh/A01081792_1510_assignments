# Linh Truong
# A01081792
# 03/06/2019


import doctest
import json


pokemon = {"Position": [0, 0], "HP": 10}


def character_name() -> str:
    """Obtain name input from user.

    RETURN string of entered name
    """
    global pokemon
    name = input("Enter your name, adventurer.\n")
    name = name.title()
    if not name.isalpha():
        print("I'm sorry, I don't quite understand!")
        character_name()

    confirm_name = input("Did I get that right, %s (Y/N)?\n" % name)
    if confirm_name.strip().upper() == "N":
        print("I'm sorry!")
        return character_name()
    elif confirm_name.strip().upper() == "Y":
        print("Welcome to the magical Pokemon SUD, %s!\n"
              "Before we begin, you will need to choose your pokemon.\n"
              "From there, the adventure will begin.\n" % name)
        pokemon.update({"Name": name})
    else:
        print("I'm sorry, I didn't quite understand that.")
        character_name()


def class_selection() -> None:
    """Obtain selected class from user.

    RETURN selected class from set dictionary.
    """
    global pokemon
    class_type = {"1": "Squirtle", "2": "Charmander", "3": "Bulbasaur\n"}
    class_input = input("Enter the corresponding number of your desired Pokemon type:\n"
                        "1. Squirtle\n2. Charmander\n3. Bulbasaur\n")
    class_input = class_input.strip()
    if class_input in class_type.keys():
        pokemon.update({"Class": class_type[class_input]})
    else:
        print("Please enter a number to choose your Pokemon type!")
        class_selection()


def character_information() -> None:
    """Store all user input into a dictionary.

    RETURN dictionary of character information
    """
    global pokemon
    character_name()
    class_selection()

    print("Hello, %s the %s! The goal of this world is to roam the regions, defeating all Pokemon encountered.\n"
          "If you encounter a Pokemon, you may flee or flight; however, the battle will be a combat to the death.\n"
          "Fear not, if you leave a battle wounded, 1HP will be added to your health until you reach a max of 10HP.\n"
          "Your HP will only go up, for every move where you are not in battle. "
          "If you choose to flee from a battle,\nthere is a chance that your opponent will attack at "
          "the same time; keep this in mind moving forward.\n\n"
          "You may only move in directions of North, East, South and West within the constraints of our \n"
          "fantastic world and at any time, enter 'quit' to end the game. Good Luck!\n"
          % (pokemon["Name"], pokemon["Class"]))


def get_row():
    """Obtain current row position from user.

    RETURN integer of current row position
    """
    return pokemon["Position"][0]


def get_column():
    """Obtain current column position from user.

    RETURN integer of current column position
    """

    return pokemon["Position"][1]


def get_hp():
    """Obtain current row position from user.

    RETURN integer of current row position
    """
    return pokemon["HP"]


def change_hp(change: int) -> None:
    """Change global variable pokemon HP.
    """
    global pokemon
    pokemon["HP"] += change


def change_row(position: int) -> None:
    """Change global variable pokemon row position.
    """
    global pokemon
    pokemon["Position"][0] += position


def change_column(position: int) -> None:
    """Change global variable pokemon column position.
    """
    global pokemon
    pokemon["Position"][1] += position


def save_character() -> None:
    """Save user character information into a JSON file.

    PARAM character must be a well formed dictionary seen in character_information
    """
    global pokemon
    filename = "character.json"
    with open(filename, 'w') as file_object:
        json.dump(pokemon, file_object)


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
