"""Tests for the class ReadingTip
"""
import unittest
from entities.readingtip import ReadingTip

class TestTip(unittest.TestCase):

    def test_the_commetnt_is_saveds_as_is(self):
        """Tests if the class holds the string given to it as
        input
        """
        tip = ReadingTip("Hello World")
        self.assertEqual("Hello World", tip.__str__())

    def test_base_class_returns_none_type(self):
        """Tests if the class return it's type as None
        """
        tip = ReadingTip("Goodbye World")
        self.assertIsNone(tip.type())
