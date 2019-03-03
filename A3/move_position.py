from global_helper import user_input_type


def move_west(char: dict) -> int:
    """Moves character West on arbitrary map.

    RETURN x coordinate of characters new position - 1"""
    current_x_position = char["Position"][0]

    if (current_x_position - 1) == -1:
        print("You head West out of bounds and feeling scared. Due to this, you head back to your original position.")
        move_character(char)
    elif char["HP"] < 10:
        return char["Position"][0] - 1 and char["HP"] + 1
    else:
        return char["Position"][0] - 1


def move_east(char: dict) -> int:
    """Moves character East on arbitrary map.

    RETURN x coordinate of characters new position, + 1"""
    current_x_position = char["Position"][0]
    if (current_x_position + 1) == 4:
        print("You head East out of bounds and step in mud! You go back to your original position, to clean your feet")
        move_character(char)
    elif char["HP"] < 10:
        return char["Position"][0] + 1 and char["HP"] + 1
    else:
        return char["Position"][0] + 1


def move_north(char: dict) -> int:
    """Moves character North on arbitrary map.

    RETURN y coordinate of characters new position - 1"""
    current_y_position = char["Position"][1]
    if (current_y_position - 1) == -1:
        print("You head North out of bounds and find a bush of berries. Unfortunately, they're poisonous and "
              "make you sick. Due to this, you head back to your original position.")
        move_character(char)
    elif char["HP"] < 10:
        return char["Position"][1] - 1 and char["HP"] + 1
    else:
        return char["Position"][1] - 1


def move_south(char: dict) -> int:
    """Moves character south on arbitrary map.

    RETURN y coordinate of characters new position, + 1"""
    current_y_position = char["Position"][1]
    if (current_y_position + 1) == 4:
        print("You head South out of bounds and feeling scared. Due to this, you head back to your original position.")
        move_south(current_y_position)
    elif char["HP"] < 10:
        return char["Position"][1] + 1 and char["HP"] + 1
    else:
        return char["Position"][1] + 1


def move_character(pokemon: dict):
    """Obtain user input to determine new position."""
    print("|¯|¯|¯|¯|\n|¯|¯|¯|¯|\n|¯|¯|¯|¯|\n|¯|¯|¯|¯|\n")
    current_position = pokemon["Position"]
    user_direction_input = user_input_type("Position(x, y): %s | HP: %s\nWhere would you like to go? (N/E/S/W)\n"
                                           % (current_position, pokemon["HP"]))

    if user_direction_input.strip().upper() == "W":
        move_west(pokemon)
    elif user_direction_input.strip().upper() == "E":
        move_east(pokemon)
    elif user_direction_input.strip().upper() == "N":
        move_north(pokemon)
    elif user_direction_input.strip().upper() == "S":
        move_south(pokemon)
    else:
        print("I can't understand Pokemon language! Please try again.")
        move_character(pokemon)
