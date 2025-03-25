from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget


class LedgerScreen(QWidget):

    def setup_ui(self):
        layout = QVBoxLayout()
        self.button = QPushButton("Ledger")
        layout.addWidget(self.button)
        self.setLayout(layout)
