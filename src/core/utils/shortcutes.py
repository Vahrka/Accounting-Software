from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtGui import QFontDatabase

# Reources
# Local imports
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


def load_fonts():
    """Load custom fonts from resources."""
    font_aliases = [
        "Vazirmatn-RD-UI-FD-Black",
        "Vazirmatn-RD-UI-FD-Black",
        "Vazirmatn-RD-UI-FD-Bold",
        "Vazirmatn-RD-UI-FD-ExtraBold",
        "Vazirmatn-RD-UI-FD-ExtraLight",
        "Vazirmatn-RD-UI-FD-Light",
        "Vazirmatn-RD-UI-FD-Medium",
        "Vazirmatn-RD-UI-FD-Regular",
        "Vazirmatn-RD-UI-FD-SemiBold",
        "Vazirmatn-RD-UI-FD-Thin",
    ]
    QFontDatabase.removeAllApplicationFonts()
    # BUG: Force first time bug
    # Loading font for first time will got in to unknown problem
    # We have to add this to later codes works
    QFontDatabase.addApplicationFont(":/fonts/Vazirmatn-RD-UI-FD-Regular")

    for alias in font_aliases:
        font_path = f":/fonts/{alias}"
        if not QFontDatabase.addApplicationFont(font_path):
            if QFile(font_path).ex0ists():
                logger.error(f"{alias} exists but failed to load font.")
            else:
                logger.error(f"{alias} dosn't exists.")
