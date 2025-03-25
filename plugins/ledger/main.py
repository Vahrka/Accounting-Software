from PySide6.QtWidgets import QPushButton

from src.core.plugins.plugin_base import PluginBase

from .ledger_screen import LedgerScreen


class Ledger(PluginBase):

    def register(self):
        ledger_screen = LedgerScreen()
        btn = QPushButton(self.tr("Ledger"))
        btn.setObjectName("Ledger")
        btn.clicked.connect(self.go_to_ledger)

        self.main_window.add_to_screen(btn, ledger_screen)

    def unregister(self):
        self.main_window.remove_plugin_btn_screen("Ledger")

    def go_to_ledger(self):
        self.main_window.go_to_screen(self.ledger_screen_id)
