class ReadingtipLibrary:

    def __init__(self):
        self.value = "value"

    def input(self, value):
        self.value = value

    def output_should_contain(self, value):
        self.value = value
