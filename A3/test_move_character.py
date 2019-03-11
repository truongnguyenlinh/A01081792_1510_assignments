from character import pokemon, get_row, get_column, get_hp
from unittest import TestCase
from sud import move_character
from unittest.mock import patch
import io
import random
import unittest


class TestMoveCharacter(TestCase):
    def setUp(self):
        pokemon["Position"][0] = 1
        pokemon["Position"][1] = 2
        pokemon["HP"] = 8

    @patch('builtins.input', side_effect=['G', 'e'])
    def test_move_character_east(self, mock_user_input):
        """Assert that character row position is added by one."""
        move_character()
        self.assertEqual(get_row(), 2)

    @patch('builtins.input', side_effect=['w'])
    def test_move_character_west(self, mock_user_input):
        """Assert that character row position is subtracted by one."""
        move_character()
        self.assertEqual(get_row(), 0)

    @patch('builtins.input', side_effect=['s'])
    def test_move_character_south(self, mock_user_input):
        """Assert that character column position is added by one."""
        move_character()
        self.assertEqual(get_column(), 3)

    @patch('builtins.input', side_effect=['n'])
    def test_move_character_north(self, mock_user_input):
        """Assert that character column position is subtracted by one."""
        move_character()
        self.assertEqual(get_column(), 1)

    @patch('builtins.input', side_effect=['h', 'u', 'w'])
    def test_move_character_hp(self, mock_user_input):
        """Assert that HP will increase by one if HP is less than 10."""
        move_character()
        self.assertEqual(get_hp(), 9)

    @patch('builtins.input', side_effect=['e', 'w'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_character_boundary_output(self, mock_stdout, mock_user_input):
        """Assert expected print output if user it out of bounds."""
        random.seed(3)
        pokemon['Position'][0] = 7
        expected_output = '🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n' \
                          '🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n' \
                          '🌲  🌲  🌲  🌲  🌲  🌲  🌲  🐱\n' \
                          '🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n' \
                          '🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n' \
                          '🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n' \
                          '🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n' \
                          '🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n' \
                          'You head East out of bounds and step in mud! '\
                          'You go back to your original position, to clean your feet\n' \
                          '🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n' \
                          '🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n' \
                          '🌲  🌲  🌲  🌲  🌲  🌲  🌲  🐱\n' \
                          '🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n' \
                          '🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n' \
                          '🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n' \
                          '🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n' \
                          '🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲\n' \
                          'You head towards the grass and continue on your path.\n'
        move_character()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()

    @patch('builtins.input', side_effect=['e', 'w'])
    def test_move_character_row_boundary(self, mock_user_input):
        """Assert that character cannot move out of bounds and select a different direction."""
        pokemon['Position'][0] = 7
        expected_output = 6
        move_character()
        self.assertEqual(get_row(), expected_output)

    @patch('builtins.input', side_effect=['n', 'e', 'w'])
    def test_move_character_hp_max(self, mock_user_input):
        """Assert that HP will not be greater than 10."""
        pokemon['HP'] = 10
        move_character()
        self.assertEqual(get_hp(), 10)

    @patch('builtins.input', side_effect=['n', 's'])
    def test_move_character_column_boundary(self, mock_user_input):
        """Assert that character column position cannot move out of bounds and user must select different direction"""
        pokemon['Position'][1] = 0
        move_character()
        self.assertEqual(get_column(), 1)
