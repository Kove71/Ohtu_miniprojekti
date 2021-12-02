"""Vastuussa tietokannan toiminnoista
"""
from entities.blog import Blog
from entities.book import Book
from entities.readingtip import ReadingTip
from db_connection import get_connection

class DatabaseInterface:
    """Luokka joka vastaa tietokannasta
    """
    def __init__(self):
        """Luokan konstrukstori
        """
        self._db = get_connection("readingtips.db")

#    def add(self, reading_tip: ReadingTip):
         #Ottaa ReadingTip-olion, lisää tietokantaan
#        self._db.execute("INSERT INTO readingtips (description, type, visible, read) VALUES (?, 0, 1, 0)", [reading_tip.description])

    def add_book(self, book: Book):
        """Ottaa Book- olion, lisää tietokantaan readingtips ja book-tauluihin kirjan tiedot
        """
        sql = "INSERT INTO readingtips (name, description, type, read) VALUES (:name, :description, :type, :read)"
        self._db.execute(sql, {"name":book.name, "description":book.description, "type":1, "read":0})
        result = self._db.execute("SELECT rowid from readingtips order by ROWID DESC limit 1")
        book_id = result.fetchone()[0]
        self._db.execute("INSERT INTO book (author, isbn, tip_id) VALUES (:author, :isbn, :tip_id)",{"author":book.author, "isbn":book.isbn, "tip_id":int(book_id)})

    def add_blog(self, blog: Blog):
        """Ottaa Blog-olion ja lisää sen tietokantaan
        """
        sql = "INSERT INTO readingtips (name, description, type, read) VALUES (:name, :description, :type, :read)"
        self._db.execute(sql, {"name":blog.name, "description":blog.description, "type":2, "read":0})
        result = self._db.execute("SELECT rowid from readingtips order by ROWID DESC limit 1")
        blog_id = result.fetchone()[0]
        self._db.execute("INSERT INTO blog (title, author, url, tip_id) VALUES (:title, :author, :url, :tip_id)",{"title":blog.title, "author":blog.author, "url":blog.url, "tip_id":blog_id})

    def read(self):
        """Palauttaa listan reading_tip-olioita
        """
        sql = "SELECT id, name FROM readingtips WHERE visible"
        return [ReadingTip(reading_tip[1]) for reading_tip in self._db.execute(sql).fetchall()]

    def remove_tip(self, index: int):
        """Poistaa yhden lukuvinkin näkyvistä
        """
        self._db.execute("UPDATE readingtips SET visible = 0 WHERE id = (?)", [index])
