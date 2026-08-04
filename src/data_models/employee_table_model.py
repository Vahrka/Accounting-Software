from typing import Any

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

from models import Employee


class EmployeeTableModel(QAbstractTableModel):
    """Table model exposing Employee records."""

    HEADERS = (
        "Employee ID", "Full Name", "Department", "Position",
        "Hire Date", "Salary", "Pay Rate", "Pay Frequency",
        "Status",
    )

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._employees: list[Employee] = []

    def refresh(self, search: str = "", department: str = "") -> None:
        query = Employee.get_active()
        if search:
            like = f"%{search}%"
            query = query.where(
                (Employee.employee_id ** like)
                | (Employee.first_name ** like)
                | (Employee.last_name ** like)
                | (Employee.email ** like)
            )
        if department:
            query = query.where(Employee.department == department)

        self.beginResetModel()
        self._employees = list(query.order_by(Employee.employee_id))
        self.endResetModel()

    def employee_at(self, row: int) -> Employee | None:
        if 0 <= row < len(self._employees):
            return self._employees[row]
        return None

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:  # noqa: N802
        return 0 if parent.isValid() else len(self._employees)

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

        emp = self._employees[index.row()]
        col = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            if col == 0:
                return emp.employee_id
            if col == 1:
                return emp.full_name
            if col == 2:
                return emp.department or ""
            if col == 3:
                return emp.position or ""
            if col == 4:
                return (emp.hire_date.strftime("%Y-%m-%d")
                        if emp.hire_date else "")
            if col == 5:
                return f"{emp.salary:.2f}"
            if col == 6:
                return (f"{emp.pay_rate:.2f}"
                        if emp.pay_rate is not None else "")
            if col == 7:
                return emp.pay_frequency
            if col == 8:
                if emp.is_terminated:
                    return "Terminated"
                return "Active" if emp.is_active else "Inactive"

        if role == Qt.ItemDataRole.BackgroundRole:
            if emp.is_terminated:
                from PySide6.QtGui import QColor
                return QColor(255, 200, 200)

        return None

    def sort(self, column: int,  # noqa: N802
              order: Qt.SortOrder = Qt.SortOrder.AscendingOrder) -> None:
        self.beginResetModel()
        reverse = order == Qt.SortOrder.DescendingOrder
        key_map = {
            0: lambda e: e.employee_id,
            1: lambda e: e.full_name.lower(),
            2: lambda e: e.department or "",
            3: lambda e: e.position or "",
            4: lambda e: e.hire_date or "",
            5: lambda e: e.salary,
        }
        key_fn = key_map.get(column, lambda e: e.employee_id)
        self._employees.sort(key=key_fn, reverse=reverse)
        self.endResetModel()