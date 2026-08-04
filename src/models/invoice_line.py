from peewee import (CharField, DecimalField, ForeignKeyField,
                    IntegerField, TextField)

from .base import BaseModelExtended
from .inventory_item import InventoryItem
from .invoice import Invoice
from .tax import Tax


class InvoiceLine(BaseModelExtended):
    """Individual line item within an invoice."""

    invoice = ForeignKeyField(Invoice, backref='lines', on_delete='CASCADE')
    item = ForeignKeyField(
        InventoryItem, backref='invoice_lines', null=True,
        on_delete='SET NULL',
    )
    description = TextField(null=True)
    quantity = DecimalField(max_digits=12, decimal_places=2)
    unit_price = DecimalField(max_digits=12, decimal_places=2)
    discount = DecimalField(max_digits=10, decimal_places=2, default=0)
    tax = ForeignKeyField(
        Tax, backref='invoice_lines', null=True,
        on_delete='SET NULL',
    )
    tax_rate = DecimalField(max_digits=8, decimal_places=4, default=0)
    line_total = DecimalField(max_digits=14, decimal_places=2)
    sort_order = IntegerField(default=0)

    class Meta:  # type: ignore
        table_name = 'invoice_lines'

    def __str__(self) -> str:
        return f"Line {self.sort_order} – {self.description or self.item}"

    @property
    def subtotal(self) -> 'Decimal':
        from decimal import Decimal
        return (self.quantity * self.unit_price - self.discount).quantize(
            Decimal('0.01'),
        )

    def calculate_totals(self) -> None:
        from decimal import Decimal
        sub = (self.quantity * self.unit_price - self.discount).quantize(
            Decimal('0.01'),
        )
        tax_amount = (sub * self.tax_rate / 100).quantize(Decimal('0.01'))
        self.line_total = sub + tax_amount
        self.save()
