from db_connection import get_connection
from db_clear import clear_database

def build_database():
    database_name = "readingtips.db"
    database = get_connection(database_name)
    sql = "CREATE TABLE IF NOT EXISTS readingtips (id INTEGER PRIMARY KEY, description TEXT)"
    database.execute(sql)

if __name__ == "__main__":
    clear_database()
    build_database()
