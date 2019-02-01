# Linh Truong
# A01081792
# 01-25-2019


from unittest import TestCase
from A1 import lotto


class TestNumberGenerator(TestCase):
    def test_number_generator_length(self):
        self.assertEqual(6, len(lotto.number_generator()))

    def test_number_generator_integer_true(self):
        self.assertTrue(type(lotto.number_generator()[0]) is int)
        self.assertTrue(type(lotto.number_generator()[1]) is int)
        self.assertTrue(type(lotto.number_generator()[2]) is int)
        self.assertTrue(type(lotto.number_generator()[3]) is int)
        self.assertTrue(type(lotto.number_generator()[4]) is int)
        self.assertTrue(type(lotto.number_generator()[5]) is int)

    def test_number_generator_range(self):
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                   11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                   21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                   31, 32, 33, 34, 35, 36, 37, 38, 49, 41,
                   42, 43, 44, 45, 46, 47, 48, 49]

        lotto_one = lotto.number_generator()[0]
        lotto_two = lotto.number_generator()[1]
        lotto_three = lotto.number_generator()[2]
        lotto_four = lotto.number_generator()[3]
        lotto_five = lotto.number_generator()[4]
        lotto_six = lotto.number_generator()[5]

        self.assertTrue(lotto_one in my_list)
        self.assertTrue(lotto_two in my_list)
        self.assertTrue(lotto_three in my_list)
        self.assertTrue(lotto_four in my_list)
        self.assertTrue(lotto_five in my_list)
        self.assertTrue(lotto_six in my_list)

    def test_number_generator_unique(self):
        lotto_number = lotto.number_generator()

        lotto_one = lotto.number_generator()[0]
        lotto_two = lotto.number_generator()[1]
        lotto_three = lotto.number_generator()[2]
        lotto_four = lotto.number_generator()[3]
        lotto_five = lotto.number_generator()[4]
        lotto_six = lotto.number_generator()[5]

        self.assertTrue(1, lotto_number.count(lotto_one))
        self.assertTrue(1, lotto_number.count(lotto_two))
        self.assertTrue(1, lotto_number.count(lotto_three))
        self.assertTrue(1, lotto_number.count(lotto_four))
        self.assertTrue(1, lotto_number.count(lotto_five))
        self.assertTrue(1, lotto_number.count(lotto_six))

