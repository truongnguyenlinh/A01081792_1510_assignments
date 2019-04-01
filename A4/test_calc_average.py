from unittest import TestCase
from crud import calc_average
from unittest.mock import patch, mock_open
import io


class TestCalcAverage(TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data="Mundy Angus A12345678 False 59 78 89\n"
                                                              "Zhao Jason A00000000 True")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calc_average(self, mock_stdout, mock_open):
        expected = "The class average is 75.33.\n\n"
        calc_average()
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('builtins.open', new_callable=mock_open, read_data="Last First A00000000 False")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_calc_average_none(self, mock_stdout, mock_open):
        expected = "The class currently has no grades!\n"
        calc_average()
        self.assertEqual(mock_stdout.getvalue(), expected)

