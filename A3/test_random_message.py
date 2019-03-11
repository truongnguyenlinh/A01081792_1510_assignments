from unittest import TestCase
from sud import random_message
import unittest.mock
import random
import io


class TestRandomMessage(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_random_message_output(self, mock_stdout):
        """Assert random string output."""
        random.seed(4)
        expected_value = "Looks like there's something shiny behind a tree. "\
                         "You head towards the tree and find a Big Pearl.\n"\
                         "The pearlescent sheen is irresistible, so you put it in your bag.\n"
        random_message()
        self.assertEqual(mock_stdout.getvalue(), expected_value)
        random.seed()

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_random_message_random(self, mock_stdout):
        """Assert random string output."""
        random.seed(1)
        expected_value = "After stepping out of the grass, you find some Gooey Mulch.\nAlthough a maniac would " \
                         "buy this to use as fertilizer on a Berry Crop, you decide not to pick it up.\n"
        random_message()
        self.assertEqual(mock_stdout.getvalue(), expected_value)
        random.seed()
