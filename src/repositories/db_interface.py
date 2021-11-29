import sqlite3
import os
from entities.readingtip import ReadingTip

class DatabaseInterface:
    """Luokka joka vastaa tietokannasta
    """
    def __init__(self):
        """Luokan konstrukstori
        """
        self._db = sqlite3.connect(os.path.realpath("") + "/data/lukuvinkit.db")
        self._db.isolation_level = None
        sql = "CREATE TABLE IF NOT EXISTS lukuvinkit (id INTEGER PRIMARY KEY, kuvaus TEXT)"
        self._db.execute(sql)

    def add(self, lukuvinkki: ReadingTip):
        """Ottaa LukuVinkki-olion, lisää tietokantaan
        """
        self._db.execute("INSERT INTO lukuvinkit (kuvaus) VALUES (?)", [lukuvinkki.description])

    def read(self):
        """Palauttaa listan LukuVinkki-olioita
        """
        sql = "SELECT * FROM lukuvinkit"
        return [ReadingTip(lukuvinkki[1]) for lukuvinkki in self._db.execute(sql).fetchall()]


    def clear(self):
        """ Tyhjentää tietokannan
        """
        self._db.execute("DELETE FROM lukuvinkit")
        self._db.execute("VACUUM")

    def delete(self):
        """Poistaa tietokannan
        """
        os.remove(os.path.realpath("") + "/data/lukuvinkit.db")
