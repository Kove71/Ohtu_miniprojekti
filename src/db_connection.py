"""Hakee yhteyden tietokantaan
"""
import sqlite3
from config import DATABASE_FILE_PATH

connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.isolation_level = None

def get_connection(database_name: str):
    """Hakee yhteyden tietokantaan ja palauttaa sen.
    """
    return connection
