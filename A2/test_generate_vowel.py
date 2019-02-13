from unittest import TestCase
import random
import dungeonsanddragons


class TestGenerateVowel(TestCase):
    def test_generate_vowel(self):
        vowel_letters = 'aeiouy'
        self.assertIn(dungeonsanddragons.generate_vowel(), vowel_letters)

    def test_generate_vowel_length(self):
        self.assertEqual(len(dungeonsanddragons.generate_vowel()), 1)

    def test_generate_vowel_type(self):
        self.assertEqual(type(dungeonsanddragons.generate_vowel()), str)

    def test_generate_vowel_alpha(self):
        dnd_vowel = dungeonsanddragons.generate_vowel()
        self.assertTrue(dnd_vowel.isalpha())

    def test_generate_vowel_random(self):
        random.seed(3)
        fixed = dungeonsanddragons.generate_vowel()
        self.assertEqual("e", fixed)

