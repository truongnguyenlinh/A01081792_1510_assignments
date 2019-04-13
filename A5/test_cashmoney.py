from unittest import TestCase
from q05 import cashmoney


class TestCashMoney(TestCase):
    def test_cashmoney_zero(self):
        self.assertEqual(cashmoney(0.0),
                         {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0})

    def test_cashmoney_type(self):
        self.assertIsInstance(cashmoney(87.5), dict)

    def test_cashmoney_large(self):
        self.assertEqual(cashmoney(1050),
                         {0.01: 0,
                          0.05: 0,
                          0.1: 0,
                          0.25: 0,
                          1: 0,
                          2: 0,
                          5: 0,
                          10: 0,
                          20: 0,
                          50: 1,
                          100: 10})

    def test_cash_money_error(self):
        with self.assertRaises(ValueError):
            cashmoney(-19)
