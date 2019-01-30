# Linh Truong
# A01081792
# 01-25-2019

RED = "red"
BLUE = "blue"
YELLOW = "yellow"

def colour_mixer():
    """Return colour mixture of two primary colours.
    """
    primary_1 = input("Enter a primary colour.").strip().lower()

    primary_2 = input("Enter a secondary primary colour.").strip().lower()

    if (primary_1 == RED) and (primary_2 == BLUE):
        print("purple")
    elif (primary_1 == BLUE) and (primary_2 == RED):
        print("purple")
    elif (primary_1  == RED) and (primary_2 == YELLOW):
        print("orange")
    elif (primary_1 == YELLOW) and (primary_2 == RED):
        print("orange")
    elif (primary_1  == YELLOW) and (primary_2 == BLUE):
        print("green")
    elif (primary_1 == BLUE) and (primary_2 == YELLOW):
        print("green")
    elif (primary_1 == RED) and (primary_2 == RED):
        print("First and second input colours are the same;unable to produce secondary colour.")
    elif (primary_1 == BLUE) and (primary_2 == BLUE):
        print("First and second input colours are the same;unable to produce secondary colour.")
    elif (primary_1 == YELLOW) and (primary_2 == YELLOW):
        print("First and second input colours are the same;unable to produce secondary colour.")
    else:
        print("The entered values are not a primary colour.")

def main():
    colour_mixer()

if __name__ == '__main__':
    main()