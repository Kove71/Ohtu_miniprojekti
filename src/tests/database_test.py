"""Testataan tietokantaluokan toimintaa.
"""
import unittest
from entities.readingtip import ReadingTip
from repositories.db_interface import DatabaseInterface

class TestDatabaseInterface(unittest.TestCase):
    """Testiluokka DatabaseInterface-luokalle.
    """
    def setUp(self):
        """Alustaa ReadingTip- ja DatabaseInterface-oliot.
        """
        self.reading_tip = ReadingTip("kirja")
        self.database = DatabaseInterface()

    def test_add(self):
        """Testaa tallentuuko tietokantaan olion tiedot, kun
        kutstutaan sen add()-metodia.
        """
        self.database.add(self.reading_tip)
        self.assertEqual(len(self.database.read()), 1)

    def test_clear(self):
        """Testaa tyhjentyykö tietokanta, kun kutstutaan
        sen clear()-metodia.
        """
        self.database.add(self.reading_tip)
        self.database.clear()
        self.assertEqual(len(self.database.read()), 0)
