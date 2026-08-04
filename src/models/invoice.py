from datetime import datetime

from peewee import (BooleanField, CharField, DateTimeField, DecimalField,
                    ForeignKeyField, IntegerField, TextField)

from .base import BaseModelExtended, SoftDeleteMixin, TimestampMixin
from .currency import Currency
from .customer import Customer
from .tax import Tax
from .user import User


INVOICE_STATUSES = (
    'draft',
    'pending',
    'paid',
    'partially_paid',
    'overdue',
    'cancelled',
)


class Invoice(BaseModelExtended, TimestampMixin, SoftDeleteMixin):
    """Sales / purchase invoice."""

    invoice_number = CharField(max_length=50, unique=True, index=True)
    invoice_date = DateTimeField(index=True)
    due_date = DateTimeField(null=True, index=True)
    customer = ForeignKeyField(
        Customer, backref='invoices', null=True,
        on_delete='SET NULL',
    )
    currency = ForeignKeyField(
        Currency, backref='invoices', null=True,
        on_delete='SET NULL',
    )
    tax = ForeignKeyField(
        Tax, backref='invoices', null=True,
        on_delete='SET NULL',
    )
    subtotal = DecimalField(max_digits=14, decimal_places=2, default=0)
    tax_amount = DecimalField(max_digits=14, decimal_places=2, default=0)
    discount = DecimalField(max_digits=14, decimal_places=2, default=0)
    total = DecimalField(max_digits=14, decimal_places=2, default=0)
    paid_amount = DecimalField(max_digits=14, decimal_places=2, default=0)
    status = CharField(
        max_length=20, default='draft', index=True,
    )
    payment_terms = CharField(max_length=30, null=True)
    notes = TextField(null=True)
    terms_and_conditions = TextField(null=True)
    created_by = ForeignKeyField(
        User, backref='created_invoices', null=True,
        on_delete='SET NULL',
    )
    is_recurring = BooleanField(default=False)
    recurring_interval_days = IntegerField(null=True)
    logo_path = CharField(max_length=500, null=True)

    class Meta:  # type: ignore
        table_name = 'invoices'

    def __str__(self) -> str:
        return f"Invoice #{self.invoice_number}"

    @property
    def balance_due(self) -> float:
        from decimal import Decimal
        return float(
            (self.total or Decimal('0')) - (self.paid_amount or Decimal('0'))
        )

    @property
    def is_paid(self) -> bool:
        return self.balance_due <= 0 and self.status == 'paid'

    @property
    def is_overdue(self) -> bool:
        if self.status in ('paid', 'cancelled'):
            return False
        if self.due_date is None:
            return False
        return self.due_date < datetime.now()

    def recalculate_totals(self) -> None:
        from decimal import Decimal
        from .invoice_line import InvoiceLine

        lines = list(self.lines)
        self.subtotal = sum(
            (line.subtotal for line in lines),
            Decimal('0.00'),
        )
        tax_amount = Decimal('0.00')
        if self.tax:
            tax_amount = self.tax.calculate_tax(self.subtotal)
        elif lines:
            tax_amount = sum(
                (line.subtotal * line.tax_rate / 100 for line in lines),
                Decimal('0.00'),
            ).quantize(Decimal('0.01'))
        self.tax_amount = tax_amount
        self.total = (self.subtotal - self.discount + tax_amount).quantize(
            Decimal('0.01'),
        )
        self.save()

    def mark_paid(self) -> None:
        self.paid_amount = self.total
        self.status = 'paid'
        self.save()
