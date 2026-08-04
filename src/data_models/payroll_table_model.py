from typing import Any

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

from models import Payroll


class PayrollTableModel(QAbstractTableModel):
    """Table model exposing Payroll records."""

    HEADERS = (
        "#", "Employee", "Period Start", "Period End",
        "Gross Pay", "Deductions", "Net Pay", "Pay Type",
        "Status", "Pay Date",
    )

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._payrolls: list[Payroll] = []

    def refresh(
        self,
        search: str = "",
        status: str = "",
    ) -> None:
        query = Payroll.get_active()
        if search:
            like = f"%{search}%"
            query = query.where(
                (Payroll.employee__employee_id ** like)
                | (Payroll.employee__first_name ** like)
                | (Payroll.employee__last_name ** like)
            )
        if status:
            query = query.where(Payroll.status == status)

        self.beginResetModel()
        self._payrolls = list(
            query.order_by(Payroll.pay_period_start.desc())
        )
        self.endResetModel()

    def payroll_at(self, row: int) -> Payroll | None:
        if 0 <= row < len(self._payrolls):
            return self._payrolls[row]
        return None

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:  # noqa: N802
        return 0 if parent.isValid() else len(self._payrolls)

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

        pr = self._payrolls[index.row()]
        col = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            if col == 0:
                return pr.id
            if col == 1:
                return pr.employee.full_name
            if col == 2:
                return pr.pay_period_start.strftime("%Y-%m-%d")
            if col == 3:
                return pr.pay_period_end.strftime("%Y-%m-%d")
            if col == 4:
                return f"{pr.gross_pay:.2f}"
            if col == 5:
                return f"{pr.total_deductions:.2f}"
            if col == 6:
                return f"{pr.net_pay:.2f}"
            if col == 7:
                return pr.pay_type
            if col == 8:
                return pr.status
            if col == 9:
                return (pr.pay_date.strftime("%Y-%m-%d")
                        if pr.pay_date else "")

        if role == Qt.ItemDataRole.BackgroundRole:
            from PySide6.QtGui import QColor
            if pr.status == 'paid':
                return QColor(220, 245, 220)
            if pr.status == 'cancelled':
                return QColor(255, 220, 220)

        if role == Qt.ItemDataRole.ForegroundRole and col == 8:
            from PySide6.QtGui import QColor
            colors = {
                'draft': QColor(150, 150, 150),
                'approved': QColor(200, 150, 0),
                'paid': QColor(0, 128, 0),
                'cancelled': QColor(200, 0, 0),
            }
            return colors.get(pr.status)

        return None

    def sort(self, column: int,  # noqa: N802
              order: Qt.SortOrder = Qt.SortOrder.AscendingOrder) -> None:
        self.beginResetModel()
        reverse = order == Qt.SortOrder.DescendingOrder
        key_map = {
            0: lambda p: p.id,
            1: lambda p: p.employee.full_name.lower(),
            2: lambda p: p.pay_period_start,
            3: lambda p: p.pay_period_end,
            6: lambda p: p.net_pay,
            8: lambda p: p.status,
        }
        key_fn = key_map.get(column, lambda p: p.pay_period_start)
        self._payrolls.sort(key=key_fn, reverse=reverse)
        self.endResetModel()
