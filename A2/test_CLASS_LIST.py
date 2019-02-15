from unittest import TestCase
import dungeonsanddragons


class TestClassList(TestCase):
    def test_class_list_equal(self):
        self.assertEqual(dungeonsanddragons.class_list(), {"barbarian": 12, "bard": 8, "cleric": 8, "druid": 8,
                                                           "fighter": 10, "monk": 8, "paladin": 10, "ranger": 10,
                                                           "rogue": 8, "sorcerer": 6, "warlock": 8, "wizard": 6,
                                                           "blood hunter": 10})

    def test_class_list_type(self):
        self.assertEqual(type(dungeonsanddragons.class_list()), dict)

    def test_class_list_length(self):
        self.assertEqual(len(dungeonsanddragons.class_list()), 13)

    def test_class_list_key_str(self):
        key_only = dungeonsanddragons.class_list().keys()
        for key in key_only:
            self.assertEqual(type(key), str)

    def test_class_list_key_num(self):
        value_only = dungeonsanddragons.class_list().values()
        for value in value_only:
            self.assertEqual(type(value), int)

