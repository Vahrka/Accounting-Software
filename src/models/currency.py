from datetime import datetime

from peewee import BooleanField, CharField, DateTimeField, DecimalField

from .database import BaseModel


class Currency(BaseModel):
    """Supported currencies and exchange rates."""

    code = CharField(max_length=3, unique=True, index=True)
    name = CharField(max_length=50)
    symbol = CharField(max_length=5, default='')
    exchange_rate = DecimalField(
        max_digits=12, decimal_places=6, default=1.0,
    )
    rate_date = DateTimeField(default=datetime.now)
    is_base = BooleanField(default=False, index=True)
    is_active = BooleanField(default=True)

    class Meta:  # type: ignore
        table_name = 'currencies'

    def __str__(self) -> str:
        return f"{self.code} – {self.name}"

    @classmethod
    def base_currency(cls) -> 'Currency | None':
        return cls.get_or_none(cls.is_base == True)  # noqa: E712

    @classmethod
    def convert(
        cls,
        amount,
        from_code: str,
        to_code: str,
    ) -> 'float':
        """Convert *amount* from *from_code* to *to_code* via base."""
        if from_code == to_code:
            return float(amount)
        src = cls.get_or_none(cls.code == from_code)
        dst = cls.get_or_none(cls.code == to_code)
        if src is None or dst is None:
            raise ValueError(f"Unknown currency code: {from_code} or {to_code}")
        in_base = float(amount) / float(src.exchange_rate)
        return in_base * float(dst.exchange_rate)
