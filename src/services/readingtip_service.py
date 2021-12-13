from entities.book import Book
from entities.blog import Blog
from entities.podcast import Podcast
from entities.video import Video
from repositories.db_interface import DatabaseInterface

class ReadingtipService:
    """Luokka, joka vastaa sovelluslogiikasta"""
    def __init__(self, database: DatabaseInterface):
        """Luokan konstruktori
                
            Args:
                database: tietokannasta vastaava luokka
        """
        self._db = database

    def add_book(self, name, author, isbn=None, description=None):
        """Lisää kirja-olion tietokantaan
        """
        book = Book(0, name, author, isbn, description)
        self._db.add_book(book)

    def add_blog(self, name, author, url, title=None, description=None):
        """Lisää blogi-olion tietokantaan
        """
        blog = Blog(0, name, author, url, title, description)
        self._db.add_blog(blog)
    
    def add_podcast(self, name, episode, url=None, description=None):
        """lisää podcast-olion tietokantaan
        """
        podcast = Podcast(0, name, episode, url, description)
        self._db.add_podcast(podcast)

    def add_video(self, name, url, channel=None, description=None):
        """Lisää video-olion tietokantaan
        """
        video = Video(0, name, url, channel, description)
        self._db.add_video(video)

    def get_items(self):
        """Hakee kaikki lukuvinkit
        """
        items = self._db.read()
        return items

    def remove_tip(self, index):
        """Poistaa lukuvinkin tietokannasta
        """
        self._db.remove_tip(index)

    def mark_as_read(self, item):
        """Merkitsee lukuvinkin luetuksi
        """
        self._db.mark_as_read(item)

    def edit_readingtip(self, index, field, new_value):
        """Muokkaa valittua kenttää lukuvinkistä
        """
        self._db.edit_readingtip(index, field, new_value)

    def edit_book(self, index, field, new_value):
        """Muokkaa valittua kenttää kirja-lukuvinkistä
        """
        self._db.edit_book(index, field, new_value)

    def edit_blog(self, index, field, new_value):
        """Muokkaa valittua kenttää blogi-lukuvinkistä
        """
        self._db.edit_blog(index, field, new_value)

    def edit_podcast(self, index, field, new_value):
        """Muokkaa valittua kenttää podcastista
        """
        self._db.edit_podcast(index, field, new_value)

    def edit_video(self, index, field, new_value):
        """Muokkaa valittua kenttää videosta
        """
        self._db.edit_video(index, field, new_value)
