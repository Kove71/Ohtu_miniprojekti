"""Luokka video-oliolle
"""

class Video:
    """Video
    """
    def __init__(self, name, url, channel=None, description=None):
        """Videon konstruktori
        """
        self.name = name
        self.url = url
        self.channel = channel
        self.description = description

    def __str__(self):
        return f'"{self.name}", url: {self.url}"'