"""Luokka kirjaoliolle
"""

class Book:
    """Kirja
    """
    def __init__(self, id, name, author, isbn=None, description=None, read=None):
        """Kirjan konstruktori
        """
        self.id = id
        self.name = name
        self.author = author
        self.isbn = isbn or None
        self.description = description or None

        self.read = read
        self.type = 1

    def __str__(self):
        string = f"ID - {self.id} \n" \
                f"\033[92mName: {self.name}\n" \
                f"\033[93mAuthor: {self.author}\n" \
                f"ISBN: {self.isbn if self.isbn is not None else 'Unknown'}\n" \
                f"Description: {self.description if self.description is not None else 'None'}\033[0m\n"
                #f"Read: {'Yes' if self.read else 'No'}\n"
        return string
