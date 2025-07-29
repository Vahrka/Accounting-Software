from typing import Callable, override

from PySide6.QtWidgets import QPushButton, QWidget


class PluginBase(QWidget):
    def __init__(self, add_func: Callable = None, remove_func: Callable = None):
        super().__init__()
        self.__add_to_screen = add_func
        self.__remove_plugin_btn_screen = remove_func

    @override
    def register(self):
        """Register the plugin with the main application."""
        pass

    @override
    def unregister(self):
        """Unregister the plugin from the main application."""
        pass

    def add(self, btn: QPushButton, screen: QWidget):
        self.__add_to_screen(btn, screen)

    def remove(self, name: str):
        self.__remove_plugin_btn_screen(name)

    def __str__(self):
        return f"<{self.__class__.__name__}Plugin >"

    def __repr__(self):
        return self.__str__()
