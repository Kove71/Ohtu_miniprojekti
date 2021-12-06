# pylint: disable=invalid-name
"""Hyväksymistestausluokka
"""

#Pylint disablettu toistaiseksi
from stub_io import StubIO # pylint: disable=import-error
from ui.ui import UI
from repositories.db_interface import DatabaseInterface
class ReadingtipLibrary: # pylint: disable=invalid-name
    """Luokka joka vastaa vaatimusten testaamisesta
    """

    def __init__(self):
        """Luokan konstruktori
        """
        self._io = StubIO()
        self.database = DatabaseInterface()
        self._ui = UI(self.database, self._io)

    def input(self, value):
        """Luo syötteen
        """
        self._io.add_input(value)

    def output_should_contain(self, value):
        """Tarkistaa tulosteen
        """
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )


    def run_application(self):
        """Käynnistää sovelluksen
        """
        self._ui.start()

    def last_output_should_contain(self, value):
        """Tarkistaa viimeisen tulosteen
        """
        if len(self._io.outputs) > 0:
            lastoutput = self._io.output.pop()
        else:
            lastoutput = ""
        if lastoutput != value:
            raise AssertionError(
                f"{value} is not in {lastoutput}"
            )


