from pathlib import Path

from PySide6.QtWidgets import QWidget

from .ui.form_ui import Ui_Form


class SalesScreen(QWidget):

    def setup_ui(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.tabs.setTabText(0, self.tr("Invoices"))
        self.ui.tabs.setTabText(1, self.tr("Customers"))

        path = Path(__file__).parent / "styles" / "sales.qss"
        with open(path, "r", encoding="UTF-8") as style_file:
            self.setStyleSheet(style_file.read())
