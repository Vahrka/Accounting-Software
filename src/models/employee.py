from peewee import (BooleanField, CharField, DateField, DecimalField,
                    ForeignKeyField, IntegerField, TextField)

from .base import BaseModelExtended, SoftDeleteMixin, TimestampMixin
from .user import User


PAY_FREQUENCIES = (
    'monthly',
    'bi_weekly',
    'weekly',
    'daily',
)


class Employee(BaseModelExtended, TimestampMixin, SoftDeleteMixin):
    """Employee model."""

    user = ForeignKeyField(
        User, backref='employee_profile', unique=True, null=True,
        on_delete='SET NULL',
    )
    employee_id = CharField(max_length=20, unique=True, index=True)
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    department = CharField(max_length=50, null=True, index=True)
    position = CharField(max_length=50, null=True)
    email = CharField(max_length=100, unique=True, null=True, index=True)
    phone = CharField(max_length=20, null=True)
    address = TextField(null=True)
    hire_date = DateField()
    termination_date = DateField(null=True)
    salary = DecimalField(max_digits=12, decimal_places=2, default=0)
    pay_rate = DecimalField(max_digits=10, decimal_places=2, null=True)
    pay_frequency = CharField(max_length=20, default='monthly')
    tax_code = CharField(max_length=30, null=True)
    bank_account = CharField(max_length=50, null=True)
    bank_name = CharField(max_length=100, null=True)
    is_full_time = BooleanField(default=True)
    is_active = BooleanField(default=True, index=True)
    emergency_contact = TextField(null=True)
    notes = TextField(null=True)

    class Meta:  # type: ignore
        table_name = 'employees'

    def __str__(self) -> str:
        return f"{self.employee_id} – {self.full_name}"

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def is_terminated(self) -> bool:
        return self.termination_date is not None
