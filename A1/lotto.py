# Linh Truong
# A01081792
# 01-25-2019


import random


def number_generator():
    """Generate a random six-digit number using numbers [1, 49].

    RETURN random 6-digit number from lowest to highest
    """
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
               11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
               21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
               31, 32, 33, 34, 35, 36, 37, 38, 49, 41,
               42, 43, 44, 45, 46, 47, 48, 49]

    random_integer = random.sample(my_list, 6)
    random_integer.sort()
    return random_integer


def main():
    """Execute the program."""
    print(number_generator())


if __name__ == '__main__':
    main()

