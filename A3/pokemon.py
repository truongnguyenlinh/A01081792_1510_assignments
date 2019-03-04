import random


def random_pokemon() -> dict:
    """Return a dictionary of a random Pokemon.

    >>> random.seed(7)
    >>> random_pokemon()
    {'Name': 'Dragonite', 'Class': 'Dragon', 'Attack': 'Inner Focus', 'HP': 5}
    >>> random_pokemon()
    {'Name': 'Marowak', 'Class': 'Ground', 'Attack': 'Rock Head', 'HP': 5}
    >>> random_pokemon()
    {'Name': 'Palkia', 'Class': 'Water', 'Attack': 'Pressure', 'HP': 5}
    >>> random.seed()
    """
    pokemon_1 = {"Name": "Pikachu", "Class": "Electric", "Attack": "Static", "HP": 5}
    pokemon_2 = {"Name": "Marowak", "Class": "Ground", "Attack": "Rock Head", "HP": 5}
    pokemon_3 = {"Name": "Dragonite", "Class": "Dragon", "Attack": "Inner Focus", "HP": 5}
    pokemon_4 = {"Name": "Palkia", "Class": "Water", "Attack": "Pressure", "HP": 5}
    lop = [pokemon_1, pokemon_2, pokemon_3, pokemon_4]
    return random.choice(lop)
