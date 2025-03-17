from pathlib import Path

from src.core.utils.logger import setup_logger

logger = setup_logger()

__all__ = [
    'BASE_DIR',
    'APP_NAME',
    'APP_VERSION',
    'ORGANIZATION_DOMAIN',
    'ORGANIZATION_NAME',
    'get_database_path',
]

BASE_DIR = Path(__file__).parent.parent.parent

# UI Settings

# Application Metadata
APP_NAME = 'Accounting Software'
APP_VERSION = '1.0.0'
ORGANIZATION_DOMAIN = 'ac.soft'
ORGANIZATION_NAME = 'Free Tech'
