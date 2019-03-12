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
        """Assert that output is a string."""
        pokemon_map()
        self.assertEqual(type(mock_stdout.getvalue()), str)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_pokemon_map_output(self, mock_stdout):
        """Assert printed output from given character."""
        expected_output = "🐱  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n"\
                          "🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n"\
                          "🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n"\
                          "🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n"\
                          "🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n"\
                          "🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n"\
                          "🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n"\
                          "🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n"
        pokemon_map()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
