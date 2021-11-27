"""Yksinkertainen tekstikäyttöliittymä.
"""
from entities.lukuvinkki import LukuVinkki

class UI:
    """Käyttöliittymäluokka, joka pystyy lisäämään ja
    näyttämään lukuvinkkejä.
    """

    def __init__(self):
        self.actions = {
            "a": "add a new item",
            "v": "view your items",
            "q": "exit program"
        }
        #korvataan ku tietokanta tulee
        self.items = []

    def start(self):
        """Käyttöliittymälooppi. Kysyy toimintaa ja kutsuu
        sen perusteella toiminnan käsittelevää metodia.
        """
        print("Recommendations")

        while True:
            self._print_actions()
            action = input()

            if action == "v":
                self._view_items()
            elif action == "a":
                self._add_item()
            elif action == "q":
                break
            else:
                print("\ncommand not found\n")
                continue

    def _print_actions(self):
        """Tulostaa vaihtoehdot
        """
        print("choose action:")
        for i in self.actions:
            print(f"\"{i}\": {self.actions[i]}")


    def _add_item(self):
        """Kysyy lukuvinkin tiedot ja lisää sen listaan
        """
        description = input("item description: ")
        item = LukuVinkki(description)

        #väliaikanen korvataan kun tietokanta tulee käyttöön
        self.items.append(item)

        print(f"\nitem {item} added \n")


    def _view_items(self):
        """Näyttää listan lukuvinkit
        """
        print("\nitems: \n")
        for i, item in enumerate(self.items):
            print(i + 1, item, "\n")
