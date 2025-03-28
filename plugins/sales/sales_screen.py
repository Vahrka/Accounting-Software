from pathlib import Path

from PySide6.QtWidgets import QTabWidget

from .ui.form_ui import Ui_Form


class SalesScreen(QTabWidget):

    def setup_ui(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        path = Path(__file__).parent / "styles" / "sales.qss"
        with open(path, "r", encoding="UTF-8") as style_file:
            self.setStyleSheet(style_file.read())

        self.retranslateUi()

    def retranslateUi(self):
        self.setTabText(0, self.tr("Invoices"))
        self.setTabText(1, self.tr("Customers"))
