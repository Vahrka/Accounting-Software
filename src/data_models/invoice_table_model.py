from typing import Any

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

from models import Invoice


class InvoiceTableModel(QAbstractTableModel):
    """Table model exposing Invoice records."""

    HEADERS = (
        "Invoice #", "Date", "Due Date", "Customer",
        "Subtotal", "Tax", "Discount", "Total",
        "Paid", "Balance", "Status",
    )

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._invoices: list[Invoice] = []

    def refresh(
        self,
        search: str = "",
        status: str = "",
    ) -> None:
        query = Invoice.get_active()
        if search:
            like = f"%{search}%"
            query = query.where(
                (Invoice.invoice_number ** like)
                | (Invoice.customer__name ** like)
            )
        if status:
            query = query.where(Invoice.status == status)

        self.beginResetModel()
        self._invoices = list(
            query.order_by(Invoice.invoice_date.desc())
        )
        self.endResetModel()

    def invoice_at(self, row: int) -> Invoice | None:
        if 0 <= row < len(self._invoices):
            return self._invoices[row]
        return None

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:  # noqa: N802
        return 0 if parent.isValid() else len(self._invoices)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:  # noqa: N802
        return 0 if parent.isValid() else len(self.HEADERS)

    def headerData(self, section: int, orientation: Qt.Orientation,  # noqa: N802
                    role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if role != Qt.ItemDataRole.DisplayRole:
            return None
        if orientation == Qt.Orientation.Horizontal:
            return self.HEADERS[section]
        return section + 1

    def data(self, index: QModelIndex,
             role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if not index.isValid():
            return None

        inv = self._invoices[index.row()]
        col = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            if col == 0:
                return inv.invoice_number
            if col == 1:
                return inv.invoice_date.strftime("%Y-%m-%d")
            if col == 2:
                return (inv.due_date.strftime("%Y-%m-%d")
                        if inv.due_date else "")
            if col == 3:
                return inv.customer.name if inv.customer else ""
            if col == 4:
                return f"{inv.subtotal:.2f}"
            if col == 5:
                return f"{inv.tax_amount:.2f}"
            if col == 6:
                return f"{inv.discount:.2f}"
            if col == 7:
                return f"{inv.total:.2f}"
            if col == 8:
                return f"{inv.paid_amount:.2f}"
            if col == 9:
                return f"{inv.balance_due:.2f}"
            if col == 10:
                return inv.status

        if role == Qt.ItemDataRole.BackgroundRole:
            if inv.status == 'overdue':
                from PySide6.QtGui import QColor
                return QColor(255, 220, 220)
            if inv.status == 'paid':
                from PySide6.QtGui import QColor
                return QColor(220, 245, 220)

        if role == Qt.ItemDataRole.ForegroundRole and col == 10:
            from PySide6.QtGui import QColor
            status_colors = {
                'draft': QColor(150, 150, 150),
                'pending': QColor(200, 150, 0),
                'paid': QColor(0, 128, 0),
                'overdue': QColor(200, 0, 0),
                'cancelled': QColor(128, 128, 128),
                'partially_paid': QColor(0, 100, 200),
            }
            return status_colors.get(inv.status)

        return None

    def sort(self, column: int,  # noqa: N802
              order: Qt.SortOrder = Qt.SortOrder.AscendingOrder) -> None:
        self.beginResetModel()
        reverse = order == Qt.SortOrder.DescendingOrder
        key_map = {
            0: lambda i: i.invoice_number,
            1: lambda i: i.invoice_date,
            2: lambda i: i.due_date or "",
            3: lambda i: (i.customer.name if i.customer else ""),
            7: lambda i: i.total,
            9: lambda i: i.balance_due,
            10: lambda i: i.status,
        }
        key_fn = key_map.get(column, lambda i: i.invoice_date)
        self._invoices.sort(key=key_fn, reverse=reverse)
        self.endResetModel()