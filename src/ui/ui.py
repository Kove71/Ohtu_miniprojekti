"""Yksinkertainen tekstikäyttöliittymä.
"""
from entities.readingtip import ReadingTip
from repositories.db_interface import DatabaseInterface
from ui.console_io import ConsoleIO

class UI:
    """Käyttöliittymäluokka, joka pystyy lisäämään ja
    näyttämään lukuvinkkejä.
    Args:
        data: tietokanta
        console_io: io 
    """

    def __init__(self, database: DatabaseInterface, console_io: ConsoleIO):
        self._actions = {
            "a": "add a new item",
            "v": "view your items",
            "r": "remove an item",
            "q": "exit program"
        }
        self._io = console_io
        self.database = database

    def start(self):
        """Käyttöliittymälooppi. Kysyy toimintaa ja kutsuu
        sen perusteella toiminnan käsittelevää metodia.
        """
        self._io.write("Reading tips")

        while True:
            self.print_actions()
            action = self._io.read()

            if action == "v":
                self._view_items()
            elif action == "a":
                self._add_item()
            elif action == "r":
                self._remove_item()
            elif action == "q":
                break
            else:
                self._io.write("\ncommand not found\n")
                continue

    def print_actions(self):
        """Tulostaa vaihtoehdot
        """
        self._io.write("\nchoose action:")
        for key, item in self._actions.items():
            self._io.write((f"\"{key}\": {item}"))


    def _add_item(self):
        """Kysyy lukuvinkin tiedot ja lisää sen listaan
        """
        description = self._io.read("item description: ")
        item = ReadingTip(description)
        self.database.add(item)

        self._io.write(f"\nitem {item} added \n")


    def _view_items(self):
        """Näyttää listan lukuvinkit
        """
        self._io.write("\nitems: \n")
        for index, item in enumerate(self.database.read()):
            self._io.write(f'{index+1}: {item}')


    def _remove_item(self):
        """Poistaa yhden lukuvinkin
        """
        try:
            index = int(self._io.read("Clear which item?\n"))
        except:
            self._io.write("Invalid selection")
            return
        
        self.database.remove_tip(index)

