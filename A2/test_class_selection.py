from unittest import TestCase
import dungeonsanddragons
from unittest.mock import patch


class TestClassSelection(TestCase):
    @patch('builtins.input', side_effect=["MONK"])
    def test_class_selection_lower(self, mock_user_input):
        self.assertTrue(dungeonsanddragons.class_selection().islower())

    @patch('builtins.input', side_effect=["ranger"])
    def test_class_selection_input(self, mock_user_input):
        self.assertEqual(dungeonsanddragons.class_selection(), "ranger")

