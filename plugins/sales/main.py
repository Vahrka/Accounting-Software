from PySide6.QtWidgets import QPushButton, QWidget

from .sales_screen import SalesScreen


class Sales(QWidget):
    def __init__(self, add_func: callable = None, remove_func: callable = None):
        super().__init__()
        self.__add_to_screen = add_func
        self.__remove_plugin_btn_screen = remove_func

    def register(self):
        sales_screen = SalesScreen()
        sales_screen.setup_ui()
        btn = QPushButton(self.tr("Sales"))
        btn.setObjectName("Sales")

        self.add(btn, sales_screen)

    def unregister(self):
        self.remove("Sales")

    def add(self, btn: QPushButton, screen: QWidget):
        self.__add_to_screen(btn, screen)

    def remove(self, name: str):
        self.__remove_plugin_btn_screen(name)

    def __str__(self):
        return f"<{self.__class__.__name__}Plugin >"

    def __repr__(self):
        return self.__str__()
