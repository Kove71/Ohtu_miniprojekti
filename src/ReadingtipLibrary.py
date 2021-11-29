"""
Hyväksymistestausta
"""
from stub_io import StubIO

class ReadingtipLibrary:
    """
    Luokka vastaa kommunikoinnista käyttöliittymän ja testitapausten välillä
    """

    def __init__(self):
        """
        Luokan alustus
        """

        self._io = StubIO()

    def input(self, value):
        """
        Lisää syötteen käyttöliittymän suoritusjonoon
        """
        self._io.initial_add(value)

    def output_should_contain(self, value):
        """
        Tarkistaa, löytyykö annettu syöte käyttöliittymän tulostuksista
        """
        outputs = self._io.output

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )


    def run_application(self):
        """
        Käynnistää käyttöliittymän
        """
        self._io.start()

    def last_output_should_contain(self, value):
        """
        Tarkistaa, vastaako viimeisin tuloste annettua syötettä
        """
        if len(self._io.output) > 0:
            lastoutput = self._io.output.pop()
        else:
            lastoutput =  ""
        if lastoutput != value:
            raise AssertionError(
                f"{value} is not in {lastoutput}"
            )

    def database_must_be_empty(self):
        """
        Tarkistaa, onko tietokanta tyhjä
        """
        if len(self._io.database) > 0:
            raise AssertionError(
                "Database is not empty"
            )
