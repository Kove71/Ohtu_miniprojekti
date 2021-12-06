"""Luokka kirjaoliolle
"""

class Book:
    """Kirja
    """
    def __init__(self, name, author, isbn=None, description=None, read=False):
        """Kirjan konstruktori
        """
        self.name = name
        self.author = author
        self.isbn = isbn or None
        self.description = description or None

        self.read = read
        self.type = 1

    def __str__(self):
        string = f"Type: Book\n" \
                f"Name: {self.name}\n" \
                f"Author: {self.author}\n" \
                f"ISBN: {self.isbn if self.isbn is not None else 'Unknown'}\n" \
                f"Description: {self.description if self.description is not None else 'None'}\n" \
                f"Read: {'Yes' if self.read else 'No'}\n"
        return string
