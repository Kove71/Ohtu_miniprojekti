import sqlite3
import os

class DatabaseInterface:
    def __init__(self):
        self._db = sqlite3.connect(os.path.realpath("") + "/data/lukuvinkit.db")
        self._db.isolation_level = None
        self._db.execute("CREATE TABLE IF NOT EXISTS lukuvinkit (id INTEGER PRIMARY KEY, kuvaus TEXT)")

    def Add(self, description: str):
        self._db.execute("INSERT INTO lukuvinkit (kuvaus) VALUES (?)", [description])

    def Read(self):
        return self._db.execute("SELECT * FROM lukuvinkit").fetchall()

    def Clear(self):
        self._db.execute("DELETE FROM lukuvinkit")
        self._db.execute("VACUUM")

    def Delete(self):
        os.remove(os.path.realpath("") + "/data/lukuvinkit.db")