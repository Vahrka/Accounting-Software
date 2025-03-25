from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget


class SalesScreen(QWidget):

    def setup_ui(self):
        layout = QVBoxLayout()
        self.button = QPushButton("Sales")
        layout.addWidget(self.button)
        self.setLayout(layout)
