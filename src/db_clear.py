"""Tyhjentää tietokannan tiedot
"""

from db_connection import get_connection

TABLE_NAMES = ["readingtips", "book", "blog", "podcast", "video"]

def clear_database(database_path = None):
    """Metodi tietokantojen tietojen tyhjentämiseen
    """
    if not database_path:
        database = get_connection()
    else:
        database = get_connection(database_path)

    for name in TABLE_NAMES:
        database.execute(f"DROP TABLE IF EXISTS {name}")

if __name__ == "__main__":
    clear_database()
