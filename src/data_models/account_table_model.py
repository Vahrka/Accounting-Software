from typing import Any

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

from models import LedgerAccount


class AccountTableModel(QAbstractTableModel):
    """Flat table model exposing LedgerAccount records to a QTableView."""

    HEADERS = (
        "Code", "Name", "Type", "Currency", "Opening Balance",
        "Current Balance", "Active", "Description",
    )

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._accounts: list[LedgerAccount] = []

    def refresh(
        self,
        search: str = "",
        account_type: str = "",
        show_inactive: bool = False,
    ) -> None:
        query = LedgerAccount.get_active()
        if show_inactive:
            query = LedgerAccount.select()
        if search:
            like = f"%{search}%"
            query = query.where(
                (LedgerAccount.code ** like)
                | (LedgerAccount.name ** like)
            )
        if account_type:
            query = query.where(LedgerAccount.account_type == account_type)

        self.beginResetModel()
        self._accounts = list(query.order_by(LedgerAccount.code))
        self.endResetModel()

    def account_at(self, row: int) -> LedgerAccount | None:
        if 0 <= row < len(self._accounts):
            return self._accounts[row]
        return None

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:  # noqa: N802
        return 0 if parent.isValid() else len(self._accounts)

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

        acc = self._accounts[index.row()]
        col = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            if col == 0:
                return acc.code
            if col == 1:
                return acc.name
            if col == 2:
                return acc.account_type
            if col == 3:
                return acc.currency.code if acc.currency else ""
            if col == 4:
                return f"{acc.opening_balance:.2f}"
            if col == 5:
                return f"{acc.current_balance:.2f}"
            if col == 6:
                return "Yes" if acc.is_active else "No"
            if col == 7:
                return acc.description or ""

        if role == Qt.ItemDataRole.BackgroundRole and not acc.is_active:
            from PySide6.QtGui import QColor
            return QColor(200, 200, 200)

        return None

    def sort(self, column: int,  # noqa: N802
              order: Qt.SortOrder = Qt.SortOrder.AscendingOrder) -> None:
        self.beginResetModel()
        reverse = order == Qt.SortOrder.DescendingOrder
        key_map = {
            0: lambda a: a.code,
            1: lambda a: a.name,
            2: lambda a: a.account_type,
            4: lambda a: a.opening_balance,
            5: lambda a: a.current_balance,
        }
        key_fn = key_map.get(column, lambda a: a.code)
        self._accounts.sort(key=key_fn, reverse=reverse)
        self.endResetModel()
