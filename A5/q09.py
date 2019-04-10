def base_conversion(org_num: int, org_base: int, dest_base: int) -> int:
    """Convert a decimal number to a 4-digit number in a different base within {0,9}.

    RETURN the new value as an integer"""
    dec_num = int(str(org_num), org_base)
    result = ""

    while dec_num > 0:
        result += str(dec_num % dest_base)
        dec_num //= dest_base
    return int(result[::-1])


def main():
    print(base_conversion(23, 4, 2))


if __name__ == "__main__":
    main()
