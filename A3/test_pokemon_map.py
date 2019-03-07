# Linh Truong
# A01081792
# 03/06/2019


import io
import unittest
from unittest.mock import patch
from unittest import TestCase
from interactive_map import pokemon_map


class TestPokemonMap(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_pokemon_map_output_type(self, mock_stdout):
        """Determine whether output is a string."""
        pokemon_map()
        self.assertEqual(type(mock_stdout.getvalue()), str)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_pokemon_map_output(self, mock_stdout):
        """Determine printed output from given character."""
        expected_output = "P  X  X  X  X  X  X  X\n"\
                          "X  X  X  X  X  X  X  X\n"\
                          "X  X  X  X  X  X  X  X\n"\
                          "X  X  X  X  X  X  X  X\n"\
                          "X  X  X  X  X  X  X  X\n"\
                          "X  X  X  X  X  X  X  X\n"\
                          "X  X  X  X  X  X  X  X\n"\
                          "X  X  X  X  X  X  X  X\n"
        pokemon_map()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
