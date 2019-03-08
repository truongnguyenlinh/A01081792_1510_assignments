# Linh Truong
# A01081792
# 03/06/2019


import doctest
from character import get_row, get_column


def pokemon_map():
    """Interpret a square map with user location and available spots.

    >>> pokemon_map()
    🐱  🌲  🌲  🌲  🌲  🌲  🌲  🌲
    🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲
    🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲
    🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲
    🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲
    🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲
    🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲
    🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲
    """
    map_positions = [["🌲" for i in range(8)] for x in range(8)]

    pokemon_row = get_row()
    pokemon_column = get_column()
    map_positions[pokemon_column][pokemon_row] = "🐱"

    for row in map_positions:
        print("  ".join(row))


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
