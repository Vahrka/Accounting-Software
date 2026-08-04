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
        query = InventoryItem.get_active()
        if search:
            like = f"%{search}%"
            query = query.where(
                (InventoryItem.sku ** like)
                | (InventoryItem.name ** like)
                | (InventoryItem.barcode ** like)
            )
        if category:
            query = query.where(InventoryItem.category_id == int(category))

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
        col = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            if col == 0:
                return item.sku
            if col == 1:
                return item.name
            if col == 2:
                return item.category.name if item.category else ""
            if col == 3:
                return f"{item.unit_price:.2f}"
            if col == 4:
                return f"{item.cost_price:.2f}"
            if col == 5:
                return item.stock_quantity
            if col == 6:
                return item.reorder_level
            if col == 7:
                return item.location or ""
            if col == 8:
                return item.supplier.name if item.supplier else ""

        if role == Qt.ItemDataRole.BackgroundRole and item.needs_reorder:
            from PySide6.QtGui import QColor
            return QColor(255, 255, 200)

        return None

    def sort(self, column: int,  # noqa: N802
              order: Qt.SortOrder = Qt.SortOrder.AscendingOrder) -> None:
        self.beginResetModel()
        reverse = order == Qt.SortOrder.DescendingOrder
        key_map = {
            0: lambda i: i.sku,
            1: lambda i: i.name.lower(),
            2: lambda i: (i.category.name if i.category else ""),
            3: lambda i: i.unit_price,
            4: lambda i: i.cost_price,
            5: lambda i: i.stock_quantity,
        }
        key_fn = key_map.get(column, lambda i: i.sku)
        self._items.sort(key=key_fn, reverse=reverse)
        self.endResetModel()


class SupplierTableModel(QAbstractTableModel):
    """Table model exposing Supplier records to a QTableView."""

    HEADERS = ("Name", "Contact Person", "Email", "Phone", "City", "Active")

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._suppliers: list[Supplier] = []

    def refresh(self, search: str = "") -> None:
        """Reload suppliers from the database, optionally filtered."""
        query = Supplier.get_active()
        if search:
            like = f"%{search}%"
            query = query.where(
                (Supplier.name ** like)
                | (Supplier.email ** like)
                | (Supplier.contact_person ** like)
            )

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
        col = index.column()
        if col == 0:
            return supplier.name
        if col == 1:
            return supplier.contact_person or ""
        if col == 2:
            return supplier.email
        if col == 3:
            return supplier.phone or ""
        if col == 4:
            return supplier.city or ""
        if col == 5:
            return "Yes" if supplier.is_active else "No"
        return None

    def sort(self, column: int,  # noqa: N802
              order: Qt.SortOrder = Qt.SortOrder.AscendingOrder) -> None:
        self.beginResetModel()
        reverse = order == Qt.SortOrder.DescendingOrder
        key_map = {
            0: lambda s: s.name.lower(),
            1: lambda s: (s.contact_person or "").lower(),
            2: lambda s: s.email.lower(),
        }
        key_fn = key_map.get(column, lambda s: s.name)
        self._suppliers.sort(key=key_fn, reverse=reverse)
        self.endResetModel()
