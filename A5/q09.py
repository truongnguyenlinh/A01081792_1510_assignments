import doctest


def base_conversion(org_num: int, org_base: int, dest_base: int) -> int:
    """Convert a decimal number to a 4-digit number in a different base within {0,9}.

    PRECONDITION org_base must be a base number from 2-10
    PRECONDITION org_num must be a positive integer
    PRECONDITION dest_base must be a base number from 2-10
    RETURN the new value as an integer
    >>> base_conversion(23, 4, 7)
    14
    >>> base_conversion(3, 10, 2)
    11
    >>> base_conversion(10, 10, 9)
    11"""
    result = ""
    try:
        dec_num = int(str(org_num), org_base)
        while dec_num > 0:
            result += str(dec_num % dest_base)
            dec_num //= dest_base
        return int(result[::-1]) if result != '' else 0
    except ValueError:
        print("The number entered is cannot be converted!")


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
