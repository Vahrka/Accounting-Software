from decimal import Decimal, InvalidOperation

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QHeaderView, QMessageBox, QTabWidget

from data_models.item_table_model import ItemTableModel, SupplierTableModel
from models import InventoryItem, Supplier
from ui.inventory.inventory_ui import Ui_Inventory
from utils.logger import get_logger
from utils.mixins import RetranslateMixin

logger = get_logger()


class InventoryScreen(RetranslateMixin, QTabWidget):

    @property
    def NAME(self) -> str:
        """Sidebar label, re-evaluated on every access for live translation."""
        return self.tr("Inventory")

    def setup_ui(self):
        self.ui = Ui_Inventory()
        self.ui.setupUi(self)

        self._current_item_id: int | None = None
        self._current_supplier_id: int | None = None

        self._setup_items_tab()
        self._setup_suppliers_tab()

        self.refresh_suppliers()
        self.refresh_items()

    def _setup_items_tab(self) -> None:
        self.item_model = ItemTableModel(self)
        self.ui.items_table_view.setModel(self.item_model)
        self.ui.items_table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # type: ignore

        self.ui.item_search_input.textChanged.connect(self.refresh_items)
        self.ui.item_category_filter.currentTextChanged.connect(self.refresh_items)
        self.ui.add_item_btn.clicked.connect(self.clear_item_form)
        self.ui.save_item_btn.clicked.connect(self.save_item)
        self.ui.delete_item_btn.clicked.connect(self.delete_item)
        self.ui.clear_item_btn.clicked.connect(self.clear_item_form)
        self.ui.items_table_view.selectionModel().selectionChanged.connect(self.load_selected_item)  # type: ignore

    def _setup_suppliers_tab(self) -> None:
        self.supplier_model = SupplierTableModel(self)
        self.ui.suppliers_table_view.setModel(self.supplier_model)
        self.ui.suppliers_table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # type: ignore

        self.ui.supplier_search_input.textChanged.connect(self.refresh_suppliers)
        self.ui.add_supplier_btn.clicked.connect(self.clear_supplier_form)
        self.ui.save_supplier_btn.clicked.connect(self.save_supplier)
        self.ui.delete_supplier_btn.clicked.connect(self.delete_supplier)
        self.ui.clear_supplier_btn.clicked.connect(self.clear_supplier_form)
        self.ui.suppliers_table_view.selectionModel().selectionChanged.connect(self.load_selected_supplier)  # type: ignore

    # ------------------------------------------------------------------
    # Items
    # ------------------------------------------------------------------

    @Slot(name="Refresh items table")
    def refresh_items(self, *_args) -> None:
        search = self.ui.item_search_input.text().strip()
        category = self.ui.item_category_filter.currentText().strip()
        self.item_model.refresh(search=search, category=category)
        self._refresh_category_filter()
        self._refresh_supplier_combo()

    def _refresh_category_filter(self) -> None:
        current = self.ui.item_category_filter.currentText()
        categories = sorted({
            item.category for item in InventoryItem.select(InventoryItem.category).distinct()
        })
        self.ui.item_category_filter.blockSignals(True)
        self.ui.item_category_filter.clear()
        self.ui.item_category_filter.addItem("")
        self.ui.item_category_filter.addItems(categories)
        self.ui.item_category_filter.setCurrentText(current)
        self.ui.item_category_filter.blockSignals(False)

    def _refresh_supplier_combo(self) -> None:
        current = self.ui.supplier_input.currentData()
        self.ui.supplier_input.blockSignals(True)
        self.ui.supplier_input.clear()
        self.ui.supplier_input.addItem("", None)
        for supplier in Supplier.select().order_by(Supplier.name):
            self.ui.supplier_input.addItem(supplier.name, supplier.id)
        if current is not None:
            index = self.ui.supplier_input.findData(current)
            if index >= 0:
                self.ui.supplier_input.setCurrentIndex(index)
        self.ui.supplier_input.blockSignals(False)

    @Slot(name="Load selected item into form")
    def load_selected_item(self, *_args) -> None:
        indexes = self.ui.items_table_view.selectionModel().selectedRows()
        if not indexes:
            return

        item = self.item_model.item_at(indexes[0].row())
        if item is None:
            return

        self._current_item_id = item.id
        self.ui.sku_input.setText(item.sku)
        self.ui.name_input.setText(item.name)
        self.ui.category_input.setCurrentText(item.category)
        self.ui.description_input.setPlainText(item.description or "")
        self.ui.unit_price_input.setValue(float(item.unit_price))
        self.ui.cost_price_input.setValue(float(item.cost_price))
        self.ui.stock_quantity_input.setValue(item.stock_quantity)
        self.ui.reorder_level_input.setValue(item.reorder_level)
        self.ui.location_input.setText(item.location)

        supplier_index = self.ui.supplier_input.findData(item.supplier_id)
        self.ui.supplier_input.setCurrentIndex(max(supplier_index, 0))

    @Slot(name="Save item")
    def save_item(self) -> None:
        sku = self.ui.sku_input.text().strip()
        name = self.ui.name_input.text().strip()
        category = self.ui.category_input.currentText().strip()
        location = self.ui.location_input.text().strip()

        if not all([sku, name, category, location]):
            QMessageBox.warning(self, self.tr("Validation error"),
                                 self.tr("SKU, name, category and location are required."))
            return

        supplier_id = self.ui.supplier_input.currentData()

        try:
            with InventoryItem._meta.database.atomic():
                if self._current_item_id is not None:
                    item = InventoryItem.get_by_id(self._current_item_id)
                else:
                    item = InventoryItem(sku=sku)

                item.sku = sku
                item.name = name
                item.category = category
                item.description = self.ui.description_input.toPlainText().strip() or None
                item.unit_price = Decimal(str(self.ui.unit_price_input.value()))
                item.cost_price = Decimal(str(self.ui.cost_price_input.value()))
                item.stock_quantity = self.ui.stock_quantity_input.value()
                item.reorder_level = self.ui.reorder_level_input.value()
                item.location = location
                item.supplier = supplier_id
                item.save()

            self.clear_item_form()
            self.refresh_items()

        except InvalidOperation:
            QMessageBox.warning(self, self.tr("Validation error"), self.tr("Invalid price value."))
        except Exception as error:
            logger.error(f"Failed to save inventory item:\n{error}")
            QMessageBox.critical(self, self.tr("Error"), self.tr("Could not save the item."))

    @Slot(name="Delete item")
    def delete_item(self) -> None:
        if self._current_item_id is None:
            return

        confirm = QMessageBox.question(
            self, self.tr("Delete item"),
            self.tr("Are you sure you want to delete this item?"),
        )
        if confirm != QMessageBox.StandardButton.Yes:
            return

        try:
            InventoryItem.get_by_id(self._current_item_id).delete_instance()
            self.clear_item_form()
            self.refresh_items()
        except Exception as error:
            logger.error(f"Failed to delete inventory item:\n{error}")
            QMessageBox.critical(self, self.tr("Error"), self.tr("Could not delete the item."))

    @Slot(name="Clear item form")
    def clear_item_form(self) -> None:
        self._current_item_id = None
        self.ui.sku_input.clear()
        self.ui.name_input.clear()
        self.ui.category_input.setCurrentText("")
        self.ui.description_input.clear()
        self.ui.unit_price_input.setValue(0)
        self.ui.cost_price_input.setValue(0)
        self.ui.stock_quantity_input.setValue(0)
        self.ui.reorder_level_input.setValue(0)
        self.ui.location_input.clear()
        self.ui.supplier_input.setCurrentIndex(0)
        self.ui.items_table_view.clearSelection()

    # ------------------------------------------------------------------
    # Suppliers
    # ------------------------------------------------------------------

    @Slot(name="Refresh suppliers table")
    def refresh_suppliers(self, *_args) -> None:
        search = self.ui.supplier_search_input.text().strip()
        self.supplier_model.refresh(search=search)

    @Slot(name="Load selected supplier into form")
    def load_selected_supplier(self, *_args) -> None:
        indexes = self.ui.suppliers_table_view.selectionModel().selectedRows()
        if not indexes:
            return

        supplier = self.supplier_model.supplier_at(indexes[0].row())
        if supplier is None:
            return

        self._current_supplier_id = supplier.id
        self.ui.supplier_name_input.setText(supplier.name)
        self.ui.contact_person_input.setText(supplier.contact_person or "")
        self.ui.supplier_email_input.setText(supplier.email)
        self.ui.supplier_phone_input.setText(supplier.phone)
        self.ui.supplier_address_input.setText(supplier.address or "")

    @Slot(name="Save supplier")
    def save_supplier(self) -> None:
        name = self.ui.supplier_name_input.text().strip()
        email = self.ui.supplier_email_input.text().strip()
        phone = self.ui.supplier_phone_input.text().strip()

        if not all([name, email, phone]):
            QMessageBox.warning(self, self.tr("Validation error"),
                                 self.tr("Name, email and phone are required."))
            return

        try:
            if self._current_supplier_id is not None:
                supplier = Supplier.get_by_id(self._current_supplier_id)
            else:
                supplier = Supplier()

            supplier.name = name
            supplier.contact_person = self.ui.contact_person_input.text().strip() or None
            supplier.email = email
            supplier.phone = phone
            supplier.address = self.ui.supplier_address_input.text().strip() or None
            supplier.save()

            self.clear_supplier_form()
            self.refresh_suppliers()
            self._refresh_supplier_combo()

        except Exception as error:
            logger.error(f"Failed to save supplier:\n{error}")
            QMessageBox.critical(self, self.tr("Error"), self.tr("Could not save the supplier."))

    @Slot(name="Delete supplier")
    def delete_supplier(self) -> None:
        if self._current_supplier_id is None:
            return

        confirm = QMessageBox.question(
            self, self.tr("Delete supplier"),
            self.tr("Are you sure you want to delete this supplier?"),
        )
        if confirm != QMessageBox.StandardButton.Yes:
            return

        try:
            Supplier.get_by_id(self._current_supplier_id).delete_instance()
            self.clear_supplier_form()
            self.refresh_suppliers()
            self._refresh_supplier_combo()
        except Exception as error:
            logger.error(f"Failed to delete supplier:\n{error}")
            QMessageBox.critical(self, self.tr("Error"), self.tr("Could not delete the supplier."))

    @Slot(name="Clear supplier form")
    def clear_supplier_form(self) -> None:
        self._current_supplier_id = None
        self.ui.supplier_name_input.clear()
        self.ui.contact_person_input.clear()
        self.ui.supplier_email_input.clear()
        self.ui.supplier_phone_input.clear()
        self.ui.supplier_address_input.clear()
        self.ui.suppliers_table_view.clearSelection()