from datetime import datetime

from peewee import BooleanField, CharField, DateTimeField, IntegerField

from .base import BaseModelExtended, TimestampMixin


BACKUP_STATUSES = (
    'in_progress',
    'completed',
    'failed',
)


class Backup(BaseModelExtended, TimestampMixin):
    """Record of database backup operations."""

    file_path = CharField(max_length=500)
    size_bytes = IntegerField(null=True)
    status = CharField(max_length=20, default='in_progress', index=True)
    is_auto = BooleanField(default=False)
    is_encrypted = BooleanField(default=False)
    notes = CharField(max_length=255, null=True)

    class Meta:  # type: ignore
        table_name = 'backups'

    def __str__(self) -> str:
        return f"Backup #{self.id} – {self.status}"
