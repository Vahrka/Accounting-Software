from PySide6.QtWidgets import QPushButton

from src.core.plugins.plugin_base import PluginBase

from .ledger_screen import LedgerScreen


class Ledger(PluginBase):

    def register(self):
        ledger_screen = LedgerScreen()
        ledger_screen.setup_ui()
        btn = QPushButton(self.tr("Ledger"))
        btn.setObjectName("Ledger")

        self.add(btn, ledger_screen)

    def unregister(self):
        self.remove("Ledger")
