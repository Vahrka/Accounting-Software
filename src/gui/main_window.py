from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget

from src.gui.ui.main_window_ui import Ui_MainWindow
from src.gui.widgets.base_screen import BaseScreen
from src.gui.widgets.menubar import Menubar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.MainSideNav.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Setup Menubar (handle functionality)
        self.menubar_controler = Menubar(self.ui)
        self.menubar_controler.setup_ui()

    def add_btn_to_nav(self, widget: QWidget):
        """Add buttons to the side navigation."""
        self.ui.MainSideNav.addWidget(widget)

    def add_screen_to_stack(self, screen: BaseScreen) -> int:
        """Add screens to the stacked widget."""
        return self.ui.MainStackView.addWidget(screen)

    def go_to_screen(self, screen: int):
        """Switch to a specific screen in the stack view."""
        self.ui.MainStackView.setCurrentIndex(screen)
