def gcd(a: int, b: int):
    """Return the greatest common divisor of a and b.

    RETURN the largest number that divides cleanly between a and b """
    if a == 0:
        raise ValueError("Please enter a non-zero integer!")
    else:
        if (a > 0 or a < 0) and b == 0:
            return a
        else:
            return gcd(b, a % b)


def main():
    print(gcd(8, 7))
    print(gcd(2, 0))


if __name__ == '__main__':
    main()
