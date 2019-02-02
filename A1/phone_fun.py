# Linh Truong
# A01081792
# 01-25-2019


def number_translator():
    """Return string of translated character-given phone number.

    RETURN string of numbers
    """
    letters = "ABCDEFGHIJKLMNOPQRSTUVQXYZ"
    numbers_index = "22233344455566677778889999"

    number_entered = input("Enter a phone number in format XXX-XXX-XXXX.").strip().upper()

    if len(number_entered) != 12:
        print("Please re-enter a phone number in format XXX-XXX-XXXX.")
    else:
        map_letters_numbers = number_entered.maketrans(letters, numbers_index)
        # Maketrans built-in maps letters to numbers_index.
        # Strings must be of equal length in order to map.
        return number_entered.translate(map_letters_numbers)
        # Translate returns the number_index mapped to letters.


def main():
    """Execute the program."""
    print(number_translator())


if __name__ == '__main__':
    main()

