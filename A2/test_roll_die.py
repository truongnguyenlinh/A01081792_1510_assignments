from unittest import TestCase
import random
import dungeonsanddragons


class TestRollDie(TestCase):
    def test_roll_die_type(self):
        with self.assertRaises(TypeError):
            dungeonsanddragons.roll_die('', '')

    def test_roll_die_type_rolls(self):
        with self.assertRaises(TypeError):
            dungeonsanddragons.roll_die('', 4)

    def test_roll_die_type_sides(self):
        with self.assertRaises(TypeError):
            dungeonsanddragons.roll_die(3, '')

    def test_roll_die_integer(self):
        self.assertEqual(0, dungeonsanddragons.roll_die(0, 0))

    def test_roll_die_integers(self):
        random.seed(1)
        self.assertEqual(3, dungeonsanddragons.roll_die(2, 3))
        random.seed()

    def test_roll_die_integers_seed(self):
        random.seed(1)
        self.assertEqual(12, dungeonsanddragons.roll_die(4, 10))
        random.seed()

    def test_roll_die_range_max(self):
        self.assertLessEqual(dungeonsanddragons.roll_die(2, 3), 6)

    def test_roll_die_min(self):
        self.assertGreaterEqual(dungeonsanddragons.roll_die(2, 3), 2)

