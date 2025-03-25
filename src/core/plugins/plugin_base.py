from typing import override

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QPushButton, QWidget


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

    def add(self, btn: QPushButton, screen: QWidget):
        self.main_window.add_to_screen(btn, screen)

    def remove(self, name: str):
        self.main_window.remove_plugin_btn_screen(name)
        

    def __str__(self):
        return f"<{self.__class__.__name__}Plugin >"

    def __repr__(self):
        return self.__str__()

    @Slot(str)
    def __btn_removed(self, btn_id):
        print(btn_id)
