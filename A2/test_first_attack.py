from unittest import TestCase
import dungeonsanddragons
import random


class TestFirstAttack(TestCase):
    def test_first_attack_type(self):
        self.assertEqual(type(dungeonsanddragons.first_attack()), bool)

    def test_first_attack_true(self):
        random.seed(3)
        self.assertEqual(dungeonsanddragons.first_attack(), False)

    def test_first_attack_false(self):
        random.seed(6)
        self.assertEqual(dungeonsanddragons.first_attack(), True)

