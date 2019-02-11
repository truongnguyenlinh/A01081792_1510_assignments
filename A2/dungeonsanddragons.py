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
    for i in range(syllables):
        name += generate_syllables()
    return name


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
    """Provide out a list of classes for user to choose from and print the users choice.
    """
    classes = {"barbarian": 12, "bard": 8, "cleric": 8, "druid": 8, "fighter": 10, "monk": 8, "paladin": 10,
               "ranger": 10, "rogue": 8, "sorcerer": 6, "warlock": 8, "wizard": 6, "blood hunter": 10}
    class_input = str(input("Select one of the following classes: Barbarian, Bard, Cleric, Druid, \n"
                            "Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard, Blood Hunter")).strip().lower()
    if class_input not in classes.keys():
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
    attribute = ['Strength', 'Dexterity', 'Constitution',
                 'Intelligence', 'Wisdom', 'Charisma']
    character = {"Name": generate_name(syllable)}

    strength = {attribute[0]: roll_die(3, 6)}
    dexterity = {attribute[1]: roll_die(3, 6)}
    constitution = {attribute[2]: roll_die(3, 6)}
    intelligence = {attribute[3]: roll_die(3, 6)}
    wisdom = {attribute[4]: roll_die(3, 6)}
    charisma = {attribute[5]: roll_die(3, 6)}

    character.update({"Class": class_list()})
    character.update({"HP": 0})
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


def print_character(character):
    """Print a character with its attributes and name.

    PARAM character: is a list
    PRECONDITION character: is a list formatted as seen in create_character function
    """
    print("Name:", character[0])
    for index in range(1, 7):
        print(str(character[index][0]) + ': ' + str(character[index][1]))
    print("Inventory:", str(character[7]).strip('[]'))

