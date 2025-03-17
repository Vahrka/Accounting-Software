from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QMainWindow, QPushButton,
                               QStackedWidget, QVBoxLayout, QWidget)

from src.gui.widgets import AccountsWidget, DashboardWidget, LedgerWidget
from src.gui.widgets.menubar import Menubar

# Codes Here


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Main container
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        menubar = Menubar()
        menubar.setup_ui()
        self.setMenuBar(menubar)

        # Modern layout
        self.main_window = QHBoxLayout()
        self.main_window
        self.actionRegister = QAction()

        main_widget.setLayout(self.main_window)

        # Side Navigation
        self.side_nav_frame = QFrame()
        self.side_nav_frame.setFixedWidth(240)
        self.side_nav_frame.setObjectName("SideNav")
        self.side_nav = QVBoxLayout(self.side_nav_frame)
        self.side_nav.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.main_window.addWidget(self.side_nav_frame)

        # Content Area
        self.stacked_widget = QStackedWidget()  # Manages screens
        self.main_window.addWidget(self.stacked_widget)

        # Add navigation buttons and screens
        self._add_core_navs()
        self._setup_screens()

    def _add_core_navs(self):
        """Add buttons to the side navigation."""
        dashboard_button = QPushButton(self.tr("Dashboard"))
        ledger_button = QPushButton(self.tr("General Ledger"))
        accounts_button = QPushButton(self.tr("Accounts"))

        # Connect buttons to switch screens
        dashboard_button.clicked.connect(lambda: self.switch_screen(0))
        ledger_button.clicked.connect(lambda: self.switch_screen(1))
        accounts_button.clicked.connect(lambda: self.switch_screen(2))

        self.side_nav.addWidget(dashboard_button)
        self.side_nav.addWidget(ledger_button)
        self.side_nav.addWidget(accounts_button)

    def _setup_screens(self):
        """Add screens to the stacked widget."""
        self.stacked_widget.addWidget(DashboardWidget())  # Screen 0
        self.stacked_widget.addWidget(LedgerWidget())    # Screen 1
        self.stacked_widget.addWidget(AccountsWidget())  # Screen 2

    def add_screen_to_stack(self, screen):
        pass

    def switch_screen(self, index):
        """Switch to the screen at the given index."""
        self.stacked_widget.setCurrentIndex(index)
