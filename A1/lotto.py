# Linh Truong
# A01081792
# 01-25-2019


import random


def number_generator():
    """Generate a random six-digit number using numbers [1, 49].

    RETURN random 6-digit number from lowest to highest
    """

    random_integer = random.sample(range(1, 50), 6)
    random_integer.sort()
    return random_integer


def main():
    print(number_generator())


if __name__ == '__main__':
    main()