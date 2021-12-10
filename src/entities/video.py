"""Luokka video-oliolle
"""

class Video:
    """Video
    """
    def __init__(self, id, name, url, channel=None, description=None, read=None):
        """Videon konstruktori
        """
        self.id = id
        self.name = name
        self.url = url
        self.description = description
        self.channel = channel
        self.id = id
        self.type = 4
        self.read = read

    def __str__(self):
        string = f"Video {self.id}" \
                f"\n\033[92mName: {self.name}\n" \
                f"\033[93mURL: {self.url if self.url is not None else 'Unknown'}\n" \
                f"Channel: {self.channel if self.channel is not None else 'Unknown'}\n" \
                f"Description: {self.description if self.description is not None else 'None'}\n" \
                f"Watched: {self.read}\033[0m\n"
        return string
        
