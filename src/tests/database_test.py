"""Testataan tietokantaluokan toimintaa.
"""
import unittest
from repositories.db_interface import DatabaseInterface
from db_build import build_database
from db_clear import clear_database
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
        clear_database()
        self.book = Book("kirja", "aino")
        self.blog = Blog("blogi", "pekka", "https://...")
        self.podcast = Podcast("podcast", "5.jakso")
        self.video = Video("video", "hassu kissa", "https://")
        self.database = DatabaseInterface()

    def test_add_book(self):
        """Testaa tallentuuko tietokantaan Book-olion tiedot, kun
        kutstutaan sen add_book()-metodia.
        """
        build_database()
        self.database.add_book(self.book)
        self.assertEqual(len(self.database.read()), 1)

    def test_add_blog(self):
        """Testaa tallentuuko tietokantaan Blog-olion tiedot, kun
        kutstutaan sen add_blog()-metodia.
        """
        build_database()
        self.database.add_blog(self.blog)
        self.assertEqual(len(self.database.read()), 1)

    def test_add_podcast(self):
        """Testaa tallentuuko tietokantaan Podcast-olion tiedot, kun
        kutstutaan sen add_podcast()-metodia.
        """
        build_database()
        self.database.add_podcast(self.podcast)
        print(self.database.read())
        self.assertEqual(len(self.database.read()), 1)

    def test_add_video(self):
        """Testaa tallentuuko tietokantaan Video-olion tiedot, kun
        kutstutaan sen add_video()-metodia.
        """
        build_database()
        self.database.add_video(self.video)
        self.assertEqual(len(self.database.read()), 1)

    def test_remove_tip(self):
        """Testaa poistuuko tietokannasta olio, kun kutsutaan 
        remove_tip-metodia
        """
        build_database()
        self.database.add_video(self.video)
        self.database.add_book(self.book)
        self.assertEqual(len(self.database.read()), 2)

        self.database.remove_tip(1)
        self.assertEqual(len(self.database.read()), 1)
