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
    sql = '''CREATE TABLE IF NOT EXISTS readingtips (
        id INTEGER PRIMARY KEY, 
        name TEXT,
        description TEXT, 
        type INTEGER, 
        visible INTEGER, 
        read INTEGER)'''
    database.execute(sql)

if __name__ == "__main__":
    clear_database()
    build_database()
