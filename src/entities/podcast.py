"""Luokka podcast-oliolle
"""

class Podcast:
    """Podcast
    """
    def __init__(self, name, episode, url=None, description=None):
        """Podcastin konstruktori
        """
        self.name = name
        self.episode = episode
        self.url = url
        self.description = description

    def __str__(self):
        return f'{self.name} - {self.episode}'
        