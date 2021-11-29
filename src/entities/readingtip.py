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
        self._type = None
        self.description = description

    def type(self):
        """Metodi joka palauttaa lukuvinkin tyypin,
        perusluokassa None

        returns: None
        """
        return self._type

    def __str__(self):
        return self.description
