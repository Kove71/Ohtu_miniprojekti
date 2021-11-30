"""Käyttöliittymäsimulaatio
"""

class StubIO:
    """
    Luokka simuloi käyttöliittymän toimintaa
    """

    def __init__(self):
        """
        Alustaa käyttöliittymäsimulaation
        """
        self.actions = {
            "a": "add readingtip",
            "v": "view readingtips",
            "c": "clear all readingtips",
            "q": "exit"
        }
        self.database = []
        self.output = []
        self.input = []

    def start(self):
        """
        Simuloi käyttöliittymän käynnistämistä
        """
        while True:

            action = self.read()
            if not action:
                break

            if action == "v":
                self._view_all()
            elif action == "a":
                self._add_readingtip()
            elif action == "c":
                self._clean_db()
            elif action == "q":
                self.database = []
                break
            else:
                self.output.append("command not found")
                continue

    def _print_actions(self):
        """
        Tulostaa kaikki käyttöliittymän toiminnot
        """
        self.output.append("choose action:")
        for i in self.actions:
            self.output.append(i)

    def _add_readingtip(self):
        """
        Simuloi lukuvinkin lisäämistä käyttöliittymään
        """
        description = self.read()
        self.database.append(description)
        self.output.append(f'item {description}' + " added")

    def _view_all(self):
        """
        Simuloi käyttöliittymän tulostustoimintaa
        """
        self.output.append("items: ")
        for i in self.database:
            self.output.append(i)


    def _clean_db(self):
        """
        Simuloi käyttöliittymän lukuvinkkien poistamistoimintaa
        """
        self.database = []

    def read(self):
        """
        Lukee annetuista syötteistä ensimmäisen
        """
        if len(self.input) > 0:
            return self.input.pop(0)
        return ""

    def initial_add(self, value):
        """
        Lisää annetun syötteen suoritusjonoon
        """
        self.input.append(value)
