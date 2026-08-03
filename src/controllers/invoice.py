from pathlib import Path
from typing import TYPE_CHECKING

from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QStandardItem, QStandardItemModel, QIcon, QPixmap
from PySide6.QtWidgets import (QAbstractItemView, QDialog, QFileDialog,
                               QHBoxLayout, QHeaderView, QLineEdit,
                               QPushButton, QTabWidget, QTableView,
                               QToolButton, QVBoxLayout, QWidget)

from models import Billing, Customer, db_manager
from ui.invoice.invoice_ui import Ui_Invoice
from utils.logger import get_logger
from utils.mixins import RetranslateMixin

if TYPE_CHECKING:
    from models import Customer as CustomerType

logger = get_logger()

# TODO: do not add item to db before saving using save btn


class CustomerSelectDialog(RetranslateMixin, QDialog):
    """Dialog for searching and selecting a customer."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("CustomerSelectDialog")
        self.setMinimumSize(650, 450)
        self.selected_customer: CustomerType | None = None
        self._customers: list[CustomerType] = []
        self._setup_ui()
        self._load_customers()

    def _setup_ui(self):
        main_layout = QVBoxLayout(self)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText(self.tr("Search by name, email or phone…"))
        self.search_input.textChanged.connect(self._apply_filter)
        main_layout.addWidget(self.search_input)

        self.table_view = QTableView()
        self.table_view.setObjectName("customerSelectTable")
        self.table_view.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.table_view.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )
        self.table_view.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.table_view.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.table_view.doubleClicked.connect(self._on_accept)
        main_layout.addWidget(self.table_view)

        self.table_model = QStandardItemModel(self)
        self.table_model.setHorizontalHeaderLabels([
            self.tr("Name"),
            self.tr("Email"),
            self.tr("Phone"),
            self.tr("City"),
            self.tr("Country"),
        ])
        self.table_view.setModel(self.table_model)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        self.ok_btn = QPushButton(self.tr("Select"))
        self.ok_btn.setObjectName("dialogOkBtn")
        self.cancel_btn = QPushButton(self.tr("Cancel"))
        self.cancel_btn.setObjectName("dialogCancelBtn")
        self.ok_btn.clicked.connect(self._on_accept)
        self.cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(self.ok_btn)
        btn_layout.addWidget(self.cancel_btn)
        main_layout.addLayout(btn_layout)

    # ------------------------------------------------------------------
    # Data
    # ------------------------------------------------------------------

    def _load_customers(self, search: str = "") -> None:
        query = Customer.select()
        if search:
            like = f"%{search}%"
            query = query.where(
                (Customer.name ** like)
                | (Customer.email ** like)
                | (Customer.phone ** like)
            )
        self._customers = list(query.order_by(Customer.name))
        self._populate_table()

    def _populate_table(self) -> None:
        self.table_model.removeRows(0, self.table_model.rowCount())
        for customer in self._customers:
            name_item = QStandardItem(customer.name)
            name_item.setData(customer, Qt.ItemDataRole.UserRole)
            name_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            email_item = QStandardItem(customer.email)
            email_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            phone_item = QStandardItem(customer.phone)
            phone_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            city_item = QStandardItem(customer.city)
            city_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            country_item = QStandardItem(customer.country)
            country_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.table_model.appendRow([
                name_item, email_item, phone_item,
                city_item, country_item,
            ])

    # ------------------------------------------------------------------
    # Slots
    # ------------------------------------------------------------------

    def _apply_filter(self, text: str) -> None:
        self._load_customers(text.strip())

    def _on_accept(self) -> None:
        indexes = self.table_view.selectionModel().selectedRows()
        if not indexes:
            return
        row = indexes[0].row()
        if 0 <= row < len(self._customers):
            self.selected_customer = self._customers[row]
            self.accept()


class InvoiceScreen(RetranslateMixin, QTabWidget):

    @property
    def NAME(self) -> str:
        """Sidebar label, re-evaluated on every access for live translation."""
        return self.tr("Invoice")

    def setup_ui(self):
        self.ui = Ui_Invoice()
        self.ui.setupUi(self)

        self.ui.save_btn.clicked.connect(self.save)
        self.ui.select_logo_btn.clicked.connect(self.select_logo)
        self.ui.add_to_record_btn.clicked.connect(self.add_record)
        self.ui.select_costumer_btn.clicked.connect(self.select_costumer)

        self._selected_customer = None

        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # type: ignore
        # self.ui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)  # type: ignore
        self.ui.tableView.setColumnWidth(0, 5000)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels([
            self.tr("Name"),
            self.tr("Price"),
            self.tr("Count"),
            self.tr("Total"),
            self.tr("Action"),
        ])
        self.ui.tableView.setModel(self.model)

    @Slot(name="Save to db")
    def save(self):
        print("Saved")

    @Slot(name="Select Logo")
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

    @Slot(name="Add record to list")
    def add_record(self) -> None:
        name = self.ui.billing_name_input.text()
        price = self.ui.price_input.text() or 0
        count = self.ui.count_input.text() or 0
        if all([name, price, count]):
            try:
                price = int(price)
                count = int(count)

                self.model = self.ui.tableView.model()
                row_items = ([
                    QStandardItem(name),
                    QStandardItem(str(price)),
                    QStandardItem(str(count)),
                    QStandardItem(str(price * count)),
                    QStandardItem(),
                ])

                for i in range(len(row_items)):
                    row_items[i].setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                self.model.appendRow(row_items)  # type: ignore
                self.add_delete_button(self.model.rowCount() - 1)

                self.ui.billing_name_input.clear()
                self.ui.price_input.clear()
                self.ui.count_input.clear()

            except ValueError as value_error:
                logger.error(f"Price and Count must be integer number.\n{value_error}",)

            except Exception as error:
                logger.fatal(f"Unexpected error happend.\n{error}",)

    def add_delete_button(self, row: int) -> None:
        # Create a container widget for perfect centering
        container = QWidget()
        layout = QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create icon button
        btn = QToolButton()
        btn.setProperty("class", "table_delete_btn")
        icon = QIcon(":/icons/delete-2.svg")
        btn.setIcon(icon)
        btn.setToolTip(self.tr("Delete"))
        btn.clicked.connect(lambda checked, r=row: self.delete_row(r))
        layout.addWidget(btn)

        # Set container in table cell
        self.ui.tableView.setIndexWidget(
            self.model.index(row, 4),  # Assuming column 4 is action column
            container
        )

    def delete_row(self, row: int) -> None:
        try:
            # Remove from table
            self.model.removeRow(row)

            # Reindex remaining buttons
            for r in range(row, self.model.rowCount()):
                self.add_delete_button(r)

        except Exception as e:
            logger.error(f"Error deleting row:\n{e}")

    @Slot(name="Select Customer")
    def select_costumer(self) -> None:
        dialog = CustomerSelectDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self._selected_customer = dialog.selected_customer
            if self._selected_customer:
                self._update_customer_display()

    def _update_customer_display(self) -> None:
        """Fill customer-related widgets in the invoice UI.

        Widget names below must match the ``.ui`` file.
        If a widget is missing the attribute is simply skipped.
        """
        c = self._selected_customer
        if c is None:
            return

        for attr, value in (
            ("customer_name_input", c.name),
            ("customer_email_input", c.email),
            ("customer_phone_input", c.phone),
            ("customer_address_input", c.address),
            ("customer_city_input", c.city),
            ("customer_state_input", c.state),
            ("customer_country_input", c.country),
            ("customer_postal_code_input", c.postal_code),
        ):
            widget = getattr(self.ui, attr, None)
            if widget is not None:
                widget.setText(str(value or ""))
