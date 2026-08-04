from decimal import Decimal, ROUND_HALF_UP

from peewee import (BooleanField, CharField, DecimalField, ForeignKeyField,
                    IntegerField, TextField, fn)

from .base import BaseModelExtended, SoftDeleteMixin, TimestampMixin
from .currency import Currency
from .user import User


ACCOUNT_TYPES = (
    'asset',
    'liability',
    'equity',
    'revenue',
    'expense',
)


class LedgerAccount(BaseModelExtended, TimestampMixin, SoftDeleteMixin):
    """Chart of accounts – each row is one ledger account."""

    code = CharField(max_length=20, unique=True, index=True)
    name = CharField(max_length=100, index=True)
    account_type = CharField(
        max_length=20,
        index=True,
    )
    description = TextField(null=True)
    parent = ForeignKeyField(
        'self', backref='children', null=True,
        on_delete='SET NULL',
    )
    currency = ForeignKeyField(
        Currency, backref='ledger_accounts', null=True,
        on_delete='SET NULL',
    )
    opening_balance = DecimalField(
        max_digits=16, decimal_places=2, default=Decimal('0.00'),
    )
    current_balance = DecimalField(
        max_digits=16, decimal_places=2, default=Decimal('0.00'),
    )
    is_active = BooleanField(default=True, index=True)
    is_contra = BooleanField(default=False)
    created_by = ForeignKeyField(
        User, backref='created_accounts', null=True,
        on_delete='SET NULL',
    )

    class Meta:  # type: ignore
        table_name = 'ledger_accounts'
        indexes = (
            (('code', 'name'), False),
        )

    def __str__(self) -> str:
        return f"{self.code} – {self.name}"

    # ------------------------------------------------------------------
    # Balance helpers
    # ------------------------------------------------------------------

    @classmethod
    def get_balance(cls, account_id: int) -> Decimal:
        """Return the current balance of an account.

        For asset/expense accounts: debit increases balance.
        For liability/equity/revenue accounts: credit increases balance.
        """
        from .transaction import JournalTransaction, TransactionEntry

        account = cls.get_or_none(cls.id == account_id)
        if account is None:
            return Decimal('0.00')

        posted_entries = (
            TransactionEntry
            .select(fn.SUM(TransactionEntry.debit).alias('dr'),
                    fn.SUM(TransactionEntry.credit).alias('cr'))
            .join(JournalTransaction)
            .where(
                (TransactionEntry.account_id == account_id)
                & (JournalTransaction.is_posted == True)  # noqa: E712
            )
            .dicts()
            .get()
        )
        total_debit = posted_entries['dr'] or Decimal('0.00')
        total_credit = posted_entries['cr'] or Decimal('0.00')

        if account.account_type in ('asset', 'expense'):
            raw = account.opening_balance + total_debit - total_credit
        else:
            raw = account.opening_balance + total_credit - total_debit

        return raw.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    @classmethod
    def root_accounts(cls) -> list:
        """Return top-level accounts (no parent)."""
        return list(
            cls.select()
            .where(cls.parent.is_null(True))
            .order_by(cls.code)
        )

    @property
    def full_code(self) -> str:
        """Dotted path from root to this account (e.g. 1.1.10)."""
        parts = [self.code]
        parent = self.parent
        while parent is not None:
            parts.append(parent.code)
            parent = parent.parent
        return '.'.join(reversed(parts))

    def is_debit_nature(self) -> bool:
        """True for asset & expense accounts (normal debit balance)."""
        return self.account_type in ('asset', 'expense')

    def recalculate_balance(self) -> None:
        """Refresh cached current_balance from posted entries."""
        self.current_balance = self.get_balance(self.id)
        self.save()
