"""Testataan tietokantaluokan toimintaa.
"""
import unittest
from repositories.db_interface import DatabaseInterface
from db_build import build_database
from entities.blog import Blog
from entities.book import Book
from entities.podcast import Podcast
from entities.video import Video
from entities.readingtip import ReadingTip


class TestDatabaseInterface(unittest.TestCase):
    """Testiluokka DatabaseInterface-luokalle.
    """
    def setUp(self):
        """Alustaa ReadingTip- ja DatabaseInterface-oliot.
        """
        build_database()
        self.book = Book("kirja", "aino")
        self.database = DatabaseInterface()

    def test_add_book(self):
        """Testaa tallentuuko tietokantaan olion tiedot, kun
        kutstutaan sen add()-metodia.
        """
        self.database.add_book(self.book)
        self.assertEqual(len(self.database.read()), 1)

