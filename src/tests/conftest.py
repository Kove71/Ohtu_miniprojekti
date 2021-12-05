from db_clear import clear_database

def pytest_configure():
    clear_database()
