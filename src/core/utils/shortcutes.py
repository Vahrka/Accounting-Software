from pathlib import Path

from src.core.utils.logger import get_logger
from src.core.utils.settings import BASE_DIR

logger = get_logger()

# Database Path exists


def check_db_path_exist() -> Path:
    data_dir = BASE_DIR / 'data'
    data_dir.mkdir(exist_ok=True, parents=True)
    return data_dir


# Database Settings
def get_database_path() -> Path:
    """Get the path to the SQLite database file"""
    data_dir = check_db_path_exist()
    return data_dir / 'accounting.db'
