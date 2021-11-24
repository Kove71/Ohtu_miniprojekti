import unittest
from index import main

class TestIndex(unittest.TestCase):
    
    """Testataan kui nää testit toimii. väliakanen.
    """

    def test_main(self):
        """Testataan, palauttaako index.py:n main-metodi
        0
        """
        self.assertAlmostEqual(0, main())