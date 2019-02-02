# Linh Truong
# A01081792
# 01-25-2019


def colour_mixer():
    """Return colour mixture of two primary colours.
    """
    primary_1 = input("Enter a primary colour.").strip().lower()

    primary_2 = input("Enter a secondary primary colour.").strip().lower()

    if (primary_1 == "red") and (primary_2 == "blue"):
        print("purple")
    elif (primary_1 == "blue") and (primary_2 == "red"):
        print("purple")
    elif (primary_1 == "red") and (primary_2 == "yellow"):
        print("orange")
    elif (primary_1 == "yellow") and (primary_2 == "red"):
        print("orange")
    elif (primary_1 == "yellow") and (primary_2 == "blue"):
        print("green")
    elif (primary_1 == "blue") and (primary_2 == "yellow"):
        print("green")
    elif (primary_1 == "red") and (primary_2 == "red"):
        print("First and second input colours are the same;unable to produce secondary colour.")
    elif (primary_1 == "blue") and (primary_2 == "blue"):
        print("First and second input colours are the same;unable to produce secondary colour.")
    elif (primary_1 == "yellow") and (primary_2 == "yellow"):
        print("First and second input colours are the same;unable to produce secondary colour.")
    else:
        print("The entered values are not a primary colour.")


def main():
    """Execute the program."""
    colour_mixer()


if __name__ == '__main__':
    main()

