from unittest import TestCase
import dungeonsanddragons
import random


class TestGenerateName(TestCase):
    def test_generate_name_length(self):
        self.assertEqual(len(dungeonsanddragons.generate_name(3)), 6)

    def test_generate_name_type(self):
        self.assertEqual(type(dungeonsanddragons.generate_name(2)), str)

    def test_generate_name_random(self):
        random.seed(2)
        self.assertEqual(dungeonsanddragons.generate_name(2), "Cadi")

    def test_generate_name_alpha(self):
        dnd_name = dungeonsanddragons.generate_name(3)
        self.assertTrue(dnd_name.isalpha())

