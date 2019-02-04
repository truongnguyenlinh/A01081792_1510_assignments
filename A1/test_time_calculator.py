# Linh Truong
# A01081792
# 01-25-2019


from unittest import TestCase
import time_calculator


class TestTimeCalculator(TestCase):
    """Convert seconds only."""
    def test_time_calculator_one(self):
        self.assertEqual([0, 0, 0, 1], time_calculator.time_calculator(1))

    def test_time_calculator_min(self):
        """Convert seconds and minutes only."""
        self.assertEqual([0, 0, 3, 5], time_calculator.time_calculator(185))

    def test_time_calculator_mid(self):
        """Convert seconds, minutes and hours only."""
        self.assertEqual([0, 2, 26, 5], time_calculator.time_calculator(8765))

    def test_time_calculator_large(self):
        """Convert seconds, minutes, hours and days only."""
        self.assertEqual([11, 10, 14, 24], time_calculator.time_calculator(987264))

