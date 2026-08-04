from datetime import datetime

from peewee import (BooleanField, CharField, DateTimeField, DecimalField,
                    ForeignKeyField, TextField)

from .base import BaseModelExtended, TimestampMixin
from .invoice import Invoice


RECEIPT_STATUSES = (
    'pending',
    'processed',
    'matched',
    'failed',
)


class Receipt(BaseModelExtended, TimestampMixin):
    """Scanned / uploaded receipt (e.g. from OCR)."""

    file_path = CharField(max_length=500)
    file_hash = CharField(max_length=64, null=True, index=True)
    extracted_text = TextField(null=True)
    extracted_json = TextField(null=True)  # raw OCR JSON result
    invoice = ForeignKeyField(
        Invoice, backref='receipts', null=True,
        on_delete='SET NULL',
    )
    receipt_date = DateTimeField(null=True)
    total = DecimalField(max_digits=12, decimal_places=2, null=True)
    tax_amount = DecimalField(max_digits=12, decimal_places=2, null=True)
    vendor = CharField(max_length=200, null=True, index=True)
    category = CharField(max_length=100, null=True)
    status = CharField(max_length=20, default='pending', index=True)
    ocr_confidence = DecimalField(max_digits=5, decimal_places=2, null=True)
    notes = TextField(null=True)

    class Meta:  # type: ignore
        table_name = 'receipts'

    def __str__(self) -> str:
        return f"Receipt – {self.vendor or 'Unknown'} (${self.total or 0})"
