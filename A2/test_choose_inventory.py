from unittest import TestCase
import dungeonsanddragons
import unittest.mock
import io


class TestChooseInventory(TestCase):
    def test_choose_inventory_same_items(self):
        items = ["Armor", "Shield", "Consumables", "Weapons",
                 "Gear", "Tools", "Wands", "Gold"]
        selected_items = dungeonsanddragons.choose_inventory(items, 4)
        for gear in selected_items:
            self.assertTrue(gear in items)  # ask Chris

    def test_choose_inventory_len(self):
        items = ["Armor", "Shield", "Consumables", "Weapons",
                 "Gear", "Tools", "Wands", "Gold"]
        self.assertEqual(len(dungeonsanddragons.choose_inventory(items, 3)), 3)

    def test_choose_inventory_type(self):
        items = ["Armor", "Shield", "Consumables", "Weapons",
                 "Gear", "Tools", "Wands", "Gold"]
        self.assertEqual(type(dungeonsanddragons.choose_inventory(items, 5)), list)

    def test_choose_inventory_empty_list(self):
        self.assertEqual(dungeonsanddragons.choose_inventory([], 0), [])

    def test_choose_inventory_no_selection(self):
        self.assertEqual(dungeonsanddragons.choose_inventory(["Gear", "Tools", "Armor"], 0), [])

    def test_choose_inventory_equivalent(self):
        inventory_list = ["Armor", "Shield", "Consumables", "Weapons"]
        self.assertEqual(dungeonsanddragons.choose_inventory(inventory_list, 4), sorted(inventory_list))

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory_large_selection(self, mock_stdout):
        items = ["Armor", "Shield", "Consumables", "Weapons",
                 "Gear", "Tools", "Wands", "Gold"]
        expected_output = 'Error: Not enough elements in list to select.\n'
        dungeonsanddragons.choose_inventory(items, 12)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory(self, mock_stdout):
        items = ["Armor", "Shield", "Consumables", "Weapons",
                 "Gear", "Tools", "Wands", "Gold"]
        expected_output = 'Error: Selection must be a positive integer.\n'
        dungeonsanddragons.choose_inventory(items, -4)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

