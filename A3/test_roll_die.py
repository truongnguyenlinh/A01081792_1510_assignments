# Linh Truong
# A01081792
# 03/06/2019


from unittest import TestCase
from global_helper import roll_die
import random


class TestRollDie(TestCase):
    def test_roll_die_output_type(self):
        """Determine output type."""
        self.assertEqual(type(roll_die(1, 6)), int)

    def test_roll_die_both_zero(self):
        """Determine output when both parameters are 0."""
        self.assertEqual(roll_die(0, 0), 0)

    def test_roll_die_zero_sides(self):
        """Determine output when number_of_sides is 0."""
        self.assertEqual(roll_die(4, 0), 0)

    def test_roll_die_zero_rolls(self):
        """Determine output when number_of_rolls is 0."""
        self.assertEqual(roll_die(0, 8), 0)

    def test_roll_die_random_output(self):
        """Determine random output."""
        random.seed(56)
        self.assertEqual(roll_die(8, 100), 581)
        random.seed()

    def test_roll_die_range_max(self):
        """Determine output is less than or equal to max."""
        self.assertLessEqual(roll_die(1, 8), 8)

    def test_roll_die_min(self):
        """Determine output is greater than or equal to min."""
        self.assertGreaterEqual(roll_die(1, 103), 1)
