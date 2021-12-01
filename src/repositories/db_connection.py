"""Hakee yhteyden tietokantaan
"""
import os
import sqlite3

DIRNAME = os.path.dirname(__file__)

def get_connection(database_name: str):
    """Hakee yhteyden tietokantaan ja palauttaa sen.
    """
    conn = sqlite3.connect(os.path.join(DIRNAME, "..", "..", "data", database_name))
    conn.isolation_level = None
    return conn
