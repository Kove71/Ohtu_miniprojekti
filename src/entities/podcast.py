"""Luokka podcast-oliolle
"""

class Podcast:
    """Podcast
    """
    def __init__(self, id, name, episode, url=None, description=None, read=None):
        """Podcastin konstruktori
        """
        self.id = id
        self.name = name
        self.episode = episode
        self.url = url if url != "" else None 
        self.description = description if description != "" else None

        self.read = read
        self.type = 3

    def __str__(self):
        string = f"\033[1;37;40mPodcast {self.id: <69}" \
                f"\033[0;31;47m\nName: \033[0;30;47m{self.name: <50}" \
                f"\033[1;34;0m\nEpisode: {self.episode}\n" \
                f"URL: {self.url if self.url is not None else 'Unknown'}\n" \
                f"Description: {self.description if self.description is not None else 'None'}\033[0;0;0m\n" \
                f"Listened: {'Not listened' if self.read is None else self.read}\n"
        return string
        
    def short_form(self):
        return f"Podcast {self.id}: {self.name} episode {self.episode}"