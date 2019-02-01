# Linh Truong
# A01081792
# 01-25-2019


from unittest import TestCase
from A1 import compound_interest


class TestCompoundInterest(TestCase):
    def test_compound_interest_small(self):
        self.assertEqual(10.0, compound_interest.compound_interest(10, 2.0, 1, 0))

    def test_compound_interest_mid(self):
        self.assertEqual(672.7499949325611, compound_interest.compound_interest(100, 0.2, 2, 10))

    def test_compound_interest_large(self):
        self.assertEqual(2465.934403715073, compound_interest.compound_interest(600, 0.5, 4, 3))

    def test_compound_interest_zero(self):
        self.assertRaises(ZeroDivisionError)

