import character
import move_position
import random


def roll_die(number_of_rolls: int, number_of_sides: int) -> int:
    """Return the random number after given number of rolls of a die.

    Range of potential output is determined by number_of_rolls and number_of_sides.
    PRECONDITION number_of_rolls is a positive int
    PRECONDITION number_of_sides is a positive int
    RETURN total value from number of rolls and sided die"""
    if number_of_rolls != int or number_of_sides != int:
        print("Please enter a a positive integer")
    elif number_of_rolls == 0 or number_of_sides == 0:
        return 0
    else:
        return random.randint((1 * number_of_rolls), (number_of_sides * number_of_rolls))


def main():
    print("______________________________________________________________________")
    print("[]    ,-`  ,-`’```’-,:`’-,       \                      ,--,:`,     []")
    print("[]   ,/  /`           `’-,:`’-,   \,-     ,,,         ./¯¯) `)\     []")
    print("[]   |  |                  `-,:`’- /    ,/¯) .\       |¯¯. ,/`’/’   []")
    print("[]   \  |                     `’-,’,    ( ¯’__|        ¯¯¯   ,-`    []")
    print("[]   `\  \                        ‘’`-,   ¯¯                ,’-`    []")
    print("[]     \   \                       '-_/’-‘--,- ---,, __,,-`         []")
    print("======================================================================")
    pokemon = character.character_information()
    move_position.move_character(pokemon)


if __name__ == '__main__':
    main()
