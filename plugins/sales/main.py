from PySide6.QtWidgets import QPushButton

from .sales_screen import SalesScreen


class Sales:

    def register(self):
        sales_screen = SalesScreen()
        sales_screen.setup_ui()
        btn = QPushButton(self.tr("Sales"))
        btn.setObjectName("Sales")

        self.add(btn, sales_screen)

    def unregister(self):
        self.remove("Sales")
