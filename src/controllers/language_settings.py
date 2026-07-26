from PySide6.QtCore import (QCoreApplication, QLocale, QSettings, Qt,
                            QTranslator, Slot)
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import QWidget

from ui.settings.select_language_ui import Ui_LanguageSetting
from utils.logger import get_logger
from utils.mixins import RetranslateMixin

logger = get_logger()


class LanguageSettingsController(RetranslateMixin, QWidget):
    def setup_ui(self):
        self.ui = Ui_LanguageSetting()
        self.ui.setupUi(self)
        self.ui.save_btn.clicked.connect(self.save)

        # Get the main application instance
        self.app: QCoreApplication = QCoreApplication.instance()  # type: ignore

        self.font_families = QFontDatabase().families()

        # Dictionary mapping language display names to locale codes
        # FIXME: Update this code for `PySide6.QtCore.QLocal`. This option would being update after we add every language support in the world. Until then we just hard coding.
        self.language_list = [
            "en",
            "fa",
            "de",
            "az",
            "tu",
            "az-ir",
            "ru",
        ]

        # Load saved language preference
        self.load_saved_language()

        # Load current font
        self.load_font_families()

    def load_saved_language(self):
        """Load and set saved language preference"""
        settings = QSettings()
        saved_lang_code = settings.value("language", "en")

        self.ui.language_input.setCurrentIndex(self.language_list.index(str(saved_lang_code)))

    @Slot()
    def save(self):
        """Save language preference and apply changes"""
        # Get selected language index from combobox
        selected_language = self.ui.language_input.currentIndex()
        language_code = self.language_list[selected_language]

        self.change_language(language_code)
        self.save_language_preference(language_code)
        logger.info(f"Language changed to: `{language_code}`")

        selected_font_idx = self.ui.font_input.currentIndex()
        self.save_font_prefrence(selected_font_idx)

    def change_language(self, language_code: str):
        app_translator = QTranslator(self.app)
        app_translator.load(f":/locales/{language_code}")
        self.app.installTranslator(app_translator)
        logger.info(f"Loaded app translations :/locales/{language_code}")
        locale = QLocale(language_code)
        if locale.textDirection() == Qt.LayoutDirection.RightToLeft:
            self.app.setLayoutDirection(Qt.LayoutDirection.RightToLeft)  # pyright: ignore[reportAttributeAccessIssue]
        else:
            self.app.setLayoutDirection(Qt.LayoutDirection.LeftToRight)  # pyright: ignore[reportAttributeAccessIssue]

        self.save_language_preference(language_code)

    def save_language_preference(self, language_code: str):
        """Save language preference to settings"""
        settings = QSettings()
        settings.setValue("language", language_code)
        settings.sync()

    def load_font_families(self):

        for font in self.font_families:
            self.ui.font_input.addItem(font)

        current_font: QFont = self.app.font()  # pyright: ignore[reportAttributeAccessIssue]
        try:
            self.ui.font_input.setCurrentIndex(self.font_families.index(current_font.family()))
        except:
            self.ui.font_input.setCurrentIndex(-1)


    # FIXME: If user deletes some system fonts it may crash after loading again. 
    def save_font_prefrence(self, font_idx):
        settings = QSettings()
        settings.setValue("font-family", {self.font_families[font_idx]: font_idx})
        settings.sync()
