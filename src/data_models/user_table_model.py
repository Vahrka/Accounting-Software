from typing import Any

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

from models import User


class UserTableModel(QAbstractTableModel):
    """Table model exposing User records."""

    HEADERS = (
        "Username", "Full Name", "Email", "Roles",
        "Active", "Last Login",
    )

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._users: list[User] = []

    def refresh(self, search: str = "") -> None:
        query = User.select()
        if search:
            like = f"%{search}%"
            query = query.where(
                (User.username ** like)
                | (User.full_name ** like)
                | (User.email ** like)
            )

        self.beginResetModel()
        self._users = list(query.order_by(User.username))
        self.endResetModel()

    def user_at(self, row: int) -> User | None:
        if 0 <= row < len(self._users):
            return self._users[row]
        return None

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:  # noqa: N802
        return 0 if parent.isValid() else len(self._users)

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

        user = self._users[index.row()]
        col = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            if col == 0:
                return user.username
            if col == 1:
                return user.full_name
            if col == 2:
                return user.email
            if col == 3:
                return ", ".join(r.name for r in user.roles)
            if col == 4:
                return "Yes" if user.is_active else "No"
            if col == 5:
                return (user.last_login.strftime("%Y-%m-%d %H:%M")
                        if user.last_login else "Never")

        if role == Qt.ItemDataRole.BackgroundRole and not user.is_active:
            from PySide6.QtGui import QColor
            return QColor(240, 240, 240)

        return None

    def sort(self, column: int,  # noqa: N802
              order: Qt.SortOrder = Qt.SortOrder.AscendingOrder) -> None:
        self.beginResetModel()
        reverse = order == Qt.SortOrder.DescendingOrder
        key_map = {
            0: lambda u: u.username.lower(),
            1: lambda u: u.full_name.lower(),
            2: lambda u: u.email.lower(),
            5: lambda u: u.last_login or "",
        }
        key_fn = key_map.get(column, lambda u: u.username)
        self._users.sort(key=key_fn, reverse=reverse)
        self.endResetModel()
