"""väliaikasta
"""

from ui.ui import UI
from ui.console_io import ConsoleIO
from repositories.db_interface import DatabaseInterface

def main():
    """Ohjelman päämetodi. Luo käyttöliittymän.
    """
    console_io = ConsoleIO
    data_base = DatabaseInterface()
    program_ui = UI(data_base, console_io)
    program_ui.start()

if __name__ == "__main__":
    main()
