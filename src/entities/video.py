"""Luokka video-oliolle
"""

class Video:
    """Video
    """
    def __init__(self, name, url, channel=None, description=None, read=None):
        """Videon konstruktori
        """
        self.name = name
        self.url = url
        self.channel = channel
        self.description = description

        self._type = 3
        self.read = read

    def __str__(self):
        string = f"Type: Video\n" \
                f"Name: {self.name}\n" \
                f"URL: {self.url if self.url is not None else 'Unknown'}\n" \
                f"Channel: {self.channel if self.channel is not None else 'Unknown'}\n" \
                f"Description: {self.description if self.description is not None else 'None'}\n" \
                f"Watched: {'Yes' if self.read else 'No'}\n"
        return string
        
