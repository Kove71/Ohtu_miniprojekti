"""Vastuussa tietokannan toiminnoista
"""
from datetime import date
from entities.blog import Blog
from entities.book import Book
from entities.podcast import Podcast
from entities.video import Video
from db_connection import get_connection

class DatabaseInterface:
    # pylint: disable=locally-disabled, multiple-statements, fixme, line-too-long
    # Tietokantakomentojen on perusteltua olla yli 100 merkkiä pitkiä

    """Luokka joka vastaa tietokannasta
    """

    def __init__(self, database_path = None):
        """Luokan konstrukstori
        """
        if not database_path:
            self._db = get_connection()
        else:
            self._db = get_connection(database_path)

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
        """Palauttaa listan olioita
        """
        found_reading_tips = []
        found_reading_tips = found_reading_tips + self.get_books()
        found_reading_tips = found_reading_tips + self.get_blogs()
        found_reading_tips = found_reading_tips + self.get_podcasts()
        found_reading_tips = found_reading_tips + self.get_videos()
        found_reading_tips.sort(key=lambda tip: tip.id)

        return found_reading_tips

    def get_books(self):
        """Hakee tietokannasta kaikki kirjat ja palauttaa ne Kirja- objekteina
        """
        books = []
        sql = "SELECT R.id, R.name, B.author, B.isbn, R.description, R.read " \
              "FROM readingtips R LEFT JOIN book B ON R.id=B.tip_id " \
              "WHERE visible AND R.type=1"
        results = self._db.execute(sql).fetchall()
        for book in results:
            read = None if book[5] == 0 else book[5]
            books.append(Book(book[0], book[1], book[2], book[3], book[4], read))
        return books

    def get_blogs(self):
        """Hakee tietokannasta kaikki blogit ja palauttaa ne Blogi- objekteina
        """
        blogs = []
        sql = "SELECT R.id, R.name, B.author, B.url, B.title, R.description, R.read " \
              "FROM readingtips R LEFT JOIN blog B ON R.id=B.tip_id " \
              "WHERE visible AND R.type=2"
        results = self._db.execute(sql).fetchall()
        for blog in results:
            read = None if blog[6] == 0 else blog[6]
            blogs.append(Blog(blog[0], blog[1], blog[2], blog[3], blog[4], blog[5], read))
        return blogs

    def get_podcasts(self):
        """Hakee tietokannsta kaikki podcastit ja palauttaa ne Podcast- objekteina
        """
        podcasts = []
        sql = "SELECT R.id, R.name, P.episode, P.url, R.description, R.read " \
              "FROM readingtips R LEFT JOIN podcast P ON R.id=P.tip_id " \
              "WHERE visible AND R.type=3"
        results = self._db.execute(sql).fetchall()
        for podcast in results:
            read = None if podcast[5] == 0 else podcast[5]
            podcasts.append(Podcast(podcast[0], podcast[1], podcast[2], podcast[3], podcast[4], read))
        return podcasts

    def get_videos(self):
        """Hakee tietokannasta kaikki videot ja palauttaa ne Video- objekteina
        """
        videos = []
        sql = "SELECT R.id, R.name, V.url, V.author, R.description, R.read " \
              "FROM readingtips R LEFT JOIN video V ON R.id=V.tip_id " \
              "WHERE visible AND R.type=4"
        results = self._db.execute(sql).fetchall()
        for video in results:
            read = None if video[5] == 0 else video[5]
            videos.append(Video(video[0], video[1], video[2], video[3], video[4], read))
        return videos

    def remove_tip(self, index: int):
        """Poistaa yhden lukuvinkin näkyvistä
        """
        self._db.execute("UPDATE readingtips SET visible = 0 WHERE id = (?)", [index])

    def mark_as_read(self, index: int):
        """Lisää lukuvinkkiin aikaleiman
        """
        timestamp = date.now()

        self._db.execute("UPDATE readingtips SET read = (?) WHERE id = (?)", [timestamp, index])

        return True

    def edit_readingtip(self, index, field, new_value):
        """Muokkaa lukuvinkistä halutun kentän
        """
        if field == 1:
            self._db.execute("UPDATE readingtips SET name = (?) WHERE id = (?)", [new_value, index])
        if field == 4:
            self._db.execute("UPDATE readingtips SET description = (?) WHERE id = (?)", [new_value, index])

    def edit_book(self, index, field, new_value):
        """Muokkaa kirja-oliosta halutun kentän
        """
        if field == 2:
            self._db.execute("UPDATE book SET author = (?) WHERE tip_id = (?)", [new_value, index])
        if field == 3:
            self._db.execute("UPDATE book SET isbn = (?) WHERE tip_id = (?)", [new_value, index])

    def edit_blog(self, index, field, new_value):
        """Muokkaa blogi-oliosta halutun kentän
        """
        if field == 2:
            self._db.execute("UPDATE blog SET author = (?) WHERE tip_id = (?)", [new_value, index])
        if field == 3:
            self._db.execute("UPDATE blog SET url = (?) WHERE tip_id = (?)", [new_value, index])
        if field == 5:
            self._db.execute("UPDATE blog SET title = (?) WHERE tip_id = (?)", [new_value, index])

    def edit_podcast(self, index, field, new_value):
        """Muokkaa podcast-oliosta halutun kentän
        """
        if field == 2:
            self._db.execute("UPDATE podcast SET episode = (?) WHERE tip_id = (?)", [new_value, index])
        if field == 3:
            self._db.execute("UPDATE podcast SET url = (?) WHERE tip_id = (?)", [new_value, index])

    def edit_video(self, index, field, new_value):
        """Muokkaa video-oliosta halutun kentän
        """
        if field == 2:
            self._db.execute("UPDATE video SET url = (?) WHERE tip_id = (?)", [new_value, index])
        if field == 3:
            self._db.execute("UPDATE video SET author = (?) WHERE tip_id = (?)", [new_value, index])
