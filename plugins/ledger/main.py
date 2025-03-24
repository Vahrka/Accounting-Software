from PySide6.QtWidgets import QPushButton

from src.core.plugins.plugin_base import PluginBase

from .ledger_screen import LedgerScreen


class Ledger(PluginBase):

    def register(self):
        self.ledger_screen = LedgerScreen()
        self.ledgr_screen_id = self.main_window.add_screen_to_stack(self.ledger_screen)
        self.btn = QPushButton(self.tr("Ledger"))
        self.btn.clicked.connect(self.go_to_ledger)

        self.main_window.add_btn_to_nav(self.btn)

    def go_to_ledger(self):
        self.main_window.go_to_screen(self.ledgr_screen_id)
