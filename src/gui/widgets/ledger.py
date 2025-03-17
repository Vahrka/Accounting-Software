from PySide6.QtCore import QSortFilterProxyModel
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QHeaderView, QLineEdit, QTableView, QVBoxLayout

from src.gui.widgets.base_screen import BaseScreen


class LedgerWidget(BaseScreen):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setup_model()

    def setup_ui(self):
        """Initialize the UI components."""
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Search Bar
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search transactions...")
        layout.addWidget(self.search_input)

        # Table View
        self.table_view = QTableView()
        self.table_view.setSelectionBehavior(QTableView.SelectRows)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table_view)

        self.setLayout(layout)

    def setup_model(self):
        """Set up the table model."""
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels([
            "Date", "Description", "From Account", "To Account", "Amount"
        ])

        # Proxy model for filtering
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)
        self.table_view.setModel(self.proxy_model)

        # Add sample data
        self.add_sample_data()

    def add_sample_data(self):
        """Add sample transactions to the model."""
        transactions = [
            ("2024-01-01", "Initial Capital", "Owner's Equity", "Cash", "10000.00"),
            ("2024-01-05", "Office Rent", "Cash", "Expenses", "1500.00"),
            ("2024-01-10", "Client Payment", "Accounts Receivable", "Revenue", "5000.00"),
        ]

        for transaction in transactions:
            items = [QStandardItem(item) for item in transaction]
            self.model.appendRow(items)
