from peewee import (BooleanField, CharField, DecimalField, ForeignKeyField,
                    IntegerField, TextField)

from .base import BaseModelExtended, SoftDeleteMixin, TimestampMixin
from .currency import Currency


class Supplier(BaseModelExtended, TimestampMixin, SoftDeleteMixin):
    """Supplier model."""

    name = CharField(max_length=100, unique=True, index=True)
    contact_person = CharField(max_length=100, null=True)
    email = CharField(max_length=100, unique=True, index=True)
    phone = CharField(max_length=20, null=True)
    fax = CharField(max_length=20, null=True)
    website = CharField(max_length=200, null=True)
    address = TextField(null=True)
    city = CharField(max_length=50, null=True)
    state = CharField(max_length=50, null=True)
    country = CharField(max_length=50, null=True)
    postal_code = CharField(max_length=20, null=True)
    tax_id = CharField(max_length=50, null=True)
    bank_account = CharField(max_length=50, null=True)
    payment_terms = CharField(max_length=30, null=True)
    is_active = BooleanField(default=True, index=True)
    notes = TextField(null=True)

    class Meta:  # type: ignore
        table_name = 'suppliers'

    def __str__(self) -> str:
        return self.name


class Category(BaseModelExtended):
    """Product / item category."""

    name = CharField(max_length=50, unique=True, index=True)
    description = CharField(max_length=255, null=True)
    parent = ForeignKeyField(
        'self', backref='children', null=True, on_delete='SET NULL',
    )

    class Meta:  # type: ignore
        table_name = 'categories'

    def __str__(self) -> str:
        return self.name


class InventoryItem(BaseModelExtended, TimestampMixin, SoftDeleteMixin):
    """Inventory item model."""

    sku = CharField(max_length=50, unique=True, index=True)
    name = CharField(max_length=100, index=True)
    description = TextField(null=True)
    category = ForeignKeyField(
        Category, backref='inventory_items', null=True,
        on_delete='SET NULL',
    )
    unit_price = DecimalField(max_digits=12, decimal_places=2)
    cost_price = DecimalField(max_digits=12, decimal_places=2, default=0)
    stock_quantity = IntegerField(default=0)
    reorder_level = IntegerField(default=0)
    location = CharField(max_length=100, null=True, index=True)
    barcode = CharField(max_length=50, null=True, index=True)
    unit_of_measure = CharField(max_length=20, default='pcs')
    supplier = ForeignKeyField(
        Supplier, backref='inventory_items', null=True,
        on_delete='SET NULL',
    )
    currency = ForeignKeyField(
        Currency, backref='inventory_items', null=True,
        on_delete='SET NULL',
    )
    notes = TextField(null=True)
    is_active = BooleanField(default=True, index=True)

    class Meta:  # type: ignore
        table_name = 'inventory_items'
        indexes = (
            (('sku', 'name'), False),
        )

    def __str__(self) -> str:
        return f"{self.sku} – {self.name}"

    @property
    def in_stock(self) -> bool:
        return self.stock_quantity > 0

    @property
    def needs_reorder(self) -> bool:
        return self.stock_quantity <= self.reorder_level

    @property
    def is_low_stock(self) -> bool:
        return self.needs_reorder

    @property
    def inventory_value(self) -> float:
        return float(self.stock_quantity * self.cost_price)

    def update_stock(self, qty: int) -> None:
        """Add *qty* (positive or negative) to stock. Raises on underflow."""
        new_qty = self.stock_quantity + qty
        if new_qty < 0:
            raise ValueError(
                f"Insufficient stock. Current: {self.stock_quantity}, "
                f"requested: {-qty}"
            )
        self.stock_quantity = new_qty
        self.save()
