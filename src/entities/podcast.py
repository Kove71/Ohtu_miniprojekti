"""Luokka podcast-oliolle
"""

class Podcast:
    """Podcast
    """
    # pylint: disable=locally-disabled, multiple-statements, fixme, too-many-arguments, invalid-name
    # Podcastin ominaisuudet vaativat useamman kuin 5 parametria

    def __init__(self, id_, name, episode, url=None, description=None, read=None):
        """Podcastin konstruktori
        """
        self.id = id_
        self.name = name
        self.episode = episode
        self.url = url if url != "" else None
        self.description = description if description != "" else None
        self.read = read
        self.type = 3

    def __str__(self):
        string = f"\033[1;37;45mPodcast {self.id: <48}\033[0;0;0m\n" \
                f"\033[0;35;47mName: \033[0;30;47m{self.name: <50}\033[0;0;0m\n" \
                f"Episode: {self.episode}\n" \
                f"URL: {self.url if self.url is not None else 'Unknown'}\n" \
                f"Description: " \
                f"{self.description if self.description is not None else 'None'}\033[0;0;0m\n" \
                f"Listened: {'Not listened' if self.read is None else self.read}\n"
        return string

    def short_form(self):
        """Metodi palauttaa podcast-olion id:n, nimen ja jakson
        """
        return f"Podcast {self.id}: {self.name} episode {self.episode}"
    