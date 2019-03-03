import random
from global_helper import user_input_type, roll_die


def combat_round(pokemon: dict, opponent: dict):
    """Determine the amount of damage between two opponents.

    PRECONDITION pokemon: must be a well-formed dictionary from character
    PRECONDITION opponent: must be a well-formed dictionary from random_monster
    """
    pokemon_attack = roll_die(1, 6)
    opponent_attack = roll_die(1, 6)

    if opponent["HP"] > 0:
        opponent["HP"] -= pokemon_attack
        print("You attacked %s with a slap and he took %s damage." % (opponent["Name"], pokemon_attack))
        if opponent["HP"] <= 0:
            print("Success! Your opponent has died and you gained 20 prize dollars from your battle.")

    if opponent["HP"] <= 0:
        return None

    if pokemon["HP"] > 0:
        pokemon["HP"] -= opponent_attack
        print("%s attacked you with %s and you took %s damage."
              % (opponent["Name"], opponent["Attack"], opponent_attack))
        if pokemon["HP"] <= 0:
            print("You died. Try again next time!")
            exit()

    while True:
        return combat_round(pokemon, opponent)


def potential_attack(pokemon: dict, opponent: dict):
    opponent_probability_attack = (1, 10)
    opponent_attack = roll_die(1, 4)

    if opponent_probability_attack == 1:
        pokemon["HP"] -= opponent_attack
        print("Despite fleeing, %s still attacked you! He inflicted you by %s damage."
              % (opponent["Name"], opponent_attack))


def fight_flee(pokemon: dict, opponent: dict):
    """Determine whether opponent will fight or flee.
    """
    encounter_percentage = random.randint(1, 10)
    if encounter_percentage == 1:
        print("You encountered another Pokemon!")
        user_input = user_input_type("Would you like to fight or flee?\n")

        while user_input.strip().title() != "Fight" and user_input.strip().title() != "Flee":
            print("Was that in Pokemon language? I couldn't understand that!")
            user_input = user_input_type("Would you like to fight or flee?\n")

        if user_input.strip().title() == "Fight":
            print("You encountered %s! It's time for a Poke-Battle." % opponent["Name"])
            combat_round(pokemon, opponent)
        elif user_input.strip().title() == "Flee":
            potential_attack(pokemon, opponent)
