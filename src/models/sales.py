from datetime import datetime

from peewee import (CharField, DateTimeField, DecimalField, ForeignKeyField,
                    IntegerField, TextField)

from .base import BaseModelExtended, TimestampMixin
from .customer import Customer
from .inventory_item import InventoryItem
from .user import User


class Sale(BaseModelExtended, TimestampMixin):
    """Sales record (cash-sale shortcut without full invoicing)."""

    customer = ForeignKeyField(
        Customer, backref='sales', null=True, on_delete='SET NULL',
    )
    user = ForeignKeyField(
        User, backref='sales', null=True, on_delete='SET NULL',
    )
    sale_date = DateTimeField(default=datetime.now, index=True)
    total_amount = DecimalField(max_digits=12, decimal_places=2)
    discount = DecimalField(max_digits=10, decimal_places=2, default=0)
    tax_amount = DecimalField(max_digits=10, decimal_places=2, default=0)
    status = CharField(max_length=20, default='pending', index=True)
    # status: pending, completed, cancelled, refunded
    payment_method = CharField(max_length=30, null=True)
    reference = CharField(max_length=100, null=True)
    notes = TextField(null=True)

    class Meta:  # type: ignore
        table_name = 'sales'

    def __str__(self) -> str:
        return f"Sale #{self.id}"

    @property
    def net_amount(self) -> float:
        return float(self.total_amount - self.discount + self.tax_amount)


class SaleItem(BaseModelExtended):
    """Individual items in a sale."""

    sale = ForeignKeyField(Sale, backref='items', on_delete='CASCADE')
    item = ForeignKeyField(
        InventoryItem, backref='sale_items', null=True, on_delete='SET NULL',
    )
    description = TextField(null=True)
    quantity = IntegerField()
    unit_price = DecimalField(max_digits=10, decimal_places=2)
    discount = DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = DecimalField(max_digits=10, decimal_places=2)

    class Meta:  # type: ignore
        table_name = 'sale_items'

    def __str__(self) -> str:
        return f"{self.quantity}x {self.item.name if self.item else 'N/A'}"


class Billing(BaseModelExtended):
    """Generic billing line items (used for quick invoicing UI)."""

    name = CharField(max_length=50)
    price = DecimalField(max_digits=10, decimal_places=2)
    count = DecimalField(max_digits=10, decimal_places=2)
    description = TextField(null=True)

    class Meta:  # type: ignore
        table_name = 'billings'
