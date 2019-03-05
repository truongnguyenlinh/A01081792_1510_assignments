import io
import unittest
from unittest.mock import patch
from unittest import TestCase
from interactive_map import pokemon_map


class TestPokemonMap(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_pokemon_map_output_type(self, mock_stdout):
        """Determine whether output is a string."""
        pokemon = {"Name": "Walter", "Class": "Charmander", "Position": [3, 1], "HP": 7}
        pokemon_map(pokemon)
        self.assertEqual(type(mock_stdout.getvalue()), str)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_pokemon_map_output(self, mock_stdout):
        """Determine printed output from given character."""
        pokemon = {"Name": "Eggus", "Class": "Bulbasaur", "Position": [2, 1], "HP": 5}
        expected_output = expected_output = "X X X X\n"\
                                            "X X P X\n"\
                                            "X X X X\n"\
                                            "X X X X\n"
        pokemon_map(pokemon)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
