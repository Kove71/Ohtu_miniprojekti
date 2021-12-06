"""Luokka video-oliolle
"""

class Video:
    """Video
    """
    def __init__(self, name, url, channel=None, description=None, read=False):
        """Videon konstruktori
        """
        self.name = name
        self.url = url
        self.channel = channel
        self.description = description

        self.read = read
        self._type = 4

    def type(self):
        return self._type

    def __str__(self):
        string = f"Type: Video\n" \
                f"Name: {self.name}\n" \
                f"URL: {self.url}\n" \
                f"Channel: {self.channel if self.channel is not None else 'Unknown'}\n" \
                f"Description: {self.description if self.description is not None else 'None'}\n" \
                f"{'Already watched' if self.read else 'Not watched'}\n"   
        return string
        