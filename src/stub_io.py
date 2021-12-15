"""Io-luokan stub
"""

class StubIO:
    """Io-luokan stub
    """

    def __init__(self, inputs=None):
        """Luokan konstruktori
        """
        self.inputs = inputs or []
        self.outputs = []

    def write(self, value):
        """Lisää annetun parametrin outputs-listalle
        """
        self.outputs.append(str(value))

    def read(self, prompt=None):
        """Palauttaa viimeisimmän alkion inputs-listalta
        """
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            return "q"

    def add_input(self, value):
        """Lisää annetun parametrin inputs-listalle
        """
        self.inputs.append(value)

    def clear_outputs(self):
        """Poistaa kakki alkiot outpust-listalta
        """
        self.outputs.clear()
