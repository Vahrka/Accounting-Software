from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget


class AccountScreen(QWidget):

    def setup_ui(self):
        layout = QVBoxLayout()
        self.button = QPushButton("Account")
        layout.addWidget(self.button)
        self.setLayout(layout)
