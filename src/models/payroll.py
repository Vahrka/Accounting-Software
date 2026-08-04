from datetime import datetime, date

from peewee import (BooleanField, CharField, DateField, DateTimeField,
                    DecimalField, ForeignKeyField, IntegerField, TextField)

from .base import BaseModelExtended, SoftDeleteMixin, TimestampMixin
from .employee import Employee
from .user import User


PAYROLL_STATUSES = (
    'draft',
    'approved',
    'paid',
    'cancelled',
)

PAY_TYPES = (
    'salary',
    'hourly',
    'contract',
    'commission',
)

DEDUCTION_TYPES = (
    'tax',
    'insurance',
    'pension',
    'loan',
    'other',
)

EARNING_TYPES = (
    'bonus',
    'overtime',
    'commission',
    'allowance',
    'other',
)


class Payroll(BaseModelExtended, TimestampMixin, SoftDeleteMixin):
    """Single payroll run for an employee in a pay period."""

    employee = ForeignKeyField(Employee, backref='payrolls')
    pay_period_start = DateField()
    pay_period_end = DateField()
    pay_date = DateField(null=True)
    gross_pay = DecimalField(max_digits=12, decimal_places=2, default=0)
    total_deductions = DecimalField(max_digits=12, decimal_places=2, default=0)
    total_earnings = DecimalField(max_digits=12, decimal_places=2, default=0)
    net_pay = DecimalField(max_digits=12, decimal_places=2, default=0)
    pay_type = CharField(max_length=20, default='salary')
    hours_worked = DecimalField(max_digits=8, decimal_places=2, null=True)
    pay_rate = DecimalField(max_digits=10, decimal_places=2, null=True)
    status = CharField(max_length=20, default='draft', index=True)
    processed_by = ForeignKeyField(
        User, backref='processed_payrolls', null=True,
        on_delete='SET NULL',
    )
    payment_method = CharField(max_length=30, null=True)
    payment_reference = CharField(max_length=100, null=True)
    notes = TextField(null=True)

    class Meta:  # type: ignore
        table_name = 'payrolls'
        indexes = (
            (('employee', 'pay_period_start', 'pay_period_end'), False),
        )

    def __str__(self) -> str:
        return (f"Payroll #{self.id} – {self.employee.employee_id} "
                f"({self.status})")

    def calculate_pay(self) -> None:
        from decimal import Decimal
        self.total_earnings = sum(
            (e.amount for e in self.earnings),
            Decimal('0.00'),
        )
        self.total_deductions = sum(
            (d.amount for d in self.deductions),
            Decimal('0.00'),
        )
        self.gross_pay = self.total_earnings
        self.net_pay = (self.gross_pay - self.total_deductions).quantize(
            Decimal('0.01'),
        )


class PayrollDeduction(BaseModelExtended):
    """Individual deduction line on a payroll record."""

    payroll = ForeignKeyField(Payroll, backref='deductions', on_delete='CASCADE')
    deduction_type = CharField(max_length=20)
    name = CharField(max_length=100)
    amount = DecimalField(max_digits=12, decimal_places=2)
    description = TextField(null=True)

    class Meta:  # type: ignore
        table_name = 'payroll_deductions'

    def __str__(self) -> str:
        return f"{self.name}: -${self.amount}"


class PayrollEarning(BaseModelExtended):
    """Individual earning / addition line on a payroll record."""

    payroll = ForeignKeyField(Payroll, backref='earnings', on_delete='CASCADE')
    earning_type = CharField(max_length=20)
    name = CharField(max_length=100)
    amount = DecimalField(max_digits=12, decimal_places=2)
    hours = DecimalField(max_digits=8, decimal_places=2, null=True)
    rate = DecimalField(max_digits=10, decimal_places=2, null=True)
    description = TextField(null=True)

    class Meta:  # type: ignore
        table_name = 'payroll_earnings'

    def __str__(self) -> str:
        return f"{self.name}: +${self.amount}"
