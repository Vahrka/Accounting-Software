from typing import Any, Sequence

from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt

from models import LedgerAccount


class AccountTreeNode:
    """Internal node representing one row in the account tree."""

    def __init__(
        self,
        account: LedgerAccount | None = None,
        parent: 'AccountTreeNode | None' = None,
    ) -> None:
        self.account = account
        self.parent = parent
        self.children: list[AccountTreeNode] = []

    def append_child(self, child: 'AccountTreeNode') -> None:
        self.children.append(child)

    def child_count(self) -> int:
        return len(self.children)

    def child_at(self, row: int) -> 'AccountTreeNode | None':
        if 0 <= row < len(self.children):
            return self.children[row]
        return None

    def row_of(self) -> int:
        if self.parent is not None:
            return self.parent.children.index(self)
        return 0

    @property
    def is_root(self) -> bool:
        return self.account is None


class AccountTreeModel(QAbstractItemModel):
    """Hierarchical tree model for the chart of accounts."""

    COLUMNS = ("Code", "Name", "Type", "Balance")

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._root = AccountTreeNode()

    # ------------------------------------------------------------------
    # Public
    # ------------------------------------------------------------------

    def refresh(self) -> None:
        accounts = list(LedgerAccount.select().order_by(LedgerAccount.code))
        node_map: dict[int, AccountTreeNode] = {}

        for acc in accounts:
            node_map[acc.id] = AccountTreeNode(account=acc)

        self.beginResetModel()
        self._root = AccountTreeNode()
        for acc in accounts:
            node = node_map[acc.id]
            parent_node = node_map.get(acc.parent_id, self._root)
            if parent_node is None:
                parent_node = self._root
            parent_node.append_child(node)
        self.endResetModel()

    def account_at_index(self, index: QModelIndex) -> LedgerAccount | None:
        if not index.isValid():
            return None
        node = index.internalPointer()
        return node.account if node else None

    # ------------------------------------------------------------------
    # QAbstractItemModel overrides
    # ------------------------------------------------------------------

    def index(self, row: int, column: int,  # noqa: N802
               parent: QModelIndex = QModelIndex()) -> QModelIndex:
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
        parent_node = parent.internalPointer() if parent.isValid() else self._root
        child = parent_node.child_at(row)
        if child is not None:
            return self.createIndex(row, column, child)
        return QModelIndex()

    def parent(self, index: QModelIndex) -> QModelIndex:  # noqa: N802
        if not index.isValid():
            return QModelIndex()
        node = index.internalPointer()
        if node is None or node.parent is None or node.parent.is_root:
            return QModelIndex()
        return self.createIndex(node.parent.row_of(), 0, node.parent)

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:  # noqa: N802
        if parent.column() > 0:
            return 0
        parent_node = parent.internalPointer() if parent.isValid() else self._root
        return parent_node.child_count()

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:  # noqa: N802
        return len(self.COLUMNS)

    def headerData(self, section: int, orientation: Qt.Orientation,  # noqa: N802
                    role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if (role == Qt.ItemDataRole.DisplayRole
                and orientation == Qt.Orientation.Horizontal):
            return self.COLUMNS[section]
        return None

    def data(self, index: QModelIndex,  # noqa: N802
             role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if not index.isValid():
            return None
        node = index.internalPointer()
        if node is None or node.account is None:
            return None
        acc = node.account
        col = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            if col == 0:
                return acc.code
            if col == 1:
                return acc.name
            if col == 2:
                return acc.account_type
            if col == 3:
                return f"{acc.current_balance:.2f}"

        if role == Qt.ItemDataRole.FontRole and not acc.is_active:
            from PySide6.QtGui import QFont
            font = QFont()
            font.setItalic(True)
            return font

        return None
