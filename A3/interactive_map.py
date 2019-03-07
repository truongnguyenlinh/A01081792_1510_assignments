# Linh Truong
# A01081792
# 03/06/2019


import doctest
from character import get_pokemon


def pokemon_map():
    """Interpret a square map with user location and available spots.

    PRECONDITION character must be a well-formed dictionary seen in get_pokemon

    >>> pokemon_map()
    P  X  X  X  X  X  X  X
    X  X  X  X  X  X  X  X
    X  X  X  X  X  X  X  X
    X  X  X  X  X  X  X  X
    X  X  X  X  X  X  X  X
    X  X  X  X  X  X  X  X
    X  X  X  X  X  X  X  X
    X  X  X  X  X  X  X  X
    """
    map_positions = [["X" for i in range(8)] for x in range(8)]

    pokemon_row = get_pokemon()["Position"][0]
    pokemon_column = get_pokemon()["Position"][1]
    map_positions[pokemon_column][pokemon_row] = "P"

    for row in map_positions:
        print("  ".join(row))


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
