"""väliaikasta
"""

from ui.ui import UI

def main():
    """Ohjelman päämetodi. Luo käyttöliittymän.

    returns: 0
    """
    program_ui = UI()
    program_ui.start()
    return 0

if __name__ == "__main__":
    main()
