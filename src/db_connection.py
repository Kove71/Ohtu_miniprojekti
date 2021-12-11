"""Hakee yhteyden tietokantaan
"""
import sqlite3
from config import DATABASE_FILE_PATH

CONNECTION = sqlite3.connect(DATABASE_FILE_PATH)
CONNECTION.isolation_level = None

def get_connection(database_path = None):
    """Hakee yhteyden tietokantaan ja palauttaa sen.
    """
    if not database_path:
        return CONNECTION
    else:
        alt_connection = sqlite3.connect(database_path)
        alt_connection.isolation_level = None
        return alt_connection