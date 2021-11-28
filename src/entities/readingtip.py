"""Sisältää perus lukuvinkki luokan
"""

class ReadingTip:
    """Perus lukuvinkki luokka joka sisältää kuvauksen
    """
    def __init__(self, description):
        """
        Args:
            str description: Kuvaus lukuvinkistä
        """
        self.description = description

    def __str__(self):
        return self.description