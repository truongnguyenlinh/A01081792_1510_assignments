def dungeon_map(pokemon: dict):
    """Interpret a square map of potential positions which a user can move to.
    """
    map_positions = [["X", "X", "X", "X"],
                     ["X", "X", "X", "X"],
                     ["X", "X", "X", "X"],
                     ["X", "X", "X", "X"]]

    pokemon_x = pokemon["Position"][0]
    pokemon_y = pokemon["Position"][1]
    map_positions[pokemon_y][pokemon_x] = "P"

    for row in map_positions:
        print(" ".join(row))
