from unittest import TestCase
import dungeonsanddragons


class TestClassList(TestCase):
    def test_CLASS_LIST_equal(self):
        self.assertEqual(dungeonsanddragons.CLASS_LIST(), {"barbarian": 12, "bard": 8, "cleric": 8, "druid": 8,
                                                           "fighter": 10, "monk": 8, "paladin": 10, "ranger": 10,
                                                           "rogue": 8, "sorcerer": 6, "warlock": 8, "wizard": 6,
                                                           "blood hunter": 10})

    def test_CLASS_LIST_type(self):
        self.assertEqual(type(dungeonsanddragons.CLASS_LIST()), dict)

    def test_CLASS_LIST_length(self):
        self.assertEqual(len(dungeonsanddragons.CLASS_LIST()), 13)

    def test_CLASS_LIST_key_str(self):
        key_only = dungeonsanddragons.CLASS_LIST().keys()
        for key in key_only:
            self.assertEqual(type(key), str)

    def test_CLASS_LIST_value_num(self):
        value_only = dungeonsanddragons.CLASS_LIST().values()
        for value in value_only:
            self.assertEqual(type(value), int)

