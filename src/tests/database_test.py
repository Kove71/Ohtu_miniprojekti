import unittest
from entities.readingtip import ReadingTip
from repositories.db_interface import DatabaseInterface

class TestDatabaseInterface(unittest.TestCase):
    def setUp(self):
        self.lukuvinkki = ReadingTip("kirja")
        self.db = DatabaseInterface()
    
    def test_add(self):
        self.db.add(self.lukuvinkki)
        self.assertEqual(len(self.db.read()), 1)
    
    def test_clear(self):
        self.db.add(self.lukuvinkki)
        self.db.clear()
        self.assertEqual(len(self.db.read()), 0)


