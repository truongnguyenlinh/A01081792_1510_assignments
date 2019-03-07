# Linh Truong
# A01081792
# 03/06/2019


from unittest import TestCase
from pokemon import random_pokemon
import random


class TestRandomPokemon(TestCase):
    def test_random_pokemon_type(self):
        """Determine output type."""
        self.assertEqual(type(random_pokemon()), dict)

    def test_random_pokemon_length(self):
        """Determine output length."""
        self.assertEqual(len(random_pokemon()), 4)

    def test_random_pokemon_output(self):
        """Determine random dictionary output."""
        random.seed(2)
        self.assertEqual(random_pokemon(), {'Name': 'Pikachu', 'Class': 'Electric', 'Attack': 'Static', 'HP': 5})
        random.seed()

    def test_random_pokemon_key_str(self):
        """Determine key type."""
        key_only = random_pokemon().keys()
        for key in key_only:
            self.assertEqual(type(key), str)
