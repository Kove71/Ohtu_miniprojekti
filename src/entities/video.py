"""Luokka video-oliolle
"""

class Video:
    """Video
    """
    # pylint: disable=locally-disabled, multiple-statements, fixme, too-many-arguments, invalid-name
    # Videon ominaisuudet vaativat useamman kuin 5 parametria

    def __init__(self, id_, name, url, channel=None, description=None, read=None):
        """Videon konstruktori
        """
        self.id = id_
        self.name = name
        self.url = url
        self.description = description if description != "" else None
        self.channel = channel if channel != "" else None
        self.type = 4
        self.read = read

    def __str__(self):
        string = f"\033[1;37;42mVideo {self.id: <50}\033[0;0;0m\n" \
                f"\033[0;32;47mName: \033[0;30;47m{self.name: <50}\033[0;0;0m\n" \
                f"URL: {self.url}\n" \
                f"Channel: {self.channel if self.channel is not None else 'Unknown'}\n" \
                f"Description: " \
                f"{self.description if self.description is not None else 'None'}\033[0;0;0m\n" \
                f"Watched: {'Not watched' if self.read is None else self.read}\n"
        return string

    def short_form(self):
        """Metodi palauttaa video-olion id:n, nimen ja url-osoitteen
        """
        return f"Video {self.id}: {self.name} url:{self.url}"
