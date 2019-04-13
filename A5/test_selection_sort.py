from unittest import TestCase
from q04 import selection_sort


class TestSelectionSort(TestCase):
    def test_selection_sort_type(self):
        self.assertIsInstance(selection_sort(["c", "b", "a"]), list)

    def test_selection_sort_empty(self):
        with self.assertRaises(ValueError):
            selection_sort([])

    def test_selection_sort_ints(self):
        self.assertEqual(selection_sort([9, 100, 0, 2]), [0, 2, 9, 100])

    def test_selection_sort_str(self):
        self.assertEqual(selection_sort(["hello", "a", "bun"]), ["a", "bun", "hello"])

    def test_selection_sort_multi_type(self):
        with self.assertRaises(TypeError):
            selection_sort(["a", 10, "de"])
