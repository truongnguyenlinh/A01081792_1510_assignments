from unittest import TestCase
from q09 import base_conversion
from unittest.mock import patch
import io


class TestBaseConversion(TestCase):
    def test_base_conversion_type(self):
        self.assertIsInstance(base_conversion(2, 10, 8), int)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_base_conversion_error(self, mock_stdout):
        expected = "The number entered is cannot be converted!\n"
        base_conversion(27, 4, 10)
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_base_conversion_same_base(self):
        self.assertEqual(base_conversion(80, 10, 10), 80)

    def test_base_conversion_low_high(self):
        self.assertEqual(base_conversion(67, 10, 2), 1000011)

    def test_base_conversion_high_low(self):
        self.assertEqual(base_conversion(1234, 9, 2), 1110011010)

    def test_base_conversion_zero_same(self):
        self.assertEqual(base_conversion(0, 10, 10), 0)

    def test_base_conversion_zero_high_low(self):
        self.assertEqual(base_conversion(0, 9, 4), 0)

    def test_base_conversion_zero_low_high(self):
        self.assertEqual(base_conversion(0, 3, 8), 0)
