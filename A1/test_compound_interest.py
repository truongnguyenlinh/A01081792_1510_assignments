from unittest import TestCase
from A1 import compound_interest


class TestCompound_interest(TestCase):
    def test_compound_interest_small(self):
        self.assertEqual(0.0, compound_interest.compound_interest(0.0, 2.0, 1, 0))

    def test_compound_interest_mid(self):
        self.assertEqual(672.7500, compound_interest.compound_interest(100, 0.2, 2, 10))

    def test_compound_interest_large(self):
        self.assertEqual(2465.9344, compound_interest.compound_interest(600, 0.5, 4, 3))