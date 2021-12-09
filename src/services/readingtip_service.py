from entities.book import Book
from entities.blog import Blog
from entities.podcast import Podcast
from entities.video import Video

class ReadingtipService:
    """Luokka, joka vastaa sovelluslogiikasta"""
    def __init__(self, database):
        """Luokan konstruktori
                
            Args:
                database: tietokannasta vastaava luokka
        """
        self._db = database

    def add_book(self, name, author, isbn=None, description=None):
        """Lisää kirja-olion tietokantaan
        """
        book = Book(name, author, isbn, description)
        self._db.add_book(book)

    def add_blog(self, name, author, url, title=None, description=None):
        """Lisää blogi-olion tietokantaan
        """
        blog = Blog(name, author, url, title, description)
        self._db.add_blog(blog)
    
    def add_podcast(self, name, episode, url=None, description=None):
        """lisää podcast-olion tietokantaan
        """
        podcast = Podcast(name, episode, url, description)
        self._db.add_podcast(podcast)

    def add_video(self, name, url, channel=None, description=None):
        """Lisää video-olion tietokantaan
        """
        video = Video(name, url, channel, description)
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
    
