from datetime import datetime

from peewee import (BooleanField, CharField, DateTimeField, DecimalField,
                    DeferredForeignKey, ForeignKeyField, IntegerField,
                    TextField)

from .base import BaseModelExtended, TimestampMixin
from .currency import Currency
from .user import User


JOURNAL_STATUSES = (
    'draft',
    'posted',
    'reversed',
    'cancelled',
)


class JournalTransaction(BaseModelExtended, TimestampMixin):
    """Double-entry journal transaction (general journal).

    Every journal transaction must have at least two ``TransactionEntry``
    rows where **total_debit == total_credit**.
    """

    reference_no = CharField(max_length=100, unique=True, index=True)
    transaction_date = DateTimeField(index=True)
    description = TextField(null=True)
    total_debit = DecimalField(
        max_digits=16, decimal_places=2, default=0,
    )
    total_credit = DecimalField(
        max_digits=16, decimal_places=2, default=0,
    )
    is_posted = BooleanField(default=False, index=True)
    posted_at = DateTimeField(null=True)
    created_by = ForeignKeyField(
        User, backref='journal_transactions', null=True,
        on_delete='SET NULL',
    )
    currency = ForeignKeyField(
        Currency, backref='journal_transactions', null=True,
        on_delete='SET NULL',
    )
    reversal_of = ForeignKeyField(
        'self', backref='reversals', null=True,
        on_delete='SET NULL',
    )
    notes = TextField(null=True)
    source = CharField(max_length=50, null=True)  # manual, import, auto
    source_ref = CharField(max_length=100, null=True)

    class Meta:  # type: ignore
        table_name = 'journal_transactions'
        indexes = (
            (('reference_no', 'transaction_date'), False),
        )

    def __str__(self) -> str:
        return f"JV-{self.reference_no} ({self.status_label})"

    @property
    def status_label(self) -> str:
        if self.reversal_of_id:
            return 'reversed'
        return 'posted' if self.is_posted else 'draft'

    # ------------------------------------------------------------------
    # Actions
    # ------------------------------------------------------------------

    def post(self) -> None:
        """Mark the journal as posted after validation."""
        if self.is_posted:
            return
        self._validate_balanced()
        self.is_posted = True
        self.posted_at = datetime.now()
        self.save()

    def reverse(self, reverse_date: datetime = None) -> 'JournalTransaction':
        """Create a reversing journal entry.

        Returns the new JournalTransaction without posting it.
        """
        new_ref = f"REV-{self.reference_no}"
        reversal = JournalTransaction.create(
            reference_no=new_ref,
            transaction_date=reverse_date or datetime.now(),
            description=f"Reversal of {self.reference_no}",
            reversal_of=self,
            created_by=self.created_by,
        )
        for entry in self.entries:
            TransactionEntry.create(
                transaction=reversal,
                account=entry.account,
                debit=entry.credit,
                credit=entry.debit,
                description=f"Reverse: {entry.description or ''}",
            )
        reversal.total_debit = self.total_credit
        reversal.total_credit = self.total_debit
        reversal.save()
        return reversal

    def _validate_balanced(self) -> bool:
        """Raise ValueError if debit != credit."""
        from decimal import Decimal
        entries = list(self.entries)
        if len(entries) < 2:
            raise ValueError(
                "A journal transaction must have at least two entries."
            )
        total_dr = sum((e.debit for e in entries), Decimal('0.00'))
        total_cr = sum((e.credit for e in entries), Decimal('0.00'))
        if total_dr != total_cr:
            raise ValueError(
                f"Journal is not balanced: debit={total_dr}, credit={total_cr}"
            )
        return True

    def recalculate_totals(self) -> None:
        """Sum entries into total_debit / total_credit and save."""
        from decimal import Decimal
        entries = list(self.entries)
        self.total_debit = sum(
            (e.debit for e in entries), Decimal('0.00'),
        )
        self.total_credit = sum(
            (e.credit for e in entries), Decimal('0.00'),
        )
        self.save()


class TransactionEntry(BaseModelExtended):
    """A single debit or credit line within a JournalTransaction."""

    transaction = ForeignKeyField(
        JournalTransaction, backref='entries', on_delete='CASCADE',
    )
    account = DeferredForeignKey(
        'LedgerAccount', backref='transaction_entries',
        on_delete='RESTRICT',
    )
    debit = DecimalField(max_digits=16, decimal_places=2, default=0)
    credit = DecimalField(max_digits=16, decimal_places=2, default=0)
    description = TextField(null=True)

    class Meta:  # type: ignore
        table_name = 'transaction_entries'
        indexes = (
            (('transaction', 'account'), False),
        )

    def __str__(self) -> str:
        side = 'DR' if self.debit > 0 else 'CR'
        amount = self.debit if self.debit > 0 else self.credit
        return f"{side} {amount} → {self.account}"


# ----------------------------------------------------------------------
# Payment transaction (kept for backward compatibility with existing code)
# ----------------------------------------------------------------------

class PaymentTransaction(BaseModelExtended, TimestampMixin):
    """Payment received/paid against an invoice (AR/AP)."""

    invoice_id = IntegerField(null=True, index=True)
    customer_id = IntegerField(null=True, index=True)
    user = ForeignKeyField(
        User, backref='payment_transactions', null=True,
        on_delete='SET NULL',
    )
    transaction_id = CharField(max_length=100, unique=True, index=True)
    amount = DecimalField(max_digits=10, decimal_places=2)
    payment_method = CharField(max_length=50, index=True)
    payment_date = DateTimeField(default=datetime.now)
    status = CharField(max_length=20, default='pending', index=True)
    reference = CharField(max_length=100, null=True)
    notes = TextField(null=True)

    class Meta:  # type: ignore
        table_name = 'payment_transactions'
        indexes = (
            (('transaction_id', 'payment_method'), False),
        )

    def __str__(self) -> str:
        return f"Payment {self.transaction_id} – ${self.amount}"

    @classmethod
    def get_by_transaction_id(cls, transaction_id: str) -> 'PaymentTransaction | None':
        return cls.get_or_none(transaction_id=transaction_id)
