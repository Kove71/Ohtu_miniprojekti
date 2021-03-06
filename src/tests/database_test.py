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


class TestDatabaseInterface(unittest.TestCase):
    """Testiluokka DatabaseInterface-luokalle.
    """
    def setUp(self):
        """Alustaa ReadingTip- ja DatabaseInterface-oliot.
        """
        clear_database()
        self.book = Book(1, "kirja", "aino")
        self.blog = Blog(2, "blogi", "pekka", "https://...")
        self.podcast = Podcast(3, "podcast", "5.jakso")
        self.video = Video(4, "video", "hassu kissa", "https://")
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

    def test_mark_as_read(self):
        """Testaa merkkaako tietokannan metodi mark_as_read
        lukuvinkin luetuksi
        """
        build_database()
        self.database.add_book(self.book)
        self.assertEqual(self.database.mark_as_read(1), True)

    def test_edit_book(self):
        """Testaa kirjan muokkausta
        """
        build_database()
        self.database.add_book(self.book)
        self.database.edit_book(1, 2, "uusi nimi")
        self.assertEqual(self.database.get_books()[0].author, "uusi nimi")
        self.database.edit_book(1, 3, "uusi isbn")
        self.assertEqual(self.database.get_books()[0].isbn, "uusi isbn")

    def test_edit_blog(self):
        """Testaa blogin muokkausta
        """
        build_database()
        self.database.add_blog(self.blog)
        self.database.edit_blog(1, 2, "uusi nimi")
        self.assertEqual(self.database.get_blogs()[0].author, "uusi nimi")
        self.database.edit_blog(1, 3, "uusi url")
        self.assertEqual(self.database.get_blogs()[0].url, "uusi url")
        self.database.edit_blog(1, 5, "uusi otsikko")
        self.assertEqual(self.database.get_blogs()[0].title, "uusi otsikko")

    def test_edit_podcast(self):
        """Testaa podcastin muokkausta
        """
        build_database()
        self.database.add_podcast(self.podcast)
        self.database.edit_podcast(1, 2, "uusi jakso")
        self.assertEqual(self.database.get_podcasts()[0].episode, "uusi jakso")
        self.database.edit_podcast(1, 3, "uusi url")
        self.assertEqual(self.database.get_podcasts()[0].url, "uusi url")

    def test_edit_video(self):
        """Testaa videon muokkausta
        """
        build_database()
        self.database.add_video(self.video)
        self.database.edit_video(1, 2, "uusi url")
        self.assertEqual(self.database.get_videos()[0].url, "uusi url")
        self.database.edit_video(1, 3, "uusi kanava")
        self.assertEqual(self.database.get_videos()[0].channel, "uusi kanava")

    def test_edit_readingtip(self):
        """Testaa lukuvinkin muokkausta
        """
        build_database()
        self.database.add_book(self.book)
        self.database.edit_readingtip(1, 1, "uusi nimi")
        self.assertEqual(self.database.get_books()[0].name, "uusi nimi")
        self.database.edit_readingtip(1, 4, "uusi kuvaus")
        self.assertEqual(self.database.get_books()[0].description, "uusi kuvaus")
