"""Luokka kirjaoliolle
"""

class Book:
    """Kirja
    """
    def __init__(self, name, author, isbn=None, description=None):
        """Kirjan konstruktori
        """
        self.name = name
        self.author = author
        self.isbn = isbn or None
        self.description = description or None

    def __str__(self):
        return f'{self.author}: "{self.name}"'