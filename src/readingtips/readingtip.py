"""Contains the base class for reading tips
"""

class ReadingTip:
    """Base class for reading tips that contains their description 
    """
    def __init__(self, description):
        """
        Args:
            str description: 
        """
        self.description = description

    def __str__(self):
        return self.description