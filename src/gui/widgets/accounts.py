from PySide6.QtWidgets import (QInputDialog, QListWidget, QPushButton,
                               QVBoxLayout)

from src.gui.widgets.base_screen import BaseScreen


class AccountsWidget(BaseScreen):

    def setup_ui(self):
        """Initialize the UI components."""
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Accounts List
        self.accounts_list = QListWidget()
        layout.addWidget(self.accounts_list)

        # Add Account Button
        self.add_button = QPushButton("Add Account")
        self.add_button.clicked.connect(self.add_account)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

        # Load sample accounts
        self.load_sample_accounts()

    def load_sample_accounts(self):
        """Load sample accounts into the list."""
        accounts = ["Cash", "Accounts Receivable", "Revenue", "Expenses"]
        self.accounts_list.addItems(accounts)

    def add_account(self):
        """Add a new account to the list."""
        account_name, ok = QInputDialog.getText(self, "Add Account", "Account Name:")
        if ok and account_name:
            self.accounts_list.addItem(account_name)
