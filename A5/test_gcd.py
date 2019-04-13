from unittest import TestCase
from q02 import gcd


class TestGcd(TestCase):
    def test_gcd_zero_type(self):
        self.assertIsInstance(gcd(8, 10), int)

    def test_gcd_zero(self):
        self.assertEqual(gcd(0, 0), 0)

    def test_gcd_zero_b(self):
        self.assertEqual(gcd(0, 9), 9)

    def test_gcd_zero_a(self):
        self.assertEqual(gcd(101, 0), 101)

    def test_gcd_primes(self):
        self.assertEqual(gcd(11, 7), 1)

    def test_gcd_evens(self):
        self.assertEqual(gcd(2, 10), 2)
