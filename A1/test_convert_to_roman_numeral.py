# Linh Truong
# A01081792
# 01-25-2019


from unittest import TestCase
from A1 import roman_numbers


class TestConvertToRomanNumeral(TestCase):

    def test_convert_to_roman_numeral_one(self):
        self.assertEqual("I", roman_numbers.convert_to_roman_numeral(1))

    def test_to_convert_to_roman_numeral_large(self):
        self.assertEqual("MMDLXXVIII", roman_numbers.convert_to_roman_numeral(2578))

    def test_to_convert_to_roman_numeral_greater_than_ten(self):
        self.assertEqual("LXXVI", roman_numbers.convert_to_roman_numeral(76))

    def test_to_convert_to_roman_numeral_mid(self):
        self.assertEqual("MMMMMMMMMM", roman_numbers.convert_to_roman_numeral(10000))

