"""Testaa ReadingTip-luokkaa
"""
import unittest
from entities.readingtip import ReadingTip

class TestTip(unittest.TestCase):
    """Testausluokka ReadintTip-luokalle
    """
    def test_the_comment_is_saved_as_is(self):
        """Testaa säilyttääkö luokka sille annetun syötteen.
        """
        tip = ReadingTip("Hello World")
        self.assertEqual("Hello World\n", tip.__str__())

    def test_base_class_returns_none_type(self):
        """Testaa palauttaako luokka tyyppinään None
        """
        tip = ReadingTip("Goodbye World")
        self.assertIsNone(tip.type())
