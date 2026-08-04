from contextlib import contextmanager
from pathlib import Path

from peewee import Model, SqliteDatabase

# Single database instance
_db = SqliteDatabase(None)


class BaseModel(Model):
    """Base model that all models inherit from"""
    class Meta:
        database = _db


def init_database(db_path: Path | str = "database.db") -> SqliteDatabase:
    """Initialize database connection"""
    _db.init(str(db_path), pragmas={
        'journal_mode': 'wal',
        'cache_size': -1024 * 64,
        'foreign_keys': 1,
    })
    return _db


class DatabaseManager:
    """Singleton database connection manager"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._connected = False
        return cls._instance

    def connect(self) -> SqliteDatabase:
        """Connect to database"""
        if not self._connected:
            if _db.is_closed():
                _db.connect()
            self._connected = True
        return _db

    def close(self) -> None:
        """Close database connection"""
        if not _db.is_closed():
            _db.close()
            self._connected = False

    @contextmanager
    def connection(self):
        """Context manager for database operations"""
        self.connect()
        try:
            yield _db
        except Exception as e:
            _db.rollback()
            raise e

    @property
    def db(self) -> SqliteDatabase:
        """Get database instance"""
        return self.connect()

    def is_connected(self) -> bool:
        """Check if database is connected"""
        return self._connected and not _db.is_closed()


# Singleton instance
db_manager = DatabaseManager()
