import doctest


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b.

    RETURN the largest number that divides cleanly between a and b
    >>> gcd(0, 0)
    0
    >>> gcd(0, 4)
    4
    >>> gcd(10, 189)
    1
    >>> gcd(56, 0)
    56"""
    try:
        a % b
    except ZeroDivisionError:
        return a
    else:
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
