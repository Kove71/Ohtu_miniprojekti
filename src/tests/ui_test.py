import unittest
from unittest.mock import Mock, ANY, patch
from ui.ui import UI

class TestUi(unittest.TestCase):
    def setUp(self):
        self.console_io_mock = Mock()
        self.service_mock = Mock()
        self.service_mock.get_items.terurn_value = "book"
        self.ui = UI(self.console_io_mock, self.service_mock)
    
    def test_print_actions(self):
        self.ui.print_actions()
        self.console_io_mock.write.assert_called()
    
    def test_remove_item(self):
        self.service_mock.get_items.assert_called()
        self.console_io.write.assert_called()


