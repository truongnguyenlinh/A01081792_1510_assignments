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

    pokemon_x = get_pokemon()["Position"][0]
    pokemon_y = get_pokemon()["Position"][1]
    map_positions[pokemon_y][pokemon_x] = "P"

    for row in map_positions:
        print("  ".join(row))


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
