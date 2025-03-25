from PySide6.QtWidgets import QPushButton

from src.core.plugins.plugin_base import PluginBase

from .sales_screen import SalesScreen


class Sales(PluginBase):

    def register(self):
        self.ledger_screen = SalesScreen()
        self.btn = QPushButton(self.tr("Sales"))
        self.btn.setObjectName("Sales")

        self.add(self.btn, self.ledger_screen)

    def unregister(self):
        self.remove("Sales")
