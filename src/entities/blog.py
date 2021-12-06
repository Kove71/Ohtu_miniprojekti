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
        self._type = 2

    def type(self):
        return self._type

    def __str__(self):
        string = f"Type: Video\n" \
                f"Name: {self.name}\n" \
                f"Author: {self.author}\n" \
                f"URL: {self.url}\n" \
                f"Title: {self.title if self.title is not None else 'Unknown'}\n" \
                f"Description: {self.description if self.description is not None else 'None'}\n" \
                f"{'Already Read' if self.read else 'Not Read'}\n"   
        return string
        