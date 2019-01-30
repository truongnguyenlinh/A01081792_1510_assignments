# Linh Truong
# A01081792
# 01-25-2019


import random


def rock_paper_scissors():
    """
    Generate a game of rock, paper or scissors with the computer..
    """

    random_num = random.randint(0, 2)

    options = ['rock', 'paper', 'scissors']
    random_choice = options[random_num]

    guess = input("Rock, paper or scissors?").strip().lower()

    if (guess != "rock") and (guess != "paper") and (guess != "scissors"):
        print("Incorrect value entered.")
    elif (guess == "paper") and (random_choice == "rock"):
        print("The computer entered rock so you've won!")
    elif (guess == "scissors") and (random_choice == "paper"):
        print("The computer entered paper so you've won!")
    elif (guess == "rock") and (random_num == "scissors"):
        print("The computer entered scissors so you've won!")
    elif guess == random_choice:
        print("The computer also entered", random_choice, "so it was a tie.")
    else:
        print("The computer entered", random_choice, "so you've lost.")


def main():
    rock_paper_scissors()


if __name__ == '__main__':
    main()