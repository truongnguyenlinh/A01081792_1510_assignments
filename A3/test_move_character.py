from character import pokemon, get_row, get_column
from unittest import TestCase
from sud import move_character
from unittest.mock import patch


class TestMoveCharacter(TestCase):
    def setUp(self):
        pokemon["Position"][0] = 1
        pokemon["Position"][1] = 2

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
