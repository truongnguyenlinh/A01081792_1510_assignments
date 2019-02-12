# Linh Truong
# A01081792
# 02/05/2019


import random


def roll_die(number_of_rolls, number_of_sides):
    """Return the random number after given number of rolls of a die.

    Range of potential output is determined by number_of_rolls and number_of_sides.
    PARAM number_of_rolls is an int
    PARAM number_of_sides is an int
    PRECONDITION number_of_rolls is a positive int
    PRECONDITION number_of_sides is a positive int
    """
    total = random.randint(1 * number_of_rolls, number_of_sides * number_of_rolls)

    if number_of_rolls == 0 or number_of_sides == 0:
        return 0
    else:
        return total


def generate_vowel():
    """Return a randomly selected vowel letter.

    RETURN random vowel from vowel letters"""
    vowel_letters = 'aeiouy'
    return random.choice(vowel_letters)


def generate_consonant():
    """Return a randomly selected consonant letter.

    RETURN random vowel from consonant letters
    """
    consonant_letters = 'bcdfghjklmnpqrstvwxyz'
    return random.choice(consonant_letters)


def generate_syllables():
    """Return one consonant and one vowel letter, concatenated.

    RETURN a string of two characters
    """
    return generate_consonant() + generate_vowel()


def generate_name(syllables):
    """Return string of concatenated syllables.

    PARAM syllables a positive integer
    PRECONDITION syllables must be a positive non-zero integer
    RETURN string composed of specified number of syllables
    """
    name = ""
    for num in range(syllables):
        name += generate_syllables()
    return name.title()


def choose_inventory(inventory, selection):
    """Return a sorted list of random elements in a list.

    PARAM inventory is a list
    PARAM selection is an int
    PRECONDITION inventory must be a list
    PRECONDITION selection must be a positive integer
    RETURN sorted list
    """
    items = ["Armor", "Shield", "Consumables", "Weapons",
             "Gear", "Tools", "Wands", "Gold"]

    if (inventory is list()) or (selection == 0):
        return []
    elif selection < 0:
        print('Error: Selection must be a positive integer.')
        return None
    elif selection > len(inventory):
        print('Error: Not enough elements in list to select.')
        return None
    elif selection == len(inventory):
        return {"Inventory": sorted(items[:])}
    else:
        return {"Inventory": random.sample(sorted(items[:]), selection)}


def class_list():
    """Provide a dictionary of classes with roll die for user to choose from.

    RETURN dictionary of all classes and values
    """
    return {"barbarian": 12, "bard": 8, "cleric": 8, "druid": 8, "fighter": 10, "monk": 8, "paladin": 10,
            "ranger": 10, "rogue": 8, "sorcerer": 6, "warlock": 8, "wizard": 6, "blood hunter": 10}


def class_selection():
    """Gather class input from user from class_list dictionary.

    RETURN class string if input is in dictionary keys
    """
    class_input = str(input("Select one of the following classes: Barbarian, Bard, Cleric, Druid, \n"
                            "Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard, Blood Hunter")).strip().lower()
    if class_input not in class_list().keys():
        print("Error: please select from classes provided")
        return None
    else:
        return class_input


def create_character(syllable):
    """Return name, with given syllables.

    PARAM syllables is an int
    PRECONDITION syllables is a positive, non-zero integer
    RETURN string with syllable number
    """
    # items = ["armor", "shield", "consumables", "weapons",
    #          "gear", "tools", "wands", "gold"]

    character = {"Name": generate_name(syllable)}

    strength = {'Strength': roll_die(3, 6)}
    dexterity = {'Dexterity': roll_die(3, 6)}
    constitution = {'Constitution': roll_die(3, 6)}
    intelligence = {'Intelligence': roll_die(3, 6)}
    wisdom = {'Wisdom': roll_die(3, 6)}
    charisma = {'Charisma': roll_die(3, 6)}

    character.update({"Class": class_selection()})
    character.update({"HP": random.randint(1, class_list()[character['Class']])})
    character.update(strength)
    character.update(dexterity)
    character.update(constitution)
    character.update(intelligence)
    character.update(wisdom)
    character.update(charisma)
    character.update({"XP": 0})
    character.update({"Inventory": []})

    if syllable < 0:
        print('Error: Given length must be a positive, non-zero integer.')
        return None
    else:
        return character


def combat_round(opponent_one, opponent_two):
    """Produce a single round of combat between two characters.

    PARAM opponent_one: a dictionary
    PARAM opponent_two: a dictionary
    PRECONDITION opponent_one: must be a well-formed dictionary with correct character
    PRECONDITION opponent_two: must be a well-formed dictionary with correct character
    """
    opponent_one_roll = random.randint(1, 20)
    opponent_two_roll = random.randint(1, 20)

    if opponent_one_roll == opponent_two_roll:
        combat_round(opponent_one, opponent_two)
        print("Both opponents missed!")
        return None

    if opponent_one_roll > opponent_two_roll:
        attacker = opponent_one
        victim = opponent_two
    else:
        attacker = opponent_two
        victim = opponent_one

    if random.randint(1, 20) > victim['Dexterity']:
        damage = random.randint(1, random.randint(1, class_list()[attacker['Class']]))
        victim['HP'] -= damage
        print(attacker['Name'], "hit", victim['Name'], "a total of", damage, "and",
              victim['Name'], "now has HP of", victim['HP'])
        return None
    else:
        damage = random.randint(1, random.randint(1, class_list()[victim['Class']]))
        attacker['HP'] -= damage
        print(victim['Name'], "hit", attacker['Name'], "a total of", damage, "and",
              attacker['Name'], "now has HP of", attacker['HP'])
        return None


def print_character(character):
    """Print a character with its attributes and name.

    PARAM character: is a dictionary
    PRECONDITION character: is a dictionary formatted as seen in create_character function
    """
    for key, value in character.items():
        print(str(key) + ': ' + str(value))


def main():
    opponent_one = create_character(4)
    opponent_two = create_character(3)
    print_character(opponent_one)
    print_character(opponent_two)
    combat_round(opponent_one, opponent_two)


if __name__ == '__main__':
    main()

