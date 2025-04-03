from PySide6.QtWidgets import QPushButton

from plugins.accounts.account_screen import AccountScreen


class Account:

    def register(self):
        button = QPushButton(self.tr("Account"))
        button.setObjectName("Account")
        account_screen = AccountScreen()
        account_screen.setup_ui()

        self.add(button, account_screen)

    def unregister(self):
        self.remove("Account")
