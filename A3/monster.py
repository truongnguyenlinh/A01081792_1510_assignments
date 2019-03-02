import random


def random_pokemon():
    """Return a dictionary of a random Pokemon."""
    pokemon_1 = {"Name": "Pikachu", "Class": "Electric", "HP": 5}
    pokemon_2 = {"Name": "Marowak", "Class": "Ground", "HP": 5}
    pokemon_3 = {"Name": "Dragonite", "Class": "Dragon", "HP": 5}
    pokemon_4 = {"Name": "Palkia", "Class": "Water", "HP": 5}
    lop = [pokemon_1, pokemon_2, pokemon_3, pokemon_4]
    return random.choice(lop)
