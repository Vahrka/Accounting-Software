from PySide6.QtWidgets import QPushButton

from plugins.accounts.account_screen import AccountScreen
from src.core.plugins.plugin_base import PluginBase


class Account(PluginBase):

    def register(self):
        button = QPushButton(self.tr("Account"))
        button.setObjectName("Account")
        account_screen = AccountScreen()

        self.add(button, account_screen)

    def unregister(self):
        self.remove("Account")
