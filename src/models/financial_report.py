from datetime import datetime

from peewee import (CharField, DateTimeField, ForeignKeyField,
                    IntegerField, TextField)

from .base import BaseModelExtended, TimestampMixin
from .user import User


REPORT_TYPES = (
    'balance_sheet',
    'income_statement',
    'cash_flow',
    'trial_balance',
    'general_ledger',
    'accounts_receivable',
    'accounts_payable',
    'custom',
)

FILE_FORMATS = (
    'pdf',
    'xlsx',
    'csv',
    'json',
)


class FinancialReport(BaseModelExtended, TimestampMixin):
    """Generated financial reports metadata."""

    name = CharField(max_length=200, index=True)
    report_type = CharField(max_length=30, index=True)
    generated_at = DateTimeField(default=datetime.now)
    format = CharField(max_length=10, default='pdf')
    file_path = CharField(max_length=500, null=True)
    parameters = TextField(null=True)  # JSON-encoded filter params
    period_start = DateTimeField(null=True)
    period_end = DateTimeField(null=True)
    generated_by = ForeignKeyField(
        User, backref='generated_reports', null=True,
        on_delete='SET NULL',
    )
    notes = TextField(null=True)

    class Meta:  # type: ignore
        table_name = 'financial_reports'

    def __str__(self) -> str:
        return f"{self.name} ({self.report_type})"
