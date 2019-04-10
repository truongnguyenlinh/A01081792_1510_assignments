def database_shared_headings(database: dict):
    """Accept a database structured as a dictionary and return all sharing keys.

    RETURN a set of keys used in all of the inner dictionaries."""
    primary_set = set(database[next(iter(database))])

    for value in database.values():
        primary_set = primary_set.intersection(set(value))
    return primary_set


def main():
    scientists = {
        'jgoodall': {'surname': 'Goodall',
                     'name': 'Jane',
                     'born': 1934,
                     'died': None,
                     'notes': 'Primate research',
                     'author': ['In the Shadow of Man', 'The Chimps of Gombe']
                     },

        'rfranklin': {'surname': 'Franklin',
                      'name': 'Rosalind',
                      'born': 1920,
                      'died': 1927,
                      'notes': 'DNA research'
                      },

        'aturing': {'surname': 'Turing',
                    'name': 'Alan',
                    'born': 1912,
                    'died': 1954,
                    'notes': 'polymath',
                    'author': ['Systems of Logic based on Ordinals']
                    }

    }
    print(database_shared_headings(scientists))


if __name__ == '__main__':
    main()
