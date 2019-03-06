from unittest import TestCase
from character import get_pokemon, pokemon


class TestGetPokemon(TestCase):
    """Function returns a dictionary."""
    def test_get_pokemon_type(self):
        self.assertEqual(type(get_pokemon()), dict)

    def test_get_pokemon_len(self):
        """Function returns global variable with initial length of 2."""
        self.assertEqual(len(get_pokemon()), 2)

    def test_get_pokemon_same_player(self):
        """Function returns original global variable."""
        self.assertEqual(get_pokemon(), pokemon)

