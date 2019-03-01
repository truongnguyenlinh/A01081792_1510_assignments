from sud import user_input_type


def dungeon_map() -> []:
    """Interpret a square map of potential positions which a user can move to.
    """
    map_positions = [(0, 0), (1, 0), (2, 0), (3, 0),
                     (0, 1), (1, 1), (2, 1), (3, 1),
                     (0, 2), (1, 2), (2, 2), (3, 2),
                     (0, 3), (1, 3), (2, 3), (3, 3)]
    return map_positions


def move_west(char: dict) -> int:
    """Moves character West on arbitrary map.

    RETURN x coordinate of characters new position - 1"""
    current_x_position = char["Position"][0]

    if (current_x_position - 1) == -1:
        print("You're out of bounds and feeling scared. Due to this, you head back to your original position.")
        move_character(char)
    else:
        return char["Position"][0] - 1


def move_east(char: dict) -> int:
    """Moves character East on arbitrary map.

    RETURN x coordinate of characters new position, + 1"""
    current_x_position = char["Position"][0]
    if (current_x_position + 1) == 4:
        print("You head East out of bounds and step in mud! You go back to your original position, to clean your feet")
        move_character(char)
    else:
        return char["Position"][0] + 1


def move_north(char: dict) -> int:
    """Moves character North on arbitrary map.

    RETURN y coordinate of characters new position - 1"""
    current_y_position = char["Position"][1]
    if (current_y_position - 1) == -1:
        print("You're out of bounds and feeling scared. Due to this, you head back to your original position.")
        move_character(char)
    else:
        return char["Position"][1] - 1


def move_south(char: dict) -> int:
    """Moves character south on arbitrary map.

    RETURN y coordinate of characters new position, + 1"""
    current_y_position = char["Position"][1]
    if (current_y_position + 1) == 4:
        print("You're out of bounds and feeling scared. Due to this, you head back to your original position.")
        move_south(current_y_position)
    else:
        return char["Position"][1] + 1


def move_character(pokemon: dict):
    """Obtain user input to determine new position."""
    current_position = pokemon["Position"]
    user_direction_input = user_input_type("Position(x, y): %s\nWhere would you like to go? (N/E/S/W)" % current_position)

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
