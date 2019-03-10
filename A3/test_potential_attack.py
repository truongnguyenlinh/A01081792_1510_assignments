from unittest import TestCase
import unittest.mock
from combat import potential_attack
from character import get_hp, pokemon
import random
import io


class TestPotentialAttack(TestCase):
    def setUp(self):
        pokemon['Name'] = 'Kanye'
        pokemon['Class'] = 'Squirtle'
        pokemon['Position'] = [7, 3]
        pokemon['HP'] = 7

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_potential_attack_output(self, mock_stdout):
        """Assert that user successfully flees."""
        random.seed(13)
        opponent = {'Name': 'Horsea', 'Attack': 'Bubble Beam', 'HP': 5}
        potential_attack(opponent)
        self.assertEqual(mock_stdout.getvalue(), "You fled successfully!\n")
        random.seed()

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_potential_attack_second_output(self, mock_stdout):
        """Assert that user is attacked by opponent."""
        random.seed(2)
        opponent = {'Name': 'Jynx', 'Attack': 'Ice Punch', 'HP': 5}
        expected_output = "Despite fleeing, Jynx still attacked you! He inflicted you by 1 damage.\n"
        potential_attack(opponent)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()

    def test_potential_attack_hp(self):
        """Assert users HP after damage."""
        random.seed(43)
        opponent = {'Name': 'Lapras', 'Attack': 'Ice Shard', 'HP': 5}
        potential_attack(opponent)
        self.assertEqual(get_hp(), 4)
        random.seed()

    def test_potential_attack_fled(self):
        """Assert HP of user after successful flee."""
        random.seed(21)
        opponent = {'Name': 'Scyther', 'Attack': 'Slash', 'HP': 5}
        potential_attack(opponent)
        self.assertEqual(get_hp(), 7)
        random.seed()

    def test_potential_attack_global(self):
        """Assert that users HP is updated in global variable."""
        random.seed(57)
        opponent = {'Name': 'Pikachu', 'Attack': 'Thunderbolt', 'HP': 5}
        potential_attack(opponent)
        self.assertEqual(pokemon, {'Name': 'Kanye', 'Class': 'Squirtle', 'Position': [7, 3], 'HP': 4})
        random.seed()
