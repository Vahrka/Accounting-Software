from peewee import (BooleanField, CharField, DecimalField,
                    ForeignKeyField, TextField)

from .base import BaseModelExtended, SoftDeleteMixin, TimestampMixin
from .currency import Currency
from .user import User


class Customer(BaseModelExtended, TimestampMixin, SoftDeleteMixin):
    """Customer / client model."""

    name = CharField(max_length=100, index=True)
    contact_person = CharField(max_length=100, null=True)
    email = CharField(max_length=100, unique=True, index=True)
    phone = CharField(max_length=20)
    fax = CharField(max_length=20, null=True)
    website = CharField(max_length=200, null=True)
    address = TextField(null=True)
    city = CharField(max_length=50, null=True)
    state = CharField(max_length=50, null=True)
    country = CharField(max_length=50, null=True)
    postal_code = CharField(max_length=20, null=True)
    tax_id = CharField(max_length=50, null=True, index=True)
    credit_limit = DecimalField(
        max_digits=14, decimal_places=2, null=True,
    )
    opening_balance = DecimalField(
        max_digits=14, decimal_places=2, default=0,
    )
    current_balance = DecimalField(
        max_digits=14, decimal_places=2, default=0,
    )
    currency = ForeignKeyField(
        Currency, backref='customers', null=True,
        on_delete='SET NULL',
    )
    payment_terms = CharField(max_length=30, null=True)
    notes = TextField(null=True)
    is_active = BooleanField(default=True, index=True)
    created_by = ForeignKeyField(
        User, backref='customers', null=True,
        on_delete='SET NULL',
    )

    class Meta:  # type: ignore
        table_name = 'customers'
        indexes = (
            (('name', 'email'), False),
        )

    def __str__(self) -> str:
        return self.name

    @property
    def balance_due(self) -> float:
        """Total unpaid amount across all invoices."""
        from .invoice import Invoice
        from decimal import Decimal
        total = (
            Invoice
            .select()
            .where(
                (Invoice.customer == self.id)
                & (Invoice.status.in_(['pending', 'overdue']))
            )
        )
        return sum(
            (float(inv.total - inv.paid_amount) for inv in total),
            0.0,
        )
