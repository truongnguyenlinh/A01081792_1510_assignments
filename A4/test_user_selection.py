from unittest import TestCase
from crud import user_selection
from unittest.mock import patch
import io


class TestUserSelection(TestCase):
    @patch('builtins.input', side_effect=["5"])
    def test_user_selection_quit(self, mock_input):
        with self.assertRaises(SystemExit):
            user_selection("5")

    @patch('builtins.input', side_effect=[5])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_selection_type(self, mock_stdout, mock_input):
        expected = "Please enter a valid action!\n\n"
        user_selection(5)
        self.assertEqual(mock_stdout.getvalue(), expected)
