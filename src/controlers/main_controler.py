from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QStackedLayout, QVBoxLayout, QWidget

from src.gui.widgets.base_screen import BaseScreen

# Codes Here


class MainControler:
    side_nav: QVBoxLayout
    stacked_widget: QStackedLayout
    settings: QSettings

    def add_btn_to_nav(self, widget: QWidget):
        """Add buttons to the side navigation."""
        # Connect buttons to switch screens
        self.side_nav.addWidget(widget)

    def add_screen_to_stack(self, screen: BaseScreen):
        """Add screens to the stacked widget."""
        return self.stacked_widget.addWidget(screen)

    def go_to_screen(self, screen: int):
        self.stacked_widget.setCurrentIndex(screen)

    class data:
        def store(self, key, value):
            self.settings.setValue(key, value)

        def retrieve(self, key):
            return self.settings.getValue(key)
