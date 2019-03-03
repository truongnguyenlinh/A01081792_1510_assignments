import random
from combat import fight_flee
from pokemon import random_pokemon
from global_helper import user_input_type, roll_die


def random_message() -> str:
    """Return random message.

    RETURN string of random message"""

    msg_1 = "You encountered a delicious Pecha Berry bush! Feeling hungry, pick a some berries and have a snack."
    msg_2 = "Looks like there's something shiny behind a tree. You head towards the tree and find a Big Pearl.\n" \
            "The pearlescent sheen is irresistible, so you put it in your bag."
    msg_3 = "After stepping out of the grass, you find some Gooey Mulch. " \
            "Although a maniac would buy this to use as fertilizer on a Berry Crop, you decide not to pick it up."
    msg_4 = "You head towards the grass and continue on your path."

    msg_list = [msg_1, msg_2, msg_3]
    msg_probability = roll_die(1, 3)

    if msg_probability == 1:
        return random.choice(msg_list)
    else:
        return msg_4


def move_west(char: dict) -> None:
    """Moves character West on arbitrary map.

    RETURN None if character choice is outside of range"""
    current_x_position = char["Position"][0]
    opponent_pokemon = random_pokemon()
    if (current_x_position - 1) == -1:
        print("You head West out of bounds and feeling scared. Due to this, you head back to your original position.")
        move_character(char)
        return None
    elif char["HP"] < 10:
        char["Position"][0] -= 1
        char["HP"] += 1
        print(random_message())
    else:
        char["Position"][0] -= 1
        print(random_message())
    fight_flee(char, opponent_pokemon)


def move_east(char: dict) -> None:
    """Moves character East on arbitrary map.

    RETURN None if character choice is outside of range"""
    opponent_pokemon = random_pokemon()
    current_x_position = char["Position"][0]
    if (current_x_position + 1) == 4:
        print("You head East out of bounds and step in mud! You go back to your original position, to clean your feet")
        move_character(char)
        return None
    elif char["HP"] < 10:
        char["Position"][0] += 1
        char["HP"] += 1
        print(random_message())
    else:
        char["Position"][0] += 1
        print(random_message())
    fight_flee(char, opponent_pokemon)


def move_north(char: dict) -> None:
    """Moves character North on arbitrary map.

    RETURN y coordinate of characters new position - 1"""
    opponent_pokemon = random_pokemon()
    current_y_position = char["Position"][1]
    if (current_y_position - 1) == -1:
        print("You head North out of bounds and find a bush of berries. Unfortunately, they're poisonous and "
              "make you sick. Due to this, you head back to your original position.")
        move_character(char)
        return None
    elif char["HP"] < 10:
        char["Position"][1] -= 1
        char["HP"] += 1
        print(random_message())
    else:
        char["Position"][1] -= 1
        print(random_message())
    fight_flee(char, opponent_pokemon)


def move_south(char: dict) -> None:
    """Moves character south on arbitrary map.

    RETURN None if character choice is outside of range"""
    opponent_pokemon = random_pokemon()
    current_y_position = char["Position"][1]
    if (current_y_position + 1) == 4:
        print("You head South out of bounds and feeling scared. Due to this, you head back to your original position.")
        move_character(char)
        return None
    elif char["HP"] < 10:
        char["Position"][1] += 1
        char["HP"] += 1
        print(random_message())
    else:
        char["Position"][1] += 1
        print(random_message())
    fight_flee(char, opponent_pokemon)


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
