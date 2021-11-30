"""Yksinkertainen tekstikäyttöliittymä.
"""
from entities.readingtip import ReadingTip
from repositories.db_interface import DatabaseInterface

class UI:
    """Käyttöliittymäluokka, joka pystyy lisäämään ja
    näyttämään lukuvinkkejä.
    """

    def __init__(self, data_base: DatabaseInterface):
        self._actions = {
            "a": "add a new item",
            "v": "view your items",
            "c": "clear all items",
            "q": "exit program"
        }

        self.database = data_base

    def start(self):
        """Käyttöliittymälooppi. Kysyy toimintaa ja kutsuu
        sen perusteella toiminnan käsittelevää metodia.
        """
        print("Reading tips")

        while True:
            self.print_actions()
            action = input()

            if action == "v":
                self._view_items()
            elif action == "a":
                self._add_item()
            elif action == "c":
                self._clear_database()
            elif action == "q":
                self.database.delete()
                break
            else:
                print("\ncommand not found\n")
                continue

    def print_actions(self):
        """Tulostaa vaihtoehdot
        """
        print("choose action:")
        for key, item in self._actions.items():
            print(f"\"{key}\": {item}")


    def _add_item(self):
        """Kysyy lukuvinkin tiedot ja lisää sen listaan
        """
        description = input("item description: ")
        item = ReadingTip(description)
        self.database.add(item)

        print(f"\nitem {item} added \n")


    def _view_items(self):
        """Näyttää listan lukuvinkit
        """
        print("\nitems: \n")
        for index, item in enumerate(self.database.read()):
            print(f'{index+1}: {item}')
        print("")


    def _clear_database(self):
        """Poistaa kaikki lukuvinkit
        """
        self.database.clear()
