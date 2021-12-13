# pylint: disable=invalid-name
"""Hyväksymistestausluokka
"""

#Pylint disablettu toistaiseksi
import datetime
from stub_io import StubIO # pylint: disable=import-error
from ui.ui import UI
from repositories.db_interface import DatabaseInterface
from db_build import build_database
from db_clear import clear_database
from services.readingtip_service import ReadingtipService
class ReadingtipLibrary: # pylint: disable=invalid-name
    """Luokka joka vastaa vaatimusten testaamisesta
    """

    def __init__(self):
        """Luokan konstruktori
        """
        self._io = StubIO()
        self.db_name = "test_db.db"
        clear_database(self.db_name)
        build_database(self.db_name)
        self.database = DatabaseInterface(self.db_name)
        self.service = ReadingtipService(self.database)

        self._ui = UI(self._io, self.service)
        

    def input(self, value):
        """Luo syötteen
        """
        self._io.add_input(value)

    def output_should_contain(self, value):
        """Tarkistaa tulosteen
        """
        words = value.split()
        outputs = self._io.outputs

        for output in outputs:
            found = True
            for word in words:
                if not word in output:
                    found = False
                    break
            if found:
                break

        if not found:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def output_should_not_contain(self, value):
        """Tarkistaa että tulosteesta ei löydy annettua tekstiä
        """
        words = value.split()
        outputs = self._io.outputs

        for output in outputs:
            found = True
            for word in words:
                if not word in output:
                    found = False
                    break
            if found:
                break

        if found :
            raise AssertionError(
                f"Output \"{value}\" is in {str(outputs)}"
            )

    def clear_output(self):
        """Tyhjentää tulosteen
        """
        self._io.clear_outputs()


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

    def check_tip_is_read(self):
        """Tarkistaa että vinkki on merkattu luetuksi oikealla päivämäärällä
        """
        now = datetime.datetime.now()
        string_to_find = f'{now.year}-{now.month}-{now.day}'
        found = False

        for output in self._io.outputs:
            if string_to_find in output:
                found = True

        if not found:
            raise AssertionError(
                f"not marked as read / watched / listened, outputs: {self._io.outputs}"
            )