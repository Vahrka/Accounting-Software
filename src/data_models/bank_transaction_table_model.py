from typing import Any

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

from models import BankTransaction


class BankTransactionTableModel(QAbstractTableModel):
    """Table model for bank transactions."""

    HEADERS = (
        "Date", "Description", "Amount", "Balance",
        "Category", "Reconciled", "Reference",
    )

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._transactions: list[BankTransaction] = []

    def refresh(
        self,
        feed_id: int | None = None,
        search: str = "",
        show_reconciled: bool = True,
    ) -> None:
        query = BankTransaction.select()
        if feed_id:
            query = query.where(BankTransaction.feed_id == feed_id)
        if not show_reconciled:
            query = query.where(BankTransaction.is_reconciled == False)  # noqa: E712
        if search:
            like = f"%{search}%"
            query = query.where(
                (BankTransaction.description ** like)
                | (BankTransaction.reference ** like)
            )

        self.beginResetModel()
        self._transactions = list(
            query.order_by(BankTransaction.transaction_date.desc())
        )
        self.endResetModel()

    def transaction_at(self, row: int) -> BankTransaction | None:
        if 0 <= row < len(self._transactions):
            return self._transactions[row]
        return None

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:  # noqa: N802
        return 0 if parent.isValid() else len(self._transactions)

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

        tx = self._transactions[index.row()]
        col = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            if col == 0:
                return tx.transaction_date.strftime("%Y-%m-%d")
            if col == 1:
                return (tx.description[:60] + "…"
                        if len(tx.description) > 60 else tx.description)
            if col == 2:
                return f"{tx.amount:+.2f}"
            if col == 3:
                return (f"{tx.running_balance:.2f}"
                        if tx.running_balance is not None else "")
            if col == 4:
                return tx.category or ""
            if col == 5:
                return "✓" if tx.is_reconciled else ""
            if col == 6:
                return tx.reference or ""

        if role == Qt.ItemDataRole.BackgroundRole and tx.is_reconciled:
            from PySide6.QtGui import QColor
            return QColor(220, 245, 220)

        if role == Qt.ItemDataRole.ForegroundRole:
            if col == 2:
                from PySide6.QtGui import QColor
                return QColor(34, 139, 34) if tx.amount >= 0 else QColor(200, 50, 50)

        return None

    def sort(self, column: int,  # noqa: N802
              order: Qt.SortOrder = Qt.SortOrder.AscendingOrder) -> None:
        self.beginResetModel()
        reverse = order == Qt.SortOrder.DescendingOrder
        key_map = {
            0: lambda t: t.transaction_date,
            1: lambda t: t.description.lower(),
            2: lambda t: t.amount,
            3: lambda t: t.running_balance or 0,
        }
        key_fn = key_map.get(column, lambda t: t.transaction_date)
        self._transactions.sort(key=key_fn, reverse=reverse)
        self.endResetModel()
