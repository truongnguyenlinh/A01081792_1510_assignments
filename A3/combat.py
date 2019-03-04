import random
import doctest
from global_helper import user_input_type, roll_die


def combat_round(pokemon: dict, opponent: dict):
    """Determine the amount of damage between two opponents.

    PRECONDITION pokemon: must be a well-formed dictionary from character
    PRECONDITION opponent: must be a well-formed dictionary from random_pokemon

    >>> random.seed(3)
    >>> combat_round({"Name": "Tyson", "Class": "Squirtle", "Position": [0, 0], "HP": 10}, \
    {'Name': 'Palkia', 'Class': 'Water', 'Attack': 'Pressure', 'HP': 5})
    You attacked Palkia with a slap and he took 2 damage.
    Palkia attacked you with Pressure and you took 5 damage.
    You attacked Palkia with a slap and he took 5 damage.
    Success! Your opponent has fainted and you gained 20 prize dollars from your battle.
    <BLANKLINE>
    >>> combat_round({"Name": "Angus", "Class": "Bulbasaur", "Position": [3, 1], "HP": 6}, \
    {"Name": "Dragonite", "Class": "Dragon", "Attack": "Inner Focus", "HP": 5})
    You attacked Dragonite with a slap and he took 3 damage.
    Dragonite attacked you with Inner Focus and you took 5 damage.
    You attacked Dragonite with a slap and he took 4 damage.
    Success! Your opponent has fainted and you gained 20 prize dollars from your battle.
    <BLANKLINE>
    >>> random.seed()
    """
    pokemon_attack = roll_die(1, 6)
    opponent_attack = roll_die(1, 6)

    if opponent["HP"] > 0:
        opponent["HP"] -= pokemon_attack
        print("You attacked %s with a slap and he took %s damage." % (opponent["Name"], pokemon_attack))
        if opponent["HP"] <= 0:
            print("Success! Your opponent has fainted and you gained 20 prize dollars from your battle.\n")

    if opponent["HP"] <= 0:
        return None

    if pokemon["HP"] > 0:
        pokemon["HP"] -= opponent_attack
        print("%s attacked you with %s and you took %s damage."
              % (opponent["Name"], opponent["Attack"], opponent_attack))
        if pokemon["HP"] <= 0:
            print("You fainted. Try again next time!")
            exit()

    while True:
        return combat_round(pokemon, opponent)


def potential_attack(pokemon: dict, opponent: dict):
    """Determine whether opponent will do damage to user.

    PRECONDITION pokemon: must be a well-formed dictionary from character
    PRECONDITION opponent: must be a well-formed dictionary from random_pokemon

    >>> random.seed(31)
    >>> potential_attack({"Name": "Char", "Class": "Charmander", "Position": [2, 2], "HP": 8}, \
    {"Name": "Pikachu", "Class": "Electric", "Attack": "Static", "HP": 5})
    Despite fleeing, Pikachu still attacked you! He inflicted you by 4 damage.
    >>> potential_attack({"Name": "Ben", "Class": "Squirtle", "Position": [1, 0], "HP": 5}, \
    {"Name": "Pikachu", "Class": "Electric", "Attack": "Static", "HP": 5})
    You fled successfully!
    >>> random.seed()
    """

    opponent_probability_attack = roll_die(1, 10)
    opponent_attack = roll_die(1, 4)

    if opponent_probability_attack == 1:
        pokemon["HP"] -= opponent_attack
        print("Despite fleeing, %s still attacked you! He inflicted you by %s damage."
              % (opponent["Name"], opponent_attack))
    else:
        print("You fled successfully!")


def fight_flee(pokemon: dict, opponent: dict):
    """Determine whether opponent will fight or flee.

    PRECONDITION pokemon: must be a well-formed dictionary from character
    PRECONDITION opponent: must be a well-formed dictionary from random_pokemon
    """
    encounter_percentage = roll_die(1, 10)
    if encounter_percentage == 1:
        print("You encountered another Pokemon!")
        user_input = user_input_type("Would you like to fight or flee?\n")

        while user_input.strip().title() != "Fight" and user_input.strip().title() != "Flee":
            print("Was that in Pokemon language? I couldn't understand that!")
            user_input = user_input_type("Would you like to fight or flee?\n")

        if user_input.strip().title() == "Fight":
            print("%s | HP: %s \nYou encountered %s! It's time for a Poke-Battle.\n"
                  % (opponent["Name"], opponent["HP"], opponent["Name"]))
            combat_round(pokemon, opponent)
        elif user_input.strip().title() == "Flee":
            potential_attack(pokemon, opponent)


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
