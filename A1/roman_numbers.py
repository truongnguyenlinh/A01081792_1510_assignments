# Linh Truong
# A01081792
# 01-25-2019


import doctest


def convert_to_roman_numeral(positive_int):
    """Return given integer as a Roman Numeral.

    PARAM positive_int: integer
    PRECONDITION positive_int: must be in range [1, 10_000]
    POST-CONDITION: calculate roman numeral equivalent
    RETURN roman numeral equivalent as a string
    >>> convert_to_roman_numeral(67)
    'LXVII'
    >>> convert_to_roman_numeral(9999)
    'MMMMMMMMMCMXCIX'
    """

    if not (10000 >= positive_int) and (positive_int > 0):
        return "The value entered is not between 0 and 10001."
    else:
        roman_m = (positive_int // 1000) * "M"
        positive_int = positive_int % 1000

        roman_cm = (positive_int // 900) * "CM"
        positive_int = positive_int % 900

        roman_d = (positive_int // 500) * "D"
        positive_int = positive_int % 500

        roman_cd = (positive_int // 400) * "CD"
        positive_int = positive_int % 400

        roman_c = (positive_int // 100) * "C"
        positive_int = positive_int % 100

        roman_xc = (positive_int // 90) * "XC"
        positive_int = positive_int % 90

        roman_l = (positive_int // 50) * "L"
        positive_int = positive_int % 50

        roman_xl = (positive_int // 40) * "XL"
        positive_int = positive_int % 40

        roman_x = (positive_int // 10) * "X"
        positive_int = positive_int % 10

        roman_ix = (positive_int // 9) * "IX"
        positive_int = positive_int % 9

        roman_v = (positive_int // 5) * "V"
        positive_int = positive_int % 5

        roman_iv = (positive_int // 4) * "IV"
        positive_int = positive_int % 4

        roman_i = (positive_int // 1) * "I"

        return(roman_m + roman_cm + roman_d + roman_cd + roman_c
              + roman_xc + roman_l + roman_xl + roman_x + roman_ix +
               roman_v + roman_iv + roman_i)


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()

