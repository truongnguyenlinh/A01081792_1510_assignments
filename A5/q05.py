def cashmoney(double: float):
    """Determines the fewest of each bill and coin from given float."""
    cash_dict = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 3}
    for i in cash_dict.keys():
        if double // i != 0:
            cash_dict[i] = double // i
            double %= i
    return cash_dict


def main():
    print(cashmoney(66.53))


if __name__ == '__main__':
    main()
