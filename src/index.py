"""väliaikasta
"""

from ui.ui import UI
from ui.console_io import ConsoleIO
from repositories.db_interface import DatabaseInterface
from services.readingtip_service import ReadingtipService

def main():
    """Ohjelman päämetodi. Luo käyttöliittymän.
    """
    console_io = ConsoleIO
    database = DatabaseInterface()
    service = ReadingtipService(database)
    program_ui = UI(console_io, service)
    program_ui.start()

if __name__ == "__main__":
    main()
