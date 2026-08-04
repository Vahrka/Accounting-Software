from peewee import BooleanField, CharField, TextField

from .base import BaseModelExtended, TimestampMixin


class Theme(BaseModelExtended, TimestampMixin):
    """QSS theme stored in the database."""

    name = CharField(max_length=50, unique=True, index=True)
    qss_stylesheet = TextField()
    is_active = BooleanField(default=False, index=True)
    description = CharField(max_length=255, null=True)

    class Meta:  # type: ignore
        table_name = 'themes'

    def __str__(self) -> str:
        return self.name

    @classmethod
    def active_theme(cls) -> 'Theme | None':
        return cls.get_or_none(cls.is_active == True)  # noqa: E712

    def activate(self) -> None:
        """Set this theme as the only active theme."""
        for theme in Theme.select():
            theme.is_active = False
            theme.save(only=[Theme.is_active])
        self.is_active = True
        self.save(only=[Theme.is_active])
