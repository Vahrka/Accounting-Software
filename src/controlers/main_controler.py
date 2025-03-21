from PySide6.QtWidgets import QWidget

from src.gui.widgets.base_screen import BaseScreen

# Codes Here


class MainControler:
    def add_btn_to_nav(self, widget: QWidget):
        """Add buttons to the side navigation."""
        # Connect buttons to switch screens
        self.side_nav.addWidget(widget)

    def add_screen_to_stack(self, screen: BaseScreen):
        """Add screens to the stacked widget."""
        return self.stacked_widget.addWidget(screen)

    def go_to_screen(self, screen: int):
        self.stacked_widget.setCurrentIndex(screen)
