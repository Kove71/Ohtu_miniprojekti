"""Alustaa tietokannan taulut
"""
from db_connection import get_connection
from db_clear import clear_database

def build_database(database_path = None):
    """Alustaa tietokannan taulut
    toistaiseksi vain readingtips
    """
    if not database_path:
        database = get_connection()
    else:
        database = get_connection(database_path)

    sql = ['''
            CREATE TABLE IF NOT EXISTS readingtips (
            id INTEGER PRIMARY KEY, 
            name TEXT,
            description TEXT, 
            type INTEGER, 
            visible INTEGER DEFAULT 1, 
            read INTEGER)
            ''',

            '''
            CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY,
            author TEXT NOT NULL,
            isbn TEXT,
            tip_id INTEGER REFERENCES readingtips)
            ''',

            '''
            CREATE TABLE IF NOT EXISTS blog (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT NOT NULL,
            url TEXT NOT NULL,
            tip_id INTEGER REFERENCES readingtips)
            ''',

            '''
            CREATE TABLE IF NOT EXISTS podcast (
            id INTEGER PRIMARY KEY,
            episode TEXT NOT NULL,
            url TEXT,
            tip_id INTEGER REFERENCES readingtips)
            ''',

            '''
            CREATE TABLE IF NOT EXISTS video (
            id INTEGER PRIMARY KEY,
            url TEXT NOT NULL,
            author TEXT,
            tip_id INTEGER REFERENCES readingtips)
            '''
        ]
    for command in sql:
        database.execute(command)

if __name__ == "__main__":
    clear_database()
    build_database()
