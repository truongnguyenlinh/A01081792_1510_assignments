# Linh Truong
# A01081792
# 02/05/2019


import random
import doctest


def roll_die(number_of_rolls, number_of_sides):
    """Return the random number after given number of rolls of a die.

    Range of potential output is determined by number_of_rolls and number_of_sides.
    PARAM number_of_rolls is an int
    PARAM number_of_sides is an int
    PRECONDITION number_of_rolls is a positive int
    PRECONDITION number_of_sides is a positive int
    RETURN total value from number of rolls and sided die
    >>> roll_die(0, 0)
    0
    >>> roll_die(0, 10)
    0
    >>> roll_die(1, 0)
    0
    >>> random.seed(1)
    >>> roll_die(3, 18)
    11"""
    if number_of_rolls == 0 or number_of_sides == 0:
        return 0
    else:
        total = random.randint(1 * number_of_rolls, number_of_sides * number_of_rolls)
        return total


def generate_vowel():
    """Return a randomly selected vowel letter.

    RETURN random string vowel from vowel letters
    >>> random.seed(0)
    >>> generate_vowel()
    'o'
    >>> random.seed(1)
    >>> generate_vowel()
    'e'
    >>> random.seed(10)
    >>> generate_vowel()
    'u'"""
    vowel_letters = 'aeiouy'
    return random.choice(vowel_letters)


def generate_consonant():
    """Return a randomly selected consonant letter.

    RETURN random string consonant from consonant letters
    >>> random.seed(0)
    >>> generate_consonant()
    'q'
    >>> random.seed(1)
    >>> generate_consonant()
    'g'
    >>> random.seed(2)
    >>> generate_consonant()
    'c'
    >>> random.seed(3)
    >>> generate_consonant()
    'k'"""
    consonant_letters = 'bcdfghjklmnpqrstvwxyz'
    return random.choice(consonant_letters)


def generate_syllables():
    """Return one consonant and one vowel letter, concatenated.

    RETURN a string of two characters
    >>> random.seed(0)
    >>> generate_syllables()
    'qo'
    >>> random.seed(30)
    >>> generate_syllables()
    'wi'
     >>> random.seed(59)
    >>> generate_syllables()
    'ka'"""
    return generate_consonant() + generate_vowel()


def generate_name(syllables):
    """Return string of concatenated syllables.

    PARAM syllables a positive integer
    PRECONDITION syllables must be a positive non-zero integer
    RETURN string composed of specified number of syllables
    >>> random.seed(8)
    >>> generate_name(2)
    'Kiqe'
    >>> random.seed(10)
    >>> generate_name(3)
    'Xaroxa'
    >>> random.seed(20)
    >>> generate_name(4)
    'Gizanuha'"""
    name = ""
    for num in range(syllables):
        name += generate_syllables()
    return name.title()


def choose_inventory(inventory, selection):
    """Return a sorted list of random elements in a dictionary.

    PARAM inventory is a list
    PARAM selection is an int
    PRECONDITION inventory must be a list
    PRECONDITION selection must be a positive integer
    RETURN sorted dictionary of selected length for inventory
    >>> choose_inventory([],0)
    []
    >>> choose_inventory(["armor", "shield", "consumables"], 0)
    []
    >>> random.seed(0)
    >>> choose_inventory(["armor", "shield", "consumables"], 3)
    ['armor', 'shield', 'consumables']
    >>> random.seed(0)
    >>> choose_inventory(["armor", "shield", "consumables", "water"], 3)
    ['armor', 'shield', 'water']"""
    if (inventory is list()) or (selection == 0):
        return []
    elif selection < 0:
        print('Error: Selection must be a positive integer.')
        return None
    elif selection > len(inventory):
        print('Error: Not enough elements in list to select.')
        return None
    elif selection == len(inventory):
        return inventory[:]
    else:
        return sorted(random.sample(inventory, selection))


def CLASS_LIST():
    """Provide a dictionary of classes with roll die for user to choose from.

    RETURN dictionary of all classes (keys) and values
    >>> CLASS_LIST()
    {'barbarian': 12, 'bard': 8, 'cleric': 8, 'druid': 8, 'fighter': 10, 'monk': 8, 'paladin': 10, 'ranger': 10, 'rogue': 8,\
 'sorcerer': 6, 'warlock': 8, 'wizard': 6, 'blood hunter': 10}
    """
    return {"barbarian": 12, "bard": 8, "cleric": 8, "druid": 8, "fighter": 10, "monk": 8, "paladin": 10,
            "ranger": 10, "rogue": 8, "sorcerer": 6, "warlock": 8, "wizard": 6, "blood hunter": 10}


def class_selection():
    """Obtain class input from user from class_list dictionary.

    PRECONDITION user input invalid, recursively call the function
    RETURN class string, if input is in dictionary keys"""
    class_input = str(input("Select one of the following classes: Barbarian, Bard, Cleric, Druid, \n"
                            "Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard, Blood Hunter")).strip().lower()
    if class_input not in CLASS_LIST().keys():
        return class_selection()
    else:
        return class_input


def create_character(syllable):
    """Return character with its name, six attributes, HP, XP and inventory.

    PARAM syllables is an int
    PRECONDITION syllables is a positive, non-zero integer
    RETURN merged dictionary of name, attributes, HP, XP and inventory"""
    character = {"Name": generate_name(syllable)}

    strength = {'Strength': roll_die(3, 6)}
    dexterity = {'Dexterity': roll_die(3, 6)}
    constitution = {'Constitution': roll_die(3, 6)}
    intelligence = {'Intelligence': roll_die(3, 6)}
    wisdom = {'Wisdom': roll_die(3, 6)}
    charisma = {'Charisma': roll_die(3, 6)}

    character.update({"Class": class_selection()})
    character.update({"HP": random.randint(1, CLASS_LIST()[character['Class']])})
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


