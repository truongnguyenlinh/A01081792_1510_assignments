import random
import interactive_map
import doctest
from character import change_hp, change_row, change_column, get_pokemon
from combat import fight_flee
from pokemon import random_pokemon
from global_helper import user_input_type, roll_die


def random_message():
    """Return random message from predefined list.

    RETURN string of random message

    >>> random.seed(4)
    >>> random_message()
    Looks like there's something shiny behind a tree. You head towards the tree and find a Big Pearl.
    The pearlescent sheen is irresistible, so you put it in your bag.
    >>> random_message()
    After stepping out of the grass, you find some Gooey Mulch.
    Although a maniac would buy this to use as fertilizer on a Berry Crop, you decide not to pick it up.
    >>> random_message()
    You head towards the grass and continue on your path.
    >>> random.seed()
    """
    msg_1 = "You encountered a delicious Pecha Berry bush! Feeling hungry, pick a some berries and have a snack."
    msg_2 = "Looks like there's something shiny behind a tree. You head towards the tree and find a Big Pearl.\n" \
            "The pearlescent sheen is irresistible, so you put it in your bag."
    msg_3 = "After stepping out of the grass, you find some Gooey Mulch.\n" \
            "Although a maniac would buy this to use as fertilizer on a Berry Crop, you decide not to pick it up."
    msg_4 = "You head towards the grass and continue on your path."

    msg_list = [msg_1, msg_2, msg_3]
    msg_probability = roll_die(1, 3)

    if msg_probability == 1:
        print(random.choice(msg_list))
    else:
        print(msg_4)


def move_west() -> None:
    """Move character West on arbitrary map.

    RETURN None if y coordinate is out of bounds at -1"""
    current_x_position = get_pokemon()["Position"][0]
    opponent_pokemon = random_pokemon()
    if (current_x_position - 1) == -1:
        print("You head West out of bounds and feeling scared. Due to this, you head back to your original position.")
        move_character()
        return None
    elif get_pokemon()["HP"] < 10:
        change_row(-1)
        change_hp(1)
        random_message()
    else:
        change_row(-1)
        random_message()
    fight_flee(opponent_pokemon)


def move_east() -> None:
    """Move character East on arbitrary map.

    RETURN None if y coordinate is out of bounds at 4"""
    opponent_pokemon = random_pokemon()
    current_x_position = get_pokemon()["Position"][0]
    if (current_x_position + 1) == 4:
        print("You head East out of bounds and step in mud! You go back to your original position, to clean your feet")
        move_character()
        return None
    elif get_pokemon()["HP"] < 10:
        change_row(1)
        change_hp(1)
        random_message()
    else:
        change_row(1)
        random_message()
    fight_flee(opponent_pokemon)


def move_north() -> None:
    """Move character North on arbitrary map.

    RETURN None if y coordinate is out of bounds at -1"""
    opponent_pokemon = random_pokemon()
    current_y_position = get_pokemon()["Position"][1]
    if (current_y_position - 1) == -1:
        print("You head North out of bounds and find a bush of berries. Unfortunately, they're poisonous and "
              "make you sick. Due to this, you head back to your original position.")
        move_character()
        return None
    elif get_pokemon()["HP"] < 10:
        change_column(-1)
        change_hp(1)
        random_message()
    else:
        change_column(-1)
        random_message()
    fight_flee(opponent_pokemon)


def move_south() -> None:
    """Move character South on arbitrary map.

    RETURN None if y coordinate is out of bounds at 4"""
    opponent_pokemon = random_pokemon()
    current_y_position = get_pokemon()["Position"][1]
    if (current_y_position + 1) == 4:
        print("You head South out of bounds and feeling scared. Due to this, you head back to your original position.")
        move_character()
        return None
    elif get_pokemon()["HP"] < 10:
        change_column(1)
        change_hp(1)
        random_message()
    else:
        change_column(1)
        random_message()
    fight_flee(opponent_pokemon)


def move_character():
    """Obtain user input to determine new position.
    """
    interactive_map.pokemon_map(get_pokemon())
    current_position = get_pokemon()["Position"]
    user_direction_input = user_input_type("Position(x, y): %s | HP: %s\nWhere would you like to go? (N/E/S/W)\n"
                                           % (current_position, get_pokemon()["HP"]))

    if user_direction_input.strip().upper() == "W":
        move_west()
    elif user_direction_input.strip().upper() == "E":
        move_east()
    elif user_direction_input.strip().upper() == "N":
        move_north()
    elif user_direction_input.strip().upper() == "S":
        move_south()
    else:
        print("I can't understand Pokemon language! Please try again.")
        move_character()


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
