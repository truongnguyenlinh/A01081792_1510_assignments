import doctest


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b.

    RETURN the largest number that divides cleanly between a and b
    >>> gcd(1, 7)
    1
    >>> gcd(2, 4)
    2
    >>> gcd(10, 189)
    1"""
    if a == 0:
        raise ValueError("Please enter a non-zero integer!")
    else:
        if b == 0:
            return a
        else:
            return gcd(b, a % b)


def main():
    doctest.testmod()
    print(gcd(8, 7))
    print(gcd(2, 0))


if __name__ == '__main__':
    main()
