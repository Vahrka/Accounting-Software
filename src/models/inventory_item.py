from peewee import (CharField, DecimalField, ForeignKeyField, IntegerField,
                    TextField)

from .base import BaseModelExtended, TimestampMixin


class Supplier(BaseModelExtended, TimestampMixin):
    """Supplier model"""
    name = CharField(max_length=100, unique=True, index=True)
    contact_person = CharField(max_length=100, null=True)
    email = CharField(max_length=100, unique=True, index=True)
    phone = CharField(max_length=20)
    address = TextField(null=True)

    class Meta:
        table_name = 'suppliers'

    def __str__(self):
        return self.name


class InventoryItem(BaseModelExtended, TimestampMixin):
    """Inventory item model"""
    sku = CharField(max_length=50, unique=True, index=True)
    name = CharField(max_length=100, index=True)
    description = TextField(null=True)
    category = CharField(max_length=50, index=True)
    unit_price = DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = IntegerField(default=0)
    reorder_level = IntegerField(default=0)
    location = CharField(max_length=100, index=True)
    cost_price = DecimalField(max_digits=10, decimal_places=2)
    supplier = ForeignKeyField(Supplier, backref='inventory_items', null=True, on_delete='SET NULL')

    class Meta:
        table_name = 'inventory_items'
        indexes = (
            (('sku', 'name'), False),
        )

    def __str__(self):
        return f"{self.sku} - {self.name}"

    @property
    def in_stock(self) -> bool:
        """Check if item is in stock"""
        return self.stock_quantity > 0

    @property
    def needs_reorder(self) -> bool:
        """Check if item needs reordering"""
        return self.stock_quantity <= self.reorder_level

    def update_stock(self, qty: int) -> None:
        """
        Update stock quantity by adding (positive) or removing (negative) qty.
        Prevents negative stock (raises ValueError).
        """
        new_qty = self.stock_quantity + qty
        if new_qty < 0:
            raise ValueError(f"Insufficient stock. Current: {self.stock_quantity}, requested: {-qty}")
        self.stock_quantity = new_qty
        self.save()

    @property
    def is_low_stock(self) -> bool:
        """Alias for needs_reorder (to match your placeholder)"""
        return self.needs_reorder
