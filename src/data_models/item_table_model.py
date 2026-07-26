from typing import Any

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

from models import InventoryItem, Supplier


class ItemTableModel(QAbstractTableModel):
    """Table model exposing InventoryItem records to a QTableView."""

    HEADERS = (
        "SKU", "Name", "Category", "Unit Price", "Cost Price",
        "Stock", "Reorder Level", "Location", "Supplier",
    )

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._items: list[InventoryItem] = []

    def refresh(self, search: str = "", category: str = "") -> None:
        """Reload items from the database, optionally filtered."""
        query = InventoryItem.select()
        if search:
            like = f"%{search}%"
            query = query.where(
                (InventoryItem.sku ** like) | (InventoryItem.name ** like)
            )
        if category:
            query = query.where(InventoryItem.category == category)

        self.beginResetModel()
        self._items = list(query.order_by(InventoryItem.name))
        self.endResetModel()

    def item_at(self, row: int) -> InventoryItem | None:
        if 0 <= row < len(self._items):
            return self._items[row]
        return None

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:  # noqa: N802
        return 0 if parent.isValid() else len(self._items)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:  # noqa: N802
        return 0 if parent.isValid() else len(self.HEADERS)

    def headerData(self, section: int, orientation: Qt.Orientation,  # noqa: N802
                    role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if role != Qt.ItemDataRole.DisplayRole:
            return None
        if orientation == Qt.Orientation.Horizontal:
            return self.HEADERS[section]
        return section + 1

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if not index.isValid():
            return None

        item = self._items[index.row()]

        if role == Qt.ItemDataRole.DisplayRole:
            column = index.column()
            if column == 0:
                return item.sku
            if column == 1:
                return item.name
            if column == 2:
                return item.category
            if column == 3:
                return f"{item.unit_price:.2f}"
            if column == 4:
                return f"{item.cost_price:.2f}"
            if column == 5:
                return item.stock_quantity
            if column == 6:
                return item.reorder_level
            if column == 7:
                return item.location
            if column == 8:
                return item.supplier.name if item.supplier else ""

        if role == Qt.ItemDataRole.BackgroundRole and item.needs_reorder:
            return Qt.GlobalColor.yellow

        return None


class SupplierTableModel(QAbstractTableModel):
    """Table model exposing Supplier records to a QTableView."""

    HEADERS = ("Name", "Contact Person", "Email", "Phone", "Address")

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._suppliers: list[Supplier] = []

    def refresh(self, search: str = "") -> None:
        """Reload suppliers from the database, optionally filtered."""
        query = Supplier.select()
        if search:
            query = query.where(Supplier.name ** f"%{search}%")

        self.beginResetModel()
        self._suppliers = list(query.order_by(Supplier.name))
        self.endResetModel()

    def supplier_at(self, row: int) -> Supplier | None:
        if 0 <= row < len(self._suppliers):
            return self._suppliers[row]
        return None

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:  # noqa: N802
        return 0 if parent.isValid() else len(self._suppliers)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:  # noqa: N802
        return 0 if parent.isValid() else len(self.HEADERS)

    def headerData(self, section: int, orientation: Qt.Orientation,  # noqa: N802
                    role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if role != Qt.ItemDataRole.DisplayRole:
            return None
        if orientation == Qt.Orientation.Horizontal:
            return self.HEADERS[section]
        return section + 1

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if not index.isValid() or role != Qt.ItemDataRole.DisplayRole:
            return None

        supplier = self._suppliers[index.row()]
        column = index.column()
        if column == 0:
            return supplier.name
        if column == 1:
            return supplier.contact_person or ""
        if column == 2:
            return supplier.email
        if column == 3:
            return supplier.phone
        if column == 4:
            return supplier.address or ""
        return None