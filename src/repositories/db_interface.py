"""Vastuussa tietokannan toiminnoista
"""
import datetime
from entities.blog import Blog
from entities.book import Book
from entities.podcast import Podcast
from entities.video import Video
from entities.readingtip import ReadingTip
from db_connection import get_connection

class DatabaseInterface:
    """Luokka joka vastaa tietokannasta
    """
    def __init__(self):
        """Luokan konstrukstori
        """
        self._db = get_connection()


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

    def add_podcast(self, podcast: Podcast):
        """Ottaa Podcast-olion ja lisää tietokantaan
        """
        sql = "INSERT INTO readingtips (name, description, type, read) VALUES (:name, :description, :type, :read)"
        self._db.execute(sql, {"name":podcast.name, "description":podcast.description, "type":3, "read":0})
        result = self._db.execute("SELECT rowid from readingtips order by ROWID DESC limit 1")
        podcast_id = result.fetchone()[0]
        self._db.execute("INSERT INTO podcast (episode, url, tip_id) VALUES (:episode, :url, :tip_id)",{"episode":podcast.episode, "url":podcast.url, "tip_id":podcast_id})

    def add_video(self, video: Video):
        """Ottaa Video-olion ja lisää tietokantaan
        """
        sql = "INSERT INTO readingtips (name, description, type, read) VALUES (:name, :description, :type, :read)"
        self._db.execute(sql, {"name":video.name, "description":video.description, "type":4, "read":0})
        result = self._db.execute("SELECT rowid from readingtips order by ROWID DESC limit 1")
        video_id = result.fetchone()[0]
        self._db.execute("INSERT INTO video (url, author, tip_id) VALUES (:url, :author, :tip_id)",{"url":video.url, "author":video.channel, "tip_id":video_id})


    def read(self):
        """Palauttaa listan merkkijonoesityksiä olioista
        """
        found_reading_tips = []
        items = self._db.execute("SELECT * FROM readingtips WHERE visible").fetchall()
        
        for item in items:
            item_id = item[0]
            item_name = item[1]
            item_description = item[2]
            item_type = item[3]
            item_read = item[5]
            if item_read == 0:
                item_read = "no"

            if item_type == 1:
                book_info = self._db.execute("SELECT * FROM book WHERE tip_id = (?)", [item_id]).fetchone()
                author = book_info[1]
                isbn = book_info[2]

                book = Book(item_name, author, isbn, item_description)
                found_reading_tips.append(f'{item_id}: Book: {str(book)}, read: {item_read}')

            if item_type == 2:
                blog_info = self._db.execute("SELECT * FROM blog WHERE tip_id = (?)", [item_id]).fetchone()
                title = blog_info[1]
                author = blog_info[2]
                url = blog_info[3]

                blog = Blog(item_name, author, url, title, item_description)
                found_reading_tips.append(f'{item_id}: Blog: {str(blog)}, read: {item_read}')

            if item_type == 3:
                podcast_info = self._db.execute("SELECT * FROM podcast WHERE tip_id = (?)", [item_id]).fetchone()
                episode = podcast_info[1]
                url = podcast_info[2]

                podcast = Podcast(item_name, episode, url, item_description)
                found_reading_tips.append(f'{item_id}: Podcast: {str(podcast)}, read: {item_read}')

            if item_type == 4:
                video_info = self._db.execute("SELECT * FROM video WHERE tip_id = (?)", [item_id]).fetchone()
                url = video_info[1]
                channel = video_info[2]

                video = Video(item_name, url, channel, item_description)
                found_reading_tips.append(f'{item_id}: Video: {str(video)}, read: {item_read}')


        return found_reading_tips

    def remove_tip(self, index: int):
        """Poistaa yhden lukuvinkin näkyvistä
        """
        self._db.execute("UPDATE readingtips SET visible = 0 WHERE id = (?)", [index])

    def mark_as_read(self, index: int):
        """Lisää lukuvinkkiin aikaleiman
        """
        date = datetime.datetime.now()
        year = f'{date.year}'
        month = f'{date.month:02d}'
        day = f'{date.day:02d}'
        timestamp = f'{year}-{month}-{day}'

        self._db.execute("UPDATE readingtips SET read = (?) WHERE id = (?)", [timestamp, index])
