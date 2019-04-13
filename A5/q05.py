import doctest


def cashmoney(double: float) -> dict:
    """Determines the fewest of each bill and coin from given float.

    PRECONDITION double is a positive float
    >>> cashmoney(66.53)
    {100: 0, 50: 1.0, 20: 0, 10: 1.0, 5: 1.0, 2: 0, 1: 1.0, 0.25: 2.0, 0.1: 0, 0.05: 0, 0.01: 3.0}
    >>> cashmoney(0.0)
    {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0}
    >>> cashmoney(27)
    {100: 0, 50: 0, 20: 1, 10: 0, 5: 1, 2: 1, 1: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0}
    """
    cash_dict = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
    if double < 0:
        raise ValueError("Please enter a positive floating point number")
    else:
        for i in cash_dict.keys():
            if double // i != 0:
                cash_dict[i] = double // i
                double %= i
        return cash_dict


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
