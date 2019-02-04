# Linh Truong
# A01081792
# 01-25-2019


from unittest import TestCase
import roman_numbers


class TestConvertToRomanNumeral(TestCase):

    def test_convert_to_roman_numeral_one(self):
        """Produce equivalent Roman Numeral of number 1."""
        self.assertEqual("I", roman_numbers.convert_to_roman_numeral(1))

    def test_to_convert_to_roman_numeral_large(self):
        """Produce equivalent Roman Numeral of number 2578."""
        self.assertEqual("MMDLXXVIII", roman_numbers.convert_to_roman_numeral(2578))

    def test_to_convert_to_roman_numeral_greater_than_ten(self):
        """Produce equivalent Roman Numeral of number 76."""
        self.assertEqual("LXXVI", roman_numbers.convert_to_roman_numeral(76))

    def test_to_convert_to_roman_numeral_mid(self):
        """Produce equivalent Roman Numeral of number 10000."""
        self.assertEqual("MMMMMMMMMM", roman_numbers.convert_to_roman_numeral(10000))

