"""Luokka podcast-oliolle
"""

class Podcast:
    """Podcast
    """
    def __init__(self, name, episode, url=None, description=None, read=False):
        """Podcastin konstruktori
        """
        self.name = name
        self.episode = episode
        self.url = url
        self.description = description

        self.read = read
        self._type = 3

    def type(self):
        return self._type

    def __str__(self):
        string = f"Type: Podcast\n" \
                f"Name: {self.name}\n" \
                f"Episode: {self.author}\n" \
                f"URL: {self.url if self.url is not None else 'Unknown'}\n" \
                f"Description: {self.description if self.description is not None else 'None'}\n" \
                f"{'Already listened' if self.read else 'Not Listened'}\n"   
        return string
        