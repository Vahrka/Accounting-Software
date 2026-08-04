import json
from datetime import datetime

from peewee import BooleanField, DateTimeField, IntegerField

from .database import BaseModel


class TimestampMixin(BaseModel):
    """Mixin for timestamp fields"""
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        return super().save(*args, **kwargs)


class SoftDeleteMixin(BaseModel):
    """Mixin for soft delete functionality"""
    is_deleted = BooleanField(default=False)
    deleted_at = DateTimeField(null=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        """Soft delete instead of hard delete"""
        self.is_deleted = True
        self.deleted_at = datetime.now()
        return self.save()

    def hard_delete(self, *args, **kwargs):
        """Permanently delete"""
        return super().delete_instance(*args, **kwargs)

    @classmethod
    def get_active(cls):
        """Get only active (non-deleted) records"""
        return cls.select().where(cls.is_deleted == False)


class BaseModelExtended(BaseModel):
    """Extended base model with common methods and fields"""
    id = IntegerField(unique=True, primary_key=True)

    class Meta:
        abstract = True

    def to_dict(self) -> dict:
        """Convert model to dictionary"""
        data = {}
        for field_name in self._meta.fields:
            value = getattr(self, field_name)
            if hasattr(value, 'strftime'):
                data[field_name] = value.isoformat()
            else:
                data[field_name] = value
        return data

    def to_json(self) -> str:
        """Convert model to JSON"""
        return json.dumps(self.to_dict(), default=str)

    @classmethod
    def exists(cls, **kwargs) -> bool:
        """Check if record exists"""
        return cls.select().where(*[getattr(cls, k) == v for k, v in kwargs.items()]).exists()

    @classmethod
    def paginate(cls, page: int = 1, per_page: int = 20):
        """Paginate results"""
        return cls.select().paginate(page, per_page)

    @classmethod
    def count_all(cls) -> int:
        """Get total count"""
        return cls.select().count()
