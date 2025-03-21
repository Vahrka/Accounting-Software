from typing import override

from PySide6.QtWidgets import QMainWindow, QWidget


class PluginBase(QWidget):
    def __init__(self, main_window: QMainWindow):
        super().__init__()
        self.main_window = main_window

    @override
    def register(self):
        """Register the plugin with the main application."""
        pass

    @override
    def unregister(self):
        """Unregister the plugin from the main application."""
        pass

    def __str__(self):
        return f"<{self.__class__.__name__}Plugin >"

    def __repr__(self):
        return self.__str__()
