"""Testataan ReadingTipServive-luokkaa
"""

import unittest
from unittest.mock import Mock, ANY
from services.readingtip_service import ReadingtipService

class TestReadingtipService(unittest.TestCase):
    """Testiluokka ReadingTipService-luokalle
    """

    def setUp(self):
        """Alustetaa mock-database-luokan ja ReadingTipService-luokan
        """
        self.database_mock = Mock()
        self.service = ReadingtipService(self.database_mock)

    def test_add_book(self):
        """Testataan kirjan lisäämistä
        """
        self.service.add_book("name", "author")
        self.database_mock.add_book.assert_called_with(ANY)

    def test_add_blog(self):
        """Testataan blogin lisäämistä
        """
        self.service.add_blog("name", "author", "https://...")
        self.database_mock.add_blog.assert_called_with(ANY)

    def test_add_podcast(self):
        """Testataan podcastin lisäämistä
        """
        self.service.add_podcast("name", "episode")
        self.database_mock.add_podcast.assert_called_with(ANY)

    def test_add_video(self):
        """Testataan videon lisämistä
        """
        self.service.add_video("name", "https://...")
        self.database_mock.add_video.assert_called_with(ANY)

    def test_get_items(self):
        """Testataan lukuvinkkien hakua
        """
        self.service.get_items()
        self.database_mock.read.assert_called()

    def test_remove_tip(self):
        """Testataan vinkin poistoa
        """
        self.service.remove_tip(1)
        self.database_mock.remove_tip.assert_called_with(1)

    def test_mark_as_read(self):
        """Testataan luetuksi merkitsemistä
        """
        self.service.mark_as_read(1)
        self.database_mock.mark_as_read.assrt_called_with(1)

    def test_edit_readingtip(self):
        """Testataan vinkin muokkausta
        """
        self.service.edit_readingtip(1, "name", "aino")
        self.database_mock.edit_readingtip.assert_called_with(1, "name", "aino")

    def test_edit_book(self):
        """Testataan kirjan muokkausta
        """
        self.service.edit_book(1, "name", "aino")
        self.database_mock.edit_book.assert_called_with(1, "name", "aino")

    def test_edit_blog(self):
        """Testataan blogin muokkausta
        """
        self.service.edit_blog(1, "name", "aino")
        self.database_mock.edit_blog.assert_called_with(1, "name", "aino")

    def test_edit_podcast(self):
        """Testataan podcastin muokkausta
        """
        self.service.edit_podcast(1, "name", "aino")
        self.database_mock.edit_podcast.assert_called_with(1, "name", "aino")

    def test_edit_video(self):
        """Testataan videon muokkausta
        """
        self.service.edit_video(1, "name", "aino")
        self.database_mock.edit_video.assert_called_with(1, "name", "aino")
