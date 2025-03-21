#! /usr/bin/env python3.12
import sys

from PySide6.QtCore import QFile, QSettings
from PySide6.QtGui import QFont, QFontDatabase, QIcon
from PySide6.QtWidgets import QApplication

# Reources
import src.gui.source_rc
# Local imports
from src.core.database.models import initialize_database
from src.core.utils.logger import get_logger
from src.core.utils.settings import (APP_NAME, APP_VERSION,
                                     ORGANIZATION_DOMAIN, ORGANIZATION_NAME)
from src.core.utils.shortcutes import get_database_path
from src.gui.main_window import MainWindow

# Codes Here

logger = get_logger(APP_NAME)


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


def setup_application():
    """Configure the QApplication instance."""
    # Set up application settings
    QSettings.setDefaultFormat(QSettings.IniFormat)

    # Create application instance
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setOrganizationName(ORGANIZATION_NAME)
    app.setOrganizationDomain(ORGANIZATION_DOMAIN)
    app.setApplicationDisplayName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)
    app.setFont(QFont(":/fonts/Vazirmatn-RD-UI-FD-Regular", 10))
    app.setWindowIcon(QIcon(":/img-icon/icon-ico"))

    # Load stylesheet
    # In main.py
    style_file = QFile(":/styles/default-style")
    if style_file.open(QFile.ReadOnly | QFile.Text):
        app.setStyleSheet(str(style_file.readAll(), encoding="utf-8"))
    else:
        logger.error("Faild to load style sheet.")

    return app


def main():
    try:
        # Initialize database
        db_path = get_database_path()
        initialize_database(db_path)

        # Set up application
        app = setup_application()
        load_fonts()

        # Create and show main window
        main_window = MainWindow()
        # main_window.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        main_window.setMinimumWidth(1024)
        main_window.setMinimumHeight(720)
        main_window.show()

        # Start event loop
        sys.exit(app.exec())

    except Exception as e:
        logger.critical(f"Critical error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
