from db_connection import get_connection

TABLE_NAMES = ["readingtips", "book", "blog", "podcast", "video"]

def clear_database():
    database_name = "readingtips.db"
    database = get_connection(database_name)
    for name in TABLE_NAMES:
        database.execute(f"DROP TABLE IF EXISTS {name}")

if __name__ == "__main__":
    clear_database()