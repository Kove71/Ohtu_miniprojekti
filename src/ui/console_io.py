"""Lukee ja kirjoittaa konsolille käyttöliittymää varten"""

class ConsoleIO:
    """Luokka vastaa konsoliin kirjoittamisesta ja sieltä
    lukemisesta
    """

    def read(input_text = ""):
        """konsolin input
        Args:
            input_syötteen teksti
        Returns:
            value: käyttäjän antama syöte
        """
        value = input(input_text)
        return value

    def write(text = ""):
        """Tulostaa tekstin konsolille
        Args:
            text: konsolille tulostettava syöte
        """
        print(text)
