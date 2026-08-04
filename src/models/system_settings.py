from peewee import CharField, TextField

from .base import BaseModelExtended, TimestampMixin


class SystemSettings(BaseModelExtended, TimestampMixin):
    """Key-value store for application-wide settings."""

    key = CharField(max_length=100, unique=True, index=True)
    value = TextField()
    description = CharField(max_length=255, null=True)

    class Meta:  # type: ignore
        table_name = 'system_settings'

    def __str__(self) -> str:
        return f"{self.key} = {self.value[:50]}"

    @classmethod
    def get_value(cls, key: str, default: str = '') -> str:
        setting = cls.get_or_none(cls.key == key)
        return setting.value if setting else default

    @classmethod
    def set_value(cls, key: str, value: str, description: str = None) -> None:
        obj, _ = cls.get_or_create(
            key=key,
            defaults={'value': value, 'description': description},
        )
        if obj.value != value:
            obj.value = value
            if description is not None:
                obj.description = description
            obj.save()
