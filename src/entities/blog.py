"""Luokka blogille
"""

class Blog:
    """Luokka kuvaa blogityyppistä lukuvinkkiä
    """
    # pylint: disable=locally-disabled, multiple-statements, fixme, too-many-arguments, too-many-instance-attributes
    # Blogin ominaisuudet vaativat useamman kuin 5 parametria

    def __init__(self, id, name, author, url, title=None, description=None, read=None):
        """
        """
        self.id = id
        self.name = name
        self.author = author
        self.url = url
        self.description = description if description != "" else None
        self.title = title if title != "" else None
        self.read = read
        self.type = 2

    def __str__(self):
        string = f"\033[1;37;41mBlog {self.id: <51}\033[0;0;0m\n" \
                f"\033[0;31;47mName: \033[0;30;47m{self.name: <50}\033[0;0;0m\n" \
                f"Author: {self.author}\n" \
                f"Blogpost title: {self.title if self.title is not None else 'Unknown'}\n" \
                f"URL: {self.url}\n" \
                f"Description: {self.description if self.description is not None else 'None'}\n" \
                f"Read: {'Not read' if self.read is None else self.read}\n"
        return string

    def short_form(self):
        """Palauttaa blogin id:n, nimen ja tekijän string- muodossa
        """
        return f"Blog {self.id}: {self.name} by {self.author}"
