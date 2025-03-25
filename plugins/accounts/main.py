from PySide6.QtWidgets import QPushButton

from plugins.accounts.account_screen import AccountScreen
from src.core.plugins.plugin_base import PluginBase


class Account(PluginBase):

    def register(self):
        self.button = QPushButton(self.tr("Account"))
        self.button.setObjectName("Account")
        self.account_screen = AccountScreen()
        self.main_window.add_to_screen(self.button, self.account_screen)

    def unregister(self):
        self.main_window.remove_plugin_btn_screen("Account")
