import sqlite3
import os
from entities.readingtip import ReadingTip

class DatabaseInterface:
    """Luokka joka vastaa tietokannasta
    """
    def __init__(self):
        """Luokan konstrukstori
        """
        self._db = sqlite3.connect(os.path.realpath("") + "/data/readingtips.db")
        self._db.isolation_level = None
        sql = "CREATE TABLE IF NOT EXISTS readingtips (id INTEGER PRIMARY KEY, kuvaus TEXT)"
        self._db.execute(sql)

    def add(self, reading_tip: ReadingTip):
        """Ottaa ReadingTip-olion, lisää tietokantaan
        """
        self._db.execute("INSERT INTO readingtips (kuvaus) VALUES (?)", [reading_tip.description])

    def read(self):
        """Palauttaa listan reading_tip-olioita
        """
        sql = "SELECT * FROM readingtips"
        return [ReadingTip(reading_tip[1]) for reading_tip in self._db.execute(sql).fetchall()]


    def clear(self):
        """ Tyhjentää tietokannan
        """
        self._db.execute("DELETE FROM readingtips")
        self._db.execute("VACUUM")

    def delete(self):
        """Poistaa tietokannan
        """
        os.remove(os.path.realpath("") + "/data/readingtips.db")
