from database_interface import DatabaseInterface
"""väliaikasta
"""

from ui.ui import UI
from repositories.db_interface import DatabaseInterface

def main():
    """Ohjelman päämetodi. Luo käyttöliittymän.

    returns: 0
    """
<<<<<<< HEAD
    db_io = DatabaseInterface()
=======
    db = DatabaseInterface()
    program_ui = UI(db)
    program_ui.start()
>>>>>>> 85506570d8ceb8633fcc96ad4033a1f849ecc388
    return 0

if __name__ == "__main__":
    main()
