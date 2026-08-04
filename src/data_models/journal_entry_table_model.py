from typing import Any

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

from models import JournalTransaction, TransactionEntry


class JournalEntryTableModel(QAbstractTableModel):
    """Table model for journal transaction entries (debit/credit lines)."""

    HEADERS = (
        "Account", "Description", "Debit", "Credit",
    )

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._entries: list[TransactionEntry] = []

    def set_entries(self, entries: list[TransactionEntry]) -> None:
        self.beginResetModel()
        self._entries = entries
        self.endResetModel()

    def add_entry(self, entry: TransactionEntry) -> None:
        row = len(self._entries)
        self.beginInsertRows(QModelIndex(), row, row)
        self._entries.append(entry)
        self.endInsertRows()

    def remove_entry(self, row: int) -> None:
        if 0 <= row < len(self._entries):
            self.beginRemoveRows(QModelIndex(), row, row)
            self._entries.pop(row)
            self.endRemoveRows()

    def clear(self) -> None:
        self.beginResetModel()
        self._entries.clear()
        self.endResetModel()

    def entries(self) -> list[TransactionEntry]:
        return list(self._entries)

    @property
    def total_debit(self) -> float:
        return sum((float(e.debit) for e in self._entries))

    @property
    def total_credit(self) -> float:
        return sum((float(e.credit) for e in self._entries))

    @property
    def is_balanced(self) -> bool:
        from decimal import Decimal
        dr = sum((e.debit for e in self._entries), Decimal('0'))
        cr = sum((e.credit for e in self._entries), Decimal('0'))
        return dr == cr and len(self._entries) >= 2

    def entry_at(self, row: int) -> TransactionEntry | None:
        if 0 <= row < len(self._entries):
            return self._entries[row]
        return None

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:  # noqa: N802
        return 0 if parent.isValid() else len(self._entries)

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

        entry = self._entries[index.row()]
        col = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            if col == 0:
                return str(entry.account) if entry.account else ""
            if col == 1:
                return entry.description or ""
            if col == 2:
                val = float(entry.debit)
                return f"{val:.2f}" if val > 0 else ""
            if col == 3:
                val = float(entry.credit)
                return f"{val:.2f}" if val > 0 else ""

        if role == Qt.ItemDataRole.TextAlignmentRole and col in (2, 3):
            return Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter

        return None


class JournalTransactionTableModel(QAbstractTableModel):
    """Table model listing journal transactions (header level)."""

    HEADERS = (
        "Reference", "Date", "Description", "Debit", "Credit",
        "Posted", "Posted At",
    )

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._transactions: list[JournalTransaction] = []

    def refresh(self, search: str = "", show_posted_only: bool = False) -> None:
        query = JournalTransaction.select()
        if show_posted_only:
            query = query.where(JournalTransaction.is_posted == True)  # noqa: E712
        if search:
            like = f"%{search}%"
            query = query.where(
                (JournalTransaction.reference_no ** like)
                | (JournalTransaction.description ** like)
            )

        self.beginResetModel()
        self._transactions = list(
            query.order_by(JournalTransaction.transaction_date.desc())
        )
        self.endResetModel()

    def transaction_at(self, row: int) -> JournalTransaction | None:
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

        jt = self._transactions[index.row()]
        col = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            if col == 0:
                return jt.reference_no
            if col == 1:
                return jt.transaction_date.strftime("%Y-%m-%d")
            if col == 2:
                return (jt.description[:50] + "…"
                        if jt.description and len(jt.description) > 50
                        else (jt.description or ""))
            if col == 3:
                return f"{jt.total_debit:.2f}"
            if col == 4:
                return f"{jt.total_credit:.2f}"
            if col == 5:
                return "Yes" if jt.is_posted else "No"
            if col == 6:
                return (jt.posted_at.strftime("%Y-%m-%d %H:%M")
                        if jt.posted_at else "")

        if role == Qt.ItemDataRole.BackgroundRole:
            if jt.is_posted:
                from PySide6.QtGui import QColor
                return QColor(220, 245, 220)

        return None

    def sort(self, column: int,  # noqa: N802
              order: Qt.SortOrder = Qt.SortOrder.AscendingOrder) -> None:
        self.beginResetModel()
        reverse = order == Qt.SortOrder.DescendingOrder
        key_map = {
            0: lambda t: t.reference_no,
            1: lambda t: t.transaction_date,
            2: lambda t: (t.description or "").lower(),
            3: lambda t: t.total_debit,
        }
        key_fn = key_map.get(column, lambda t: t.transaction_date)
        self._transactions.sort(key=key_fn, reverse=reverse)
        self.endResetModel()
