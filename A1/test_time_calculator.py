from unittest import TestCase
from A1 import time_calculator

class TestTime_calculator(TestCase):
    def test_time_calculator_one(self):
        self.assertEqual([1], time_calculator.time_calculator(1))

    def test_time_calculator_large(self):
        self.assertEqual([11, 10, 14, 24], time_calculator.time_calculator(987264))

    def test_time_calculator_mid(self):
        self.assertEqual([2, 26, 5], time_calculator.time_calculator(8765))

