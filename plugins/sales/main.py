from PySide6.QtWidgets import QPushButton

from src.core.plugins.plugin_base import PluginBase

from .sales_screen import SalesScreen


class Sales(PluginBase):

    def register(self):
        self.ledger_screen = SalesScreen()
        self.btn = QPushButton(self.tr("Sales"))
        self.btn.setObjectName("Sales")

        self.main_window.add_to_screen(self.btn, self.ledger_screen)

    def unregister(self):
        self.main_window.remove_plugin_btn_screen("Sales")

    def go_to_ledger(self):
        self.main_window.go_to_screen(self.ledgr_screen_id)
