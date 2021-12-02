"""Alustaa tietokannan taulut
"""
from db_connection import get_connection
from db_clear import clear_database

def build_database():
    """Alustaa tietokannan taulut
    toistaiseksi vain readingtips
    """
    database_name = "readingtips.db"
    database = get_connection(database_name)
    sql = ['''CREATE TABLE IF NOT EXISTS types (
            id INTEGER PRIMARY KEY,
            type TEXT)
            ''',

            '''
            INSERT INTO types (type)
            VALUES ("book")
            ''',

            '''
            INSERT INTO types (type)
            VALUES ("blog")
            ''',

            '''
            INSERT INTO types (type)
            VALUES ("podcast")
            ''',

            '''
            INSERT INTO types (type)
            VALUES ("video")
            ''',

            '''
            CREATE TABLE IF NOT EXISTS readingtips (
            id INTEGER PRIMARY KEY, 
            name TEXT,
            description TEXT, 
            type INTEGER REFERENCES types, 
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
            title TEXT NOT NULL,
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
