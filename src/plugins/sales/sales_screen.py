from pathlib import Path

from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QAction, QPixmap
from PySide6.QtWidgets import QFileDialog, QTabWidget
from src.core.utils.logger import get_logger
from src.core.database.models import Billing, db

from .ui.form_ui import Ui_Form


logger = get_logger()

class SalesScreen(QTabWidget):

    def setup_ui(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        path = Path(__file__).parent / "styles" / "sales.qss"
        with open(path, "r", encoding="UTF-8") as style_file:
            self.setStyleSheet(style_file.read())

        self.ui.save_btn.clicked.connect(self.save)
        self.ui.select_logo_btn.clicked.connect(self.select_logo)
        self.ui.add_to_record_btn.clicked.connect(self.add_record)

        self.retranslateUi()

    def retranslateUi(self):
        self.setTabText(0, self.tr("Invoices"))
        self.setTabText(1, self.tr("Customers"))

    @Slot()
    def save(self):
        print("Saved")

    @Slot()
    def select_logo(self):
        file_path, selected_filter = QFileDialog.getOpenFileName(
            caption=self.tr("Select an Image"),
            filter=(
                "PNG (*.png);;"
                "JPEG (*.jpg *.jpeg);;"
                "SVG (*.svg);;"
                "Web (*.webp);;"
                "BMP (*.bmp);;"
                "TIFF (*.tif *.tiff);;"
                "PPM (*.ppm);;"
                "PGM (*.pgm);;"
                "PBM (*.pbm);;"
                "Favicons (*.ico)"
            ),
        )

        if file_path:
            pixmap = QPixmap(Path(file_path).absolute())
            pixmap = pixmap.scaled(250, 250, Qt.AspectRatioMode.KeepAspectRatio)
            self.ui.image_lable.setPixmap(pixmap)

    @Slot()
    def add_record(self):
        name = self.ui.billing_name_input.text()
        price = self.ui.price_input.text() or 0
        count = self.ui.count_input.text() or 0
        if all([name, price, count]):
            try:
                price = int(price)
                count = int(count)
                db.connect()
                billing = Billing(name=name, price=price, count=count)
                billing.save()
                db.close()
                logger.info(f"Item saved in DB\nname={name}\nprice={price}\ncount={count}")

                # TODO:
                # Add to table
                # self.ui.tableView.addAction(QAction(text="Hello"))
                
                
            except ValueError as value_error:
                logger.error(f"Price and Count must be integer number.\n{value_error}",)

            except Exception as error:
                logger.fatal(f"Unexpected error happend.\n{error}",)
