"""Luokka blogille
"""

class Blog:
    """Luokka kuvaa blogityyppistä lukuvinkkiä
    """
    def __init__(self, name, author, url, title=None, description=None):
        """
        """
        self.name = name
        self.author = author
        self.url = url
        self.title = title or None
        self.description = description or None

    def __str__(self):
        """Palauttaa nimen, tekijän ja urlin
        """
        return_string = f'{self.author}: {self.name}'
        if self.title != "":
            return_string += f' - ({self.title})'
        return_string += f', url: {self.url}'

        return return_string