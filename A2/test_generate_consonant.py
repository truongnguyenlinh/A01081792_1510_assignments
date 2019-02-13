from unittest import TestCase
import random
import dungeonsanddragons


class TestGenerateConsonant(TestCase):
    def test_generate_consonant(self):
        consonant_letters = 'bcdfghjklmnpqrstvwxyz'
        self.assertIn(dungeonsanddragons.generate_consonant(), consonant_letters)

    def test_generate_consonant_length(self):
        self.assertEqual(len(dungeonsanddragons.generate_consonant()), 1)

    def test_generate_consonant_type(self):
        self.assertEqual(type(dungeonsanddragons.generate_consonant()), str)

    def test_generate_vowel_alpha(self):
        dnd_consonant = dungeonsanddragons.generate_consonant()
        self.assertTrue(dnd_consonant.isalpha())

    def test_generate_vowel_random(self):
        random.seed(3)
        fixed = dungeonsanddragons.generate_consonant()
        self.assertEqual("k", fixed)

