"""Luokka blogille
"""

class Blog:
    """Luokka kuvaa blogityyppistä lukuvinkkiä
    """
    def __init__(self, name, author, url, title=None, description=None, read=False):
        """
        """
        self.name = name
        self.author = author
        self.url = url
        self.title = title
        self.description = description

        self.read = read
        self.type = 3

    def __str__(self):
        string = f"Type: Blog\n" \
                f"Name: {self.name}\n" \
                f"Author: {self.author}\n" \
                f"Title: {self.title if self.title is not None else 'No title'}\n"    \
                f"URL: {self.url if self.url is not None else 'Unknown'}\n" \
                f"Description: {self.description if self.description is not None else 'None'}\n" \
                f"Read: {'Yes' if self.read else 'No'}\n"
        return string
