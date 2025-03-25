from PySide6.QtWidgets import QPushButton

from src.core.plugins.plugin_base import PluginBase

from .sales_screen import SalesScreen


class Sales(PluginBase):

    def register(self):
        sales_screen = SalesScreen()
        sales_screen.setup_ui()
        btn = QPushButton(self.tr("Sales"))
        btn.setObjectName("Sales")

        self.add(btn, sales_screen)

    def unregister(self):
        self.remove("Sales")
