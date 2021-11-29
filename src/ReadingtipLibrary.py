#from readingtips.readingtip import ReadingTip
from stub_io import StubIO

class ReadingtipLibrary:

    def __init__(self):
        self._io = StubIO()

    def input(self, value):
        self._io.initial_add(value)

    def output_should_contain(self, value):
        outputs = self._io.output

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )


    def run_application(self):
        self._io.start()

    def last_output_should_contain(self, value):
        if len(self._io.output) > 0:
            return self._io.output.pop(0)
        else:
            return ""

    def database_must_be_empty(self):
        if len(self._io.db) > 0:
            raise AssertionError(
                "Database is not empty"
            )
