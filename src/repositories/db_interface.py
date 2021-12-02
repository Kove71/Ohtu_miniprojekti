"""Vastuussa tietokannan toiminnoista
"""
from entities.readingtip import ReadingTip
from db_connection import get_connection

class DatabaseInterface:
    """Luokka joka vastaa tietokannasta
    """
    def __init__(self):
        """Luokan konstrukstori
        """
        self._db = get_connection("readingtips.db")

    def add(self, reading_tip: ReadingTip):
        """Ottaa ReadingTip-olion, lisää tietokantaan
        """
        self._db.execute("INSERT INTO readingtips (description, type, visible, read) VALUES (?, 0, 1, 0)", [reading_tip.description])

    def read(self):
        """Palauttaa listan reading_tip-olioita
        """
        sql = "SELECT id, description FROM readingtips WHERE visible"
        return [ReadingTip(reading_tip[1]) for reading_tip in self._db.execute(sql).fetchall()]

    def remove_tip(self, index: int):
        """Poistaa yhden lukuvinkin näkyvistä
        """
        self._db.execute("UPDATE readingtips SET visible = 0 WHERE id = (?)", [index])
