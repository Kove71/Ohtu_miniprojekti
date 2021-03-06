"""Luokka kirjaoliolle
"""

class Book:
    """Kirja
    """
    # pylint: disable=locally-disabled, multiple-statements, fixme, too-many-arguments, invalid-name
    # Kirjan ominaisuudet vaativat useamman kuin 5 parametria

    def __init__(self, id_, name, author, isbn=None, description=None, read=None):
        """Kirjan konstruktori
        """
        self.id = id_
        self.name = name
        self.author = author
        self.isbn = isbn or None
        self.description = description or None
        self.read = read
        self.type = 1

    def __str__(self):
        string = f"\033[1;37;44mBook {self.id: <51}\033[0;0;0m\n" \
                f"\033[0;34;47mName: \033[0;30;47m{self.name: <50}\033[0;0;0m\n" \
                f"Author: {self.author}\n" \
                f"ISBN: {self.isbn if self.isbn is not None else 'Unknown'}\n" \
                f"Description: " \
                f"{self.description if self.description is not None else 'None'}\033[0;0;0m\n" \
                f"Read: {'Not read' if self.read is None else self.read}\n"
        return string

    def short_form(self):
        """Palauttaa kirja-olion id:n, nimen ja tekijän
        """
        return f"Book {self.id}: {self.name} by {self.author}"
