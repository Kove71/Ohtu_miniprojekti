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
