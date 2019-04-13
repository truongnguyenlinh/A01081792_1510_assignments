from unittest import TestCase
from q01 import sum_of_primes


class TestSumOfPrimes(TestCase):
    def test_sum_of_primes_type(self):
        self.assertIsInstance(sum_of_primes(0), int)

    def test_sum_of_primes_error(self):
        with self.assertRaises(ValueError):
            sum_of_primes(-1)

    def test_sum_of_primes_large(self):
        self.assertEqual(sum_of_primes(10100), 5847047)

    def test_sum_of_primes_small(self):
        self.assertEqual(sum_of_primes(5), 10)

    def test_sum_of_primes_mid(self):
        self.assertEqual(sum_of_primes(100), 1060)
