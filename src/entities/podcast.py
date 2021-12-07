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
        self.type = 2

    def __str__(self):
        string = f"\nName: {self.name}\n" \
                f"Episode: {self.episode}\n" \
                f"URL: {self.url if self.url is not None else 'Unknown'}\n" \
                f"Description: {self.description if self.description is not None else 'None'}\n"
                #f"Read: {'Yes' if self.read else 'No'}\n"
        return string
        