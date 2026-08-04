from decimal import Decimal

from peewee import BooleanField, CharField, DecimalField

from .base import BaseModelExtended, TimestampMixin


TAX_TYPES = (
    'percentage',
    'fixed',
    'compound',
)


class Tax(BaseModelExtended, TimestampMixin):
    """Tax rate definitions (VAT / GST / sales tax)."""

    name = CharField(max_length=100, unique=True, index=True)
    rate = DecimalField(max_digits=8, decimal_places=4)
    tax_type = CharField(max_length=20, default='percentage')
    is_default = BooleanField(default=False)
    country_code = CharField(max_length=3, null=True)
    description = CharField(max_length=255, null=True)
    is_active = BooleanField(default=True)

    class Meta:  # type: ignore
        table_name = 'taxes'

    def __str__(self) -> str:
        return f"{self.name} ({self.rate}%)"

    def calculate_tax(self, amount: Decimal) -> Decimal:
        if self.tax_type == 'fixed':
            return self.rate
        if self.tax_type == 'compound':
            return (amount * (1 + self.rate / 100) * self.rate / 100).quantize(
                Decimal('0.01'),
            )
        return (amount * self.rate / 100).quantize(Decimal('0.01'))

    @classmethod
    def get_default(cls) -> 'Tax | None':
        return cls.get_or_none(cls.is_default == True)  # noqa: E712