def first_attack():
    """Determine who attacks first.

    PARAM opponent_one: a dictionary
    PARAM opponent_two: a dictionary
    PRECONDITION opponent_one: must be a well-formed dictionary with correct character
    PRECONDITION opponent_two: must be a well-formed dictionary with correct character
    RETURN boolean value, otherwise recall function
    >>> random.seed(0)
    >>> first_attack()
    False
     >>> random.seed(10)
    >>> first_attack()
    True"""
    opponent_one_roll = random.randint(1, 20)
    opponent_two_roll = random.randint(1, 20)

    if opponent_one_roll == opponent_two_roll:
        return first_attack()
    elif opponent_one_roll > opponent_two_roll:
        return True
    else:
        return False


def combat_round(opponent_one, opponent_two):
    """Determine the amount of damage between two characters.

    PARAM opponent_one: a dictionary
    PARAM opponent_two: a dictionary
    PRECONDITION opponent_one: must be a well-formed dictionary with correct character
    PRECONDITION opponent_two: must be a well-formed dictionary with correct character
    >>> random.seed(0)
    >>> op_one = {'Name': 'Kuwe', 'Class': 'druid', 'HP': 4, 'Strength': 14, 'Dexterity': 18, \
    'Constitution': 5, 'Intelligence': 3, 'Wisdom': 18, 'Charisma': 11, 'XP': 0, 'Inventory': []}
    >>> op_two = {'Name': 'Carina', 'Class': 'rogue', 'HP': 18, 'Strength': 5, 'Dexterity': 4, \
    'Constitution': 10, 'Intelligence': 6, 'Wisdom': 10, 'Charisma': 4, 'XP': 0, 'Inventory': []}
    >>> combat_round(op_one, op_two)
    Carina missed, Kuwe has a total of 4 HP
    Kuwe hit Carina a total of 7 damage and Carina now has HP of 11
    >>> random.seed(23)
    >>> op_one = {'Name': 'Kuwe', 'Class': 'druid', 'HP': 4, 'Strength': 14, 'Dexterity': 18, \
                   'Constitution': 5, 'Intelligence': 3, 'Wisdom': 18, 'Charisma': 11, 'XP': 0, 'Inventory': []}
    >>> op_two = {'Name': 'Carina', 'Class': 'rogue', 'HP': 18, 'Strength': 5, 'Dexterity': 4, \
                   'Constitution': 10, 'Intelligence': 6, 'Wisdom': 10, 'Charisma': 4, 'XP': 0, 'Inventory': []}
    >>> combat_round(op_one, op_two)
    Kuwe missed, Carina has a total of 18 HP
    Carina hit Kuwe a total of 4 damage and Kuwe now has HP of 0
    Kuwe has died"""
    if first_attack():
        attacker = opponent_one
        victim = opponent_two
    else:
        victim = opponent_one
        attacker = opponent_two

    if random.randint(1, 20) > victim['Dexterity']:
        damage = random.randint(1, random.randint(1, CLASS_LIST()[attacker['Class']]))
        victim['HP'] -= damage
        print(attacker['Name'], "hit", victim['Name'], "a total of " + str(damage) + " damage and",
              victim['Name'], "now has HP of", str(victim['HP']))
        if victim['HP'] <= 0:
            print(victim['Name'], "has died")
    else:
        print(attacker['Name'], "missed,", victim['Name'], "has a total of %s HP" % str(victim['HP']))

    if victim['HP'] <= 0:
        return None

    if random.randint(1, 20) > attacker['Dexterity']:
        damage = random.randint(1, random.randint(1, CLASS_LIST()[victim['Class']]))
        attacker['HP'] -= damage
        print(victim['Name'], "hit", attacker['Name'], "a total of", str(damage), "damage and",
              attacker['Name'], "now has HP of", attacker['HP'])
        if attacker['HP'] <= 0:
            print(attacker['Name'], "has died")
    else:
        print(victim['Name'], "missed,", attacker['Name'], "has a total of %s HP" % str(attacker['HP']))


def print_character(character):
    """Print a character with its attributes and name.

    PARAM character: is a dictionary
    PRECONDITION character: is a dictionary formatted as seen in create_character function
    >>> print_character({'Name': 'Kuwe', 'Class': 'druid', 'HP': 4, 'Strength': 14, 'Dexterity': 18, \
    'Constitution': 5, 'Intelligence': 3, 'Wisdom': 18, 'Charisma': 11, 'XP': 0, 'Inventory': []})
    Name: Kuwe
    Class: druid
    HP: 4
    Strength: 14
    Dexterity: 18
    Constitution: 5
    Intelligence: 3
    Wisdom: 18
    Charisma: 11
    XP: 0
    Inventory: []
    """
    for key, value in character.items():
        print(str(key) + ': ' + str(value))


def main():
    """Execute the program."""
    doctest.testmod()

    print(roll_die(2, 8))

    items = ["armor", "shield", "consumables", "weapons",
             "gear", "tools", "wands", "gold"]

    opponent_one = create_character(int(input("Player one: enter a number from 1-10.")))
    opponent_two = create_character(int(input("Player two: enter a number from 1-10.")))

    opponent_one['Inventory'] = choose_inventory(items, int(input("Player one: enter number of inventory")))
    opponent_two['Inventory'] = choose_inventory(items, int(input("Player two: enter number of inventory")))

    print_character(opponent_one)
    print(opponent_two)

    while opponent_one['HP'] > 0 and opponent_two['HP'] > 0:
        combat_round(opponent_one, opponent_two)


if __name__ == '__main__':
    main()

