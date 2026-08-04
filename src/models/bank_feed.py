from datetime import datetime

from peewee import (BooleanField, CharField, DateTimeField, DecimalField,
                    DeferredForeignKey, ForeignKeyField, IntegerField,
                    TextField)

from .base import BaseModelExtended, TimestampMixin
from .currency import Currency
from .user import User


class BankAccount(BaseModelExtended, TimestampMixin):
    """A real-world bank account held by the business."""

    name = CharField(max_length=100, index=True)
    account_number = CharField(max_length=50, unique=True, index=True)
    bank_name = CharField(max_length=100, null=True)
    routing_number = CharField(max_length=50, null=True)
    account_type = CharField(max_length=20, default='checking')
    currency = ForeignKeyField(
        Currency, backref='bank_accounts', null=True,
        on_delete='SET NULL',
    )
    opening_balance = DecimalField(
        max_digits=16, decimal_places=2, default=0,
    )
    current_balance = DecimalField(
        max_digits=16, decimal_places=2, default=0,
    )
    is_active = BooleanField(default=True, index=True)
    notes = TextField(null=True)

    class Meta:  # type: ignore
        table_name = 'bank_accounts'

    def __str__(self) -> str:
        return f"{self.name} ({self.account_number})"


class BankFeed(BaseModelExtended, TimestampMixin):
    """A bank feed (import / sync session) for a bank account."""

    bank_account = ForeignKeyField(
        BankAccount, backref='feeds', on_delete='CASCADE',
    )
    last_sync_date = DateTimeField(null=True)
    source = CharField(max_length=50, null=True)  # csv, ofx, api
    status = CharField(max_length=20, default='pending', index=True)
    total_transactions = IntegerField(default=0)
    imported_count = IntegerField(default=0)
    notes = TextField(null=True)

    class Meta:  # type: ignore
        table_name = 'bank_feeds'

    def __str__(self) -> str:
        return f"Feed #{self.id} – {self.bank_account.name}"


class BankTransaction(BaseModelExtended, TimestampMixin):
    """A single transaction imported from a bank feed."""

    feed = ForeignKeyField(
        BankFeed, backref='transactions', on_delete='CASCADE',
    )
    bank_account = ForeignKeyField(
        BankAccount, backref='bank_transactions',
        on_delete='CASCADE',
    )
    transaction_date = DateTimeField(index=True)
    value_date = DateTimeField(null=True)
    description = TextField()
    amount = DecimalField(max_digits=14, decimal_places=2)
    running_balance = DecimalField(max_digits=14, decimal_places=2, null=True)
    reference = CharField(max_length=100, null=True, index=True)
    category = CharField(max_length=100, null=True, index=True)
    is_reconciled = BooleanField(default=False, index=True)
    is_assigned = BooleanField(default=False, index=True)
    notes = TextField(null=True)

    class Meta:  # type: ignore
        table_name = 'bank_transactions'
        indexes = (
            (('feed', 'transaction_date'), False),
        )

    def __str__(self) -> str:
        direction = 'CR' if self.amount >= 0 else 'DR'
        return f"{direction} {abs(self.amount)} – {self.description[:40]}"


class Reconciliation(BaseModelExtended, TimestampMixin):
    """Reconciliation session matching bank statement to ledger."""

    bank_account = ForeignKeyField(
        BankAccount, backref='reconciliations', on_delete='CASCADE',
    )
    statement_date = DateTimeField()
    statement_balance = DecimalField(max_digits=16, decimal_places=2)
    computed_balance = DecimalField(max_digits=16, decimal_places=2)
    difference = DecimalField(max_digits=16, decimal_places=2, default=0)
    status = CharField(max_length=20, default='in_progress', index=True)
    reconciled_by = ForeignKeyField(
        User, backref='reconciliations', null=True,
        on_delete='SET NULL',
    )
    notes = TextField(null=True)

    class Meta:  # type: ignore
        table_name = 'reconciliations'

    def __str__(self) -> str:
        return (f"Reconciliation #{self.id} – "
                f"{self.bank_account.name} ({self.status})")

    @classmethod
    def is_balanced(cls, recon_id: int) -> bool:
        recon = cls.get_or_none(cls.id == recon_id)
        if recon is None:
            return False
        return recon.difference == 0


class ReconciliationItem(BaseModelExtended):
    """Individual item in a reconciliation (bank tx ↔ journal entry)."""

    reconciliation = ForeignKeyField(
        Reconciliation, backref='items', on_delete='CASCADE',
    )
    bank_transaction = ForeignKeyField(
        BankTransaction, backref='reconciliation_items', null=True,
        on_delete='SET NULL',
    )
    journal_entry = CharField(max_length=50, null=True)  # transaction ref
    amount = DecimalField(max_digits=14, decimal_places=2)
    is_cleared = BooleanField(default=False)

    class Meta:  # type: ignore
        table_name = 'reconciliation_items'

    def __str__(self) -> str:
        return f"Recon item ${self.amount} ({'cleared' if self.is_cleared else 'pending'})"