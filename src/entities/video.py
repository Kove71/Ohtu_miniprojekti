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
        self.description = description if description != "" else None
        self.channel = channel if channel != "" else None
        self.id = id
        self.type = 4
        self.read = read

    def __str__(self):
        string = f"\033[1;37;40mVideo {self.id: <71}" \
                f"\033[0;31;47m\nName: \033[0;30;47m{self.name: <50}" \
                f"\033[1;34;0m\nURL: {self.url}\n" \
                f"ISBN: {self.channel if self.channel is not None else 'Unknown'}\n" \
                f"Description: {self.description if self.description is not None else 'None'}\033[0;0;0m\n" \
                f"Watched: {'Not watched' if self.read is None else self.read}\n"
        return string
        
    def short_form(self):
        return f"Video {self.id}: {self.name} url:{self.url}"