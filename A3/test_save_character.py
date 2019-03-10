# Linh Truong
# A01081792
# 03/06/2019


from unittest import TestCase
import character
import json
import os


class TestSaveCharacter(TestCase):
    def setUp(self):
        """Global variable pokemon setup for unit testing."""
        character.pokemon = {"Name": "Tyson", "Class": "Bulbasaur", "Position": [0, 3], "HP": 7}

    def test_save_character_file_exists(self):
        """Assert that file exists."""
        self.assertTrue(os.path.isfile('./character.json'))

    def test_save_character_read(self):
        """Assert contents are the same and are readable."""
        with open('character.json') as file_object:
            file_info = json.load(file_object)
        self.assertEqual(file_info, character.pokemon)
