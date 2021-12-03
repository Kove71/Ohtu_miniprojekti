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
        return_string = f'{self.name}: episode "{self.episode}"'
        if self.url:
            return_string += f', url: {self.url}'
        
        return return_string