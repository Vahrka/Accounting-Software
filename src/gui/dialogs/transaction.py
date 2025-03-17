from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel,
                               QLineEdit, QDateEdit, QComboBox, QDialogButtonBox)
from PySide6.QtCore import QDate

class TransactionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Transaction")
        self.setMinimumWidth(400)
        self.setup_ui()

    def setup_ui(self):
        """Initialize the dialog UI"""
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Date
        layout.addWidget(QLabel("Date:"))
        self.date_input = QDateEdit()
        self.date_input.setDate(QDate.currentDate())
        layout.addWidget(self.date_input)

        # Description
        layout.addWidget(QLabel("Description:"))
        self.description_input = QLineEdit()
        layout.addWidget(self.description_input)

        # From Account
        layout.addWidget(QLabel("From Account:"))
        self.from_account_input = QComboBox()
        self.from_account_input.addItems(["Cash", "Accounts Receivable", "Expenses"])
        layout.addWidget(self.from_account_input)

        # To Account
        layout.addWidget(QLabel("To Account:"))
        self.to_account_input = QComboBox()
        self.to_account_input.addItems(["Revenue", "Owner's Equity", "Accounts Payable"])
        layout.addWidget(self.to_account_input)

        # Amount
        layout.addWidget(QLabel("Amount:"))
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("0.00")
        layout.addWidget(self.amount_input)

        # Buttons
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)

    def get_transaction_data(self):
        """Get the transaction data from the form"""
        return [
            self.date_input.date().toString("yyyy-MM-dd"),
            self.description_input.text(),
            self.from_account_input.currentText(),
            self.to_account_input.currentText(),
            self.amount_input.text(),
        ]