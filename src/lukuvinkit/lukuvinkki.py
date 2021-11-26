"""Sisältää perusluokan lukuvinkeille
"""

class LukuVinkki:
    """Perusluokka lukuvinkeille
    """
    def __init__(self, kuvaus):
        """
        Args:
            str kuvaus, lukuvinkin kuvaus
        """
        self.kuvaus = kuvaus

    def __str__(self):
        return self.kuvaus