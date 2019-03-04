import random
import doctest


def user_input_type(msg: str) -> str:
    """End program if user input is quit.

    RETURN user input if not quit"""
    user_input = input(msg)
    if user_input.strip().lower() == "quit":
        exit()
    else:
        return user_input


def roll_die(number_of_rolls: int, number_of_sides: int) -> int:
    """Return the random number after given number of rolls of a die.

    Range of potential output is determined by number_of_rolls and number_of_sides.
    PRECONDITION number_of_rolls is a positive int
    PRECONDITION number_of_sides is a positive int
    RETURN total value from number of rolls and sided die

    >>> roll_die(0, 0)
    0
    >>> roll_die(0, 10)
    0
    >>> roll_die(1, 0)
    0
    >>> random.seed(1)
    >>> roll_die(1, 9)
    3
    """

    if type(number_of_rolls) != int or type(number_of_sides) != int:
        print("Please enter a positive integer")
    elif number_of_rolls == 0 or number_of_sides == 0:
        return 0
    else:
        return random.randint((1 * number_of_rolls), (number_of_sides * number_of_rolls))


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
