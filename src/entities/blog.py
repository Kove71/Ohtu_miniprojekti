"""Luokka blogille
"""

class Blog:
    """Luokka kuvaa blogityyppistä lukuvinkkiä
    """
    def __init__(self, id, name, author, url, title=None, description=None, read=None):
        """
        """
        self.id = id
        self.name = name
        self.author = author
        self.url = url
        self.description = description
        self.title = title

        self.read = read
        self.type = 3

    def __str__(self):
        string = f"ID - {self.id} \n" \
                f"Name: {self.name}\n" \
                f"Author: {self.author}\n" \
                f"URL: {self.url if self.url is not None else 'Unknown'}\n" \
                f"Description: {self.description if self.description is not None else 'None'}\n" 
                #f"Read: {'Yes' if self.read else 'No'}\n"
        return string

    def short_form(self):
        return f"Blog {self.id}: {self.name} by {self.author}"
