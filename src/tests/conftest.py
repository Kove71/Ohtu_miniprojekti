from db_clear import clear_database

def pytest_configure():
    """Alustaa tietokannan testejä varten"""
    clear_database()
