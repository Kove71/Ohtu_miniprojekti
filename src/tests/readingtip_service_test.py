import unittest
from unittest.mock import Mock, ANY
from services.readingtip_service import ReadingtipService
from entities.book import Book

class TestReadingtipService(unittest.TestCase):
    def setUp(self):
        self.database_mock = Mock() 
        self.service = ReadingtipService(self.database_mock)
    
    def test_add_book(self):
        self.service.add_book("name", "author")
        self.database_mock.add_book.assert_called_with(ANY)
    
    def test_add_blog(self):
        self.service.add_blog("name", "author", "https://...")
        self.database_mock.add_blog.assert_called_with(ANY)
    
    def teat_add_podcast(self):
        self.service.add_podcast("name", "episode")
        self.database_mock.add_podacst.assert_called_with(ANY)
    
    def test_add_video(self):
        self.service.add_video("name", "https://...")
        self.database_mock.add_video.assert_called_with(ANY)
    
    def test_get_items(self):
        self.service.get_items()
        self.database_mock.read.assert_called()
    
    def test_remove_tip(self):
        self.service.remove_tip(1)
        self.database_mock.remove_tip.assert_called_with(1)
    
    def test_mark_as_read(self):
        self.service.mark_as_read(1)
        self.database_mock.mark_as_read.assrt_called_with(1)
    
    def test_edit_readingtip(self):
        self.service.edit_readingtip(1, "name", "aino")
        self.database_mock.edit_readingtip.assert_called_with(1, "name", "aino")
    
    def test_edit_book(self):
        self.service.edit_book(1, "name", "aino")
        self.database_mock.edit_book.assert_called_with(1, "name", "aino")
    
    def test_edit_blog(self):
        self.service.edit_blog(1, "name", "aino")
        self.database_mock.edit_blog.assert_called_with(1, "name", "aino")
    
    def test_edit_podcast(self):
        self.service.edit_podcast(1, "name", "aino")
        self.database_mock.edit_podcast.assert_called_with(1, "name", "aino")
    
    def test_edit_video(self):
        self.service.edit_video(1, "name", "aino")
        self.database_mock.edit_video.assert_called_with(1, "name", "aino")
    

