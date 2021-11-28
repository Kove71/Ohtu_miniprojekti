"""väliaikasta
"""

from ui.ui import UI
from repositories.db_interface import DatabaseInterface

def main():
    """Ohjelman päämetodi. Luo käyttöliittymän.

    returns: 0
    """
    db = DatabaseInterface()
    program_ui = UI(db)
    program_ui.start()
    return 0

if __name__ == "__main__":
    main()
