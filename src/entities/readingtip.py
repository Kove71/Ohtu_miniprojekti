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

    def type(self):
        """Metodi joka palauttaa lukuvinkin tyypin,
        perusluokassa None

        returns: None
        """
        return None

    def __str__(self):
        return self.description
