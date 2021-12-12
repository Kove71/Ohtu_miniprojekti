"""Io-luokan stub
"""

from entities.book import Book
from entities.blog import Blog
from entities.podcast import Podcast
from entities.video import Video

class StubIO:

    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def write(self, value):
        self.outputs.append(str(value))

    def read(self, prompt=None):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            return "q"

    def add_input(self, value):
        self.inputs.append(value)
