"""väliaikasta
"""

from ui.ui import UI
from repositories.db_interface import DatabaseInterface

def main():
    """Ohjelman päämetodi. Luo käyttöliittymän.

    returns: 0
    """
    data_base = DatabaseInterface()
    program_ui = UI(data_base)
    program_ui.start()
    return 0

if __name__ == "__main__":
    main()
